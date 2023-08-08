from django.contrib import admin

from .models import NoinfoDetail
from .models import NoinfoTheme

admin.site.register(NoinfoDetail)
admin.site.register(NoinfoTheme)