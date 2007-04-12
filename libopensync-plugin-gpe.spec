%define name	libopensync-plugin-gpe
%define version	0.20
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	GPE plugin for opensync synchronization tool
Version: 	%{version}
Release: 	%{release}

Source:		svn://svn.opensync.org/plugins/gpe/%{name}-%{version}.tar.bz2
URL:		http://www.opensync.org
License:	LGPL
Group:		Office
BuildRoot:	%{_tmppath}/%{name}-buildroot

BuildRequires:	opensync-devel >= 0.20
BuildRequires:  libneon-devel

%description
This plugin allows applications using OpenSync to synchronise via GPE

%prep
%setup -q
autoreconf -sfi

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*
%{_includedir}/opensync-1.0/opensync/gpe_sync.h


