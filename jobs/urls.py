from django.urls import path

from . import views


urlpatterns = [

    # First page:
    # Customer explains what they need.
    path(
        "",
        views.create_job,
        name="create_job"
    ),

    # Customer answers follow-up questions.
    path(
        "assessment/<int:job_id>/",
        views.job_assessment,
        name="job_assessment"
    ),

    # Temporary price estimate page.
    path(
        "estimate/<int:job_id>/",
        views.job_estimate,
        name="job_estimate"
    ),

]