def status(request):
    user = request.user
    if user.is_authenticated:
        status = '(авторизован)'
    else:
        status = ''
    return {'status': status}
