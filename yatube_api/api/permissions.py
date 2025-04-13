from rest_framework import permissions


class AuthorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Require authentication for write actions (POST, PUT, PATCH, DELETE)
        if request.method not in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        return True  # Allow read-only access for unauthenticated users

    def has_object_permission(self, request, view, obj):
        # Allow read access for all, write access only for the author
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
