Summary:	A structural XML document editor
Name:		conglomerate
Version:	0.9.1
Release:	10
License:	GPLv2+
Group:		Editors
URL:		http://www.conglomerate.org/
Source:		http://prdownloads.sourceforge.net/conglomerate/%{name}-%{version}.tar.bz2
Source1:	%{name}-48.png
Patch:		conglomerate-0.9.1-format-strings.patch
BuildRequires:	gtksourceview-devel >= 0.6
BuildRequires:	libgnomeui2-devel
BuildRequires:	libxslt-devel
BuildRequires:	libglade2.0-devel >= 2.0.0
BuildRequires:	enchant-devel
BuildRequires:	scrollkeeper
BuildRequires:	gtk-doc
BuildRequires:	perl-XML-Parser
BuildRequires:	desktop-file-utils
#BuildRequires:	automake1.4
Requires(post): scrollkeeper desktop-file-utils
Requires(postun): scrollkeeper desktop-file-utils

%description
Conglomerate is an XML editor for GNOME, aiming to be as user-friendly as
possible, to help non-technical people to use DocBook and similar formats.


%prep
%setup -q
%patch -p1

%build
%configure2_5x
%make

%install
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

# menu entry
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-MoreApplications-Editors" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*


install -D pixmaps/conglomerate-icon-16.png %{buildroot}%{_miconsdir}/%{name}.png
install -D %{SOURCE1} %{buildroot}%{_liconsdir}/%{name}.png
install -D pixmaps/conglomerate-icon-32.png %{buildroot}%{_iconsdir}/%{name}.png

%{find_lang} %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%name.desktop
%{_datadir}/application-registry/*.applications
%{_datadir}/mime-info/*
#%dir %{_datadir}/omf/%name
#%{_datadir}/omf/%name/%name-C.omf
%{_datadir}/pixmaps/*
%{_datadir}/gtk-doc/html/%name
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_sysconfdir}/gconf/schemas/%{name}.schemas


%changelog
* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 0.9.1-9mdv2011.0
+ Revision: 677616
- rebuild to add gconftool as req

* Fri Jul 24 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.1-8mdv2011.0
+ Revision: 399238
- fix format strings
- update license

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.9.1-7mdv2009.0
+ Revision: 243624
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.9.1-5mdv2008.1
+ Revision: 148086
- drop old menu
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Aug 03 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.1-5mdv2008.0
+ Revision: 58476
- Import conglomerate



* Wed Aug 02 2006 Frederic Crozat <fcrozat@mandriva.com> 0.9.1-5mdv2007.0
- Rebuild with latest dbus

* Thu Jul 20 2006 Götz Waschk <waschk@mandriva.org> 0.9.1-4mdv2007.0
- add missing mime handling

* Thu Jul 20 2006 Götz Waschk <waschk@mandriva.org> 0.9.1-3mdv2007.0
- many spec fixes
- xdg menu

* Fri Nov 18 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.9.1-2mdk
- rebuild against openssl-0.9.8

* Fri Jun 24 2005 Götz Waschk <waschk@mandriva.org> 0.9.1-1mdk
- New release 0.9.1

* Tue Feb 15 2005 Jerome Soyer <saispo@mandrake.org> 0.9.0-1mdk
- New release 0.9.0

* Thu Nov  4 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.16-1mdk
- drop patch
- New release 0.7.16

* Wed Oct 27 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.15-1mdk
- drop ghost file
- fix omf file installation
- fix buildrequires
- fix docs build
- New release 0.7.15

* Fri Aug 20 2004 Austin Acton <austin@mandrake.org> 0.7.14-2mdk
- new menu

* Mon Jun 28 2004 Abel Cheung <deaddog@mandrakesoft.com> 0.7.14-1mdk
- New release 0.7.14

* Mon Jun 21 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.13-1mdk
- remove config file tag from GConf schemas
- add gtk-doc files
- buildrequires gtk-doc
- add source URL
- New release 0.7.13

* Fri May 21 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.12-3mdk
- yelp-pregenerate is dead, fix the post script

* Fri Apr 16 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.12-2mdk
- fix installation

* Tue Mar 02 2004 Abel Cheung <deaddog@deaddog.org> 0.7.12-1mdk
- New version

* Mon Feb 16 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.11-1mdk
- remove gtk-doc stuff
- new version

* Tue Jan 13 2004 Buchan Milne <bgmilne@linux-mandrake.com> 0.7.10-1mdk
- 0.7.10

* Wed Jan  7 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.8-2mdk
- fix buildrequires

* Tue Dec 23 2003 Arkadiusz Lipiec <arkadiusz.lipiec@gazeta.pl> 0.7.8-1mdk
- new version
- icon 32x32 is in pixmaps directory (no need to source2 tag)

* Fri Dec 12 2003 Abel Cheung <deaddog@deaddog.org> 0.7.7-1mdk
- new version
- Remove patch0 (upstream)

* Thu Oct 30 2003 Götz Waschk <waschk@linux-mandrake.com> 0.7.6-1mdk
- new version

* Wed Oct  8 2003 Götz Waschk <waschk@linux-mandrake.com> 0.7.5-1mdk
- fix rpmlint warning
- add gtk-doc docs
- fix changelog (Abel Cheung, can you please use ISO-8859-1 next time?)
- new version

* Mon Sep 29 2003 Abel Cheung <deaddog@deaddog.org> 0.7.4-1mdk
- 0.7.4
- Patch0: Fix path of faq XML file in document
- Convert this spec to UTF-8
- Fix doc pre-generation

* Tue Sep 23 2003 Götz Waschk <waschk@linux-mandrake.com> 0.7.3-1mdk
- new version

* Mon Sep 22 2003 Abel Cheung <deaddog@deaddog.org> 0.7.2-4mdk
- Generate help file cache
- Register help document with scrollkeeper

* Mon Sep 22 2003 Götz Waschk <waschk@linux-mandrake.com> 0.7.2-3mdk
- fix buildrequires

* Sat Sep 20 2003 Abel Cheung <deaddog@deaddog.org> 0.7.2-2mdk
- spec tweaks

* Fri Sep 19 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.7.2-1mdk
- update

* Mon Aug 11 2003 Abel Cheung <maddog@linux.org.hk> 0.5.4-1mdk
- First Mandrake spec
