from django.contrib import admin
from .models import Course, ScoreBoard
from .models import Question

# Register your models here.

admin.site.register(Course)
admin.site.register(Question)
admin.site.register(ScoreBoard)