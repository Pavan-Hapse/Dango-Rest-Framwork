from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    print('user {} log in'.format(user.username))


@receiver(user_login_failed)
def log_user_login_failed(sender, credential, user, **kwargs):
    print('user {} failed to log in'.format(user.username))


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    print('user {} logged out'.format(user.username))
