#!/usr/bin/env python

import dbus
import time
import os
import sys
from dbus.mainloop.glib import DBusGMainLoop
from subprocess import check_output, call
try:
  import glib
except ImportError:
  from gi.repository import GLib as glib

def accept():
  if os.getenv('D2_AUTOACCEPT', '1') == '1':
    return

  time.sleep(int(os.getenv('D2_AUTOACCEPTDELAY', 1)))
  call(['wmctrl', '-a', 'Dota 2'])
  call(['xdotool', 'key', 'Return'])

def notify():
  actwindow = check_output(['xdotool', 'getwindowfocus', 'getwindowname']).decode('UTF-8').strip()
  if 'Dota' not in actwindow:
    if os.getenv('D2_NOTIFY', '1') == '1':
      dirname, _ = os.path.split(os.path.abspath(__file__))
      call(['aplay', os.path.join(dirname, 'sfx/dota_matchmaking_ready.wav')])

def message_filter(bus, message):
  if message.get_member() != 'Notify':
    return

  args = message.get_args_list()
  summary = args[3]
  body = args[4]

  if 'Your game is ready' in body and 'Matchmaking Status' in summary:
    notify()
    accept()

def main():
  DBusGMainLoop(set_as_default=True)

  bus = dbus.SessionBus()
  bus.add_match_string_non_blocking("eavesdrop=true, interface='org.freedesktop.Notifications'")
  bus.add_message_filter(message_filter)

  mainloop = glib.MainLoop()

  try:
    mainloop.run()
  except:
    sys.exit(0)

main()
