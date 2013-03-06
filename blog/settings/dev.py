from blog.settings.base_settings import *

TEMPLATE_DEBUG = DEBUG = True

xampp_socket = '/opt/lampp/var/mysql/mysql.sock'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'blog',
        'PASSWORD': 'blog',
        'HOST': '',
    }
}

INSTALLED_APPS += (
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'