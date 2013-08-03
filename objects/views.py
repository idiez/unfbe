from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from objects.models import UserInfo, NFCPoint, ContactRelationship, Wall, Fblink
from django.template import RequestContext
from datetime import datetime

def restore_view(request, user_req):
	user_obj = get_object_or_404(UserInfo, user_id=user_req)
	#user_obj = UserInfo.objects.get(user_id=user_req)
	result = simplejson.dumps(UserInfo.objects.all().filter(user_id=user_req).values('user_name','user_pic_uri')[0])[:-1]+', "registered":['

	registered = user_obj.nfcpoint_set.filter(registered=True).order_by('when').reverse().values('name','posId','date','wall')	
	for reg in registered:
		result = result+simplejson.dumps(reg)+", "
	result= result.replace('user_pic_uri', 'pic_uri')
	if len(registered) == 0:
		result = result+'], "visited":['
	else:	
		result = result[:-2]+'], "visited":['

	visited = user_obj.nfcpoint_set.filter(registered=False).order_by('when').reverse().values('name','posId','date','wall')
	for vis in visited:
		result = result+simplejson.dumps(vis)+", "
	if len(visited) == 0:
		result = result+'], "friends":['
	else:	
		result = result[:-2]+'], "friends":['

	friends = user_obj.friends.all().values('user_id','user_name','user_pic_uri') 
	for fri in friends:
		result = result+simplejson.dumps(fri).replace('user','friend')+", "
	if len(friends) == 0:
		result = result+']}'
	else:	
		result = result[:-2]+']}'

	return HttpResponse(result, mimetype='application/json')	

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
				wall_description = data['wall_description']
				)
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
