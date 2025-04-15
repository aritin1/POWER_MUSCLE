from django.urls import path

from .views import WorkoutListView, DetailView, AuthorCreateView, WorkoutCreateView

urlpatterns = [
    # path('books', BookListApiView.as_view(), name='book-list-view'),
    # path('book/<int:pk>', BookDetailApiView.as_view(), name='book-detail-view')
    path('list', WorkoutListView.as_view(), name='books-list'),
    path('detail/<int:pk>', DetailView.as_view(), name='workout-detail'),
    path('author-create', AuthorCreateView.as_view(), name='author-create'),
    path('workout-create', WorkoutCreateView.as_view(), name='workout-create')
]