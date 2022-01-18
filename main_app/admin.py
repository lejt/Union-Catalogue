from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Member)
admin.site.register(Staff)
admin.site.register(Club)