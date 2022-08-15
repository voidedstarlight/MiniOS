# MiniOS
A fully self-contained graphical desktop environment written in Python 3 with the PyQt library, based on the Qt framework.

Built for high efficiency systems with minimal desktop needs such as embedded systems and servers, running on top of EGLFS to remove dependencies on traditional windowing systems (e.g. X11 and Wayland).

## Dependencies
- [_PyQt6_](https://pypi.org/project/PyQt6/) for core graphics
- Optional [_PyQt6-WebEngine_](https://pypi.org/project/PyQt6-WebEngine/) to render websites

## Usage
With a EGLFS-enabled Qt build (build with `PACKAGECONFIG` options), set a backend for EGLFS by setting the `QT_QPA_EGLFS_INTEGRATION` environment variable, generally `eglfs_kms` for most devices.

When building, check the output of the configure step to ensure that EGLFS is enabled and graphical features specific to the device are enabled. Raspberry Pis, for example, require the suboptions `OpenGL ES` and `EGLFS EGLDevice` to both be on.

Run `System/main.py` with Python 3.7 or higher and a display connected and configured through xrandr or a similar utility.

