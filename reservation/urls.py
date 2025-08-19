from django.urls import path

from . import views


app_name='reservation'
urlpatterns = [
    path('reservation_list/', views.ReservationListView.as_view(), name='reservation_list'),
    path(
        'reservation_list/make_reservation/<int:year>/<int:month>/<int:day>/',
        views.MakeReservationView.as_view(),
        name='make_reservation'
    ),
    path('user_reservation/', views.UserReservationView.as_view(), name='user_reservation'),
    path(
        'user_reservation/delete/<str:natid>/',
        views.ReservationDeleteView.as_view(),
        name='reservation_delete'
    ),
    path(
        'user_reservation/delete_done/<str:natid>/',
        views.ReservationDeleteDoneView.as_view(),
        name='reservation_delete_done'
    )
]
