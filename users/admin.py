from django.contrib import admin

from users.models import Payment, Subscription

admin.site.register(Payment)
admin.site.register(Subscription)
