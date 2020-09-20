#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'dasm'
SITENAME = 'blog.smigiel.dev'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# all defaults to True.
#DISPLAY_HEADER = True
#DISPLAY_FOOTER = True
#DISPLAY_HOME   = True
#DISPLAY_MENU   = True

ARCHIVES_URL       = 'archives'
ARCHIVES_SAVE_AS   = 'archives.html'

MENU_INTERNAL_PAGES = (
    ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
)

# additional menu items
MENUITEMS = (
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

SUMMARY_MAX_LENGTH = 50
DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
