from django.shortcuts import redirect, render, get_object_or_404
from accounts.models import Profile
from accounts.views import address_creation
from dashboard.models import *
from django.contrib.auth.models import User
from .forms import AddCandidate,AddUser
from .decorators import *
from dashboard.functions import add_Candidate
from .models import Election

# Create your views here.
@allowed_users(allowed_roles=['Admin', 'Staff'])
def officer(request):
    is_status = Election.objects.get(id=1)
    can_count = Candidate.objects.all().count()
    user_count = Profile.objects.all().count()
    quary_count = Feedback.objects.all().count()
    return render(request, 'officer/officer.html', {
        'cancount':can_count,
        'usercount':user_count,
        'quarycount':quary_count,
        'status': is_status.status
        })

@allowed_users(allowed_roles=['Admin', 'Staff'])
def candidate(request):
    can_data = Candidate.objects.all()
    return render(request, 'officer/candidate.html', {
        'candata':can_data
    })

@allowed_users(allowed_roles=['Admin', 'Staff'])
def add_candidate(request):
    fm = AddCandidate(request.POST)
    if fm.is_valid():
        fm.save()
        return redirect('/officer/candidates')
    else:
        return render(request, 'officer/add-candidate.html', {'form':fm})

@allowed_users(allowed_roles=['Admin', 'Staff'])
def delete_candidate(request):
    data = request.POST
    id = data.get('id')
    canddata = Candidate.objects.get(id=id)
    canddata.delete()
    return redirect('/officer/candidates')

# def edit_candidate(request, id):
#     cand = Candidate.objects.get(id=id)
#     fm = AddCandidate(request.POST)
#     return render(request, 'edit-candidate.html', {'form':fm})
#     if fm.is_valid():
#         fm.save()
#         return redirect('/officer')

@allowed_users(allowed_roles=['Admin', 'Staff'])
def edit_candidate(request, id):
    context ={}
    obj = get_object_or_404(Candidate, id = id)
    form = AddCandidate(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return redirect('/officer/candidates')

    context["form"] = form
    return render(request, "officer/edit-candidate.html", context)


# USER CRUD OPERATIONS
@allowed_users(allowed_roles=['Admin', 'Staff'])
def realuser(request):
    user_data = User.objects.all()
    return render(request, 'officer/user.html', {
        'userdata':user_data
    })

@allowed_users(allowed_roles=['Admin', 'Staff'])
def add_user(request):
    fm = AddUser(request.POST)
    if fm.is_valid():
        fm.save()
        return redirect('/officer/users')
    else:
        return render(request, 'officer/add-user.html', {'form':fm})

@allowed_users(allowed_roles=['Admin', 'Staff'])
def delete_user(request):
    data = request.POST
    id = data.get('id')
    userdata = User.objects.get(id=id)
    userdata.delete()
    return redirect('/officer/users')

@allowed_users(allowed_roles=['Admin', 'Staff'])
def edit_user(request, id):
    context ={}
    obj = get_object_or_404(User, id = id)
    form = AddUser(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return redirect('/officer/users')

    context["form"] = form
 
    return render(request, "officer/edit-user.html", context)

@allowed_users(allowed_roles=['Admin', 'Staff'])
def quaries(request):
    quaries_data = Feedback.objects.all()
    return render(request, 'officer/contact_res.html', {
        'quariesdata':quaries_data
    })

@allowed_users(allowed_roles=['Admin', 'Staff'])
def quarysolved(request):
    data = request.POST
    id = data.get('id')
    quariesdata = Feedback.objects.get(id=id)
    quariesdata.delete()
    return redirect('/officer/quaries')

@allowed_users(allowed_roles=['Admin', 'Staff'])
def Approved_candidate(request):
    print("Approving candidate...")
    candidate = Candidate.objects.all()
    add_Candidate(candidate)
    print("Candidate Approved...")

@allowed_users(allowed_roles=['Admin', 'Staff'])
def start_election(request):
    address_creation()
    Approved_candidate(request)
    return redirect('/officer/')

@allowed_users(allowed_roles=['Admin', 'Staff'])
def end_election(request):
    is_sts = Election.objects.get(id=1)
    is_sts.status = False
    is_sts.isCandidateAdded = False
    is_sts.save()
    return redirect('/officer/')


