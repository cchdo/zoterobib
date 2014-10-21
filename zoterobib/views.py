import json

from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from pyzotero import zotero

from zoterobib.memoize import TimedMemoize


class ZoteroExhibitConvertor:

    def __init__(self, *args):
        self.zot = zotero.Zotero(*args)

    @TimedMemoize(60 * 5)
    def items(self, limit=None):
        self.zot.add_parameters(itemType="-attachment")
        return self.zot.top(limit=limit)

    def to_exhibit_json(self, limit=None):
        items = self.items(limit)
        itemlist = [self.item_to_dict(item) for item in items]

        exhibit_json = {
            "types": {
                "Document": {
                    "pluralLabel":  "Documents",
                },
            },
            "items": itemlist,
        }
        return json.dumps(exhibit_json)

    @classmethod
    def creator_to_string(cls, creator):
        return ', '.join([
            creator.get('lastName', None), creator.get('firstName', None)])

    @classmethod
    def creators_to_string(cls, creators):
        return '; '.join([cls.creator_to_string(ccc) for ccc in creators])

    @classmethod
    def item_to_dict(cls, item):
        try:
            item = item['data']
        except KeyError:
            return {}
        else:
            return {
                'label': item.get('title', ''),
                'year': item.get('date', ''),
                'authors': cls.creators_to_string(item.get('creators', [])),
                'uri': item.get('url', ''),
                'publisher': item.get('publicationTitle', ''),
            }


def index(request):
    return render(request, "bibliography/index.html")


zot = ZoteroExhibitConvertor(*settings.ZOTEROBIB_SETTINGS)


def load(request):
    json = zot.to_exhibit_json()
    return HttpResponse(json, content_type="application/json")
