# -*- coding: utf-8 -*-
from postkasterl.mailer import sendmail
from postkasterl.secure import secure_decrypt
from pyramid.httpexceptions import HTTPForbidden
from pyramid.httpexceptions import HTTPInternalServerError
from pyramid.view import view_config
from validate_email import validate_email
import logging

logger = logging.getLogger(__name__)


def _handle_form(request, data):
    result = {
        'errors': {},
    }
    # validate form
    if 'name' not in data or not data['name']:
        result['errors']['name'] = "required"
    if 'email' not in data or not data['email']:
        result['errors']['email'] = "required"
    elif not validate_email(data['email'], verify=True):
        result['errors']['email'] = "invalid"
    if result['errors']:
        return result
    if 'recipient' not in data or not data['recipient']:
        raise HTTPForbidden('Not allowed to call w/o recipient.')
    secret = request.registry.settings.get('postkasterl.secret')
    if not secret:
        raise HTTPInternalServerError('No secret configured.')
    try:
        recipient = secure_decrypt(data['recipient'], secret)
    except Exception, e:
        logger.exception(e)
        raise HTTPForbidden('Invalid recipient.')
    del data['recipient']
    # send email
    success = sendmail(recipient, data['name'], data['email'], data, request)
    if not success:
        raise HTTPInternalServerError('Can not send email (server problem).')
    return result


@view_config(
    route_name='main',
    request_method='POST',
    renderer="json", )
def json_handler(request):
    if request.headers['Content-Type'] == "application/json":
        data = request.json
    else:
        data = request.POST.mixed()
    return _handle_form(request, data)
