install:
	install -m 755 Toolbox-creatextra /usr/bin
	install -m 755 Toolbox-icon /usr/bin

uninstall:
	rm -f /usr/bin/Toolbox-creatextra
	rm -f /usr/bin/Toolbox-icon

.PHONY:install uninstall
