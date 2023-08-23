from rest_framework import permissions

class IsOwnerOrPublic(permissions.BasePermission):
    """
    Custom permission to allow access to PUT and DELETE only for the owner of the post/blog
    and GET access if the post/blog is public or if the user is the owner.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # GET is safe, allow it if the post/blog is public or if the user is the owner
            return obj.is_public or obj.owner == request.user
        # Only allow PUT and DELETE if the user is the owner
        return obj.owner == request.user