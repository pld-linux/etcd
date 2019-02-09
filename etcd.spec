# git rev-parse --short v3.3.10
%define		githash	d57e8b8
Summary:	A highly-available key value store for shared configuration
Name:		etcd
Version:	3.3.12
Release:	1
License:	Apache v2.0
Group:		Daemons
Source0:	https://github.com/coreos/etcd/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	23bc317f1db7730bcd408575616ea651
Patch0:		nogit.patch
URL:		https://github.com/coreos/etcd/
BuildRequires:	golang >= 1.2.1-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# disable debug packages for go packages
%define		debug_package %{nil}

# this will fool adapter not to touch 'etcd'
%define		_sysconfdir	__bogus__value

%description
A highly-available key value store for shared configuration.

%prep
%setup -q
%patch0 -p1

%build
GIT_SHA=%{githash} \
sh -xe build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p bin/etcd $RPM_BUILD_ROOT%{_bindir}
install -p bin/etcdctl $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md Documentation/v2/internal-protocol-versioning.md
%attr(755,root,root) %{_bindir}/etcd
%attr(755,root,root) %{_bindir}/etcdctl
