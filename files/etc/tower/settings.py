# AWX settings file

import os


ADMINS = ()

STATIC_ROOT = '/var/lib/awx/public/static'

PROJECTS_ROOT = '/var/lib/awx/projects'

JOBOUTPUT_ROOT = '/var/lib/awx/job_status'

SECRET_KEY = os.getenv('SECRET_KEY', 'privateawx')

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

INTERNAL_API_URL = 'http://awxweb:8052'

AWX_TASK_ENV['HOME'] = '/var/lib/awx'

# Container environments don't like chroots
AWX_PROOT_ENABLED = False

CLUSTER_HOST_ID = os.getenv('CLUSTER_HOST_ID', 'awx')
SYSTEM_UUID = '00000000-0000-0000-0000-000000000000'
CELERY_QUEUES += (Queue(CLUSTER_HOST_ID, Exchange(CLUSTER_HOST_ID), routing_key=CLUSTER_HOST_ID),)
CELERY_ROUTES['awx.main.tasks.cluster_node_heartbeat'] = {'queue': CLUSTER_HOST_ID, 'routing_key': CLUSTER_HOST_ID}
CELERY_ROUTES['awx.main.tasks.purge_old_stdout_files'] = {'queue': CLUSTER_HOST_ID, 'routing_key': CLUSTER_HOST_ID}


###############################################################################
# EMAIL SETTINGS
###############################################################################

SERVER_EMAIL = os.getenv('SERVER_EMAIL', 'root@localhost')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'webmaster@localhost')
EMAIL_SUBJECT_PREFIX = os.getenv('EMAIL_SUBJECT_PREFIX', '[AWX] ')

EMAIL_HOST = os.getenv('EMAIL_HOST', 'localhost')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 25))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'no').lower() in ('no', 'false', 'off', '0')


###############################################################################
# LOGGING SETTINGS
###############################################################################

LOGGING['handlers']['console'] = {
    '()': 'logging.StreamHandler',
    'level': os.getenv('LOGGING_LEVEL', 'DEBUG'),
    'formatter': 'simple',
}

LOGGING['loggers']['django.request']['handlers'] = ['console']
LOGGING['loggers']['rest_framework.request']['handlers'] = ['console']
LOGGING['loggers']['awx']['handlers'] = ['console']
LOGGING['loggers']['awx.main.commands.run_callback_receiver']['handlers'] = ['console']
LOGGING['loggers']['awx.main.commands.inventory_import']['handlers'] = ['console']
LOGGING['loggers']['awx.main.tasks']['handlers'] = ['console']
LOGGING['loggers']['awx.main.scheduler']['handlers'] = ['console']
LOGGING['loggers']['django_auth_ldap']['handlers'] = ['console']
LOGGING['loggers']['social']['handlers'] = ['console']
LOGGING['loggers']['system_tracking_migrations']['handlers'] = ['console']
LOGGING['loggers']['rbac_migrations']['handlers'] = ['console']
LOGGING['loggers']['awx.isolated.manager.playbooks']['handlers'] = ['console']
LOGGING['handlers']['callback_receiver'] = {'class': 'logging.NullHandler'}
LOGGING['handlers']['fact_receiver'] = {'class': 'logging.NullHandler'}
LOGGING['handlers']['task_system'] = {'class': 'logging.NullHandler'}
LOGGING['handlers']['tower_warnings'] = {'class': 'logging.NullHandler'}
LOGGING['handlers']['rbac_migrations'] = {'class': 'logging.NullHandler'}
LOGGING['handlers']['system_tracking_migrations'] = {'class': 'logging.NullHandler'}
LOGGING['handlers']['management_playbooks'] = {'class': 'logging.NullHandler'}


###############################################################################
# DATABASE SETTINGS
###############################################################################

DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'transaction_hooks.backends.postgresql_psycopg2',
        'NAME': os.getenv("DATABASE_NAME", None),
        'USER': os.getenv("DATABASE_USER", None),
        'PASSWORD': os.getenv("DATABASE_PASSWORD", None),
        'HOST': os.getenv("DATABASE_HOST", None),
        'PORT': os.getenv("DATABASE_PORT", None),
    }
}


###############################################################################
# BROKER SETTINGS
###############################################################################

BROKER_URL = 'amqp://{}:{}@{}:{}/{}'.format(
    os.getenv("RABBITMQ_USER", None),
    os.getenv("RABBITMQ_PASSWORD", None),
    os.getenv("RABBITMQ_HOST", None),
    os.getenv("RABBITMQ_PORT", "5672"),
    os.getenv("RABBITMQ_VHOST", "tower"))

CHANNEL_LAYERS = {
    'default': {'BACKEND': 'asgi_amqp.AMQPChannelLayer',
                'ROUTING': 'awx.main.routing.channel_routing',
                'CONFIG': {'url': BROKER_URL}}
}


###############################################################################
# CACHE SETTINGS
###############################################################################

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '{}:{}'.format(os.getenv("MEMCACHED_HOST", None),
                                   os.getenv("MEMCACHED_PORT", "11211"))
    },
}


###############################################################################
# LDAP SETTINGS
###############################################################################

uri = os.getenv('AUTH_LDAP_SERVER_URI')
if uri is not None:
    AUTH_LDAP_SERVER_URI = uri
    AUTH_LDAP_BIND_DN = os.getenv('AUTH_LDAP_BIND_DN', '')
    AUTH_LDAP_BIND_PASSWORD = os.getenv('AUTH_LDAP_BIND_PASSWORD', '')
    user_subtree = os.getenv('AUTH_LDAP_USER_SEARCH_SUBTREE')
    user_search = os.getenv('AUTH_LDAP_USER_SEARCH')
    if user_subtree is not None and user_search is not None:
        import ldap
        from django_auth_ldap.config import LDAPSearch
        AUTH_LDAP_USER_SEARCH = LDAPSearch(user_subtree, ldap.SCOPE_SUBTREE,
                                           user_search)
    bind_template = os.getenv('AUTH_LDAP_USER_DN_TEMPLATE')
    if bind_template is not None:
        AUTH_LDAP_USER_DN_TEMPLATE = bind_template
    AUTH_LDAP_START_TLS = os.getenv('AUTH_LDAP_START_TLS', 'no').lower() in ('yes', 'true', 'on', '1')
