#
# Conditional build:
%bcond_with	mmx	# use MMX (makes sense on i586/i686)
#
%ifarch athlon pentium3 pentium4
%define	with_mmx	1
%endif
Summary:	Fast movie recorder and player for Linux
Summary(pl.UTF-8):	Szybka nagrywarka i odtwarzacz filmów pod Linuksa
Name:		NuppelVideo
Version:	0.52a
Release:	5
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://frost.htu.tuwien.ac.at/~roman/nuppelvideo/%{name}-%{version}.tar.gz
# Source0-md5:	320fa43a19c71778ea0d403528125c1e
Patch0:		%{name}-make.patch
Patch1:		%{name}-nonx86.patch
URL:		http://frost.htu.tuwien.ac.at/~roman/nuppelvideo/
BuildRequires:	XFree86-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NuppelVideo is a simple low consuming and fast capture program for
bttv-cards (BT8x8) it is based on the RTjpeg2.0 test3* programs from
Justin Schoemann, who wrote the very fast and fine RTjpeg2.0 codec
(improved by Joerg Walter and Wim Taymans).

%description -l pl.UTF-8
NuppelVideo jest prostym, mało zasobożernym i szybkim programem do
zrzucania obrazu z kart bttv (BT8x8) bazującym na programach RTjpeg2.0
test3* Justina Schoemanna, który napisał bardzo szybki i dobry codec
RTjpeg2.0 (poprawiony przez Joerga Waltera i Wima Taymansa).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

sed -i -e 's@-L/usr/X11R6/lib@-L/usr/X11R6/%{_lib}@' Makefile

%build
%{__make} \
	CC="%{__cc}" \
	COPTS="%{rpmcflags}%{?with_mmx: -DMMX}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* LICENSE*
%attr(755,root,root) %{_bindir}/*
