from rest_framework import permissions

class IsManager(permissions.BasePermission):
  def has_permission(self, request, view):
    return request.user.role == 'manager'

class IsAdmin(permissions.BasePermission):
  def has_permission(self, request, view):
    return request.user.role == 'admin'

class IsUser(permissions.BasePermission):
  def has_permission(self, request, view):
    return request.user.role   == 'user'