AWX-Web Docker Image
================

A Docker image for the awx_web service, part of [Ansible AWX](https://github.com/ansible/awx).

## Variables

| Variable                        | Default               | Description                                           |
|---------------------------------|-----------------------|-------------------------------------------------------|
| `SECRET_KEY`                    | `privateawx`          | Encryption key used by AWX                            |
| `ALLOWED_HOSTS`                 | `*`                   | Comma-separated list of hosts that can access awx_web |
| `CLUSTER_HOST_ID`               | `awx`                 | Used for Celery queue naming                          |
| `SERVER_EMAIL`                  | `root@localhost`      |                                                       |
| `DEFAULT_FROM_EMAIL`            | `webmaster@localhost` |                                                       |
| `EMAIL_SUBJECT_PREFIX`          | `[AWX] `              |                                                       |
| `EMAIL_HOST`                    | `localhost`           | SMTP server to use to send email                      |
| `EMAIL_PORT`                    | `25`                  | Port to connect to SMTP server                        |
| `EMAIL_HOST_USER`               | (empty string)        | User to authenticate to SMTP server with              |
| `EMAIL_HOST_PASSWORD`           | (empty string)        | Password used for SMTP authentication                 |
| `EMAIL_USE_TLS`                 | `no`                  | Whether to use TLS when connecting to SMTP server     |
| `LOGGING_LEVEL`                 | `DEBUG`               | Logging level                                         |
| `DATABASE_NAME`                 | (none)                |                                                       |
| `DATABASE_USER`                 | (none)                |                                                       |
| `DATABASE_PASSWORD`             | (none)                |                                                       |
| `DATABASE_HOST`                 | (none)                |                                                       |
| `DATABASE_PORT`                 | (none)                |                                                       |
| `RABBITMQ_USER`                 | (none)                |                                                       |
| `RABBITMQ_PASSWORD`             | (none)                |                                                       |
| `RABBITMQ_HOST`                 | (none)                |                                                       |
| `RABBITMQ_PORT`                 | `5672`                |                                                       |
| `RABBITMQ_VHOST`                | `tower`               |                                                       |
| `MEMCACHED_HOST`                | (none)                |                                                       |
| `MEMCACHED_PORT`                | `11211`               |                                                       |
| `AUTH_LDAP_SERVER_URI`          | (none)                | LDAP URI of LDAP server for authentication            |
| `AUTH_LDAP_BIND_DN`             | (none)                |                                                       |
| `AUTH_LDAP_BIND_PASSWORD`       | (none)                |                                                       |
| `AUTH_LDAP_USER_SEARCH_SUBTREE` | (none)                | Base LDAP path where users are found                  |
| `AUTH_LDAP_USER_SEARCH`         | (none)                | Search string to use for finding users                |
| `AUTH_LDAP_USER_DN_TEMPLATE`    | (none)                | User DN template                                      |
| `AUTH_LDAP_START_TLS`           | `no`                  | Whether to use TLS in LDAP connection                 |
