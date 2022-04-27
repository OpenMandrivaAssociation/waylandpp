%define major 1
%define libname %mklibname %{name} %{major}
%define devel %mklibname %name -d

Name:           waylandpp
Version:        1.0.0
Release:        1
Summary:        Wayland C++ bindings
Group:          Development/C++
License:        BSD and MIT and GPLv3+
URL:            https://github.com/NilsBrause/waylandpp/
Source0:        https://github.com/NilsBrause/waylandpp/archive/%{version}/waylandpp-%{version}.tar.gz 

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  egl-devel
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(pugixml)

%description
Wayland is an object oriented display protocol, which features request and
events. Requests can be seen as method calls on certain objects, whereas
events can be seen as signals of an object. This makes the Wayland protocol
a perfect candidate for a C++ binding.

The goal of this library is to create such a C++ binding for Wayland using
the most modern C++ technology currently available, providing an easy to use
C++ API to Wayland.

%package -n %{libname}
Summary:        Library files for %{name}
Provides:       %{name} = %{version}-%{release}
 
%description -n %{libname}
The %{libname} package contains library files for %{name}.

%package -n %{devel}
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}-%{release}
 
%description -n %{devel}
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.
 
%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
 
%description doc
The %{name}-doc package contains development documentation for %{name}.

%prep
%autosetup

%build
%cmake -DCMAKE_INSTALL_DOCDIR=%{_defaultdocdir}/%{name}-doc/
%make_build

%install
%make_install -C build

# Drop LaTeX documentation (HTML documentation is already built)
rm -r $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-doc/latex/

%files -n %{libname}
%{_libdir}/*.so.%{major}{,.*}

%files -n %{devel}
%doc example/
%{_bindir}/wayland-scanner++
%{_libdir}/*.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_datadir}/%{name}/
%{_mandir}/man3/*.3.*

%files doc
%doc README.md
%license LICENSE
%{_defaultdocdir}/%{name}-doc/
