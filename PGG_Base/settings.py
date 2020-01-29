import os
from os import environ
import dj_database_url

import otree.settings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))
TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)
# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True

DEBUG = False  # !!!


SECRET_KEY = '--%lhy*1ope97ndb+b$!0-j^2)6ox_$wc1!a)!rr6qgdbs0&*d'

DATABASES = {
    'default': dj_database_url.config(

        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}


AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

AUTH_LEVEL = 'STUDY'  # !!!

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

ADMIN_PASSWORD = "GarbageCan2018#"
# ADMIN_PASSWORD = "admin"

# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')

AWS_ACCESS_KEY_ID = 'AKIAJE3CJP7JLJS2WUPQ'
AWS_SECRET_ACCESS_KEY = 'yuA2LdsWFNby0/0UaL/hJR2ZbcB5T9RkMcmNapfx'

# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
POINTS_DECIMAL_PLACES = 2

# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'en'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_HTML = """
<ul>
    <li>
        <a href="https://github.com/oTree-org/otree" target="_blank">
            oTree on GitHub
        </a>.
    </li>
    <li>
        <a href="http://www.otree.org/" target="_blank">
            oTree homepage
        </a>.
    </li>
</ul>
<p>
    Here are various games implemented with oTree. These games are all open
    source, and you can modify them as you wish.
</p>
"""

ROOMS = [
    {
        'name': 'econ101',
        'display_name': 'Econ 101 class',
        'participant_label_file': '_rooms/econ101.txt',
    },
    {
        'name': 'live_demo',
        'display_name': 'Room for live demo (no participant labels)',
    },
]

mturk_hit_settings = {
    'keywords': ['bonus', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7 * 24,  # 7 days
    # 'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': []
}

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.02,
    'participation_fee': 5.00,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}

# ROOT_URLCONF = 'testing.urls'

SESSION_CONFIGS = [
    {
        'name': 'PGG0',
        'display_name': "PGG0",
        'num_demo_participants': 4,
        'app_sequence': ['PGG0']
    },

    {
        'name': 'PGG_Baseline',
        'display_name': "PGG_Baseline",
        'num_demo_participants': 4,
        'app_sequence': ['PGG0', 'PGG_Base_Questionnaire'],
        'reinforcement': 3
    }
]

otree.settings.augment_settings(globals())
