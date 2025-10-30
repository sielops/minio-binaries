Name:           mc
Version:        placeholder
Release:        1
Summary:        MinIO Client (mc)
License:        AGPL-3.0
URL:            https://min.io
Source0:        mc
BuildArch:      x86_64

%description
MinIO Client (mc) provides UNIX-like commands for filesystems and object storage.

%prep
mkdir -p %{_builddir}/%{name}-%{version}

%build
# Nothing to build

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/local/bin/mc

%files
/usr/local/bin/mc
