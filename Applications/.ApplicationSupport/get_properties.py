# -*- coding: utf-8 -*-
"""
Applications/.ApplicationSupport/get_properties.py
returnProperties function returns dictionary with values from System/config JSON files
Based on Python 3 and PyQt for Application Support in the SimplifycOS project: https://github.com/voidedstarlight/SimplifycOS
"""

__import__("sys").path.insert(1, "System/")
import config


def returnProperties() -> dict:
	return {**config.ThemeConfig.returnConfig(), **config.FontConfig.returnConfig(), **config.WindowConfig.returnConfig()}


def returnBackgroundProperties() -> dict:
	return config.Themes.getThemes()[config.ThemeConfig.returnConfig()["theme"]]
