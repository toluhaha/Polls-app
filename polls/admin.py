from django.contrib import admin
from .models import Question, Choice
# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'published_date', 'was_recently_published', 'author')
    list_filter = ('published_date', 'author')
    search_fields = ('question_text',)
    date_hirerachy = ('published')

@admin.register(Choice)
class ChoiceAamin(admin.ModelAdmin):
    list_display = ('choice_text', 'vote')
    list_filter = ( 'question',)
