Name:		toolbox-extra-tools
Version:	1.2.0
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
install -p -D -m 755 bin/tet-launcher %{buildroot}/%{_bindir}/tet-launcher
install -p -D -m 644 share/toolbox-extra-tools/toolbox.svg %{buildroot}/%{_datadir}/%{name}/toolbox.svg

%files
%{_bindir}/tet-create
%{_bindir}/tet-icon
%{_bindir}/tet-launcher
%{_datadir}/%{name}/toolbox.svg

%changelog
* Mon Jan 13 2025 Adrien.D <adriend@linuxtricks.lan> - 1.2.0-1.fc41
- Update to 1.2.0 version
* Sat Nov 23 2024 Adrien.D <adriend@linuxtricks.lan> - 1.1.0-1.fc41
- Update to 1.1.0 version
* Sun Nov 17 2024 Adrien.D <adriend@linuxtricks.lan> - 1.0.1-1.fc41
- Update to 1.0.1 version
* Sat Nov 16 2024 Adrien.D <adriend@linuxtricks.lan> - 1.0.0-1.fc41
- First Release
