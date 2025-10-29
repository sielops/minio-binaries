Name:           minio
Version:        placeholder
Release:        1
Summary:        MinIO High Performance Object Storage
License:        AGPL-3.0
URL:            https://min.io
Source0:        minio
Source1:        minio.service
Source2:        minio.default
BuildArch:      x86_64

%description
MinIO is a high performance, S3 compatible object storage server.

%prep
mkdir -p %{_builddir}/%{name}-%{version}

%build
# Nothing to build

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/local/bin/minio

install -Dm644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/minio.service

install -Dm644 %{SOURCE2} %{buildroot}/etc/default/minio

%pre
getent group minio-user >/dev/null || groupadd -r minio-user
getent passwd minio-user >/dev/null || useradd -r -g minio-user -s /sbin/nologin minio-user

%post
if [ $1 -eq 1 ] ; then
    systemctl daemon-reload >/dev/null 2>&1 || :
    systemctl enable minio.service >/dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 0 ] ; then
    systemctl --no-reload disable minio.service >/dev/null 2>&1 || :
    systemctl stop minio.service >/dev/null 2>&1 || :
fi

%postun
systemctl daemon-reload >/dev/null 2>&1 || :

%files
/usr/local/bin/minio
/usr/lib/systemd/system/minio.service
/etc/default/minio
