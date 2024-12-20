import importlib
from abc import ABCMeta, abstractmethod
from typing import Optional

from .. import log


class PluginMeta(ABCMeta):
    plugins = {}

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        if not getattr(cls, 'abstract'):
            PluginMeta.plugins[name] = cls


class BasePlugin(metaclass=PluginMeta):
    abstract = True

    @abstractmethod
    def search(self, keyword: str, tags, date_range,
               proxies, system_proxy: Optional, **extra_options):
        pass


def get_plugin(name: str):
    """
    Get a plugins by its name.

    Args:
    - name: Name of the plugins

    Returns:
    - Plugin class if found, otherwise None
    """
    try:
        importlib.import_module(f".{name}", package=__name__)
    except ImportError:
        log.info(f"The plugins {name} cannot be automatically imported, please import it manually")

    return PluginMeta.plugins.get(name.title())
