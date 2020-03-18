#!/usr/bin/python3
# -*- coding:utf-8 -*-


import inspect
import os
import gi
from signal import signal, SIGINT, SIG_DFL
from subprocess import Popen
from sys import exit
try:
    # python 3
    from urllib.request import urlopen, pathname2url
except ImportError:
    # python 2
    from urllib import urlopen, pathname2url
from webbrowser import open_new_tab
from json import dumps as to_json
gi.require_version('WebKit2', '4.0')
from gi.repository import WebKit2, Gtk
gi.require_version:('Gtk', '3.0')
window = Gtk.Window()
webview = WebKit2.WebView()
webview.load_uri("https://s.tradingview.com/widgetembed/?frameElementId=tradingview_04652&symbol=OANDA%3ANAS100USD&interval=1&hidesidetoolbar=0&saveimage=0&toolbarbg=f1f3f6&studies=%5B%5D&hideideas=1&theme=White&style=1&timezone=Etc%2FUTC&studies_overrides=%7B%7D&overrides=%7B%7D&enabled_features=%5B%5D&disabled_features=%5B%5D&locale=en&utm_source=www.livecharts.co.uk&utm_medium=widget&utm_campaign=chart&utm_term=OANDA%3ANAS100USD")
#window.set_title("TRIANTARES 2019")
window.set_decorated(False)
window.set_default_size(800,600)
window.add(webview)
window.show_all()

window.connect("destroy",Gtk.main_quit)

Gtk.main()
