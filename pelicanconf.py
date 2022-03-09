AUTHOR = 'Haley Gomez'
SITENAME = 'Haley Gomez'
SITEURL = ''
SITELOGO = "/images/haley-gomez1.jpg"
FAVICON = "/images/favicon.ico"
SITENAME = "Haley Gomez"
SITETITLE = "Haley Gomez"
SITESUBTITLE = "Professor of Astrophysics"

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'themes/Flex'

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('Home','/'),
    ('CosmicDust','/cosmic-dust/'),
    ('Publications','/publications/'),
    ('Talks','/talks/'),
    ('Outreach','/outreach/'),
    ('Academic CV','/academic-cv/'),
    ('The Team','/my-group/'),
    )

LINKS = MENUITEMS
