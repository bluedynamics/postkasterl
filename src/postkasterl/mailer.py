# -*- coding: utf-8 -*-
from postkasterl.utils import format_template
from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message

import logging

logger = logging.getLogger(__name__)


def sendmail(recipient, sender_name, sender_email, data, request):
    body_data = {
        'name': sender_name,
        'email': sender_email,
        'recipient': recipient,
    }
    body_data['fields'] = ""
    for key in sorted(data.keys()):
        body_data['fields'] += "[{0:s}]\n".format(key)
        body_data['fields'] += data[key]
        body_data['fields'] += '\n\n'

    sender_line = '{0:s} <{1:s}'.format(sender_name, sender_email)
    subject, body = format_template('default_tpl.txt', body_data)
    message = Message(
        subject=subject,
        sender=sender_line,
        recipients=[recipient],
        body=body
    )
    mailer = get_mailer(request)
    try:
        mailer.send_immediately(message, fail_silently=False)
    except Exception, e:
        logger.exception(e)
        return False
    return True
