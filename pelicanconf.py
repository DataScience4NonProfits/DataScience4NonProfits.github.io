#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = 'Flex'

PATH = 'content'
STATIC_PATHS = ['images', 'static']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
IGNORE_FILES = [".ipynb_checkpoints"]

DEFAULT_LANG = 'en'
TIMEZONE = 'America/Los_Angeles'

AUTHOR = 'DataScience4NonProfits'
SITEURL = 'https://DataScience4NonProfits.github.io'
SITENAME = 'DataScience4NonProfits'
SITETITLE = 'Data Science for Non-Profits'
SITESUBTITLE = 'San Diego, CA'
SITEDESCRIPTION = 'Data Science for Non-Profits Blog'
SITELOGO = SITEURL + '/images/ds4np_profile.jpeg'
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

MENUITEMS = (('Archives', '/archives.html'),
              ('Categories', '/categories.html'),
              ('Tags', '/tags.html'),
)
LINKS_IN_NEW_TAB = 'external'

# Blogroll
LINKS = (('Our Meetup Group', 'https://www.meetup.com/Data-Science-for-Non-Profits'),
         ('SD Regional Data Library', 'https://www.sandiegodata.org/'),
         ('SD Open Data', 'https://data.sandiego.gov/'),     
)

# Social widget
SOCIAL = (('github', 'https://github.com/DataScience4NonProfits'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
