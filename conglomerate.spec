%define version 0.9.1
%define release %mkrel 9

Summary:	A structural XML document editor
Name:		conglomerate
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Editors
URL:		http://www.conglomerate.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
rm -rf %{buildroot}
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

# menu entry
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-MoreApplications-Editors" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


install -D pixmaps/conglomerate-icon-16.png %{buildroot}%{_miconsdir}/%{name}.png
install -D %{SOURCE1} %{buildroot}%{_liconsdir}/%{name}.png
install -D pixmaps/conglomerate-icon-32.png %{buildroot}%{_iconsdir}/%{name}.png

#install -m 0644 doc/C/faq.xml %{buildroot}%{_datadir}/gnome/help/%{name}/C/faq.xml

%{find_lang} %{name} --with-gnome
#for omf in %buildroot%_datadir/omf/%name/%name-??*.omf;do 
#echo "%lang($(basename $omf|sed -e s/%name-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
#done

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%update_scrollkeeper
%post_install_gconf_schemas %name
%update_desktop_database
%endif

%preun
%preun_uninstall_gconf_schemas %name

%if %mdkversion < 200900
%postun
%clean_menus
%clean_scrollkeeper
%clean_desktop_database
%endif

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%name.desktop
%{_datadir}/application-registry/*.applications
%{_datadir}/mime-info/*
%dir %{_datadir}/omf/%name
%{_datadir}/omf/%name/%name-C.omf
%{_datadir}/pixmaps/*
%{_datadir}/gtk-doc/html/%name
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_sysconfdir}/gconf/schemas/%{name}.schemas
