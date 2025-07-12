from django.contrib import admin
from .models import Flat, Complaint, Owner



@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "pure_phone", )
    search_fields = ("name", "phone", )
    raw_id_fields = ('owned_flats',)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ("town", "town_district", "address", "owner_pure_phone",)
    readonly_fields = ("created_at",)
    list_display = ("address", "price", "new_building", "construction_year", "town",)
    list_editable = ("new_building",)
    list_filter = ("new_building", "rooms_number", "has_balcony",)
    raw_id_fields = ('liked_by','owners',)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['user', 'flat', 'text']
    raw_id_fields = ('user', 'flat')