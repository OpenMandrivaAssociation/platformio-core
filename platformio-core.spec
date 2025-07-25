%global debug_package %{nil}
%define bname platformio

Name:       platformio-core
Version:    6.1.18
Release:    1
URL:        https://github.com/platformio/platformio-core
Source0:    https://github.com/platformio/platformio-core/archive/refs/tags/v%version.tar.gz#/%name-%version.tar.gz
Summary:   Professional tool for embedded systems engineers and for software developers who write applications for embedded products.
License:    Apache-2.0
Group:      Development

BuildSystem: python

%description
PlatformIO is a cross-platform, cross-architecture, multiple framework, professional tool for embedded systems engineers and for software developers who write applications for embedded products.

%files
%{py_sitedir}/%{bname}/*
%{py_sitedir}/%{bname}-%{version}-*.egg-info*
%{_bindir}/pio
%{_bindir}/piodebuggdb
%{_bindir}/platformio
