from django.contrib import admin

# Register your models here.

from .models import Choice, Question
'''
用来将models中定义的模型注册到后台admin管理   并编辑显示的属性
'''


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
#
# admin.site.register(Question,QuestionAdmin)


# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]
#
# admin.site.register(Question, QuestionAdmin)

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),    #分块显示 并定义class属性
    ]

    inlines = [ChoiceInline]        #显示相关联表
    list_display = ('question_text', 'pub_date')   # 显示 字段
    list_filter = ['pub_date']     #增加筛选字段
    search_fields = ['question_text']  #增加搜索字段

admin.site.register(Question, QuestionAdmin)

# admin.site.register(Choice)

