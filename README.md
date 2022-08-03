# MiniOS
A fully self-contained graphical desktop environment written in Python 3 with the PyQt library, based on the Qt framework.

Built for high efficiency systems with minimal desktop needs such as embedded systems and servers, running on top of EGLFS to remove dependencies on traditional windowing systems (e.g. X11 and Wayland).

## Dependencies
- [_PyQt6_](https://pypi.org/project/PyQt6/) for core graphics
- Optional [_PyQt6-WebEngine_](https://pypi.org/project/PyQt6-WebEngine/) to render websites

## Run
Run `System/main.py` with Python 3.7 or higher and a display connected and configured through xrandr or a similar utility.

