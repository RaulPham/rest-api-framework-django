from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    data = {
        "message": "Hi there!",
    }

    return JsonResponse(data)