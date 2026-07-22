from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)

from .forms import JobForm
from .models import (
    Answer,
    Job,
    Question,
)


def create_job(request):

    # If the customer submits the form,
    # request.method will be POST.
    if request.method == "POST":

        # Create the form using submitted data.
        form = JobForm(
            request.POST,
            request.FILES
        )

        # Check whether the submitted information
        # is valid.
        if form.is_valid():

            # Save the job to the database.
            job = form.save()

            # Instead of sending the customer to
            # a success page, send them to the
            # assessment process.
            return redirect(
                "job_assessment",
                job_id=job.id
            )

    else:

        # Show an empty form when the customer
        # first visits the page.
        form = JobForm()

    return render(
        request,
        "jobs/create_job.html",
        {
            "form": form
        }
    )


def job_assessment(request, job_id):

    # Find the job that the customer just created.
    job = get_object_or_404(
        Job,
        id=job_id
    )

    # Get all active questions.
    questions = Question.objects.filter(
        active=True
    ).order_by(
        "order"
    )

    # If the customer submits answers.
    if request.method == "POST":

        # Loop through every question.
        for question in questions:

            # Each answer is stored using
            # the question's ID.
            answer_text = request.POST.get(
                f"question_{question.id}"
            )

            # Only save an answer if the customer
            # actually provided one.
            if answer_text:

                Answer.objects.create(
                    job=job,
                    question=question,
                    answer=answer_text
                )

        # After answering questions,
        # move to the price estimate page.
        return redirect(
            "job_estimate",
            job_id=job.id
        )

    return render(
        request,
        "jobs/job_assessment.html",
        {
            "job": job,
            "questions": questions,
        }
    )


def job_estimate(request, job_id):

    # Find the customer's job.
    job = get_object_or_404(
        Job,
        id=job_id
    )

    return render(
        request,
        "jobs/job_estimate.html",
        {
            "job": job,
        }
    )
