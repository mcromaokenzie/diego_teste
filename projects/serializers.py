from rest_framework import serializers
from rest_framework.views import Response
from rest_framework.validators import UniqueValidator
from .models import Project
from techs.serializers import TechSerializer
from django.forms.models import model_to_dict


class ProjectSerializer(serializers.ModelSerializer):
    repository = serializers.URLField(
        validators=[
            UniqueValidator(
                queryset=Project.objects.all(),
                message="A project with that repository already exists",
            )
        ]
    )

    techs = TechSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "repository",
            "link_deploy",
            "img",
            "created_at",
            "techs",
        ]

        read_only_fields = ["id", "created_at"]

    def create(self, validated_data: dict):

        techs = validated_data.pop("techs")

        new_project = Project.objects.create(**validated_data)

        for tech in techs:
            new_project.techs.add(tech)

        new_project.save()

        serializer = ProjectSerializer(instance=new_project)

        return Response(serializer.data)
