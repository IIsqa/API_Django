from rest_framework.permissions import BasePermission

class IsAdminOrReadOnlyForUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'admin':
            return True
        elif request.user.is_authenticated and request.user.role == 'user':
            return request.method != 'DELETE'
        return False