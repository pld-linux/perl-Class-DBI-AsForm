#
# Conditional build:
# _with_tests	- do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	DBI-AsForm
Summary:	Produce HTML form elements for database columns
Summary(pl):	Twórz pola formularzy HTML z kolumn baz danych
Name:		perl-%{pdir}-%{pnam}
Version:	1.0
Release:	1
License:	Unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	78c56252f32209f2b8eccaf6aa75c4af
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Class-DBI >= 0.94
Requires:	perl(Class::DBI) >= 0.94
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module helps to generate HTML forms for creating new database
rows or editing existing rows. It maps column names in a database
table to HTML form elements which fit the schema. Large text fields
are turned into textareas, and fields with a has-a relationship to
other Class::DBI tables are turned into select drop-downs populated
with objects from the joined class.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/%{pdir}/DBI/AsForm.pm
%{_mandir}/man3/*
