from rest_framework.permissions import BasePermission
class IsAdminOrManager(BasePermission):
  def has_Permission(self,request,view):
    return request.user.is_authenticated and request.user.role in['Cashier','Admin']
    
