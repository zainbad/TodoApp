from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns=[

path('home/', views.home, name='home'),
path('todo/<int:pk>', views.list_tasks, name='list_tasks'),
path('todo/<int:pk>/task', views.add_task, name='add_task_ajax'),
path('list/', views.add_list, name='add_list_ajax'),
path('task/<int:pk>', views.done_task, name='done_task'),
path('task/completed', views.complete_task, name='complete_task'),

path('', views.loginPage, name='login'),
path('register/', views.registerPage, name='register'),

path('delete/list/<int:pk>', views.delete_list, name='delete_list'),
path('delete_done/list/<int:pk>', views.delete_list_done, name='delete_list_done'),

path('done/task/', views.done_task_ajax, name='done_task_ajax'),

path('profile/<int:pk>', views.profile, name='profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)