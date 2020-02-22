from django.contrib import admin
from. import models
# Register your models here.


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display=('name','price','sale','stroe')

class userAdmin(admin.ModelAdmin):
    list_display=('userName','sex','phone','address')

class messageAdmin(admin.ModelAdmin):
    list_display=('title','time')

class noticeAdmin(admin.ModelAdmin):
    list_display=('title','time')

admin.site.register(models.GoodsInfo,GoodsInfoAdmin)
admin.site.register(models.user,userAdmin)
admin.site.register(models.message,messageAdmin)
admin.site.register(models.notice,noticeAdmin)
admin.site.register(models.brand)
admin.site.register(models.order)
admin.site.register(models.orderList)



