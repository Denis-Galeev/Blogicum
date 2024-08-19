from django.urls import path  # type: ignore
from django.views.generic import TemplateView  # type: ignore

app_name = 'pages'

urlpatterns = [
    path(  # about
        'about/',
        TemplateView.as_view(template_name='pages/about.html'),
        name='about',
    ),
    path(  # rules
        'rules/',
        TemplateView.as_view(template_name='pages/rules.html'),
        name='rules'
    ),
    path(  # zaglush
        'zaglush',
        TemplateView.as_view(template_name='pages/zaglush.html'),
        name='zaglush'
    )
]
