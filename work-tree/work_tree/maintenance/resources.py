from import_export import resources
from maintenance.models import MaintenancePlan


class MaintenancePlanResources(resources.ModelResource):
    class meta:
        model = MaintenancePlan
        
