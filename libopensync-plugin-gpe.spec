%define name	libopensync-plugin-gpe
%define version	0.36
%define release %mkrel 1

Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	GPE plugin for opensync synchronization tool
Source:		http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
URL:		http://www.opensync.org
License:	GPLv2+
Group:		Office
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	cmake
BuildRequires:	opensync-devel >= 0.20
BuildRequires:  libneon-devel

%description
This plugin allows applications using OpenSync to synchronise via GPE

%prep
%setup -q

%build
%cmake
%make

%install
rm -rf $RPM_BUILD_ROOT
cd build
%makeinstall_std
cd -

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS
%{_libdir}/opensync-1.0/plugins/*
%{_datadir}/opensync-1.0/defaults/*
