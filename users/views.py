from django.shortcuts import render,redirect
from .models import UserProfile, UserProfiletwo
from .forms import UserForm, UserProfileForms
from django.contrib.auth import login,logout
from django.contrib import messages
from .forms import UserProfileForm,UserForm
from django.contrib.auth.forms import AuthenticationForm

def Home(request):
    return render(request,'user/home.html')

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
            return redirect('home')   

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
            return redirect('home')
        else:
            messages.error(request,'lütfen bilgilerinizi kontrol edin.')
            return redirect('login')
    return render(request,'user/user_login.html',{'form':form})


def user_logout(request):
    messages.success(request, "You Logout!")
    logout(request)
    return render(request,'user/logout.html')


def user_profile(request):
     if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})
