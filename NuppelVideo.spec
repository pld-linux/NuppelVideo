Summary:	Fast movie recorder and player for Linux
Summary(pl):	Szybka nagrywarka i odtwarzacz filmów pod Linuksa
Name:		NuppelVideo
Version:	0.52a
Release:	3
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://mars.tuwien.ac.at/~roman/nuppelvideo/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
URL:		http://mars.tuwien.ac.at/~roman/nuppelvideo/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}

%define		_prefix		/usr/X11R6

%description
NuppelVideo is a simple low consuming and fast capture program for
bttv-cards (BT8x8) it is based on the RTjpeg2.0 test3* programs from
Justin Schoemann, who wrote the very fast and fine RTjpeg2.0 codec
(improved by Joerg Walter and Wim Taymans).

%description -l pl
NuppelVideo jest prostym, ma³o zasobo¿ernym i szybkim programem do
zrzucania obrazu z kart bttv (BT8x8) bazuj±cym na programach RTjpeg2.0
test3* Justina Schoemanna, który napisa³ bardzo szybki i dobry codec
RTjpeg2.0 (poprawiony przez Joerga Waltera i Wima Taymansa).

%prep
%setup  -q
%patch0 -p1

%build
%{__make} \
	CC=%{__cc} \
%ifarch athlon
	COPTS="%{rpmcflags} -DMMX"
%else
	COPTS="%{rpmcflags}"
%endif

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
