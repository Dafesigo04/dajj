from unicodedata import name
from django.contrib import admin
# Register your models here.
from. models import Product, Category, Supplier, Schedule, Servicio

#admin.site.register(Product)
admin.site.register(Category)

@admin.register(Product)
class Productadmin(admin.ModelAdmin):
    list_display = ("name", "price","Imagen_Product","quanty")
    #list_display_links = ("name", "price")
    list_editable = ["price"]
    search_fields = ["name"]
    list_filter = ["category"]
    list_per_page = 10

@admin.register(Supplier)
class Supplieradmin(admin.ModelAdmin):
    list_display = ("rut", "name", "direction", "number")

@admin.register(Schedule)
class Scheduleadmin(admin.ModelAdmin):
    list_display = ("name", "apellido", "cedula", "horaen", "horasal")

admin.site.register(Servicio)


