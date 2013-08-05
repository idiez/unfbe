from django.db import models
from django.utils import simplejson
from datetime import datetime

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
	def getJsonInfo(self):
		result = simplejson.dumps(UserInfo.objects.all().filter(user_id=self.user_id).values('user_name','user_pic_uri')[0])[:-1]+', "registered":['
		registered = self.nfcpoint_set.filter(registered=True).order_by('when').reverse().values('name','posId','date','wall')	
		for reg in registered:
			result = result+simplejson.dumps(reg)+", "
		result= result.replace('user_pic_uri', 'pic_uri')
		if len(registered) == 0:
			result = result+'], "visited":['
		else:	
			result = result[:-2]+'], "visited":['
		visited = self.nfcpoint_set.filter(registered=False).order_by('when').reverse().values('name','posId','date','wall')
		for vis in visited:
			result = result+simplejson.dumps(vis)+", "
		if len(visited) == 0:
			result = result+'], "friends":['
		else:	
			result = result[:-2]+'], "friends":['
		friends = self.friends.all().values('user_id','user_name','user_pic_uri') 
		for fri in friends:
			result = result+simplejson.dumps(fri).replace('user','friend')+", "
		if len(friends) == 0:
			result = result+']}'
		else:	
			result = result[:-2]+']}'
		return result		



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
	wall_description = models.CharField(max_length=140)
	wall_last_seen = models.CharField(max_length=50, blank = True)
	def getJsonInfo(self, user_req):
		result = simplejson.dumps(Wall.objects.all().filter(wall_id=self.wall_id).values('wall_pos_type','wall_title','wall_description')[0])[:-1]+', "mean_rating":"'
		ratings = self.rating_set.all()
		total = len(ratings)
		cummulative = 0
		for r in ratings:
			cummulative = cummulative + r.value
		if total == 0:
			mean_rating = 0
		else:
			mean_rating = cummulative/total
		result = result+str(mean_rating)+'", "my_rating":"'
		mine =ratings.filter(user_id=user_req)
		if len(mine) == 0:
			my_rating = 0
		else:
			my_rating = mine[0].value
		result = result+str(my_rating)+'", "entry_list": ['
		entries = self.entry_set.all().order_by('when').reverse().values('time_stamp','message','author_name')
		for entry in entries:
			result = result+simplejson.dumps(entry)+", "
		if len(entries) == 0:
			result = result+']}'
		else:	
			result = result[:-2]+']}'
		return result


class Entry(models.Model):
	wall = models.ForeignKey(Wall)
	when = models.DateTimeField('date registered')
	time_stamp = models.CharField(max_length=50)
	author_name = models.CharField(max_length=50, blank=True)
	message = models.CharField(max_length=140)  #tweet length!
	author_pic_uri = models.CharField(max_length=50, default = "dummy_4")

class Rating(models.Model):
	wall = models.ForeignKey(Wall)
	user_id = models.CharField(max_length=50)
	value = models.IntegerField(blank=True)

class Fblink(models.Model):
	fb_id = models.CharField(max_length=50)
	user_id = models.CharField(max_length=50)
