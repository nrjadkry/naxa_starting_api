from rest_framework.routers import DefaultRouter
from django.urls import path , include
from api.viewsets import core_viewset

router=DefaultRouter()
 
#register StudentViewset with Router
router.register('api/studentapi', core_viewset.StudentViewSet, basename='student')
router.register('api/student', core_viewset.UserViewSet, basename='students')


urlpatterns=[
    path('',include(router.urls)),
    path('api/studentdata/',core_viewset.StudentAPI.as_view()),
    path('api/studentdata/<int:pk>/',core_viewset.StudentAPI.as_view()),
	
]