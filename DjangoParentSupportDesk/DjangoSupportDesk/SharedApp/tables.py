import django_tables2 as tables

class CaseTable(tables.Table):
    case_id = tables.Column(verbose_name='Saks-ID')
    title = tables.Column(verbose_name='Tittel')
    category = tables.Column(verbose_name='Kategori')
    urgency = tables.Column(verbose_name='Hastegrad')
    status = tables.Column(verbose_name='Status')
    created_at = tables.DateTimeColumn(verbose_name='Opprettet', format='Y-m-d H:i')
    
    class Meta:
        attrs = {'class': 'table table-striped'}
        order_by = '-created_at'
