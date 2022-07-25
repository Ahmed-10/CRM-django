from django.urls import path
from . import views

app_name = "lead"

urlpatterns = [
    path('', views.LeadsListView.as_view(), name='list'),
    path('create/', views.LeadCreateView.as_view(), name='create'),
    path('<int:pk>/update', views.LeadUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.LeadDeleteView.as_view(), name='delete'),
    path('<pk>/', views.LeadDetailView.as_view(), name='detail'),
]
