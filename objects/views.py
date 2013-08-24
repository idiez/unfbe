from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from objects.models import UserInfo, NFCPoint, ContactRelationship, Wall, Fblink
from django.template import RequestContext
from datetime import datetime

def restore_view(request, user_req):
	user_obj = get_object_or_404(UserInfo, user_id=user_req)
	return HttpResponse(user_obj.getJsonInfo() , mimetype='application/json')	

def regpoint_view(request, user_req, isReg):
	user_obj = get_object_or_404(UserInfo, user_id = user_req)
	if isReg == 'True':
		reg = True 
		regwall(request)
	else:
		reg = False
	data = simplejson.loads(request.raw_post_data)
	user_obj.nfcpoint_set.create(name = data['name'],
								posId = data['posId'],
								date = data['date'],
								registered = reg,
								wall = data['wall'],
								when = datetime.now())
	return HttpResponse('OK') 
	#nfcp = NFCPoint(name=request.POST['name'],
	#				posId=request.POST['posId'],
	#				date=request.POST['date'],
	#				registered= isReg,
	#				belongsTo= user_req
	#				)
 	#return HttpResponseRedirect('OK')

def regwall(request):
	data = simplejson.loads(request.raw_post_data)
	wall = Wall(wall_id = data['wall'],
				wall_pos_type = data['posId'],
				wall_title = data['name'],
				wall_description = data['wall_description'],
				wall_tag_content = data['wall_tag_content'],
				wall_tag_private = data['wall_tag_private']
				)
	wall.save()
	return HttpResponse('OK') 

def wallupdateprivacy_view(request):
	data = simplejson.loads(request.raw_post_data)
	wall = Wall.objects.get(wall_id = data['wall'])
	wall.wall_tag_private = data['private']
	wall.save()
	return HttpResponse('OK') 

def nameupdate_view(request, user_req):
	user_obj = get_object_or_404(UserInfo, user_id = user_req)
	data = simplejson.loads(request.raw_post_data)
	user_obj.user_name = data['user_name']
	user_obj.save()
	return HttpResponse('OK')

def reguser_view(request):
	data = simplejson.loads(request.raw_post_data)
	user_obj = UserInfo(user_name=data['user_name'],
						user_id=data['user_id'],
						user_pic_uri=data['user_pic_uri']
						)
	user_obj.save()
	return HttpResponse('OK')	 

def picuriupdate_view(request, user_req):
	user_obj = get_object_or_404(UserInfo, user_id = user_req)
	data = simplejson.loads(request.raw_post_data)
	user_obj.user_pic_uri = data['pic_uri']
	user_obj.save()
	return HttpResponse('OK') 

def addfriend_view(request):
	data = simplejson.loads(request.raw_post_data)
	from_user = UserInfo.objects.get(user_id = data['from_contact'])
	to_user = UserInfo.objects.get(user_id = data['to_contact'])
	ContactRelationship.objects.create(	from_contact=from_user,
										to_contact=to_user)
	ContactRelationship.objects.create(	from_contact=to_user,
										to_contact=from_user)
	return HttpResponse('OK') 

def getfb_view(request):
	data = simplejson.loads(request.raw_post_data)
	fb = Fblink.objects.filter(fb_id=data['fb_id'])
	if not fb:
		fblink = Fblink(fb_id=data['fb_id'], user_id=data['user_id'])
		fblink.save()
	else: 
		pass
	fb = Fblink.objects.all()
	result = '{'
	for fbitem in fb:
		result = result+fbitem.fb_id+'='+fbitem.user_id+', '
	if len(fb) == 0:
		result = result+'}'
	else:	
		result = result[:-2]+'}'
	return HttpResponse(result)

def getwall_view(request, wall_req, user_req):
	wall_obj = get_object_or_404(Wall, wall_id=wall_req)
	return HttpResponse(wall_obj.getJsonInfo(user_req) , mimetype='application/json')

def ratewall_view(request):
	data = simplejson.loads(request.raw_post_data)
	wall_obj = get_object_or_404(Wall, wall_id = data['wall'])
	wall_obj.rating_set.create(user_id = data['user_id'],value = data['value'])
	ratings = wall_obj.rating_set.all()
	total = len(ratings)
	cummulative = 0
	for r in ratings:
		cummulative = cummulative + r.value
	if total == 0:
		mean_rating = 0
	else:
		mean_rating = cummulative/total
	return HttpResponse(mean_rating)	

def addentry_view(request, wall_req):
	wall_obj = get_object_or_404(Wall, wall_id=wall_req)
	data = simplejson.loads(request.raw_post_data)
	wall_obj.entry_set.create(	when = datetime.now(),
								time_stamp = data['time_stamp'],
								author_name = data['author_name'],
								author_pic_uri = data['author_pic_uri'],
								message = data['message'])
	return HttpResponse('OK') 

def deleteentry_view(request):
	data = simplejson.loads(request.raw_post_data)
	wall_obj = get_object_or_404(Wall, wall_id = data['wall'])
	wall_obj.entry_set.filter(message = data['message']).delete()
	return HttpResponse('OK') 
