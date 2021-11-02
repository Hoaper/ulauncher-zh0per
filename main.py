from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction


class Ext_zh0per(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordListener()())
        # self.subscribe(ItemEnterEvent, ItemEnterEvent(data))

class KeywordListener(EventListener):

    def on_event(self, event, extension):
        items = []
        for i in range(5):
            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name='Item %s' % i,
                                             description=event.get_argument(),
                                             on_enter=HideWindowAction()))

        return RenderResultListAction(items)

# class ItemEnterListener(EventListener):

#     def on_event(self, event, extension):

#         data = event.get_data()
       
#         return RenderResultListAction([ ExtensionResultItem(icon='images/icon.png',
#                                                                                                             name=data['new_name'],
#                                                                                                             on_enter=HideWindowAction()) ])


if __name__ == '__main__':
    Ext_zh0per().run()

