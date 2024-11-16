install:
	install -m 755 tet-create /usr/bin
	install -m 755 tet-icon /usr/bin

uninstall:
	rm -f /usr/bin/tet-create
	rm -f /usr/bin/tet-icon

.PHONY:install uninstall
