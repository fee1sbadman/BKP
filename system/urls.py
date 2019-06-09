from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name = 'home'),
    path('disciplines/', views.discipline_list, name = 'dis_list'),
    path('disciplines/<int:pk>/', views.discipline_details, name = 'dis_details'),
    path('discipline/<int:pk>/theme/<int:theme_id>/', views.theme_details, name = 'theme_details'),
    path('discipline/<int:pk>/theme/<int:theme_id>/test/<int:test_id>/', views.test_details, name = 'test_details'),
    path('themes/', views.theme_list, name = 'theme_list'),
    path('tests/', views.test_list, name = 'test_list'),
    path('discipline/<int:pk>/theme/<int:theme_id>/test/<int:test_id>/model_of_test/', views.model_of_test, name = 'model_of_test'),
    path('discipline/<int:pk>/theme/<int:theme_id>/test/<int:test_id>/model_of_test/fixed/<int:number>/', views.fixed_test, name = 'fixed_test'),
    path('<int:number>/<int:question_id>', views.vote, name = 'vote'),
    path('result/<int:test_id>/<int:user_id>/<int:ball>/', views.zero, name = 'zero'),
    path('result/<int:test_id>/', views.bal, name = 'bal'),
    path('test/<int:test_id>/result/', views.result, name = 'result'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/<int:user_id>/', views.profile, name='profile'),
]
