"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from allauth.account.views import ConfirmEmailView
from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/fitness_clubs/", include("fitness_clubs.urls")),  # Аутентификация
    path("api/v1/trainers/", include("trainers.urls")),
    path("api/v1/clients/", include("clients.urls")),  # Профиль, документы, здоровье
    path("api/v1/payments/", include("payments.urls")),  # Блог
    # Swagger JSON
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Redoc
    path('api/v1/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/v1/auth/', include('dj_rest_auth.urls')),
    re_path(
		"^registration/account-confirm-email/(?P<key>[-:\w]+)/$",
		ConfirmEmailView.as_view(),
		name="account_confirm_email",
	),
	path('api/v1/auth/registration/', include('dj_rest_auth.registration.urls')),

]
