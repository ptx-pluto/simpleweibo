from django.http import HttpResponseForbidden, HttpResponse
import json

def rest_api(func):
    def wrap(request, *a, **kw):
        response = func(request, *a, **kw)
        return HttpResponse(json.dumps(response), content_type='application/json', status=200)

    if isinstance(func, HttpResponseForbidden):
        return func
    else:
        return wrap
