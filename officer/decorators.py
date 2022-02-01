from django.shortcuts import redirect
from django.http import HttpResponseRedirect


# def unauthenticated_user(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('dashboard:dash')
#         else:
#             return view_func(request, *args, **kwargs)

#     return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                url = ('/')
                return HttpResponseRedirect(url)
        return wrapper_func
    return decorator




# from django.http import HttpResponse
# from django.shortcuts import redirect

# def admin_only(view_func):
# 	def wrapper_function(request, *args, **kwargs):
# 		group = None
# 		if request.user.groups.exists():
# 			group = request.user.groups.all()[0].name

# 		if group == 'User':
# 			return redirect('dashboard:dash')

# 		if group == 'admin':
# 			return redirect('officer:office')

# 	return wrapper_function

