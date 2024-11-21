from django.views.generic import ListView
from .models import Servicio

class ServicioListView(ListView):
    model = Servicio
    template_name = 'services/services.html'  # Plantilla personalizada
    context_object_name = 'servicios'
