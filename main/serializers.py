from django.utils.html import strip_tags
from rest_framework import serializers
from main.models import Project, Experience, Education, Competition

class BasePortfolioSerializer(serializers.ModelSerializer):
    """Base serializer providing computed star fields for all portfolio items."""
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())


class ProjectSerializer(BasePortfolioSerializer):
    class Meta:
        model = Project
        fields = [
            "id", "title", "description", "tech_stack",
            "project_url", "project_image_url",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        return strip_tags(value)

    def validate_tech_stack(self, value):
        return strip_tags(value)


class ExperienceSerializer(BasePortfolioSerializer):
    skills_list = serializers.ReadOnlyField()
    
    class Meta:
        model = Experience
        fields = [
            "id", "title", "role", "description", "category", "skills", 
            "thumbnail", "duration", "skills_list",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_role(self, value):
        return strip_tags(value) if value else value

    def validate_description(self, value):
        return strip_tags(value)

    def validate_category(self, value):
        return strip_tags(value) if value else value


class EducationSerializer(BasePortfolioSerializer):
    coursework_list = serializers.ReadOnlyField()

    class Meta:
        model = Education
        fields = [
            "id", "degree", "institution", "date_range", 
            "description_header", "coursework", "location", "coursework_list",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_degree(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Degree cannot be empty.")
        return value

    def validate_institution(self, value):
        return strip_tags(value)

    def validate_coursework(self, value):
        return strip_tags(value)


class CompetitionSerializer(BasePortfolioSerializer):
    tags_list = serializers.ReadOnlyField()

    class Meta:
        model = Competition
        fields = [
            "id", "title", "award", "organizer", "location", 
            "date_str", "description", "tags", "tags_list",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_award(self, value):
        return strip_tags(value)

    def validate_description(self, value):
        return strip_tags(value)