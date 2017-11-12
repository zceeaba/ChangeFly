import django_tables2 as tables
from ChangeFly.models import customer_info
class customer_infoTable(tables.Table):
    class Meta:
        model=customer_info

