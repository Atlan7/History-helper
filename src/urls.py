"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from .views import AboutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AboutView.as_view(), name='about-site'),
    path('articles/', include(('articles.urls', 'articles'), namespace='articles')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('quizes/', include(('quizes.urls', 'quizes'), namespace='quizes')),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    urlpatterns += static(
        settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
    )
