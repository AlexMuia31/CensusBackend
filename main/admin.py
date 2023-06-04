from django.contrib import admin
from .models import Census, Insurance, Total, Poverty
# Register your models here.


admin.site.site_header = "Census Data"
admin.site.site_title = "Census Data Admin"
admin.site.index_title = "Welcome to census data Portal"


admin.site.register(Census)
admin.site.register(Insurance)
admin.site.register(Total)
admin.site.register(Poverty)
