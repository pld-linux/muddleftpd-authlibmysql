%define         shortname       authlibmysql
Summary:	Library to MySQL authentication for muddleftpd
Name:		muddleftpd-authlibmysql
Version:	0.1
Release:	1
License:	GPL
Group:		Daemons
Group(de):	Server
Group(pl):	Serwery
Source0:	http://www.arach.net.au/~wildfire/muddleftpd/modules/%{shortname}-%{version}.tar.gz
Patch0:		%{shortname}-paths.patch
URL:		http://www.muddleftpd.cx/
BuildRequires:	mysql-static
Requires:	muddleftpd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir		%{_libdir}/muddle

%description
This module allows muddleftpd authenticate using a MySQL server. This
module will read client information from a supplied table/database
within MySQL.

%prep
%setup -q -n %{shortname}-%{version}
%patch0 -p 1

%build
autoconf
%configure \
	--with-mysql=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -D libauthmysql.so $RPM_BUILD_ROOT/%{_pkglibdir}/libauthmysql.so

gzip -9nf AUTHORS CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(750,root,root) %{_pkglibdir}/libauthmysql.so
