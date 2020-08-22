from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated(view_func):
    def wrapper(request, *args, **kwargs):

        if request.user.is_authenticated:
            group = list(request.user.groups.values_list('name',flat = True))

            if 'Admin' in group:
                return redirect('main:adminpage')

            elif 'Project Manager' in group:
                return redirect('main:pmpage')
            
            elif 'Developer' in group:
                return redirect('main:devpage')

            elif 'Tester' in group:
                return redirect('main:testerpage')

        return view_func(request, *args, **kwargs)

    return wrapper