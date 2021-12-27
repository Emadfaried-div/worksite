from import_export import resources
from workapp.models import StoreCode


class SotreCodeResources(resources.ModelResource):
    class meta:
        model = StoreCode