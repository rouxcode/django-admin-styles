import logging


SCSS_WATCH_PATHES = [
    'pm/static/admin',
    {
        'css': 'admin_styles/static/admin_styles/css',
        'scss': 'admin_styles/static/admin_styles/scss',
        'output_style': 'compressed',
    }
]
LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'f': {
            'format': '%(message)s',
        }
    },
    'handlers': {
        'h': {
            'class': 'logging.StreamHandler',
            'formatter': 'f',
            'level': logging.DEBUG
        }
    },
    'root': {
        'handlers': ['h'],
        'level': logging.DEBUG,
    },
}
