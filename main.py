from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.OpenAction import OpenAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
import os

class Ext_zh0per(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordListener())
        self.subscribe(ItemEnterEvent, ItemEnterListener())

class KeywordListener(EventListener):

    def on_event(self, event, extension):
        items = []
        data = {'command': event.get_argument()}
        items.append(ExtensionResultItem(
            icon='images/run.png',
            name='Execute',
            description=data['command'],
            on_enter=ExtensionCustomAction(data) ))

        return RenderResultListAction(items)

class ItemEnterListener(EventListener):

    def on_event(self, event, extension):

        data = event.get_data()
        
        command = data['command']
        terminal = extension.preferences['terminal']
        try:
            os.system(teminal.format(command=command))
        except Exception as e:
            with open('/home/zh0per/Desktop/out.txt', 'w') as f:
                f.write(e)
        return HideWindowAction()


if __name__ == '__main__':
    Ext_zh0per().run()

