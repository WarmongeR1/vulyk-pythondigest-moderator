# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from vulyk.models.task_types import AbstractTaskType

from vulyk_pythondigest_moderator.models.tasks import PythonDigestModeratorTask, \
    PythonDigestModeratorAnswer


class PythonDigestModeratorTaskType(AbstractTaskType):
    """
    Names Task to work with Vulyk.
    """

    answer_model = PythonDigestModeratorAnswer
    task_model = PythonDigestModeratorTask

    name = "Интересные/неинтересные Python новости"
    description = ''

    template = 'base.html'
    helptext_template = 'help.html'
    type_name = 'pythondigest_moderator_task'

    redundancy = 3

    JS_ASSETS = ['static/scripts/handlebars.js',
                 'static/scripts/jquery.serializejson.js',
                 'static/scripts/base.js', ]

    CSS_ASSETS = ['static/styles/bootstrap-social.css',
                  'static/styles/base.css',
                  'static/styles/base/style.css', ]
