from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views import View
from . forms import UserCreateForm
from . models import UserDetail

# Create your views here.
class loginDone(View):
    
    def get(self, request, *args, **kwargs):
        if UserDetail.objects.filter(name=request.user).count()>0:
            
            notExist = False
            userDetail = UserDetail.objects.get(name=request.user)

            contents = {
                "notExist":notExist,
                "userDetail":userDetail
            }
            return render(request, "registration/index.html", {"contents":contents})
        else:
            notExist = True
            contents = {
                "notExist":notExist,
            }
            return render(request, "registration/index.html", {"contents":contents}) 
    
    def post(self, request, *args, **kwargs):
        #if UserDetail.objects.filter(name=request.user).count()>0:
        #    return redirect("registration/login_done/")
        #else:    
        grade = request.POST.get("grade")
        schoolId = request.POST.get("schoolId")
        position = request.POST.get("position")
            
        userDetail = UserDetail(name=request.user, schoolId=schoolId, grade=grade, position=position)
        userDetail.save()
            
        notExist = False
        userDetail = UserDetail.objects.get(name=request.user)

        contents = {
            "notExist":notExist,
            "userDetail":userDetail
        }
        return render(request, "registration/index.html", {"contents":contents}) 

class CreateAccount(View):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, "registration/create_account.html", {'form': form,}) 

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        return render(request, "registration/create_account.html", {'form': form,})

create_account = CreateAccount.as_view()
login_done = loginDone.as_view() 