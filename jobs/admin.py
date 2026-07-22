from django.contrib import admin

from .models import (
    Job,
    Question,
    Answer,
)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "customer_name",
        "postcode",
        "status",
        "estimated_price",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "customer_name",
        "customer_email",
        "customer_phone",
        "postcode",
        "description",
    )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    list_display = (
        "text",
        "required",
        "order",
        "active",
    )

    list_filter = (
        "required",
        "active",
    )


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):

    list_display = (
        "job",
        "question",
        "answer",
        "created_at",
    )

    search_fields = (
        "answer",
    )
