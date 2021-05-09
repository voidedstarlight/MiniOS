# -*- coding: utf-8 -*-
# Simplifyc Calculator
# Calculator made using Python 3 and PyQt, HTML, CSS, and JavaScript for the SimplifycOS project: https://github.com/voidedstarlight/SimplifycOS
# Main calculator code at calculator/index.html

# Imports
import sys
import os

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebEngine import *

application = QApplication(sys.argv) # Create new Qt application
web_view = QWebEngineView() # Create new Web Engine View
web_view.load(QUrl.fromLocalFile(os.path.abspath(os.path.join(os.path.dirname(__file__), "calculator/index.html")))) # Load HTML page at calculator/index.html
web_view.show() # Show view
application.exec_() # Execute Qt application
