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

Supported distros :
```
+--------------+------------------------------------------------+---------------------------------+
+    distro    +                 release version                +              infos              +
+--------------+------------------------------------------------+---------------------------------+
| alma         | 8 9 or latest                                  | official toolbox                |
+--------------+------------------------------------------------+---------------------------------+
| alpine       | 3.19 3.20 edge or latest                       | official toolbox                |
+--------------+------------------------------------------------+---------------------------------+
| amazon       | 2 2023 or latest                               | official toolbox                |
+--------------+------------------------------------------------+---------------------------------+
| arch         | latest                                         | official toolbox                |
+--------------+------------------------------------------------+---------------------------------+
| blackarch    | latest                                         | via docker container            |
+--------------+------------------------------------------------+---------------------------------+
| centos       | stream8 stream9 or latest                      | official toolbox                |
+--------------+------------------------------------------------+---------------------------------+
| debian       | 10 11 12 testing unstable or latest            | official toolbox                |
+--------------+------------------------------------------------+---------------------------------+
| fedora       | 39 40 41 rawhide or latest                     | official toolbox                |
+--------------+------------------------------------------------+---------------------------------+
| gentoo       | latest systemd                                 | via docker container            |
+--------------+------------------------------------------------+---------------------------------+
| mint         | 21.1                                           | distrobox                       |
+--------------+------------------------------------------------+---------------------------------+
| opensuse     | tumbleweed                                     | official toolbox                |
+--------------+------------------------------------------------+---------------------------------+
| rhel         | 8.10 9.3 9.4 ... (<major>.<minor>' format)     | official toolbox                |
+--------------+------------------------------------------------+---------------------------------+
| rocky        | 8 9 or latest                                  | official toolbox                |
+--------------+------------------------------------------------+---------------------------------+
| ubuntu       | 22.04 24.04 ... (YY.MM format)                 | official toolbox                |
+--------------+------------------------------------------------+---------------------------------+
| wolfi        | latest                                         | official toolbox                |
+--------------+------------------------------------------------+---------------------------------+
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

### tet-launcher
```
Usage:
 tet-launcher [-c|-d] -t toolbox

Tool to generate launcher for toolbox.

Options :
  -c            create .desktop file for the toolbox
  -d            delete .desktop file for the toolbox
  -l            list installed icons
  -t toolbox    toolbox name
```

## Installation

### From the sources

Download the sources, extract them and :
```
make install
```

## Uninstall

```
make uninstall
```
