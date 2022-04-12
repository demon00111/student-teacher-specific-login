
from .forms import UserUpdateForm,ProfileUpdateForm,TeacherForm,UserType
from .models import Profile
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User




# @login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST)
		p_form = ProfileUpdateForm(request.POST)

		if  u_form.is_valid():
			user_form = u_form.save()
		
			if p_form.is_valid(): 	
				gender = p_form.cleaned_data["gender"]
				mobile_number = p_form.cleaned_data['mobile_number']
				hobby = p_form.cleaned_data['hobby']
				dob = p_form.cleaned_data['dob']
				user_type = p_form.cleaned_data['user_type']
				reg = Profile(gender=gender,mobile_number=mobile_number,hobby=hobby,dob=dob,user_type=user_type)
				reg.save()
				
				
				reg.user = user_form
				reg.save()
			
			messages.success(request, f'Your Profile has been Updated Successfully')
			return redirect('profile')
	else:	
		p_form = ProfileUpdateForm()
		u_form = UserUpdateForm()
	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request,'base.html', context)

# def login(request):
#     if request.method == 'POST':
#         user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
#         if user is not None:
#             auth.login(request,user)
#             return render(request,'sdata.html')
#             #return redirect('homepage')
#         else:
#             return render(request,'slogin.html',{'error':'Username Or Password Is Incorrect !'})
#     else:
#         return render(request,'slogin.html')


def loginpage(request):
	if request.method == 'POST':
		l_form = TeacherForm(data = request.POST)
		u_form  = UserType(data = request.POST)
		if l_form.is_valid():
			tmp_user = User.objects.get(username = request.POST['username'])
			user = authenticate(username = request.POST['username'], password = request.POST['password'])
			data = Profile.objects.get(user=tmp_user.id)
			if user is not None:	
				login(request,user)
			if data.user_type == request.POST['user_type']:
				if data.user_type == 'T':
					return HttpResponseRedirect('/tdata')	    
				else:
					return HttpResponseRedirect('/sdata')

			else:
				messages.error(request, "Invalid User type.")
				return HttpResponseRedirect('/login')

	else:
		l_form = TeacherForm()
		u_form  = UserType()

	return render(request,'slogin.html',{'data': l_form,'user_type':u_form})







#     else:
#         return render(request, 'slogin.html', {'data': l_form})
     

        
def sdata(request):
    return render(request,'sdata.html')


def tdata(request):
    return render(request,'tdata.html')