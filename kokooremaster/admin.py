from django.contrib import admin
from .models import User, Template, Result

admin.site.register(User)
admin.site.register(Template)
admin.site.register(Result)