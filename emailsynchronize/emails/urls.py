from django.urls import path
from emails.views import (AlreadyExistsView, EmailFormView, ImapErrorView,
                          SuccessPage)

app_name = 'emails'

urlpatterns = [
    path('sync/', EmailFormView.as_view(), name='index'),
    path('sync/success/<str:password>', SuccessPage.as_view(), name='success'),
    path('sync/already-exists/', AlreadyExistsView.as_view(), name='exists'),
    path('sync/imap-error/', ImapErrorView.as_view(), name='imap_error')
]
