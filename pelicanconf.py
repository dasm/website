#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'dasm'
SITENAME = 'smigiel.dev'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# all defaults to True.
DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME   = True
DISPLAY_MENU   = True

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

ARCHIVES_URL       = 'archives'
ARCHIVES_SAVE_AS   = 'archives.html'

MENU_INTERNAL_PAGES = (
    ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
)

# additional menu items
#MENUITEMS = (
#    ('GitHub', 'https://github.com/'),
#)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

#DEFAULT_PAGINATION = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
