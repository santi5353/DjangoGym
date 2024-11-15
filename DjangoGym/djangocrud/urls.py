from django.contrib import admin
from django.urls import path
from tasks import views
from django.conf import settings  # Asegúrate de importar settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    # path('tasks/', views.tasks, name='tasks'),
    # path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
   
    path('instructores/', views.instructors, name='instructores'),
    path('rutinas/', views.routines, name='rutinas'),
    path('create-booking/', views.create_booking, name='create_booking'),
    path('booking-success/', views.booking_success, name='booking_success'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),  # URL para ver las reservas del usuario

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
