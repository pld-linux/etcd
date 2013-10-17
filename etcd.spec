# disable debug packages for go packages
%define debug_package %{nil}
Summary:	A highly-available key value store for shared configuration
Name:		etcd
Version:	0.1.2
Release:	1
License:	Apache v2.0
Group:		Daemons
Source0:	https://github.com/coreos/etcd/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	4d0fb3fd2fc3aa051b47ff5d8fb151cf
URL:		https://github.com/coreos/etcd/
BuildRequires:	golang
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A highly-available key value store for shared configuration.

%prep
%setup -q
sed -i "s/^\(VER=\).*HEAD)/\1%{version}/" scripts/release-version

%build
./build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md Documentation/internal-protocol-versioning.md
%attr(755,root,root) %{_bindir}/%{name}
