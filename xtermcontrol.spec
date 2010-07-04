Summary:	Dynamic control of XFree86 xterm properties
Name:		xtermcontrol
Version:	2.10
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.thrysoee.dk/xtermcontrol/%{name}-%{version}.tar.gz
# Source0-md5:	d108e24d0a8ddc1b58b37f559314eb76
URL:		http://www.thrysoee.dk/xtermcontrol/
BuildRequires:	autoconf
BuildRequires:	automake
Suggests:	xterm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xtermcontrol is an utility to dynamically query and modify xterm
properties, making it easy to query and change colors, title, font and
geometry of a running xterm.  Window manipulations such as de-/iconify,
raise/lower, maximize/restore and reset are also supported.
xtermcontrol also lets advanced users issue any xterm control sequence.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
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
