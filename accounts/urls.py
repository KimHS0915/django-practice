from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views
from . import forms

urlpatterns = [
	path('login/', LoginView.as_view(
		form_class = forms.LoginForm,
		template_name = 'accounts/login_form.html'), 
		name='login'),
	path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
	path('profile/', views.profile, name='profile'),
	path('profile/edit', views.profile_edit, name='profile_edit'),
	path('register/', views.register, name='register'),
]