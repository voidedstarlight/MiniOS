# -*- coding: utf-8 -*-
"""
Applications/.ApplicationSupport/get_properties.py
returnProperties function returns dictionary with values from System/config JSON files
Based on Python 3 and PyQt for Application Support in the MiniOS project: https://github.com/voidedstarlight/MiniOS
"""

__import__("sys").path.insert(1, "System/")
import config


def returnProperties() -> dict:
	return {**config.ThemeConfig.returnConfig(), **config.FontConfig.returnConfig()}


def returnBackgroundProperties() -> dict:
	return config.Themes.getThemes()[config.ThemeConfig.returnConfig()["theme"]]
