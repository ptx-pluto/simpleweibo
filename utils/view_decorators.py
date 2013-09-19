from django.http import HttpResponseForbidden
import json

def json_view(func):
    def wrap(request, *a, **kw):
        response = func(request, *a, **kw)
        return json_response(request, response)

    if isinstance(func, HttpResponseForbidden):
        return func
    else:
        return wrap

def json_response(request, response=None):
    return HttpResponse(json.dumps(response), minetype='application/json', status=200)
