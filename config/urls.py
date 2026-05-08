"""
URL configuration for config project.

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
# config/urls.py

"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from student.views import (
    HomePageView,
    get_student_list,
    add_student,
    add_student_submit,
    add_student_cancel,
    edit_student,
    edit_student_submit,
    delete_student,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', HomePageView.as_view(), name='home'),

    # Student routes
    path('get_student_list', get_student_list, name='get_student_list'),

    path('add_student', add_student, name='add_student'),
    path('add_student_submit', add_student_submit, name='add_student_submit'),
    path('add_student_cancel', add_student_cancel, name='add_student_cancel'),

    path('<int:student_pk>/edit_student',
         edit_student,
         name='edit_student'),

    path('<int:student_pk>/edit_student_submit',
         edit_student_submit,
         name='edit_student_submit'),

    path('<int:student_pk>/delete_student',
         delete_student,
         name='delete_student'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )