from functools import wraps

from django.contrib import messages

from . import utils


def nokia_integration_warning(msg=None):
    """
    Adds a message to inform the user about Nokia integration if their
    account is not already integrated with Nokia.

    :param msg: The message text to use if the user is not integrated. If msg
        is a callable, it is called with the request as the only parameter.
        Otherwise, msg is passed in as the message text. If no message is
        provided, the value in :ref:`NOKIA_DECORATOR_MESSAGE` is used.

    This decorator does not prevent the user from seeing the view if they are
    not integrated with Nokia - it only adds a message to the user's
    messages. If you would like to change the behavior of your view based on
    whether the user is integrated, you can check the user's status by using
    :py:func:`nokiaapp.utils.is_integrated`.

    Example::

        from django.http import HttpResponse
        from django.contrib.auth.decorators import login_required
        from nokiaapp.decorators import nokia_integration_warning

        @nokia_integration_warning(msg="Integrate your account with Nokia!")
        @login_required
        def my_view(request):
            return HttpResponse('Visible to authenticated users regardless'
                                'of Nokia integration status')

    In this example, the ``nokia_integration_warning`` decorator only
    operates if the user is logged in. The view content is visible to all
    users who are logged in, regardless of Nokia integration status.

    The template(s) for any view with this decorator should display a user's
    messages.
    """
    if not msg:
        msg = utils.get_setting('NOKIA_DECORATOR_MESSAGE')
    def inner_decorator(view_func):
        def wrapped(request, *args, **kwargs):
            user = request.user
            if not utils.is_integrated(user):
                text = msg(request) if callable(msg) else msg
                messages.error(request, text)
            return view_func(request, *args, **kwargs)
        return wraps(view_func)(wrapped)
    return inner_decorator
