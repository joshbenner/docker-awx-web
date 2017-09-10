FROM krallin/centos-tini:7

RUN export AWX_VERSION=devel && \
    yum -y install epel-release && \
    yum -y localinstall http://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm && \
    yum -y update && \
    # Workaround, see: https://bugs.centos.org/view.php?id=13669&nbn=8
    rpm -ivh https://kojipkgs.fedoraproject.org//packages/http-parser/2.7.1/3.el7/x86_64/http-parser-2.7.1-3.el7.x86_64.rpm && \
    yum -y install ansible git curl python-psycopg2 python-pip gettext bzip2 \
           python-setuptools libselinux-python setools-libs yum-utils sudo acl \
           make postgresql-devel nginx python-psutil libxml2-devel \
           libxslt-devel libstdc++.so.6 gcc cyrus-sasl-devel cyrus-sasl \
           openldap-devel libffi-devel python-pip xmlsec1-devel swig \
           krb5-devel xmlsec1-openssl xmlsec1 xmlsec1-openssl-devel \
           libtool-ltdl-devel bubblewrap gcc-c++ python-devel nodejs && \
    pip install virtualenv supervisor && \
    mkdir -p /var/lib/awx/public/static /var/log/tower /etc/tower && \
    chgrp -Rf root /var/lib/awx && chmod -Rf g+w /var/lib/awx && \
    git clone https://github.com/ansible/awx.git /awx && \
    cd /awx && git checkout $AWX_VERSION && \
    make sdist && \
    VENV_BASE=/var/lib/awx/venv make requirements && \
    yum -y remove gcc postgresql-devel libxml2-devel libxslt-devel nodejs \
           cyrus-sasl-devel openldap-devel xmlsec1-devel krb5-devel gettext \
           xmlsec1-openssl-devel libtool-ltdl-devel gcc-c++ python-devel \
           bzip2 && \
    yum -y clean all && rm -rf /root/.cache && \
    export BUILD_VERSION=`git describe --long | sed 's/\\-g.*//' | sed 's/\\-/\\./'` && \
    echo "$BUILD_VERSION" > /var/lib/awx/.tower_version && \
    OFFICIAL=yes pip install dist/awx-$BUILD_VERSION.tar.gz && \
    cd / && rm -rf /awx && \
    chmod g+w /etc/passwd && \
    chmod -R 777 /var/log/nginx /var/lib/nginx && \
    rm -rf /root/.cache

COPY files/ /

USER 1000
EXPOSE 8052
WORKDIR /var/lib/awx
CMD /usr/bin/launch_awx.sh
