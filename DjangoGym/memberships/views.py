from django.views.generic import ListView
from .models import Membresia

class MembresiaListView(ListView):
    model = Membresia
    template_name = 'memberships/memberships.html'  # Plantilla personalizada
    context_object_name = 'membresias'
