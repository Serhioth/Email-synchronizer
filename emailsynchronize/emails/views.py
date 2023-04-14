import logging
from logging.handlers import RotatingFileHandler

from django.http import HttpResponseServerError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from emails.exceptions import UserCreateError
from emails.forms import LogPassForm
from emails.main_logic import (check_user_imap, create_new_account,
                               generate_password, get_fio, parse_email)
from emails.models import LogPass

view_logger = logging.getLogger(name=__name__)
view_logger.setLevel('INFO')

handler = RotatingFileHandler(
    'main_log.log',
    maxBytes=50000000,
    backupCount=5,
    encoding='utf-8'
)
formatter = logging.Formatter(
    '%(asctime)s, %(levelname)s, %(name)s, '
    '%(funcName)s, %(levelno)s, %(message)s'
)

handler.setFormatter(formatter)
view_logger.addHandler(handler)


class EmailFormView(CreateView):
    """View-class for main page"""
    form_class = LogPassForm
    template_name = 'index.html'

    def form_valid(self, form: LogPassForm):
        """Validate user's data"""
        user = form.save(commit=False)
        view_logger.info(user.user_email)
        if not check_user_imap(
            email=user.user_email,
            password=user.portal_password
        ):
            return redirect(
                reverse_lazy('emails:imap_error')
            )

        try:
            LogPass.objects.get(user_email=user.user_email)
            view_logger.warning('Такой пользователь уже зарегистрирован')
            return redirect(
                reverse_lazy('emails:exists')
            )
        except LogPass.DoesNotExist:
            login, domain = parse_email(user.user_email)
            user.login = login
            user.domain = domain
            user.password = generate_password()
            user.fio = get_fio(login, domain)
            try:
                create_user_status = create_new_account(
                    login=user.login,
                    password=user.password,
                    domain=user.domain,
                    email_yandex=user.email_yandex,
                    password_yandex=user.password_yandex,
                    fio=user.fio
                )
                if create_user_status != 'mailbox_added':
                    if create_user_status == 'object_exists':
                        return redirect(
                            reverse_lazy('emails:exists')
                        )
                    return HttpResponseServerError()
                user.save()
                return super().form_valid(form)
            except Exception as e:
                view_logger.error(UserCreateError(e))
                raise UserCreateError(e)

    def get_success_url(self):
        password = self.request.POST.get('portal_password')
        return reverse_lazy(
            'emails:success',
            kwargs={'password': password}
        )


class SuccessPage(TemplateView):
    """View class for success page"""
    template_name = 'success.html'

    def get_context_data(self, **kwargs):
        password_yandex = self.kwargs.get('password')
        context = super(SuccessPage, self).get_context_data(**kwargs)
        context['user'] = LogPass.objects.get(password_yandex=password_yandex)
        return context


class AlreadyExistsView(TemplateView):
    """View class for error page"""
    template_name = 'already-exists.html'


class ImapErrorView(TemplateView):
    """View class for error page"""
    template_name = 'imap-error.html'
