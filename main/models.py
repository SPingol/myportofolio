import uuid
from django.db import models


class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    degree = models.CharField(max_length=255)                  # Ex: "Ilmu Komputer KKI"
    institution = models.CharField(max_length=255)             # Ex: "Universitas Indonesia"
    date_range = models.CharField(max_length=100)              # Ex: "2025 – Present"
    description_header = models.CharField(max_length=255, default="Coursework:")
    coursework = models.TextField(help_text="Newline-separated list of courses")
    location = models.CharField(max_length=255, blank=True, null=True) # Ex: "Depok, Indonesia"

    def __str__(self):
        return f"{self.degree} - {self.institution}"

    @property
    def coursework_list(self):
        """Splits newline-separated coursework into an iterable list for templates."""
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
    role = models.CharField(max_length=255, blank=True, null=True) # Ex: "Internals Staff"
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
        """Splits comma-separated skills into an iterable list for templates."""
        if not self.skills:
            return []
        return [skill.strip() for skill in self.skills.split(",")]


class Competition(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)                # Ex: "Freshman Cup 2026"
    award = models.CharField(max_length=255)                # Ex: "Co-9th Best Speaker" or "1st Place Winner"
    organizer = models.CharField(max_length=255)            # Ex: "EDS UI"
    location = models.CharField(                            # Ex: "New Haven", "United States"
        max_length=255, 
        blank=True, 
        null=True
    )
    date_str = models.CharField(                            # Ex: "Jul 2024" or "2026"
        max_length=100, 
        help_text="Display date string like 'Jul 2024' or '2026'"
    )
    description = models.TextField()                        # Event details or list of medals
    tags = models.CharField(                                # Comma-separated tag list
        max_length=255, 
        blank=True, 
        null=True, 
        help_text="Comma-separated tags (e.g. Debate, Public Speaking, Academic)"
    )

    def __str__(self):
        return f"{self.title} - {self.award}"

    @property
    def tags_list(self):
        """Splits comma-separated tags into a clean list for templates."""
        if not self.tags:
            return []
        return [tag.strip() for tag in self.tags.split(",")]