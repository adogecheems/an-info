from typing import List, Optional

from . import log
from .Anime import Anime
from .plugins import get_plugin


class AniInfoSearch:
    def __init__(self, plugin_name: str = 'bangumi', verify: Optional[bool] = None):
        self.reset()
        self.verify = verify

        try:
            self.plugin = get_plugin(plugin_name)(verify=verify)
            log.debug(f"Successfully loaded plugin: {plugin_name}")

        except Exception as e:
            log.error(f"Failed to load plugin {plugin_name}: {str(e)}")
            raise

    def reset(self) -> None:
        """Reset the search object."""
        self.animes: List[Anime] = []
        self.anime: Optional[Anime] = None
        self.if_selected = False

    def search(self, keyword: str, tags: Optional[list] = None, date_range: Optional[tuple] = None,
               proxies: Optional[dict] = None, system_proxy: Optional[bool] = None, **extra_options) -> bool:
        self.reset()

        kwargs = {'keyword': keyword}
        if tags:
            kwargs['tags'] = tags
        if date_range:
            kwargs['date_range'] = date_range
        if proxies:
            kwargs['proxies'] = proxies
        if system_proxy:
            kwargs['system_proxy'] = system_proxy
        kwargs.update(extra_options)

        try:
            self.animes = self.plugin.search(**kwargs)

            log.info(f"This search is complete: {keyword}")
            return True

        except Exception as e:
            log.error(f"Search failed: {str(e)}")
            return False

    def select(self, index: int) -> None:
        """
        Select an anime from the search results.

        Args:
        - index: Index of the anime in the results list
        """
        if not (0 <= index < len(self.animes)):
            raise IndexError("Invalid selection index")

        self.anime = self.animes[index]
        self.if_selected = True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
