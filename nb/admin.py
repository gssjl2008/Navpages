from django.contrib import admin

from .models import page_info

admin.site.site_header = '宁波导航页面后台'
admin.site.site_title = '宁波导航页面'

admin.site.register(page_info)