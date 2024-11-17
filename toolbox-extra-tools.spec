Name:		toolbox-extra-tools
Version:	1.0.0
Release:	1%{?dist}
Summary:	Extra tools for toolbox

License:	GPLv3
URL:		https://github.com/aaaaadrien/toolbox-extra-tools
Source0:	https://github.com/aaaaadrien/toolbox-extra-tools/archive/refs/tags/v%{version}.tar.gz

BuildArch:	noarch

Requires:	toolbox

%description
Useful program to make some things on toolboxes.

%prep
%autosetup

%build
#Nothing to build

%install
install -p -D -m 755 bin/tet-create %{buildroot}/%{_bindir}/tet-create
install -p -D -m 755 bin/tet-icon %{buildroot}/%{_bindir}/tet-icon

%files
%{_bindir}/tet-create
%{_bindir}/tet-icon

%changelog
* Sat Nov 16 2024 Adrien.D <adriend@linuxtricks.lan> - 1.0.0-1.fc41
- First Release
