#
# Conditional build:
# test is known to fail on version 2.2
%bcond_with	tests	# do perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	DBI-AsForm
Summary:	Produce HTML form elements for database columns
Summary(pl):	Tworzenie pól formularzy HTML z kolumn baz danych
Name:		perl-Class-DBI-AsForm
Version:	2.3
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	158e2f3eb51f10bedbf36e5199802f9a
URL:		http://search.cpan.org/dist/Class-DBI-AsForm/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-DBI >= 0.94
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-Class-DBI-Plugin-Type
%endif
Requires:	perl-Class-DBI >= 0.94
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module helps to generate HTML forms for creating new database
rows or editing existing rows. It maps column names in a database
table to HTML form elements which fit the schema. Large text fields
are turned into textareas, and fields with a has-a relationship to
other Class::DBI tables are turned into select drop-downs populated
with objects from the joined class.

%description -l pl
Modu³ ten u³atwia generowanie formularzy HTML tworz±cych nowe wiersze
bazy danych lub edytuj±cych istniej±ce wiersze. Odwzorowuje
w okre¶lony sposób nazwy kolumn bazy danych na elementy formularza
HTML.  Du¿e pola tekstowe s± przekszta³cane na wielowierszowe pola
tekstowe (textarea), a pola posiadaj±ce zwi±zki z innymi tabelami
Class::DBI s± przekszta³cane w pola wyboru wype³nione obiektami
powi±zanej klasy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/%{pdir}/DBI/AsForm.pm
%{_mandir}/man3/*
