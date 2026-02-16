from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsCustomer(BasePermission):
    message = "Only customers can access this resource."
    
    def has_permission(self, request, view):
        print("In Customer permission")
        return request.user.profile_type == "C"
    

class IsVendor(BasePermission):

    message = "Only vendors can access this resource."

    def has_permission(self, request, view):
        print("In Vendor Permisison")
        return request.user.profile_type == "V"
    

class IsVendorOrReadOnly(BasePermission):
    message = "Only vendors can access this resource."

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        return request.user.profile_type == "V"