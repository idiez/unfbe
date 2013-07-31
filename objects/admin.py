from django.contrib import admin
from objects.models import Test
from objects.models import NFCPoint
from objects.models import UserInfo
from objects.models import ContactRelationship



admin.site.register(Test)
admin.site.register(NFCPoint)
admin.site.register(UserInfo)
admin.site.register(ContactRelationship)