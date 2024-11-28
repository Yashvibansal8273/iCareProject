from django.urls import path
from iCareApp.views import ( home_page, about_page,
                            contact_us, study_list,
                            signup_view, login_view,
                            dashboard_view,
                            )

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contact/', contact_us, name='contact_us'),
    # path('studylist/', study_list, name='study_list'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    


]
