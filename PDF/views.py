from django.shortcuts import render, redirect
from .forms import CvForm
from .models import Profile
from django.contrib import messages

import io 
import pdfkit  # type: ignore
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request): 
    if request.method == "POST": 
        form = CvForm(request.POST)
        if form.is_valid(): 
            profile = Profile(
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                phone = form.cleaned_data['phone'],
                summary = form.cleaned_data['summary'],
                degree = form.cleaned_data['degree'],
                school = form.cleaned_data['school'],
                university = form.cleaned_data['university'],
                previous_work = form.cleaned_data['previous_work'],
                skills = form.cleaned_data['skills']
            )
            profile.save()
            messages.success(request, 'successfully added, cv is currently being generated')
            return redirect('home')
        else: 
            messages.error(request, 'Fill All fields')

    return render(request, 'pdf/accept.html')


def resume(request, id): 
    user_profile = Profile.objects.get(pk=id)

    tremplate = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile': user_profile})
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
    }


    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['content-Disposition'] = 'attachment'
    filename = 'resume.pdf'
    
    return  response