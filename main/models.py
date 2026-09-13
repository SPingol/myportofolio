import uuid
from django.db import models

class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    date_range = models.CharField(max_length=100)
    description_header = models.CharField(max_length=255, default="Coursework:")
    coursework = models.TextField(help_text="Newline-separated list of courses")
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.degree} - {self.institution}"

    @property
    def coursework_list(self):
        if not self.coursework:
            return []
        return [course.strip() for course in self.coursework.strip().split("\n") if course.strip()]

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ("internship", "Internship"),
        ("research", "Research"),
        ("volunteer", "Volunteer"),
        ("part-time", "Part-Time"),
        ("full-time", "Full-Time"),
        ("freelance", "Freelance"),
        ("organization", "Organization"),
        ("leadership", "Leadership"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    role = models.CharField(max_length=255, blank=True, null=True) # Added to support roles like "Internals Staff"
    description = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES,
        default="full-time",
    )
    skills = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Comma-separated skills/tags",
    )
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def is_ongoing(self):
        return self.ended_at is None

    @property
    def skills_list(self):
        if not self.skills:
            return []
        return [skill.strip() for skill in self.skills.split(",")]

class Competition(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    award = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    date_str = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.award}"

    @property
    def tags_list(self):
        if not self.tags:
            return []
        return [tag.strip() for tag in self.tags.split(",")]