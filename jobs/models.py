from django.db import models


from django.db import models


class Job(models.Model):

    STATUS_CHOICES = [
        ("new", "New"),
        ("reviewing", "Reviewing"),
        ("quoted", "Quoted"),
        ("booked", "Booked"),
        ("completed", "Completed"),
    ]

    # Customer details
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)

    # Customer address
    address_line_1 = models.CharField(max_length=200)
    address_line_2 = models.CharField(
        max_length=200,
        blank=True
    )
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)

    # Job details
    description = models.TextField()

    photo = models.ImageField(
        upload_to="job_photos/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.description[:50]}"