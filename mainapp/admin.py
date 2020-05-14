from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.
class FactAdmin(admin.ModelAdmin):
    list_display = ('fact_no', 'fact')
    list_display_links = ('fact_no', 'fact')
class FactResources(resources.ModelResource):
    class Meta:
        model = fact
        skip_unchanged = True
        report_skipped = True
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
        skip_unchanged = True
        report_skipped = True
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
        skip_unchanged = True
        report_skipped = True
        fields = ('id', 'name', 'mobile', 'desgn', 'show')
        export_order = fields
@admin.register(FounderContact)
class FounderContactAdmin(ImportExportModelAdmin, FounderContactAdmin):
    resource_class = FounderContactResources

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'desgn', 'state', 'pos', 'show')
    list_display_links = ('name',)
    list_editable = ('show',)
    list_filter = ('pos',)
class ContactResources(resources.ModelResource):
    class Meta:
        model = Contact
        skip_unchanged = True
        report_skipped = True
        fields = ('id', 'name', 'mobile', 'desgn', 'state', 'pos', 'show')
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


class account_infoAdmin(admin.ModelAdmin):
    list_display = ('id','acc_no', 'ifsc', 'bank_name')
    list_display_links = ('id',)
    list_editable = ('acc_no', 'ifsc', 'bank_name')

class account_infoResources(resources.ModelResource):
    class Meta:
        model = account_info
        skip_unchanged = True
        report_skipped = True
        fields = ('id', 'acc_no', 'ifsc', 'bank_name')
        export_order = fields
@admin.register(account_info)
class account_infoAdmin(ImportExportModelAdmin, account_infoAdmin):
    resource_class = account_infoResources

class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department
        skip_unchanged = True
        report_skipped = True
        fields = ('id','name',)

@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin):
    resource_class = DepartmentResource

class DistrictResource(resources.ModelResource):
    class Meta:
        model = District
        skip_unchanged = True
        report_skipped = True
        fields = ('id','name',)

@admin.register(District)
class DistrictAdmin(ImportExportModelAdmin):
    resource_class = DistrictResource


class MISAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'department', 'post', 'accepted')
    list_display_links = ('name', )
    list_editable = ('mobile', 'accepted')
    list_filter = ('category','Class', 'gender', 'married' ,'district')

class MISResource(resources.ModelResource):
    class Meta:
        model = MIS
        skip_unchanged = True
        report_skipped = True
        fields = ('id', 'name', 'guardian_name', 'married', 'date_of_birth', 'gender', 'category', 'caste', 'age', 'mobile', 'qualification', 'department', 'date_of_joining_in_depart', 'post', 'Class', 'promotion_date' ,'district', 'block', 'postal_addr', 'pan_no', 'acc_no', 'ifsc', 'bank_name', 'permanent_addr', 'pincode', 'accepted')
        export_order = fields

@admin.register(MIS)
class MISAdmin(ImportExportModelAdmin, MISAdmin):
    resource_class = MISResource

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