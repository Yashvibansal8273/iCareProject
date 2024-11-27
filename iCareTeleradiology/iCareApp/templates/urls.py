from django.urls import path
from iCareApp.views import ( login_page, about_page
                            , LoginAPIView, contact_us,
                            study_list)

urlpatterns = [
    path('', login_page, name='login'),
    path('about/', about_page, name='about'),
    path('login/', LoginAPIView.as_view(), name='login-api'),
    path('contact/', contact_us, name='contact_us'),
    path('studylist/', study_list, name='study_list'),


]
