from django.shortcuts import render,redirect
from .models import UserProfile
from .forms import UserForm, UserUpdateForm,UserProfileForm
from django.contrib.auth import login,logout
from django.contrib import messages
from .forms import UserProfileForm,UserForm
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    form_user = UserForm()
    form_profile = UserProfileForm()

    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_profile = UserProfileForm(request.POST,request.FILES)

        if form_profile.is_valid()  and form_user.is_valid():
            user = form_user.save() 
            profile = form_profile.save(commit=False) #! tüm bılgılerı al olustur ama henuz db kaydetme
            profile.user = user   #! userın kım olacagını belırledık. profile içinde user vardı.
            profile.save()  #! kaydettik.
            login(request,user) #! şuanki kullanıcı bılgılerıne gore login işlemi yap.
            messages.success(request,'Register Succesfull')
            return redirect('list')   

    context = {
        "form_user" : form_user,
        "form_profile" : form_profile
    }
    return render(request,'user/register.html',context)



def user_login(request):
    form = AuthenticationForm(request,data=request.POST) 
    #! form dolu geldıyse bılgılerı otomatık ıcıne  koyar. AuthenticationForm'a özel 
    if form.is_valid():
        user = form.get_user() #! formun ıcındekı bılgılerı aldım...  AuthenticationForm has komut...
        if user:
            messages.success(request,'login successfull')
            login(request,user)
            return redirect('list')
        else:
            messages.error(request,'lütfen bilgilerinizi kontrol edin.')
            return redirect('login')
    return render(request,'user/user_login.html',{'form':form})


def user_logout(request):
    messages.success(request, "You Logout!")
    logout(request)
    return render(request,'user/logout.html')



def user_profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    form = UserUpdateForm(instance=profile)
    form_profile = UserProfileForm(instance=profile)
    if request.method == 'POST':
        form = UserProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('list')


    context = {
        "form" : form,
        "form_profile" : form_profile,
        'user' : user,
        "profile" : profile
    }
    return render(request,'user/profile.html',context)