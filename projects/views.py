from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import Request
from .models import Project
from .serializers import ProjectSerializer
from techs.models import Tech
from users.permissions import IsSuperUser

# Create your views here.


class ProjectView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def create(self, request: Request, *args, **kwargs):
        request_techs_data = request.data.pop("techs")
        tech_list = []

        for tech_id in request_techs_data:
            try:
                find_tech = Tech.objects.get(pk=tech_id)
                tech_list.append(find_tech)
            except Tech.DoesNotExist:
                pass

        self.kwargs["techs"] = tech_list

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return self.perform_create(serializer)

    def perform_create(self, serializer):
        return serializer.save(techs=self.kwargs["techs"])


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def update(self, request: Request, *args, **kwargs):
        instance = self.get_object()
        partial = kwargs.pop("partial", False)

        try:
            request_techs_data = request.data.pop("techs")
            tech_list = []

            for tech_id in request_techs_data:
                try:
                    find_tech = Tech.objects.get(pk=tech_id)
                    tech_list.append(find_tech)
                except Tech.DoesNotExist:
                    pass

            self.kwargs["techs"] = tech_list
        except Exception:
            pass

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        return self.perform_update(serializer)

    def perform_update(self, serializer):
        try:
            return serializer.save(techs=self.kwargs["techs"])
        except Exception:
            return serializer.save()
