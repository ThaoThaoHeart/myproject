from django.urls import path

from . import views

urlpatterns = [
    path('globalmessages/', views.globalmessage_list),
    path('globalmessages/<int:pk>/', views.globalmessage_detail),
]

# from django.urls import path
# from colossus.globalmessages.views import GlobalMessageViewSet

# globalmessages_urlpatterns = [
#     path('', GlobalMessageViewSet.as_view({'get': 'list'})),
#     path('<int:pk>/', GlobalMessageViewSet.as_view({'get': 'retrieve'})),
# ]