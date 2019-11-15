"""recipe URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from recipe import views
from recipe.models import Author, RecipeItem
from django.conf import settings
from django.conf.urls.static import static

admin.site.register(Author)
admin.site.register(RecipeItem)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),
    path('recipes/<int:id>/', views.recipe_view, name='recipepage'),
    path('author/<int:id>/', views.author_view, name='authorpage'),
    path('recipeadd/', views.addrecipeview, name='recipeadd'),
    path('authoradd/', views.addauthorview, name='authoradd'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)