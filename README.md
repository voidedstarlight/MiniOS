# MiniOS
<<<<<<< HEAD
A fully self-contained graphical desktop environment written in Python 3 with the PyQt library, based on the Qt framework.

Built for high efficiency systems with minimal desktop needs such as embedded systems and servers, running on top of EGLFS to remove dependencies on traditional windowing systems (e.g. X11 and Wayland).

## Dependencies
- [_PyQt6_](https://pypi.org/project/PyQt6/) for core graphics
- Optional [_PyQt6-WebEngine_](https://pypi.org/project/PyQt6-WebEngine/) to render websites

## Run
Run `System/main.py` with Python 3.7 or higher and a display connected and configured through xrandr or a similar utility.

=======
#### A graphical OS as an application made using Python 3 and PyQt and the PyQt library.
_**This file (and project) is a work-in-progress**_
## Run
`cd` into the downloaded MiniOS-master directory, and run the main.py file using the `python3 main.py` bash command.
## Requirements
### Python 3
This program requires Python 3.5 or later to run. To download python, visit https://www.python.org/downloads/.
### Libraries
This program uses the _PyQt5_ GUI library for graphics, and uses the _PyQtWebEngine_ library to access web content. For more on these libraries, visit https://pypi.org/project/PyQtWebEngine/ and https://pypi.org/project/PyQt5/. If the PyQt5 or PyQtWebEngine library is not installed, the program will show a prompt (in `System/import_modules.py`: https://github.com/voidedstarlight/MiniOS/blob/master/System/import_modules.py#L13-L30) to install the library. To install, enter 'install'. Alternatively, manually run the `pip3 install PyQt5` (to install PyQt5) and/or the `pip3 install PyQtWebEnigne` (to install PyQt WebEngine) bash command, depending on the missing library.
## Features
### Files
_This feature is not finished_

Files within the `Home/Desktop` directory ending in an os extension (`.MiniOS`, representing a file, or `.MiniOSDIR`, representing a directory) get displayed on the desktop with an icon above it. The icon for files is:

![File icon](https://home.voidedstarlight.repl.co/host_images/document.png)

The icon for directories is:

![File icon](https://home.voidedstarlight.repl.co/host_images/directory.png)

If there is an extension before the os extension, the program attempts to find an icon associated with the extension and displays the new icon instead of the default icon.
