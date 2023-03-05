from .signals import user_subscribed, user_unsubscribed
from django.http import HttpResponse


def subscribe(request):
    user_email = request.GET.get('user_email')
    if user_email is None:
        return HttpResponse("Please provide a user_email parameter in GET request.")
    else:
        user_subscribed.send(sender=request.user, user_email=user_email)
        return HttpResponse(f"Subscribed {user_email} to our newsletter.")
    
def unsubscribe(request):
    user_email = request.GET.get('user_email')
    if user_email is None:
        return HttpResponse("Please provide a user_email parameter in GET request.")
    else:
        user_unsubscribed.send(sender=request.user, user_email=user_email)
        return HttpResponse(f"Unsubscribed {user_email} from our newsletter.")