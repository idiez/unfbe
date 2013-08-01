from django.contrib import admin
from objects.models import NFCPoint
from objects.models import UserInfo
from objects.models import ContactRelationship

class NFCPointInline(admin.TabularInline):
    model = NFCPoint
    extra = 1

class UserInfoAdmin(admin.ModelAdmin):
	fieldsets = [
				('Nombre de usuario',	{'fields':['user_name']}),
				('ID de usuario',	{'fields':['user_id']}),
				('URI de foto',	{'fields':['user_pic_uri']}),
				]
	list_display = ('user_name', 'user_id','user_pic_uri')
	inlines = [NFCPointInline]

class NFCPointAdmin(admin.ModelAdmin):
	list_display = ('name', 'date', 'posId','registered')


admin.site.register(NFCPoint, NFCPointAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(ContactRelationship)