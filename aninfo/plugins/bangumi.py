from typing import Optional
import json

from . import BasePlugin
from ..Anime import Anime
from .. import log
from ._webpost import post_data

URL = "https://api.bgm.tv/v0/search/subjects"


class Bangumi(BasePlugin):
    abstract = False

    def __init__(self, verify: bool = False):
        super().__init__()

        self.verify = verify

    def search(self, keyword: str, tags: Optional[list[str]]=None, date_range: Optional[tuple[str, str]]=None,
               proxies: Optional[dict]=None, system_proxy: Optional[bool]=False, **extra_options) -> list[Anime]:
        if keyword is None:
            raise ValueError("Keyword cannot be None.")

        data = {
            "keyword": keyword,
            "filter": {
                "type": [2,],
            }
        }

        if tags is not None:
            data['filter']['tag'] = tags
        if date_range is not None and len(date_range) == 2:
            data['filter']['air_date'] = [f">={date_range[0]}", f"<={date_range[1]}"]

        data['filter'].update(extra_options)

        request = json.dumps(data, ensure_ascii=False)
        response = post_data(URL, data=request, proxies=proxies, system_proxy=system_proxy, verify=self.verify)

        if response.status_code == 200 and response.headers['Content-Type'] == 'application/json':
            result = response.json()
            animes = []

            for item in result['data']:
                name = item['name']
                name_cn = item['name_cn']
                date = item.get('date', None)
                image = item['image']
                summary = item['summary']
                tags = [tag['name'] for tag in item['tags']]
                info = {info_item['key']: info_item['value'] for info_item in item['infobox']}
                eps = item['eps']
                id = item['id']

                anime = Anime(name, name_cn, image, date, summary, tags, info, eps, id)
                animes.append(anime)

        else:
            log.error(f"Unexpected response when searching by {keyword}.")
            raise Exception(f"Unexpected response when searching by {keyword}.")

        return animes
