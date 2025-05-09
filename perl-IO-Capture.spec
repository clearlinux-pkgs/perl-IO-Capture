#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-IO-Capture
Version  : 0.05
Release  : 32
URL      : https://cpan.metacpan.org/authors/id/R/RE/REYNOLDS/IO-Capture-0.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RE/REYNOLDS/IO-Capture-0.05.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-capture-perl/libio-capture-perl_0.05-4.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-IO-Capture-license = %{version}-%{release}
Requires: perl-IO-Capture-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
IO::Capture
The IO::Capture Module defines an abstract base class that can be
used to create any number of useful sub-classes that capture output
being sent on a filehandle such as STDOUT or STDERR.
Several modules come with the distribution that define sub-
classes of IO::Capture to do just that. (I.e., capture STDOUT and STDERR)
See the man page IO::Capture::Overview for a discussion of these
modules and how to build a module to sub-class the B<IO::Capture>
class yourself.
To build and install this module, follow the standard procedures:

%package dev
Summary: dev components for the perl-IO-Capture package.
Group: Development
Provides: perl-IO-Capture-devel = %{version}-%{release}
Requires: perl-IO-Capture = %{version}-%{release}

%description dev
dev components for the perl-IO-Capture package.


%package license
Summary: license components for the perl-IO-Capture package.
Group: Default

%description license
license components for the perl-IO-Capture package.


%package perl
Summary: perl components for the perl-IO-Capture package.
Group: Default
Requires: perl-IO-Capture = %{version}-%{release}

%description perl
perl components for the perl-IO-Capture package.


%prep
%setup -q -n IO-Capture-0.05
cd %{_builddir}
tar xf %{_sourcedir}/libio-capture-perl_0.05-4.debian.tar.xz
cd %{_builddir}/IO-Capture-0.05
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/IO-Capture-0.05/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IO-Capture
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-IO-Capture/45bafea63a1ecddcfcc1e22844930ca8f7f56ccb || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::Capture.3
/usr/share/man/man3/IO::Capture::Overview.3
/usr/share/man/man3/IO::Capture::Stderr.3
/usr/share/man/man3/IO::Capture::Stdout.3
/usr/share/man/man3/IO::Capture::Tie_STDx.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IO-Capture/45bafea63a1ecddcfcc1e22844930ca8f7f56ccb

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
