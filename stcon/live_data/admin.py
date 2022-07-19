from django.contrib import admin

from .models import *



# stations SCZ
# ---------------------------------------------------------------

class ListStAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id', 'number')
    list_dispay_links = ('id', 'number')
    search_fields = ('id', 'number')

class StAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id', 'u', 'i', 'p1', 'p2', 'time_create')
    list_dispay_links = ('id', 'u', 'i', 'p1', 'p2', 'time_create')
    search_fields = ('id', 'time_create')
    list_filter = ('time_create',)


class AddressIpAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'ip_address', 'port_address', 'time_create')
    list_dispay_links = ('id', 'number', 'ip_address', 'port_address', 'time_create')
    search_fields = ('id', 'time_create')

class LogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'st_number', 'code', 'title', 'content', 'time_create', 'is_checked')
    list_dispay_links = ('id', 'st_number', 'code', 'title', 'content', 'time_create', 'is_checked')
    search_fields = ('id', 'time_create')
    list_filter = ('time_create',)



# stations Normel
# ---------------------------------------------------------------

class StNormelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'u_in_f1', 'u_in_f2', 'u_in_f3', 'u_out_f1', 'u_out_f2', 'u_out_f3', 'i_in_f1', 'i_in_f2', 'i_in_f3', 'i_out_f1', 'i_out_f2', 'i_out_f3',  'time_create')
    list_dispay_links = ('u_in_f1', 'u_in_f2', 'u_in_f3', 'u_out_f1', 'u_out_f2', 'u_out_f3', 'i_in_f1', 'i_in_f2', 'i_in_f3', 'i_out_f1', 'i_out_f2', 'i_out_f3',  'time_create')
    search_fields = ('id', 'time_create')
    list_filter = ('time_create',)
    
class NormelListStAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id', 'number')
    list_dispay_links = ('id', 'number')
    search_fields = ('id', 'number')
    
class NormelAddressIpAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'ip_address', 'port_address', 'time_create')
    list_dispay_links = ('id', 'number', 'ip_address', 'port_address', 'time_create')
    search_fields = ('id', 'time_create')




admin.site.register(AddressIp, AddressIpAdmin)
admin.site.register(ListSt, ListStAdmin)
admin.site.register(St30, StAdmin)
admin.site.register(St31, StAdmin)
admin.site.register(LogsSt, LogsAdmin)
#
admin.site.register(StNormel1, StNormelAdmin)
admin.site.register(NormelAddressIp, NormelAddressIpAdmin)
admin.site.register(NormelListSt, NormelListStAdmin)
