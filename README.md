# toolbox-extra-tools

Useful program to make some things on toolboxes.

## Usage

### tet-create
```
Usage:
 tet-create [-d] [-r] [-l] [-h] toolbox-name

Tool to create toolbox for unsupported OS in toolbox project.

Options :
  -d		Distro
  -r		Release
  -l		List distros available
  -h		Help
  toolbox-name	Name of your toolbox (instead of distro-toolbox-release)
```

### tet-icon
```
Usage:
 tet-icon [-c|-d] -t toolbox -p program

Tool to generate icons for programmes installed in toolbox.

Options :
  -c		create .desktop file for the toolbox program
  -d		delete .desktop file for the toolbox program
  -l		list installed icons
  -t toolbox	toolbox name
  -p program	program name
```

## Installation

### From the sources 

Download the sources, extract them and :
```
make install
```

### From package manager

Fedora (supported versions) : 
```
dnf copr enable adriend/fedora-apps
```
```
dnf install toolbox-extra-tools
```

RHEL (8 9 10) and derivatives :
```
dnf copr enable adriend/el-apps
```
```
dnf install toolbox-extra-tools
```


## Uninstall 

If installed manually : 
```
make uninstall
```

If installed by package-manager : 
```
dnf remove toolbox-extra-tools
```

