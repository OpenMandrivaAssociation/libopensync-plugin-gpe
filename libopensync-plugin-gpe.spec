Name: 	 	libopensync-plugin-gpe
Version: 	0.22
Epoch:		1
Release: 	%{mkrel 2}
Summary: 	GPE plugin for OpenSync synchronization framework
Source0:	http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
URL:		http://www.opensync.org
License:	LGPLv2+
Group:		Office
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libopensync-devel < 0.30
BuildRequires:  libneon-devel
Requires:	libopensync >= %{epoch}:%{version}

%description
This plugin allows GPE-based devices to synchronize using the OpenSync
framework.

%prep
%setup -q
autoreconf -sfi

%build
%configure2_5x
%make
										
%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{_includedir}/opensync-1.0/opensync/gpe_sync.h

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*

