%define realname IO-Stringy

Summary:	Perl module for I/O on in-core objects like strings and arrays
Name:		perl-%{realname}
Version:	2.113
Release:	1
License:	Artistic/GPLv2
Group:		Development/Perl
Url:		https://metacpan.org/dist/IO::Stringy
Source0:	https://cpan.metacpan.org/authors/id/C/CA/CAPOEIRAB/IO-Stringy-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl
BuildRequires:	perl(Test::More)
%rename perl-IO-stringy

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
%autosetup -p1 -n %{realname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make_build test

%install
%make_install

%files
%doc README
%{perl_vendorlib}/IO
%{_mandir}/man3/*
