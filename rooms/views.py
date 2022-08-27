from math import ceil

# from django.shortcuts import render, redirect
# from django.core.paginator import Paginator, EmptyPage
# from django.utils import timezone
from django.views.generic import ListView, DetailView

# from django.http import Http404
# from django.urls import reverse
from . import models

# 3. class based view
class HomeView(ListView):

    """HomeView Denifition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"
    # page_kwarg = "page"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     now = timezone.now()
    #     context["now"] = now
    #     return context


# 5. class based view - room detail
class RoomDetail(DetailView):

    """RoomDetail Definition"""

    model = models.Room


# 4. function based view - room detail
# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {"room": room})
#     except models.Room.DoesNotExist:
#         raise Http404()


# 2. use paginator
# def all_rooms(request):
#     page = request.GET.get("page", 1)
#     room_list = models.Room.objects.all()  # 그냥 쿼리셋을 생성할 뿐, 즉시 호출하지는 않음
#     paginator = Paginator(room_list, 10, orphans=5)  # 페이지당 리스트 갯수 = 10
#     try:
#         rooms = paginator.page(int(page))
#         return render(request, "rooms/home.html", {"page": rooms})
#     except EmptyPage:
#         return redirect("/")


# 1. pagination 하드코딩방법
# def all_rooms(request):
#     page = request.GET.get("page", 1) #page가 없다면 기본값으로 1을 넘겨라
#     page = int(page or 1)
#     page_size = 10
#     limit = page_size * page
#     offset = limit - page_size
#     all_rooms = models.Room.objects.all()[offset:limit]
#     page_count = ceil(models.Room.objects.count() / page_size)
#     return render(
#         request,
#         "rooms/home.html",
#         context={
#             "rooms": all_rooms,
#             "page": page,
#             "page_count": page_count,
#             "page_range": range(1, page_count),
#         },
#     )
