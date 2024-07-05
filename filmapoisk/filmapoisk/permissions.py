from rest_framework import permissions

class IsAuthorUser(permissions.BasePermission):
    message = 'User is not author of object.'

    def has_permission(self, request, view):
        return not request.method == 'POST'

    def has_object_permission(self, request, view, obj):
        return (
            request.method in {'PUT', 'PATCH', 'DELETE'}
            and request.user.is_authenticated
            and obj.author == request.user
        )
