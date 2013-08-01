from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from objects.models import UserInfo, NFCPoint
from django.template import RequestContext

def restore_view(request, user_req):
	user_obj = get_object_or_404(UserInfo, user_id=user_req)
	#user_obj = UserInfo.objects.get(user_id=user_req)
	result = simplejson.dumps(UserInfo.objects.all().filter(user_id=user_req).values('user_name','user_pic_uri')[0])[:-1]+', "registered":['

	registered = user_obj.nfcpoint_set.filter(registered=True).values('name','posId','date')	
	for reg in registered:
		result = result+simplejson.dumps(reg)+", "
	result= result.replace('user_pic_uri', 'pic_uri')
	result = result[:-2]+'], "visited":['

	visited = user_obj.nfcpoint_set.filter(registered=False).values('name','posId','date')
	for vis in visited:
		result = result+simplejson.dumps(vis)+", "
	result = result[:-2]+'], "friends":['

	friends = user_obj.friends.all().values('user_id','user_name','user_pic_uri') 
	for fri in friends:
		result = result+simplejson.dumps(fri).replace('user','friend')+", "
	result = result[:-2]+']}'

	return HttpResponse(result, mimetype='application/json')	

def regpoint_view(request, user_req, isReg):
	user_obj = get_object_or_404(UserInfo, user_id = user_req)
	if isReg == 'True':
		reg = True 
	else:
		reg = False
	data = simplejson.loads(request.raw_post_data)
	user_obj.nfcpoint_set.create(name = data['name'],
								posId = data['posId'],
								date = data['date'],
								registered = reg)
	return HttpResponse('OK') 
	#nfcp = NFCPoint(name=request.POST['name'],
	#				posId=request.POST['posId'],
	#				date=request.POST['date'],
	#				registered= isReg,
	#				belongsTo= user_req
	#				)
 	#return HttpResponseRedirect('OK')
