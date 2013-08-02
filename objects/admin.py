from django.contrib import admin
from objects.models import NFCPoint
from objects.models import UserInfo
from objects.models import ContactRelationship
from objects.models import Wall
from objects.models import Entry
from objects.models import Rating

class NFCPointInline(admin.TabularInline):
    model = NFCPoint
    extra = 1

class EntryInline(admin.TabularInline):
    model = Entry
    extra = 1

class RatingInline(admin.TabularInline):
    model = Rating
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
	list_display = ('name', 'when', 'date', 'posId','registered', 'wall')

class WallAdmin(admin.ModelAdmin):
	list_display = ('wall_id', 'wall_pos_type',	'wall_title', 'wall_description', 'wall_last_seen')
	inlines = [EntryInline, RatingInline]


admin.site.register(NFCPoint, NFCPointAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Wall, WallAdmin)
admin.site.register(ContactRelationship)