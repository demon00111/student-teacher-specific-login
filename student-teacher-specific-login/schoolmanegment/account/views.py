
from .forms import UserUpdateForm,ProfileUpdateForm,TeacherForm
from .models import Profile
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User


# id_instance = id_profile


# @login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST)
		p_form = ProfileUpdateForm(request.POST,request.FILES)


		if  u_form.is_valid():
			user_form = u_form.save()
			if p_form.is_valid(): 	
				gender = p_form.cleaned_data["gender"]
				mobile_number = p_form.cleaned_data['mobile_number']
				hobby = p_form.cleaned_data['hobby']
				dob = p_form.cleaned_data['dob']
				user_type = p_form.cleaned_data['user_type']
				caption = p_form.cleaned_data['caption']
				video = request.FILES['video']
				reg = Profile(gender=gender,mobile_number=mobile_number,hobby=hobby,dob=dob,user_type=user_type,caption=caption,video=video)
				# print("!!!!!!!!!!!!!!!!!!!!!!!!1111111111111111",reg)
				reg.user = user_form
				# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!',user_form)
				reg.save()	
				
			
				messages.success(request, f'Your Profile has been Updated Successfully')
				return redirect('profile')


	else:	
		p_form = ProfileUpdateForm()
		u_form = UserUpdateForm()

	context = {
		'u_form': u_form,
		'p_form': p_form,
	}
	return render(request,'base.html', context)




def loginpage(request):
	if request.method == 'POST':
		l_form = TeacherForm(data = request.POST)
		if l_form.is_valid():
			user = authenticate(username = request.POST['username'], password = request.POST['password'])
			tmp_user = User.objects.get(username = request.POST['username'])
			data = Profile.objects.get(user=tmp_user.id)
			# global id_profile
			# id_profile = data
			# p_form = ProfileUpdateForm(instance=data)
			# print('+++++++++++++++++++++++++++++++',p_form)
			if user is not None:	
				login(request,user)
				if data.user_type == 'T':
					
					video_id= Profile.objects.get(pk=data.id)
	 
					video= Profile.objects.filter(id = video_id.id).values_list('video','caption')
					# print("!!!!!!!!!!!!!!!!!!!!!!!!!!..//./././././././",video[0])
					print("!!!!!!!!!!!!!!!!!!!!!!!!!!..//./././././././",video[0][0])
					if video != None:
						return render(request,'tdata.html',{'videos':video[0][0],'captions':video[0][1]})
					else:
						return render(request,'tdata.html')


				elif data.user_type == 's':
					return HttpResponseRedirect('/sdata')

				else:
					messages.error(request, "Invalid User type.")
					return HttpResponseRedirect('/login')

	else:
		l_form = TeacherForm()

	return render(request,'slogin.html',{'data': l_form})

        
def sdata(request):
    return render(request,'sdata.html')


def tdata(request):
    return render(request,'tdata.html')


def edit(request):
	std = Profile.objects.all()
	user_from = User.objects.all()


	return render(request,'update.html',{'form1':std,'form2':user_from})



def iteams(request, id):

	if request.method == 'POST':
		std = Profile.objects.get(pk=id)
		reg = User.objects.get(pk=std.user.id)

		p_form = ProfileUpdateForm(request.POST,instance=std)
		user_from = UserUpdateForm(request.POST,instance=reg)

		if p_form.is_valid() and user_from.is_valid():
			p_form.save()
			user_from.save()
			return redirect('edit')

	else:
		std = Profile.objects.get(pk=id)
		reg = User.objects.get(pk=std.user.id)
		
		user_from = UserUpdateForm(instance=std.user)

		p_form = ProfileUpdateForm(instance=std)


		return render(request, 'edit.html',{'form1':p_form ,'form2':user_from})		