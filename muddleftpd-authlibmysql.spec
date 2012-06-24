%define         shortname       authlibmysql
Summary:	Library to MySQL authentication for muddleftpd
Summary(pl.UTF-8):   Biblioteka autentykacji MySQL dla muddleftpd
Name:		muddleftpd-authlibmysql
Version:	0.1
Release:	3.1
License:	GPL
Group:		Daemons
Source0:	http://www.arach.net.au/~wildfire/muddleftpd/modules/%{shortname}-%{version}.tar.gz
# Source0-md5:	7abbc5e21b08fbdddbb20fb9fd4ba837
Patch0:		%{shortname}-paths.patch
Patch1:		%{shortname}-vmailpwd.patch
URL:		http://www.muddleftpd.cx/
BuildRequires:	autoconf
BuildRequires:	mysql-static
Requires:	muddleftpd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir		%{_libdir}/muddle

%description
This module allows muddleftpd authenticate using a MySQL server. This
module will read client information from a supplied table/database
within MySQL.

%description -l pl.UTF-8
Ten moduł pozwala muddleftpd autentykować użytkowników przy użyciu
serwera MySQL. Moduł czyta informacje o kliencie z podanej tabeli/bazy
MySQL.

%prep
%setup -q -n %{shortname}-%{version}
%patch0 -p 1
%patch1 -p 1

%build
%{__autoconf}
%configure \
	--with-mysql=%{_prefix}
%{__make} LIBS="-lmysqlclient"

%install
rm -rf $RPM_BUILD_ROOT
install -D libauthmysql.so $RPM_BUILD_ROOT%{_pkglibdir}/libauthmysql.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README*
%attr(750,root,root) %{_pkglibdir}/libauthmysql.so
