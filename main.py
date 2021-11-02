from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.OpenAction import OpenAction


class Ext_zh0per(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordListener())
        # self.subscribe(ItemEnterEvent, ItemEnterEvent(data))

class KeywordListener(EventListener):

    def on_event(self, event, extension):

        items = list(ExtensionResultItem(
            icon='images/icon.png',
            name='Execute',
            description=event.get_argument(),
            on_enter=OpenAction('gnome-terminal -e "bash"') ))

        return RenderResultListAction(items)

# class ItemEnterListener(EventListener):

#     def on_event(self, event, extension):

#         data = event.get_data()
       
#         return RenderResultListAction([ ExtensionResultItem(icon='images/icon.png',
#                                                                                                             name=data['new_name'],
#                                                                                                             on_enter=HideWindowAction()) ])


if __name__ == '__main__':
    Ext_zh0per().run()

