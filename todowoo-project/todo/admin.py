from django.contrib import admin
from .models import FamilyRole, Family, Person

# Register your models here.
class FamilyRoleInline(admin.TabularInline):
    model = FamilyRole


class FamilyInline(admin.TabularInline):
    model = Family


class PersonAdmin(admin.ModelAdmin):
    inlines = [FamilyRoleInline]


admin.site.register(FamilyRole)
admin.site.register(Family)
admin.site.register(Person, PersonAdmin,)
