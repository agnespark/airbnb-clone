from django.urls import path
from rooms import views as room_views

app_name = "core"

urlpatterns = [
    path(
        "", room_views.HomeView.as_view(), name="home"
    ),  # function이 아닌, class based view에선 as_view()를 사용
    # path("", room_views.all_rooms, name="home"),
]
