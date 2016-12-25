# coding=utf-8
import json

from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.db.models import QuerySet
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy

from .models import BigGod, Tag


# Register your models here.
# admin.site.register(BigGod)

# admin.site.register(Tag)

def make_test(modeladmin, request, queryset):
    print "aaaa"
    print modeladmin
    print request
    if isinstance(queryset, QuerySet):
        for i in queryset.all():
            print i
    modeladmin.message_user(request, u'操作成功!!!')


# make_test.short_description = u"测试action"


def export_selected_objects(modeladmin, request, queryset):
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    ct = ContentType.objects.get_for_model(queryset.model)
    print ct
    return HttpResponseRedirect("/export/?ct=%s&ids=%s" % (ct.pk, ",".join(selected)))


@admin.register(BigGod)
class BigGodAdmin(admin.ModelAdmin):
    # fields = (('name', 'english_name', 'image', 'tags'), 'birthday')
    readonly_fields = ('tags_only',)

    def tags_only(self, instance):
        return format_html(
            '<span stype="color:green">aaaaaa</span>',
            # instance.tags
        )

    tags_only.short_description = 'tags_desc'

    fieldsets = (
        (u'用户', {
            'classes': ('wide2222', 'extrapretty'),
            'fields': ('name', 'english_name', 'birthday'),
        }),
        (u'其他', {
            'fields': ('image', 'tags')
        })
    )
    list_display = ('name', 'name2')
    # list_display_links = ('name',)
    list_filter = ('tags',)
    list_per_page = 3

    def make_test2(self, request, queryset):
        print "aaaa"
        print request
        if isinstance(queryset, QuerySet):
            print queryset.first().name
        self.message_user(request, u"操作成功")

    make_test2.short_description = u"测试2"
    actions = [make_test, make_test2, export_selected_objects]
    date_hierarchy = 'birthday'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


admin.site.add_action(make_test, u'测试')
BigGodAdmin.actions_on_bottom = True
BigGodAdmin.actions_on_top = False
BigGodAdmin.actions_selection_counter = True
# BigGodAdmin.list_per_page = 2
# BigGodAdmin.save_as
# BigGodAdmin.save_as_continue
# BigGodAdmin.search_fields = ('name', 'english_name')
# BigGodAdmin.show_full_result_count

admin.AdminSite.site_header = ugettext_lazy(u'九门金榜')
admin.AdminSite.site_title
admin.AdminSite.site_url
