#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-Capture
Version  : 0.05
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/R/RE/REYNOLDS/IO-Capture-0.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RE/REYNOLDS/IO-Capture-0.05.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-capture-perl/libio-capture-perl_0.05-4.debian.tar.xz
Summary  : Abstract Base Class to build modules to capture output.
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-IO-Capture-license = %{version}-%{release}
BuildRequires : buildreq-cpan

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


%prep
%setup -q -n IO-Capture-0.05
cd ..
%setup -q -T -D -n IO-Capture-0.05 -b 1
mkdir -p deblicense/
cp -r %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/IO-Capture-0.05/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IO-Capture
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-IO-Capture/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.2/IO/Capture.pm
/usr/lib/perl5/vendor_perl/5.28.2/IO/Capture/Overview.pod
/usr/lib/perl5/vendor_perl/5.28.2/IO/Capture/Stderr.pm
/usr/lib/perl5/vendor_perl/5.28.2/IO/Capture/Stdout.pm
/usr/lib/perl5/vendor_perl/5.28.2/IO/Capture/Tie_STDx.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::Capture.3
/usr/share/man/man3/IO::Capture::Overview.3
/usr/share/man/man3/IO::Capture::Stderr.3
/usr/share/man/man3/IO::Capture::Stdout.3
/usr/share/man/man3/IO::Capture::Tie_STDx.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IO-Capture/deblicense_copyright
