from django.shortcuts import render
from .models import Agent, Lead

def leads_list(request):
    
    Agents = Agent.objects.all()
    Leads = Lead.objects.all()

    context = {
        'Leads':Leads,
        'Agents':Agents
    }


    return render(request, 'home_page.html', context)