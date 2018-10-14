from import_export import resources
from .models import Appartment

class AppartmentResource(resources.ModelResource):
    class Meta:
        model = Appartment