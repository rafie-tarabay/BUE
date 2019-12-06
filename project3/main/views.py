from django.shortcuts import render
from .models import MarcTemplate
from django.views import generic

class MarcTemplateList(generic.ListView):
    template_name='main/marctemplate_list.html'
    context_object_name='All_MarcTemplate'

    def get_queryset(self):
        return MarcTemplate.objects.all()

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
class MarcTemplateAddView(CreateView):
    model=MarcTemplate
    template_name = 'main/marctemplate_form.html'
    success_url=reverse_lazy('main:marctemplatelist')
    fields=['MarcTemplateTitle','biblio_type_id','Description','jsonObject']

class MarcTemplateUpdateView(UpdateView):
    model=MarcTemplate
    template_name = 'main/marctemplate_form.html'
    success_url=reverse_lazy('main:marctemplatelist')

    fields=['MarcTemplateTitle','biblio_type_id','Description','jsonObject']

class MarcTemplateDeleteView(DeleteView):
    model=MarcTemplate
    success_url=reverse_lazy('main:marctemplatelist')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


        