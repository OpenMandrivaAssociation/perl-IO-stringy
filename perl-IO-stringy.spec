%define realname IO-stringy
%define	version	2.110

Summary:	Perl module for I/O on in-core objects like strings and arrays
Name:		perl-%{realname}
Version:	%{version}
Release:	15
License:	Artistic/GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{realname}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/IO/%{realname}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl

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
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/IO
%{_mandir}/man3/*

