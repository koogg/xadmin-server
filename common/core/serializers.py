#!/usr/bin/env python
# -*- coding:utf-8 -*-
# project : xadmin-server
# filename : serializers
# author : ly_13
# date : 12/21/2023
from inspect import isfunction

from django.conf import settings
from django.db.models.fields import NOT_PROVIDED
from rest_framework.fields import empty
from rest_framework.request import Request
from rest_framework.serializers import ModelSerializer

from common.core.fields import BasePrimaryKeyRelatedField, LabeledChoiceField


class BaseModelSerializer(ModelSerializer):
    serializer_related_field = BasePrimaryKeyRelatedField
    serializer_choice_field = LabeledChoiceField
    ignore_field_permission = False  # 忽略字段权限

    class Meta:
        model = None
        table_fields = []  # 用于控制前端table的字段展示

    def get_value(self, dictionary):
        # We override the default field access in order to support
        # nested HTML forms.
        # 下面两行注释是因为已经在前面处理过form-data，这里无需再次处理
        # if html.is_html_input(dictionary):
        #     return html.parse_html_dict(dictionary, prefix=self.field_name) or empty
        return dictionary.get(self.field_name, empty)

    def get_uniqueness_extra_kwargs(self, field_names, declared_fields, extra_kwargs):
        """
        # 该方法是为了让继承BaseModelSerializer的方法，增加request传参,例如下面，为meta这个字段的序列化增加request参数
        class MenuSerializer(BaseModelSerializer):
            meta = MenuMetaSerializer()
        """
        for field_name in declared_fields:
            if declared_fields[field_name] and isinstance(declared_fields[field_name],
                                                          (BaseModelSerializer, BasePrimaryKeyRelatedField)):
                obj = declared_fields[field_name]
                declared_fields[field_name] = obj.__class__(*obj._args, **obj._kwargs, request=self.request)

        extra_kwargs, hidden_fields = super().get_uniqueness_extra_kwargs(field_names, declared_fields, extra_kwargs)
        return super().get_uniqueness_extra_kwargs(field_names, declared_fields, extra_kwargs)

    def get_allow_fields(self, fields, ignore_field_permission):
        """
        self.fields: 默认定义的字段
        fields: 需要展示的字段
        allow_fields: 字段权限允许的字段
        """
        _fields = set(self.fields)
        if fields is None:
            fields = _fields

        if self.ignore_field_permission or ignore_field_permission or (
                self.request and hasattr(self.request, "ignore_field_permission")):
            return set(fields) & _fields

        allow_fields = []
        # 获取权限字段，如果没有配置，则为定义的所有字段
        if self.request and settings.PERMISSION_FIELD_ENABLED and not self.ignore_field_permission:
            if hasattr(self.request, "user") and self.request.user and self.request.user.is_superuser:
                allow_fields = _fields
            elif hasattr(self.request, "fields"):
                if self.request.fields and isinstance(self.request.fields, dict):
                    allow_fields = self.request.fields.get(self.Meta.model._meta.label_lower, [])
        else:
            allow_fields = _fields

        return set(fields) & _fields & set(allow_fields)

    def __init__(self, instance=None, data=empty, request=None, fields=None, ignore_field_permission=False, **kwargs):
        """
        :param instance:
        :param data:
        :param request: Request 对象
        :param fields: 序列化展示的字段， 默认定义的全部字段
        :param ignore_field_permission: 忽略字段权限控制
        """
        super().__init__(instance, data, **kwargs)
        self.request: Request = request or self.context.get("request", None)
        if self.request is None:
            return
        allowed = self.get_allow_fields(fields, ignore_field_permission)
        for field_name in set(self.fields) - allowed:
            self.fields.pop(field_name)

    def build_standard_field(self, field_name, model_field):
        field_class, field_kwargs = super().build_standard_field(field_name, model_field)
        default = getattr(model_field, 'default', NOT_PROVIDED)
        if default != NOT_PROVIDED:
            # 将model中的默认值同步到序列化中
            if isfunction(default):
                default = default()
            field_kwargs.setdefault("default", default)
        return field_class, field_kwargs

    def create(self, validated_data):
        if self.request:
            user = self.request.user
            if user and user.is_authenticated:
                if hasattr(self.Meta.model, 'creator') or hasattr(self.instance, 'creator'):
                    validated_data["creator"] = user
                if hasattr(self.Meta.model, 'dept_belong') or hasattr(self.instance, 'dept_belong'):
                    validated_data["dept_belong"] = user.dept
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if self.request:
            user = self.request.user
            if user and user.is_authenticated:
                if hasattr(self.instance, 'modifier'):
                    validated_data["modifier"] = user
        return super().update(instance, validated_data)
