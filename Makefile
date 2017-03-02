conf:
	sed templates/d2_automation.service -e 's#:PATH:#$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))#g' -e 's/:USER:/$(USER)/g' > d2_automation.service

	@echo
	@echo COMPLETED
	@echo
	@echo run sudo make install to configure service

clean:
	rm -f /usr/local/bin/d2_automation

install:
	ln -s $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))/start_script.sh /usr/local/bin/d2_automation

systemd_install:
	systemctl link $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))/d2_automation.service
	systemctl daemon-reload
	systemctl enable d2_automation.service
	systemctl start d2_automation.service

systemd_uninstall:
	systemctl stop d2_automation.service
	systemctl disable d2_automation.service
	rm -f d2_automation.service
	systemctl daemon-reload
