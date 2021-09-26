from rest_framework import permissions


class OwnerOrSafeMethods(permissions.BasePermission):
    message = 'У вас недостаточно прав для выполнения данного действия.'

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user
                )
#
#
# class Anonymous(permissions.BasePermission):
#     message = 'Учетные данные не были предоставлены.'
#
#     def has_permission(self, request, view):
#         return request.user.is_authenticated
