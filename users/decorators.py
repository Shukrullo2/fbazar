from django.http import HttpResponseForbidden

def user_is_active(view_func):
    def _wrapped_view(request, *args, **kwargs):
        # Check if the user is authenticated and active
        if request.user.is_authenticated and request.user.is_active:
            return view_func(request, *args, **kwargs)
        else:
            # If not active, return a forbidden response
            return HttpResponseForbidden("You don't have permission to access this page.")

    return _wrapped_view