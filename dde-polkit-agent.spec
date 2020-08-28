%global repo dde-polkit-agent
%global release_name test+c1

Name:           dde-polkit-agent
Version:        5.0.10
Release:        2
Summary:        Deepin Polkit Agent
License:        GPLv3
URL:            https://github.com/linuxdeepin/dde-polkit-agent
Source0:        %{repo}_%{version}-%{release_name}.orig.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  dtkcore-devel >= 5.1
BuildRequires:  dtkwidget-devel >= 5.1.1
BuildRequires:  dde-qt-dbus-factory-devel
BuildRequires:  dde-qt-dbus-factory
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  qt5-linguist
BuildRequires:  gsettings-qt-devel
BuildRequires:  qt5-qtmultimedia-devel 
BuildRequires:  qt5-qtx11extras-devel

%description
DDE Polkit Agent is the polkit agent used in Deepin Desktop Environment.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{repo}-%{version}-%{release_name}
sed -i 's|lrelease|lrelease-qt5|' translate_generation.sh
sed -i 's|/usr/lib|/usr/libexec|' dde-polkit-agent.pro polkit-dde-authentication-agent-1.desktop \
    pluginmanager.cpp

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%license LICENSE
/usr/libexec/polkit-1-dde/dde-polkit-agent
%{_datadir}/%{repo}/

%files devel
%{_includedir}/dpa/agent-extension-proxy.h
%{_includedir}/dpa/agent-extension.h

%changelog
* Fri Aug 28 2020 chenbo pan <panchenbo@uniontech.com> - 5.0.10-2
- fix compile fail

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.0.10-1
- Package init
