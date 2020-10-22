from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated(view_func):
    def wrapper(request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect('main:projects')
        
        return view_func(request, *args, **kwargs)

    return wrapper


def allowed_users(allowed_roles = []):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):

            flag = False

            if request.user.groups.exists():
                group = list(request.user.groups.values_list('name',flat = True))
                for i in group:
                    if i in allowed_roles:
                        flag = True
                        break 
            
            if flag:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You aren't allowed to view this page")
            
        return wrapper
    return decorator