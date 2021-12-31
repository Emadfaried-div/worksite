from import_export import resources
from workapp.models import StoreCode, KapasFollowUp


class SotreCodeResources(resources.ModelResource):
    class meta:
        model = StoreCode
        
class KapasFollowUpResources(resources.ModelResource):
    class meta:
        model = KapasFollowUp
             