from django.shortcuts import render  # type: ignore


def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)


def page_500(request):
    return render(request, 'pages/500.html', status=500)


def csrf_failure(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)
