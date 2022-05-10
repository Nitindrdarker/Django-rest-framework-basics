
from django.urls import path
from .views import TaskList, TaskDetail, TaskPost, TaskUpdate, TaskDelete
urlpatterns = [
    path('task-list/', TaskList.as_view(), name='task-list'),
    path('task-detail/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('task-post/', TaskPost.as_view(), name='task-post'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]