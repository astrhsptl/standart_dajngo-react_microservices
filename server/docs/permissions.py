from rest_framework.permissions import BasePermission

class IsOwnerPermission(BasePermission):
    '''This permission check get permission for files (user is owner or not)'''
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author