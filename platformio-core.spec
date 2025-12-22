%global debug_package %{nil}
%define bname platformio

Name:       platformio-core
Version:    6.1.18
Release:    3
URL:        https://github.com/platformio/platformio-core
Source0:    https://github.com/platformio/platformio-core/archive/refs/tags/v%version.tar.gz#/%name-%version.tar.gz
Summary:   Professional tool for embedded systems engineers and for software developers who write applications for embedded products.
License:    Apache-2.0
Group:      Development

Requires:   python%{pyver}dist(ajsonrpc) >= 1.2
Requires:   python%{pyver}dist(bottle) >= 0.13
Requires:   python%{pyver}dist(click) >= 8.0.4
Requires:   python%{pyver}dist(colorama)
Requires:   python%{pyver}dist(marshmallow) >= 3
Requires:   python%{pyver}dist(pyelftools) >= 0.27
Requires:   python%{pyver}dist(pyserial) >= 3.5
Requires:   python%{pyver}dist(requests) >= 2
Requires:   python%{pyver}dist(semantic-version) >= 2.10
Requires:   python%{pyver}dist(setuptools)
Requires:   python%{pyver}dist(starlette) >= 0.19
Requires:   python%{pyver}dist(tabulate) >= 0
Requires:   python%{pyver}dist(uvicorn) >= 0.16
Requires:   python%{pyver}dist(wsproto) >= 1

BuildSystem: python

%description
PlatformIO is a cross-platform, cross-architecture, multiple framework, professional tool for embedded systems engineers and for software developers who write applications for embedded products.

%files
%{py_sitedir}/%{bname}/*
%{py_sitedir}/%{bname}-%{version}-*.egg-info*
%{_bindir}/pio
%{_bindir}/piodebuggdb
%{_bindir}/platformio
