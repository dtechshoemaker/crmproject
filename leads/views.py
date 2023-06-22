from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Agent, Lead
from .forms import LeadForm, SignupForm

def leads_list(request):
    Agents = Agent.objects.all()
    Leads = Lead.objects.all()
    context = {
        'Leads':Leads,
        'Agents':Agents
    }
    return render(request, 'home_page.html', context)

def lead_detail(request, new_test):
    lead_detail = Lead.objects.get(id=new_test)
    context = {
        'lead_detail':lead_detail,
    }
    return render(request, 'detail_page.html', context)


def createLead(request):
    form = LeadForm()
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    else:
        form = LeadForm()
        context = {"form":form}
    return render(request, 'createform.html',  context)

def updateLead(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadForm(instance=lead)
    
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid:
            form.save()
            return redirect('/')
    context = { 'form':form}
    return render(request, 'createform.html', context)


def deleteLead(request, pk):
    lead = Lead.objects.get(id=pk)
    if request.method == 'POST':
        lead.delete()
        return redirect('/')
    context = {'lead':lead}
    return render(request,'delete.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid:
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm
    context = {
        'form':form
    }
    return render(request, 'auth/signup.html', context)
