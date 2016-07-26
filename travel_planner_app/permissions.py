from rest_framework import permissions

class IsOwnerOrReadONly(permissions.BasePermission):
	"""
	custom permission to only allow owners of an object to edit it
	"""

	def has_object_permission(self, request, view, obj):
		# Read permissions are allowed to any request
		#always allow GET, HEAD or OPTIONS request
		if request.method in permissions.SAFE_METHODS:
			return true

		#write permissions are only allowed to the owner
		return obj.owner==request.user