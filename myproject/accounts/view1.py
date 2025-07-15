from django.http import HttpResponse


def set_session(request):
    request.session['username'] = 'harun_dev'
    request.session['role'] = 'admin'
    request.session['login_count'] = request.session.get('login_count', 0) + 1
    request.session.set_expiry(1800)  # 30 minutes
    return HttpResponse("Session data set.")
def get_session(request):
    username = request.session.get('username', 'Guest')
    role = request.session.get('role', 'none')
    login_count = request.session.get('login_count', 0)
    return HttpResponse(f"User: {username}, Role: {role}, Logins: {login_count}")
def delete_key(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return HttpResponse("Username session key deleted.")
def visit_counter(request):
    visits = request.session.get('visits', 0)
    request.session['visits'] = visits + 1
    return HttpResponse(f"You have visited this page {request.session['visits']} times.")