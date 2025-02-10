install:
	install -m 755 bin/tet-create /usr/bin
	install -m 755 bin/tet-icon /usr/bin
	install -m 755 bin/tet-launcher /usr/bin
	install -m 755 bin/tet-vm /usr/bin
	mkdir -p /usr/share/toolbox-extra-tools
	install -m 644 share/toolbox-extra-tools/toolbox.svg /usr/share/toolbox-extra-tools/toolbox.svg
	install -m 644 profile.d/toolbox-extra-tools.sh /etc/profile.d/toolbox-extra-tools.sh

uninstall:
	rm -f /usr/bin/tet-create
	rm -f /usr/bin/tet-icon
	rm -f /usr/bin/tet-launcher
	rm -f /usr/bin/tet-vm
	rm -f /usr/share/toolbox-extra-tools/toolbox.svg
	rm -r /usr/share/toolbox-extra-tools
	rm -f /etc/profile.d/toolbox-extra-tools.sh

.PHONY:install uninstall
