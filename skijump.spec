%define	name	skijump
%define	version	0.2.0
%define	rel	11
%define release %mkrel %rel

%define	Summary	Open Ski Jumping

Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		https://skijump.sourceforge.net/	
Source0:	http://prdownloads.sourceforge.net/skijump/%{name}-%{version}.tar.bz2
#Source11:	%{name}-16x16.png
#Source12:	%{name}-32x32.png
#Source13:	%{name}-48x48.png
Patch0:		skijump-0.2.0-compile-fix.patch
Patch1:		skijump-0.2.0-fix-install-as-non-root.patch
Patch2:		skijump-0.2.0-fix-vardir.patch
Patch3:		skijump-0.2.0-allegro-4.2.patch
Patch4:		skijump-0.2.0-compile-fix-2.patch
License:	GPLv2
Group:		Games/Sports
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Summary:	%{Summary}
BuildRequires:  allegro-devel
BuildRequires:	automake autoconf

%description
A clone of Deluxe Ski Jump

%prep
%setup -q

%patch1 -p0
%patch2 -p0
%patch3 -p1
%patch4 -p1

aclocal
automake --add-missing --copy --foreign
autoconf

%patch0 -p1

%build
%configure2_5x	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std


install -d %{buildroot}%{_datadir}/applications
cat <<EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Name=%{Summary}
Comment=%{Summary}
Exec=%{_gamesbindir}/%{name}
Icon=sport_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;SportsGame;X-MandrivaLinux-MoreApplications-Games-Sports;
EOF

#%{__install} -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
#%{__install} -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
#%{__install} -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README
%{_gamesdatadir}/%{name}
#%{_iconsdir}/%{name}.png
#%{_liconsdir}/%{name}.png
#%{_miconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
%attr(4755,games,games) %{_gamesbindir}/*
%dir %attr(0775,games,games) %{_localstatedir}/games/%{name}
%dir %attr(0775,games,games) %{_localstatedir}/games/%{name}/replays
%attr(0664,games,games) %{_localstatedir}/games/%{name}/*.txt
%attr(0664,games,games) %{_localstatedir}/games/%{name}/replays/*.rpl

