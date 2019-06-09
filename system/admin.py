from django.contrib import admin
from .models import *
# Register your models here.
    

class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'info')

admin.site.register(Test, TestAdmin)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields' : ['test']}),
        (None,               {'fields': ['text']}),
        (None,               {'fields': ['complexity']}),
        (None,               {'fields': ['image']}),
        ('Date information', {'fields': ['right_choice']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Discipline)
admin.site.register(Theme)