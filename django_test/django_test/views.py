from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf

from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail
from django.core.mail import send_mail, BadHeaderError

from django.template import Context,RequestContext
from django import forms

from django.shortcuts import render
from django_test.forms import ProfileForm









def show_profileform(request):
	
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProfileForm(request.POST)
		
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thankyou/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProfileForm()

    return render(request, 'profileform.html', {'form': form})
	
def thankyou(request):
	return render_to_response('thankyou.html')
	
def home(request):
	return render_to_response('home.html')
	
	


	



	
	

	
	

	
	

			
		

	
	
					
		
	
	
	
	