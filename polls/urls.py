from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static


app_name = "polls"
urlpatterns = [
    path('', views.index_view.as_view(), name='index'),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("create_q/", views.create_q, name="create_q"),
]