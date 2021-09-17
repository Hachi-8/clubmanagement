from django.contrib import admin

# Register your models here.
from .models import Conditions, MatchResult, MatchResultDetail, freeThrough, threeMen, Shooting

admin.site.register(Conditions)
admin.site.register(freeThrough)
admin.site.register(threeMen)
admin.site.register(MatchResult)
admin.site.register(MatchResultDetail)
admin.site.register(Shooting)