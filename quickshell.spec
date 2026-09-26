Name:		quickshell
Version:	0.3.1
Release:	1
Summary:	Flexible QtQuick based desktop shell toolkit
License:	LGPL-3.0-only AND GPL-3.0-only
URL:		https://github.com/quickshell-mirror/quickshell
Source0:	https://github.com/quickshell-mirror/quickshell/archive/v%{version}/%{name}-%{version}.tar.gz
Group:		Window Manager/Bar

BuildSystem:	cmake
BuildOption:	-DBUILD_SHARED_LIBS=OFF
BuildOption:	-DCMAKE_BUILD_TYPE=RelWithDebInfo
BuildOption:	-DDISTRIBUTOR="OpenMandriva LX"
BuildOption:	-DDISTRIBUTOR_DEBUGINFO_AVAILABLE=YES
BuildOption:	-DINSTALL_QMLDIR="%{_qtdir}/qml"
BuildOption:	-DINSTALL_QML_PREFIX="%{_qtdir}/qml"

BuildRequires:	cmake
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6ShaderTools)
BuildRequires:	cmake(Qt6WaylandClient)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	pkgconfig(CLI11)
# breakpad was dropped upstream in favor of cpptrace
BuildRequires:	cmake(cpptrace)
BuildRequires:	pkgconfig(gbm)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(libpipewire-0.3)
BuildRequires:	pkgconfig(jemalloc)
BuildRequires:	qt6-qtbase-theme-gtk3
BuildRequires:	pkgconfig(pam)
BuildRequires:	pkgconfig(wayland-protocols)
# new in 0.3.1: src/services/polkit/CMakeLists.txt
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(polkit-agent-1)
BuildRequires:	pkgconfig(polkit-gobject-1)
BuildRequires:	spirv-tools
BuildRequires:	cmake(VulkanHeaders)

Recommends:	(%{name}-hyprland = %{EVRD} if hyprland)
Recommends:	(%{name}-i3 = %{EVRD} if i3)
Recommends:	(%{name}-wayland = %{EVRD} if %{mklibname wayland-client})
Recommends:	(%{name}-x11 = %{EVRD} if x11-server)
Recommends:	(%{name}-greetd = %{EVRD} if greetd)

Obsoletes:	quickshell = 1~1.gited52826-1

%description
Flexible QtQuick based desktop shell toolkit

%package hyprland
Summary:	Hyprland integration for %{name}
Requires:	%{name} = %{EVRD}
Requires:	hyprland

%description hyprland
Hyprland integration for %{name}

%package i3
Summary:	i3 integration for %{name}
Requires:	%{name} = %{EVRD}
Requires:	i3

%description i3
i3 integration for %{name}

%package wayland
Summary:	Wayland integration for %{name}
Requires:	%{name} = %{EVRD}

%description wayland
Wayland integration for %{name}

%package x11
Summary:	X11 integration for %{name}
Requires:	%{name} = %{EVRD}
Requires:	x11-server

%description x11
X11 integration for %{name}

%package greetd
Summary:	GreetD integration for %{name}
Requires:	%{name} = %{EVRD}
Requires:	greetd

%description greetd
GreetD integration for %{name}

%files
%license LICENSE LICENSE-GPL
%{_bindir}/qs
%{_bindir}/quickshell
%{_datadir}/applications/org.quickshell.desktop
%{_iconsdir}/hicolor/scalable/apps/org.quickshell.svg
%dir %{_qtdir}/qml/Quickshell
%{_qtdir}/qml/Quickshell/Bluetooth
%{_qtdir}/qml/Quickshell/DBusMenu
%{_qtdir}/qml/Quickshell/Io
%{_qtdir}/qml/Quickshell/Network
%dir %{_qtdir}/qml/Quickshell/Services
%{_qtdir}/qml/Quickshell/Services/Mpris
%{_qtdir}/qml/Quickshell/Services/Notifications
%{_qtdir}/qml/Quickshell/Services/Pam
%{_qtdir}/qml/Quickshell/Services/Pipewire
%{_qtdir}/qml/Quickshell/Services/Polkit
%{_qtdir}/qml/Quickshell/Services/SystemTray
%{_qtdir}/qml/Quickshell/Services/UPower
%{_qtdir}/qml/Quickshell/Widgets
%{_qtdir}/qml/Quickshell/_Window
%{_qtdir}/qml/Quickshell/qmldir
%{_qtdir}/qml/Quickshell/quickshell-core.qmltypes

%files hyprland
%{_qtdir}/qml/Quickshell/Hyprland

%files i3
%{_qtdir}/qml/Quickshell/I3

%files wayland
%{_qtdir}/qml/Quickshell/Wayland

%files x11
%{_qtdir}/qml/Quickshell/X11

%files greetd
%{_qtdir}/qml/Quickshell/Services/Greetd
