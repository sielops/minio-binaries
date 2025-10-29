Name:           minio
Version:        0.0.0
Release:        1
Summary:        MinIO - High Performance Object Storage

License:        AGPL-3.0-or-later
URL:            https://min.io
Source0:        %{name}
BuildArch:      x86_64

%description
MinIO is a high performance object storage server compatible with Amazon S3 APIs.

%prep
# No source tarball, binary-only build
mkdir -p %{_builddir}/%{name}-%{version}

%build
# Nothing to build

%install
mkdir -p %{buildroot}/usr/local/bin
cp %{SOURCE0} %{buildroot}/usr/local/bin/minio
chmod 755 %{buildroot}/usr/local/bin/minio

%files
/usr/local/bin/minio