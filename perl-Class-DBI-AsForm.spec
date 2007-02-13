#
# Conditional build:
%bcond_without	tests	# do perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	DBI-AsForm
Summary:	Produce HTML form elements for database columns
Summary(pl.UTF-8):	Tworzenie pól formularzy HTML z kolumn baz danych
Name:		perl-Class-DBI-AsForm
Version:	2.42
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5799ef3305aff13b911b2f13f36951f5
URL:		http://search.cpan.org/dist/Class-DBI-AsForm/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-DBI >= 0.94
BuildRequires:	perl-Class-DBI-Plugin-Type
BuildRequires:	perl-DBD-SQLite2
BuildRequires:	perl-HTML-Tree
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

%description -l pl.UTF-8
Moduł ten ułatwia generowanie formularzy HTML tworzących nowe wiersze
bazy danych lub edytujących istniejące wiersze. Odwzorowuje w
określony sposób nazwy kolumn bazy danych na elementy formularza HTML.
Duże pola tekstowe są przekształcane na wielowierszowe pola tekstowe
(textarea), a pola posiadające związki z innymi tabelami Class::DBI są
przekształcane w pola wyboru wypełnione obiektami powiązanej klasy.

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
