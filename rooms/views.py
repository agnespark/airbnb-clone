from math import ceil
import queue
from django.shortcuts import render, redirect

# from django.core.paginator import Paginator, EmptyPage
# from django.utils import timezone
from django.views.generic import ListView, DetailView
from django_countries import countries
from . import models, forms

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


def search(request):

    form = forms.SearchForm()

    return render(request, "rooms/search.html", {"form": form})


# form 사용하지 않는 코드
# def search(request):
# city = request.GET.get("city", "Anywhere")
# city = str.capitalize(city)
# country = request.GET.get("country", "KR")
# room_type = int(request.GET.get("room_type", 0))
# price = int(request.GET.get("price", 0))
# guests = int(request.GET.get("guests", 0))
# bedrooms = int(request.GET.get("bedrooms", 0))
# beds = int(request.GET.get("beds", 0))
# baths = int(request.GET.get("baths", 0))
# instant = bool(request.GET.get("instant", False))
# superhost = bool(request.GET.get("superhost", False))
# s_amenities = request.GET.getlist("amenities")
# s_facilities = request.GET.getlist("facilities")

# room_types = models.RoomType.objects.all()
# amenities = models.Amenity.objects.all()
# facilities = models.Facility.objects.all()

# form = {
#     "city": city,
#     "s_room_type": room_type,
#     "s_country": country,
#     "price": price,
#     "guests": guests,
#     "bedrooms": bedrooms,
#     "beds": beds,
#     "baths": baths,
#     "s_amenities": s_amenities,
#     "s_facilities": s_facilities,
#     "instant": instant,
#     "superhost": superhost,
# }

# choices = {
#     "countries": countries,
#     "room_types": room_types,
#     "amenities": amenities,
#     "facilities": facilities,
# }

# filter_args = {}

# if city != "Anywhere":
#     filter_args["city__startswith"] = city

# filter_args["country"] = country

# if room_type != 0:
#     filter_args["room_type__pk__exact"] = room_type

# if price != 0:
#     filter_args["price__lte"] = price

# if guests != 0:
#     filter_args["guests__gte"] = guests

# if bedrooms != 0:
#     filter_args["bedrooms__gte"] = bedrooms

# if beds != 0:
#     filter_args["beds__gte"] = beds

# if baths != 0:
#     filter_args["baths__gte"] = baths

# if instant is True:
#     filter_args["instant_book"] = True

# if superhost is True:
#     filter_args["host__superhost"] = True

# if len(s_amenities) > 0:
#     for s_amenities in s_amenities:
#         rooms = rooms.filter(amenities__pk=int(s_amenities))

# if len(s_facilities) > 0:
#     for s_facilities in s_facilities:
#         rooms = rooms.filter(s_facilities=int(s_facilities))

# rooms = models.Room.objects.filter(**filter_args)

# return render(
#     request,
#     "rooms/search.html",
#     {**form, **choices, "rooms": rooms},
# )


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
