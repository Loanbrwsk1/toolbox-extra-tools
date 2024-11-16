# toolbox-icon

Useful program to make some things on toolboxes.

## Usage

tet-create : tool to create toolbox for unsupported OS in toolbox project
```
Usage: tet-create [-d] [-r] [-l] [-h] toolbox-name
Options :
  -d		Distro
  -r		Release
  -l		List distros available
  -h		Help
  toolbox-name	Name of your toolbox (instead of distro-toolbox-release)
```

tet-icon : tool to generate icons for programmes installed in toolbox.
```
Usage: tet-icon [-c|-d] -t toolbox -p program
Options :
  -c		create .desktop file for the toolbox program
  -d		delete .desktop file for the toolbox program
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

Fedora : 
```
dnf copr enable adriend/fedora-apps
```
```
dnf install toolbox-extra-tools
```

RHEL :
```
dnf copr enable adriend/el-apps
```
```
dnf install toolbox-extra-tools
```


## Uninstall 

```
make uninstall
```
