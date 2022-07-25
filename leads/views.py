from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Lead


class LeadsListView(ListView):
    model = Lead
    context_object_name = 'leads'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Leads'
        return context


class LeadDetailView(DetailView):
    model = Lead
    context_object_name = 'lead'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lead Details'
        return context


class LeadCreateView(CreateView):
    model = Lead
    fields = ['first_name', 'last_name', 'age', 'agent']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Lead'
        return context


class LeadUpdateView(UpdateView):
    model = Lead
    fields = ['first_name', 'last_name', 'age', 'agent']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Lead'
        return context

    
class LeadDeleteView(DeleteView):
    model = Lead
    
    def get_success_url(self):
        return reverse('lead:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Lead'
        return context
