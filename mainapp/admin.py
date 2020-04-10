from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import events, aboutUS, eventPhoto, Rules, Gallery, Contact, FounderContact, Designation, UpcomingEvent, Brochure, fact
# Register your models here.
class FactAdmin(admin.ModelAdmin):
    list_display = ('fact_no', 'fact')
    list_display_links = ('fact_no', 'fact')
class FactResources(resources.ModelResource):
    class Meta:
        model = fact
        fields = ('id', 'fact_no', 'fact')
        export_order = fields
@admin.register(fact)
class FactAdmin(ImportExportModelAdmin, FactAdmin):
    resource_class = FactResources

class RulesAdmin(admin.ModelAdmin):
    list_display = ('rule_no', 'rule')
    list_display_links = ('rule_no', 'rule')
class RulesResources(resources.ModelResource):
    class Meta:
        model = Rules
        fields = ('id','rule_no', 'rule', 'rule_en')
        export_order = fields 
@admin.register(Rules)
class RulesAdmin(ImportExportModelAdmin, RulesAdmin):
    resource_class = RulesResources

class FounderContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'desgn', 'show')
    list_display_links = ('name',)
    list_editable = ('show',)
class FounderContactResources(resources.ModelResource):
    class Meta:
        model = FounderContact
        fields = ('id', 'name', 'mobile', 'desgn', 'show')
        export_order = fields
@admin.register(FounderContact)
class FounderContactAdmin(ImportExportModelAdmin, FounderContactAdmin):
    resource_class = FounderContactResources

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'desgn', 'pos', 'show')
    list_display_links = ('name',)
    list_editable = ('show',)
    list_filter = ('pos',)
class ContactResources(resources.ModelResource):
    class Meta:
        model = Contact
        fields = ('id', 'name', 'mobile', 'desgn', 'pos', 'show')
        export_order = fields
@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin, ContactAdmin):
    resource_class = ContactResources


@admin.register(events)
class EventAdmin(admin.ModelAdmin):
    list_display = ('date', 'name')
    list_filter = ('date',)
    list_display_links = ('date',)



class aboutUSAdmin(admin.ModelAdmin):
    list_display = ('heading','showing_order', )
    list_display_links = ('heading',)
    list_editable = ('showing_order',)
    list_filter = ('showing_order',)

admin.site.register(eventPhoto)
admin.site.register(Gallery)
admin.site.register(aboutUS, aboutUSAdmin)
admin.site.register(Brochure)
admin.site.register(Designation)


class UpcomingEventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_date')
    list_display_links = ('event_name',)
    list_editable = ('event_date',)
admin.site.register(UpcomingEvent, UpcomingEventAdmin)