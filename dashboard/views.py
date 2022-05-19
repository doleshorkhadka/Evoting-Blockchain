from queue import PriorityQueue
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Candidate
from . import functions
from django.contrib import messages
from .forms import FeedbackForm
from officer.models import Election
from accounts.models import Profile

voted = []

@login_required(login_url="/accounts/login")
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url="/accounts/login")
def votes(request):
    is_sts = Election.objects.get(id=1)
    if is_sts.status==True:
        candidates = Candidate.objects.all()
        return render(request, 'vote.html',{'candidates': candidates})
    else:
        return render(request,'noVote.html')
    
# @login_required(login_url="/accounts/submitvote")
def Vote(request,pk):
    # can = Vote.objects.get(pk=pkd)

    Voted_name = Candidate.objects.get(id=pk)
    user_token = Profile.objects.get(user=request.user)
    tok = user_token.token
    try:
        if ( tok in voted):
            return render(request, 'alreadyVoted.html')
        else:
            voted.append(tok)
            hashr = functions.Transactions(Voted_name,user_token.token)
            print(hashr)
            is_sts = Election.objects.get(id=1)
            is_sts.user_sts = True
            is_sts.save()
            return render(request, 'Voted.html')
    except:
        return render(request, 'alreadyVoted.html')
    

def Result(request):
    # is_sts = Election.objects.get(id=1)
    # if is_sts.status==False:
    try:
        result = functions.final_result()
    except:
        return render(request,'noVote.html')
    # result = functions.final_result(request)
    # candidates = functions.final_result()['candidates']
    # return render(request,'Result.html',{ 'result' : result,'candidates':candidates})
    return render(request,'Result.html',{
                        'candidate': result['candidates'],
                        'result': result['result']
                        })
    # else:
    #     return render(request,'noResult.html')
        
    


def Feedback(request):
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return render(request, 'dashboard.html')

    else:
        f = FeedbackForm()
    return render(request, 'contact.html', {'form': f})
