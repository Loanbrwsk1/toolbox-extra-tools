TARGET = Toolbox-icon
INSTALL_DIR = /usr/bin

install:
	install -m 755 $(TARGET) $(INSTALL_DIR)

uninstall:
	rm -f $(INSTALL_DIR)/$(TARGET)

.PHONY:install uninstall
