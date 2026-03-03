from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsCustomer(BasePermission):
    message = "Only customers can access this resource."
    
    def has_permission(self, request, view):
        return request.user.profile_type == "C"
    

class IsVendor(BasePermission):

    message = "Only vendors can access this resource."

    def has_permission(self, request, view):
        return request.user.profile_type == "V"
    

class IsCustomerOrVendor(BasePermission):

    message = "Only Customer and Vendor can access this resource."

    def has_permission(self, request, view):
        return request.user.profile_type == "V" or request.user.profile_type == "C"

class IsVendorOrReadOnly(BasePermission):
    message = "Only vendors can access this resource."

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        return request.user.profile_type == "V"
    

class IsAdminOrReadOnly(BasePermission):
    
    message = "Only Admin can access this resource"

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        return request.user and request.user.is_staff
