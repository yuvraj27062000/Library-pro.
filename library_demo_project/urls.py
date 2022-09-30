"""library_demo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from testApp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view),
    path('login/', views.AdminLogin),
    path('logout/', views.Adminlogout),
    path('showbooks/', views.showbook_view),
    path('addbook/', views.AddBook_view),
    path('signup/', views.signup_view),
    path('delete/<id>', views.delete_view),
    path('alldata/', views.showStudent_view),
    path('delete1/<id>', views.delete_view1),
    path('delete2/<id>', views.delete_view2),
    path('issuebook/', views.Book_issue_view),
    path('showissuebook/<id>', views.showAloteBooks_view),
    path('update/<id>', views.update_Book_issue_view),
    path('calculate/<id>', views.calculate_Book_fine_view),
    # path('showissuebook/<id>', views.Search_Student_view),
    # path('accounts/', include('django.contrib.auth.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# showbook_view AddBook