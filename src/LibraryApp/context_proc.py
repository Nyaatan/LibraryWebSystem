from django.contrib.auth.models import User

def check_if_logged_in(request):
    return {'is_logged': request.session.get('user', None) is not None}