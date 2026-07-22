from django.db import models


class Job(models.Model):

    # The different stages a job can go through.
    STATUS_CHOICES = [
        ("new", "New"),
        ("assessing", "Assessing"),
        ("quoted", "Quoted"),
        ("booked", "Booked"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    # -----------------------------
    # Customer information
    # -----------------------------

    customer_name = models.CharField(
        max_length=100,
        blank=True
    )

    customer_email = models.EmailField(
        blank=True
    )

    customer_phone = models.CharField(
        max_length=20,
        blank=True
    )

    # -----------------------------
    # Job address
    # -----------------------------

    address_line_1 = models.CharField(
        max_length=200,
        blank=True
    )

    address_line_2 = models.CharField(
        max_length=200,
        blank=True
    )

    city = models.CharField(
        max_length=100,
        blank=True
    )

    postcode = models.CharField(
        max_length=10,
        blank=True
    )

    # -----------------------------
    # Job description
    # -----------------------------

    # This is what the customer initially tells us.
    description = models.TextField()

    # -----------------------------
    # Photo
    # -----------------------------

    photo = models.ImageField(
        upload_to="job_photos/",
        blank=True,
        null=True
    )

    # -----------------------------
    # Job assessment
    # -----------------------------

    # Later, AI can identify the type of work.
    # Example: Plumbing, Electrical, Carpentry, etc.
    job_category = models.CharField(
        max_length=100,
        blank=True
    )

    # AI or the system can store a summary
    # of what it thinks the customer needs.
    job_summary = models.TextField(
        blank=True
    )

    # -----------------------------
    # Pricing
    # -----------------------------

    # Estimated price shown to the customer.
    estimated_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    # -----------------------------
    # Job status
    # -----------------------------

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    # -----------------------------
    # Timestamp
    # -----------------------------

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.customer_name or 'New Customer'} - {self.description[:50]}"


class Question(models.Model):

    # The question that will be shown to the customer.
    text = models.CharField(
        max_length=500
    )

    # If this is True, the customer must answer
    # this question before continuing.
    required = models.BooleanField(
        default=True
    )

    # Used to control the order of questions.
    order = models.PositiveIntegerField(
        default=0
    )

    # Allows us to temporarily disable
    # questions without deleting them.
    active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        # Questions will automatically be ordered
        # from lowest order number to highest.
        ordering = ["order"]

    def __str__(self):

        return self.text


class Answer(models.Model):

    # The job this answer belongs to.
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="answers"
    )

    # The question that was answered.
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="answers"
    )

    # The customer's answer.
    answer = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.question.text}: {self.answer}"
