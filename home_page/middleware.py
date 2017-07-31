# from django.core.urlresolvers import reverse
# from django.http import HttpResponseRedirect

# class ValidLogin(object):

# 	def __init__(self, get_response):
# 		self.get_response = get_response

# 	def __call__(self, request):
# 		return self.get_response(request)

# 	def process_request(request):
# 		if request.user.is_authenticated():
# 			return HttpResponseRedirect(reverse('login'))
# 		return None

import base64
from django.http import HttpResponse
from django.conf import settings

class BasicAuthMiddleware(object):

	def __init__(self, get_response): 
		self.get_response = get_response
		self.AUTH_TEMPLATE = """ <title>Authentication Required</title> Sorry, we're not ready for you yet. """

		

	def _unauthed(self):
		response = HttpResponse(self.AUTH_TEMPLATE, content_type="text/html")
		response['WWW-Authenticate'] = 'Basic realm="Development"'
		response.status_code = 401
		return response

	def __call__(self, request):

		if 'HTTP_AUTHORIZATION' not in request.META:
			return self._unauthed()
		else:
			authentication = request.META['HTTP_AUTHORIZATION']
			(auth_method, auth) = authentication.split(' ', 1)
			if 'basic' != auth_method.lower():
				return self._unauthed()
			auth = base64.b64decode(auth.strip()).decode('utf-8')
			username, password = auth.split(':', 1)
			if (
				username == settings.BASICAUTH_USERNAME and
				password == settings.BASICAUTH_PASSWORD
				):
				return self.get_response(request)

			return self._unauthed()



