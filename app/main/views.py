#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import session, redirect, render_template, url_for, current_app

from . import main


@main.route('/')
def index():
    return render_template('index.html')
