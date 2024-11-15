# toolbox-icon

Useful program to make some things on toolboxes.

Note : "Toolbox-xxxxx" commands start with an uppercase letter to avoid interfering with any official projects.

## Usage

Toolbox-creatextra : tool to create toolbox for unsupported OS in toolbox project
```
Usage: ./Toolbox-creatextra [-d] [-r] [-l] [-h] toolbox-name
Options :
  -d		Distro
  -r		Release
  -l		List distros available
  -h		Help
  toolbox-name	Name of your toolbox (instead of distro-toolbox-release)
```

Toolbox-icon : tool to generate icons for programmes installed in toolbox.
```
Usage: ./Toolbox-icon [-c|-d] -t toolbox -p program
Options :
  -c		create .desktop file for the toolbox program
  -d		delete .desktop file for the toolbox program
  -t toolbox	toolbox name
  -p program	program name
```
