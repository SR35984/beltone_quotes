from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from ..login_reg_app.models import User
from .models import Quote

def current_user(request):
	return User.objects.get(id=request.session['user_id'])

def flash_errors(request, errors):
	for error in errors:
		messages.error(request, error)

def index(request):
	user = current_user(request)
	context= {
		'user' : user
	}
	return render(request, 'quotes_app/index.html', context)

def create(request):
	if request.method == "POST":
		errors = Quote.objects.validate(request.POST) 

		if not errors:
			user = current_user(request)
			quote = Quote.objects.create_quote(request.POST)
	
		flash_errors(request, errors)
	return redirect(reverse('add_book')) 
	
def logout(request):
    print "********** logout *************** "
    return redirect(reverse('landing'))