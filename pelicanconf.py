#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = '/Users/brettcastellanos/projects/pelican-themes/Flex'

PATH = 'content'
STATIC_PATHS = ['images']
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
IGNORE_FILES = [".ipynb_checkpoints"]

DEFAULT_LANG = 'en'
TIMEZONE = 'America/Los_Angeles'

AUTHOR = 'DataScience4NonProfits'
SITEURL = 'https://DataScience4NonProfits.github.io'
SITENAME = 'DataScience4NonProfits'
SITE_TITLE = 'Data Science for Non-Profits'
SITE_SUBTITLE = 'San Diego, CA'
SITELOGO = SITEURL + '/images/profile.png'
FAVICON = SITEURL + '/images/favicon.ico'

BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-ds4nonprofits'
}
COPYRIGHT_YEAR = 2019

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAIN_MENU = True

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('meetup', 'https://www.meetup.com/Data-Science-for-Non-Profits/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
