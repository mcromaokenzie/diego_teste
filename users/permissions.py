from rest_framework import permissions
from .models import User
from rest_framework.views import View, Request


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        users = User.objects.all()

        if len(users) <= 0:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and request.user.is_superuser
