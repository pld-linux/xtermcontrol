Summary:	Dynamic control of XFree86 xterm properties
Summary(pl.UTF-8):	Dynamiczne sterowanie właściwościami xterma z XFree86
Name:		xtermcontrol
Version:	3.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.thrysoee.dk/xtermcontrol/%{name}-%{version}.tar.gz
# Source0-md5:	cbc81a6516daba5b28fd5f26b8367f3d
URL:		http://www.thrysoee.dk/xtermcontrol/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
Suggests:	xterm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xtermcontrol is an utility to dynamically query and modify xterm
properties, making it easy to query and change colors, title, font and
geometry of a running xterm. Window manipulations such as de-/iconify,
raise/lower, maximize/restore and reset are also supported.
xtermcontrol also lets advanced users issue any xterm control
sequence.

%description -l pl.UTF-8
xtermcontrol to narzędzie do dynamicznego odczytywania i modyfikowania
właściwości xterma, ułatwiające odczyt i zmianę kolorów, tytułu, fontu
oraz geometrii działającego xterma. Obsługiwane są też operacje na
oknie takie jak przejście i powrót z trybu ikony,
powiększenie/zmniejszenie, maksymalizacja/powrót i reset ustawień.
xtermcontrol pozwala także zaawansowanym użytkownikom wysyłać dowolne
sekwencje sterujące xterma.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog doc/ctlseqs.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
