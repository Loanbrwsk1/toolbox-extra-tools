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
| arch         | latest                                         | official toolbox                |
+--------------+------------------------------------------------+---------------------------------+
| centos       | stream8 stream9 or latest                      | official toolbox                |
+--------------+------------------------------------------------+---------------------------------+
| debian       | 10 11 12 testing unstable or latest            | official toolbox                |
+--------------+------------------------------------------------+---------------------------------+
| fedora       | 39 40 41 rawhide or latest                     | official toolbox                |
+--------------+------------------------------------------------+---------------------------------+
| gentoo       | latest systemd                                 | via docker container            |
+--------------+------------------------------------------------+---------------------------------+
| opensuse     | tumbleweed                                     | official toolbox                |
+--------------+------------------------------------------------+---------------------------------+
| rhel         | 8.10 9.3 9.4 ... (<major>.<minor>' format)     | official toolbox                |
+--------------+------------------------------------------------+---------------------------------+
| ubuntu       | 22.04 24.04 ... (YY.MM format)                 | official toolbox                |
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

### tet-vm (EXPERIMENTAL)
```
Usage:
 tet-vm subcommand [-d] [-r] [-l] [-h] cont-name

Tool to create a podmain container you can use as a virtual machine.

Options :
  -d		Distro
  -r		Release
  -p		Port redirection (8080:80) or multiport redirection (8080:80,8443:443)
  -l		List distros available
  -h		Help
  cont-name	Name of your container

Note:
Rootfull Mode (root) : 
	- Container is in the podman default network. (Container has podman IP address)
	- Full access to the container on all ports via container IP address from host.
Rootless Mode (user) : 
	- !! Container can't open <1024 ports !!
	- Container is in host mode. Container has same IP than host. (Container has same IP than host)
	- Container is in the podman default network if port redirection enabled. (Container has podman IP address)
```

Supported distros : 
```
+--------------+------------------------------------------------+
+    distro    +                 release version                +
+--------------+------------------------------------------------+
| alma         | 8 9 or latest                                  |
+--------------+------------------------------------------------+
| alpine       | 3.19 3.20 edge or latest                       |
+--------------+------------------------------------------------+
| arch         | latest                                         |
+--------------+------------------------------------------------+
| centos       | stream8 stream9 or latest                      |
+--------------+------------------------------------------------+
| debian       | 10 11 12 testing unstable or latest            |
+--------------+------------------------------------------------+
| fedora       | 39 40 41 rawhide or latest                     |
+--------------+------------------------------------------------+
| gentoo       | latest systemd                                 |
+--------------+------------------------------------------------+
| opensuse     | tumbleweed                                     |
+--------------+------------------------------------------------+
| rhel         | 8.10 9.3 9.4 ... (<major>.<minor>' format)     |
+--------------+------------------------------------------------+
| ubuntu       | 22.04 24.04 ... (YY.MM format)                 |
+--------------+------------------------------------------------+
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

