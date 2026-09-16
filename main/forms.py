from django.forms import ModelForm, TextInput, Textarea, URLInput, DateTimeInput
from main.models import Education, Experience, Competition

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "degree",
            "institution",
            "date_range",
            "description_header",
            "coursework",
            "location",
        ]

        labels = {
            "degree": "Degree / Level",
            "institution": "Institution",
            "date_range": "Time Period",
            "description_header": "Description Header",
            "coursework": "Coursework",
            "location": "Location",
        }

        widgets = {
            "degree": TextInput(
                attrs={
                    "placeholder": "Computer Science",
                    "maxlength": 255,
                }
            ),
            "institution": TextInput(
                attrs={
                    "placeholder": "University of Indonesia",
                    "maxlength": 255,
                }
            ),
            "date_range": TextInput(
                attrs={
                    "placeholder": "2025 – Present",
                    "maxlength": 100,
                }
            ),
            "description_header": TextInput(
                attrs={
                    "placeholder": "Coursework:",
                    "maxlength": 255,
                }
            ),
            "coursework": Textarea(
                attrs={
                    "placeholder": "Data Structures\nAlgorithms\nObject-Oriented Programming",
                    "rows": 4,
                }
            ),
            "location": TextInput(
                attrs={
                    "placeholder": "Depok, Indonesia",
                    "maxlength": 255,
                }
            ),
        }


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "role",
            "description",
            "category",
            "skills",
            "ended_at",
        ]

        labels = {
            "title": "Experience Title",
            "role": "Role / Position",
            "description": "Description",
            "category": "Category",
            "skills": "Skills",
            "ended_at": "End Date",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Company or Organization Name",
                    "maxlength": 255,
                }
            ),
            "role": TextInput(
                attrs={
                    "placeholder": "Internal Staff",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Tell us about your experience or responsibilities...",
                    "rows": 4,
                }
            ),
            "skills": TextInput(
                attrs={
                    "placeholder": "Python, Django, Leadership",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    
                }
            ),
            "ended_at": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }
            ),
        }


class CompetitionForm(ModelForm):
    class Meta:
        model = Competition
        fields = [
            "title",
            "award",
            "organizer",
            "location",
            "date_str",
            "description",
            "tags",
        ]

        labels = {
            "title": "Event Name",
            "award": "Award / Position",
            "organizer": "Organizer",
            "location": "Location",
            "date_str": "Date",
            "description": "Description",
            "tags": "Tags",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Freshman Cup 2026",
                    "maxlength": 255,
                }
            ),
            "award": TextInput(
                attrs={
                    "placeholder": "1st Place Winner",
                    "maxlength": 255,
                }
            ),
            "organizer": TextInput(
                attrs={
                    "placeholder": "EDS UI",
                    "maxlength": 255,
                }
            ),
            "location": TextInput(
                attrs={
                    "placeholder": "Depok, Indonesia",
                    "maxlength": 255,
                }
            ),
            "date_str": TextInput(
                attrs={
                    "placeholder": "Jul 2024",
                    "maxlength": 100,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Competition details or achievement specifics...",
                    "rows": 4,
                }
            ),
            "tags": TextInput(
                attrs={
                    "placeholder": "Debate, Public Speaking, Academic",
                }
            ),
        }