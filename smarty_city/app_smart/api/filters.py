import django _filters
from app_smart.models import Sensor

class SensorFilter(django_filters.FilterSet):
    resonsavel = django_filters.CharFilter(field_name = 'responsalvel', lookup_expr='icontains')
    status_Operacional = django_filters.CharFilter(field_name = 'status_operacional', lookup_expr='exact')
    tipo = django_filters.CharFilter.(field_name='tipo', lookup_expr='exact')
    localizacao = django_filters.CharFilter(field_name='localizacao', lookup_expr='icontains')
    class Meta:
        model=Sensor
        fields = ['responsavel','status_operacional','tipo', 'localizacao']