import random

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.db.models.aggregates import Count

from .models import *


# Register your models here.


class BakerAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def get_queryset(self, request):
        qs = super(BakerAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs.annotate(cakes_count=Count('cakes')).filter(cakes_count__lt=5)


class CakeAdmin(admin.ModelAdmin):

    def has_change_permission(self, request, obj=None):
        return obj and request.user == obj.baker.user



    def save_model(self, request, obj, form, change):

        baker_cakes = Cake.objects.filter(baker=obj.baker).all()
        baker_cake_length = len(baker_cakes)

        if baker_cake_length >= 10:
           raise ValidationError("A baker cant have more than 10 cakes")
        if Cake.objects.filter(name=obj.name).exists():
            raise ValidationError("A cake with that name already exists !")

        # price cannot exceed 10 000
        sum = 0
        for cake in baker_cakes:
            sum += cake.price

        if not change:
            if sum >= 10000:
                raise ValidationError("price over 10000")
        else:
            old_price = Cake.objects.filter(id=obj.id).first().price
            if sum-old_price + obj.price >= 10000:
                raise ValidationError("price over 10000")

        return super(CakeAdmin, self).save_model(request, obj, form, change)

admin.site.register(Baker,BakerAdmin)
admin.site.register(Cake,CakeAdmin)
