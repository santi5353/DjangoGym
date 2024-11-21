from django.contrib import admin
from django.urls import path
from tasks import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    # Usamos la vista basada en clase HomeView
    path('', views.HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    # Usamos la vista basada en clase UserSignupView
    path('signup/', views.UserSignupView.as_view(), name='signup'),
    path('signout/', views.UserLogoutView.as_view(), name='signout'),
    # Usamos la vista basada en clase UserLoginView
    path('signin/', views.UserLoginView.as_view(), name='signin'),
    # Usamos la vista basada en clase InstructorListView
    path('instructores/', views.InstructorListView.as_view(), name='instructores'),
    # Usamos la vista basada en clase RoutineListView
    path('rutinas/', views.RoutineListView.as_view(), name='rutinas'),
    # Usamos la vista basada en clase BookingCreateView
    path('create-booking/', views.BookingCreateView.as_view(), name='create_booking'),
    # Usamos la vista basada en clase BookingSuccessView
    path('booking-success/', views.BookingSuccessView.as_view(),
         name='booking_success'),
    # Usamos la vista basada en clase MyBookingsView
    path('my_bookings/', views.MyBookingsView.as_view(), name='my_bookings'),
     path('memberships/', include('memberships.urls')),  # URLs de Membresías
    path('services/', include('services.urls')),  # URLs de Servicios
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
