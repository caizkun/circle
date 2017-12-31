#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Thread

from flask import render_template
from flask_mail import Message

from . import mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['APP_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['APP_MAIL_SENDER'],
                  recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    # send a email in a background thread
    thread = Thread(target=send_async_email, args=[app, msg])
    thread.start()
    return thread