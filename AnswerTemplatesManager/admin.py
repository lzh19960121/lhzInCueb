from django import forms
from django.contrib import admin
import datetime
# Register your models here.
from AnswerTemplatesManager import models


class TemplatesAdmin(admin.ModelAdmin):
    # 只能查看当前用户的
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    # 保存
    def save_model(self, request, obj, form, change):
        obj.author = str(request.user)
        obj.create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        super().save_model(request, obj, form, change)

    # 更改filed类别,样式
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(TemplatesAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ['content']:
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        # if db_field.name in ['is_passed']:
        #     formfield.widget = forms.BooleanField()
        return formfield

    list_filter = ['type', 'child_type', 'title', 'child_title', 'is_passed']
    list_per_page = 10
    fields = ['type', 'child_type', 'title', 'child_title', 'content']
    list_display = ['type', 'child_type', 'title', 'child_title', 'content', 'is_passed', 'author', 'create_time']

    list_editable = [ 'child_type', 'title', 'child_title', 'content', 'is_passed']


admin.site.register(models.AnswerTemplate, TemplatesAdmin)
