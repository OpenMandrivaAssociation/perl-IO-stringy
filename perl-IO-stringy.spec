%define realname IO-stringy
%define	name	perl-%{realname}
%define	version	2.110

Summary:	Perl module for I/O on in-core objects like strings and arrays
Name:		%{name}
Version:	%{version}
Release:	13
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/IO/%{realname}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl
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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_mandir}/*/*
%{perl_vendorlib}/IO



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.110-10mdv2012.0
+ Revision: 765374
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.110-9
+ Revision: 763891
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.110-8
+ Revision: 667214
- mass rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.110-7mdv2010.1
+ Revision: 426513
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.110-6mdv2009.1
+ Revision: 351930
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.110-5mdv2009.0
+ Revision: 223799
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 2.110-4mdv2008.1
+ Revision: 180413
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 2.110-3mdv2008.0
+ Revision: 23391
- rebuild


* Fri Apr 28 2006 Scott Karns <scottk@mandriva.org> 2.110-2mdk
- Updated specfile to meet current perl packaging policies

* Thu Feb 17 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.110-1mdk
- 2.110

* Wed Apr 21 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.109-1mdk
- 2.109

* Wed Feb 25 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.108-7mdk
- rebuild
- own dir

* Wed Aug 13 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.108-6mdk
- rebuild for new perl
- drop Prefix tag
- drop $RPM_OPT_FLAGS, noarch..
- don't use PREFIX
- use %%makeinstall_std macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.108-5mdk
- rebuild for new auto{prov,req}

