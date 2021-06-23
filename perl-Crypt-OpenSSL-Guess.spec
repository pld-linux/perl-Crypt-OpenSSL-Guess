#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%define		pdir	Crypt
%define		pnam	OpenSSL-Guess
Summary:	Crypt::OpenSSL::Guess - Guess OpenSSL include path
Summary(pl.UTF-8):	Crypt::OpenSSL::Guess - zgadywanie ścieżki nagłówków OpenSSL
Name:		perl-Crypt-OpenSSL-Guess
Version:	0.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a126716a88c9e16ef5b9e4216820d322
URL:		https://metacpan.org/dist/Crypt-OpenSSL-Guess
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.64
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.98
%endif
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::OpenSSL::Guess provides helpers to guess OpenSSL include path
on any platforms.

%description -l pl.UTF-8
Crypt::OpenSSL::Guess udostępnia funkcje pomocnicze do zgadywania
ścieżki nagłówków na dowolnej platformie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

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
%{perl_vendorlib}/Crypt/OpenSSL/Guess.pm
%{_mandir}/man3/Crypt::OpenSSL::Guess.3pm*
