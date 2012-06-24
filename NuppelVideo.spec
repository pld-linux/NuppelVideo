Summary:	Fast movie recorder and player for linux
Name:		NuppelVideo
Version:	0.52a
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://mars.tuwien.ac.at/~roman/nuppelvideo/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
URL:		http://mars.tuwien.ac.at/~roman/nuppelvideo/
BUildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
NuppelVideo is a simple low consuming and fast capture program for
bttv-cards (BT8x8) it is based on the RTjpeg2.0 test3* programs from
Justin Schoemann , who wrote the very fast and fine RTjpeg2.0 codec
(improved by Joerg Walter and Wim Taymans).

%prep
%setup  -q
%patch0 -p1

%build
%{__make} \
	CC=%{__cc} \
%ifarch i686
	COPTS="%{rpmcflags} -DMMX"
%else
	COPTS="%{rpmcflags}"
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir}

gzip -9nf README* LICENSE*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
