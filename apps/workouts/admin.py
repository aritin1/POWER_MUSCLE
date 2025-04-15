from django.contrib import admin

# Register your models here.
from .models import Workout, Author

admin.site.register(Workout)
admin.site.register(Author)