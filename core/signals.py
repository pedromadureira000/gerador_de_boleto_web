from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)  # every time a user was created, a token will be generated fo that user.

#  @receiver(post_save, sender=settings.AUTH_USER_MODEL)
#  def assign_default_roles(sender, instance=None, created=False, **kwargs):
    #  if created:
        #  assign_role(instance, 'generate_boleto')

