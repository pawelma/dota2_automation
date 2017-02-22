#!/usr/bin/env python

import dbus
from dbus.mainloop.glib import DBusGMainLoop
from subprocess import check_output, call
import time
import sys
import os

try:
	import glib
except ImportError:
	from gi.repository import GLib as glib

AUTO_ACCEPT=True
ACCEPT_DELAY=1

def accept():
	if AUTO_ACCEPT == False:
		return
	
	time.sleep(ACCEPT_DELAY)
	call(["wmctrl", "-a", "Dota 2"])
	call(["xdotool", "key", "Return"])

def filter_cb(bus, message):
	if message.get_member() != "Notify":
		return
	args = message.get_args_list()
	summary=args[3]
	body=args[4]
	if 'Your game is ready' in body and 'Matchmaking Status' in summary:
		active_window=check_output(['xdotool', 'getwindowfocus', 'getwindowname']).decode('UTF-8').strip()
		if 'Dota' not in active_window:
			print('abc')
			dirname, _ = os.path.split(os.path.abspath(__file__))
			call(["aplay", os.path.join(dirname, "dota_matchmaking_ready.wav")])
		accept()

def main():
	DBusGMainLoop(set_as_default=True)
	bus = dbus.SessionBus()
	bus.add_match_string_non_blocking("eavesdrop=true, interface='org.freedesktop.Notifications'")
	bus.add_message_filter(filter_cb)
	
	mainloop = glib.MainLoop()
	try:
		mainloop.run()
	except:
		print("Exiting")
		sys.exit(0)

main()
