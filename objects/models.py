from django.db import models

# Create your models here.
class Test(models.Model):
	field1 = models.CharField(max_length=200)
	field2 = models.CharField(max_length=200, default="")

class UserInfo(models.Model):
	def __unicode__(self):
		return self.user_name
	user_id = models.CharField(max_length=50)
	user_name = models.CharField(max_length=50)
	user_pic_uri = models.CharField(max_length=50, default = "dummy_4")
	friends = models.ManyToManyField('self', symmetrical = False, blank = True, 
									null = True, through='ContactRelationship',
									related_name='friends+')

class ContactRelationship(models.Model):
    from_contact = models.ForeignKey('UserInfo', related_name='from_contacts')
    to_contact = models.ForeignKey('UserInfo', related_name='to_contacts')
    def __unicode__(self):
		return self.from_contact.user_name+'-'+self.to_contact.user_name
    class Meta:
        unique_together = ('from_contact', 'to_contact')


class NFCPoint(models.Model):
	def __unicode__(self):
		return self.name
	name = models.CharField(max_length=50)
	posId = models.CharField(max_length=50)
	date = models.CharField(max_length=50)
	address = models.CharField(max_length=50, blank = True)
	registered = models.BooleanField()
	belongsTo = models.ForeignKey(UserInfo)
	wall = models.CharField(max_length=50)
	when = models.DateTimeField('date registered')

class Wall(models.Model):
	def __unicode__(self):
		return self.wall_title
	wall_id = models.CharField(max_length=50)
	wall_pos_type = models.CharField(max_length=50)
	wall_title = models.CharField(max_length=50)
	wall_description = models.CharField(max_length=50)
	wall_last_seen = models.CharField(max_length=50, blank = True)

class Entry(models.Model):
	wall = models.ForeignKey(Wall)
	time_stamp = models.DateTimeField('date registered')
#	author = models.CharField(max_length=50)
	message = models.CharField(max_length=140)  #tweet length!

class Rating(models.Model):
	wall = models.ForeignKey(Wall)
	user_id = models.CharField(max_length=50)
	value = models.IntegerField(blank=True)

class Fblink(models.Model):
	fb_id = models.CharField(max_length=50)
	user_id = models.CharField(max_length=50)
