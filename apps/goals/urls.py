from django.urls import path
from .views import GoalListCreateView, GoalDetailView

urlpatterns = [
    path('', GoalListCreateView.as_view(), name='goal_list_create'),
    path('<int:pk>/', GoalDetailView.as_view(), name='goal_detail'),
]