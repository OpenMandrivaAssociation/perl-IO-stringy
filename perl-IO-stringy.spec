%define realname IO-stringy
%define	name	perl-%{realname}
%define	version	2.110
%define	release	%mkrel 8

Summary:	Perl module for I/O on in-core objects like strings and arrays
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/IO/%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%else
BuildRequires:	perl
%endif
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%description
This toolkit primarily provides modules for performing both traditional
and object-oriented i/o) on things *other* than normal filehandles; in
particular, the IO::Scalar manpage, the IO::ScalarArray manpage, and the
IO::Lines manpage.

If you have access to tie(), these classes will make use of the the
IO::WrapTie manpage module to inherit a convenient new_tie()
constructor. It also exports a nice wraptie() function.

In the more-traditional IO::Handle front, we have the IO::AtomicFile
manpage which may be used to painlessly create files which are updated
atomically.

And in the "this-may-prove-useful" corner, we have the IO::Wrap manpage,
whose exported wraphandle() function will clothe anything that's not a
blessed object in an IO::Handle-like wrapper... so you can just use OO
syntax and stop worrying about whether your function's caller handed you
a string, a globref, or a FileHandle.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%__make

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_mandir}/*/*
%{perl_vendorlib}/IO

