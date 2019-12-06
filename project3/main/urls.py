from django.urls import path
from . import views

app_name="main"

urlpatterns = [
path('marctemplatelist/', views.MarcTemplateList.as_view(), name='marctemplatelist'),
path('marctemplate/add/', views.MarcTemplateAddView.as_view(), name='marctemplate-add'),
path('marctemplate/update/<int:pk>/', views.MarcTemplateUpdateView.as_view(), name='marctemplate-edit'),
path('marctemplate/delete/<int:pk>/', views.MarcTemplateDeleteView.as_view(), name='marctemplate-delete'),

]
