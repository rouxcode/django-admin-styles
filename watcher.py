#!/usr/bin/env python

import os
import sys
import time

import logging
from logging.config import dictConfig

import sass
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


CONF_NAME = 'conf.py'
ROOT_PATH = os.getcwd()
sys.path.append(ROOT_PATH)


from conf import LOGGING_CONFIG, SCSS_WATCH_PATHES # NOQA


dictConfig(LOGGING_CONFIG)
logger = logging.getLogger()


class Handler(PatternMatchingEventHandler):

    pathes = None
    css = None
    scss = None
    output_style = 'compressed'

    def __init__(self, *args, **kwargs):
        if kwargs.get('pathes'):
            self.pathes = kwargs.pop('pathes')
            self.css = os.path.join(ROOT_PATH, self.pathes['css'])
            self.scss = os.path.join(ROOT_PATH, self.pathes['scss'])
            self.output_style = self.pathes.get(
                'output_style', self.output_style
            )
        super(Handler, self).__init__(*args, **kwargs)

    def on_modified(self, event):
        sass.compile(
            dirname=[self.scss, self.css],
            output_style=self.output_style,
        )
        logger.info(
            'WATCHER: compiled {} to {}'.format(
                self.pathes['scss'],
                self.pathes['css'],
            )
        )


class Watcher(object):

    watch_pathes = []

    def __init__(self):
        self.watch_pathes = self.get_watch_pathes()
        observer = Observer()
        for p in self.watch_pathes:
            event_handler = Handler(patterns=['*.scss'], pathes=p)
            observer.schedule(event_handler, p['scss'], recursive=True)

        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    def get_watch_pathes(self):
        pathes = []
        for path in SCSS_WATCH_PATHES:
            if isinstance(path, str):
                p = {
                    'css': os.path.join(path, 'css'),
                    'scss': os.path.join(path, 'scss'),
                }
            elif isinstance(path, dict):
                p = path
            else:
                # TODO notify user a path has to be either a str or a dict
                continue
            if os.path.isdir(p['css']) and os.path.isdir(p['scss']):
                pathes.append(p)
            else:
                # TODO notify user that the pathes do not exist
                continue
        return pathes


if __name__ == '__main__':
    w = Watcher()
