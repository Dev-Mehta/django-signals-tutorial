from django.dispatch import Signal
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

user_subscribed = Signal(providing_args=['user_email', 'newsletter_name'])
user_unsubscribed = Signal(providing_args=['user_email', 'newsletter_name'])

@receiver(user_subscribed)
def subscribe_newsletter(sender, **kwargs):
    user_email = kwargs['user_email']
    
    # Business logic
    print(f"\033[91m Subscribed {user_email} to our newsletter\033[0m")

@receiver(user_unsubscribed)
def unsubscribe_newsletter(sender, **kwargs):
    user_email = kwargs['user_email']
    
    # Business logic
    print(f"\033[91m Unsubscribed {user_email} from our newsletter\033[0m")

@receiver(pre_save, sender=User)
def user_created(sender, **kwargs):
    user = kwargs['instance']
    print(f"Creating user, {user}")

user_subscribed.connect(subscribe_newsletter)
user_unsubscribed.connect(unsubscribe_newsletter)