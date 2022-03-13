# Author : misbahfhm
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from PIL import Image
from kivy.utils import platform
from android.permissions import request_permissions, Permission

class convert(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._request_android_permissions()

    @staticmethod
    def is_android():
        return platform == 'android'

    def _request_android_permissions(self):
        if not self.is_android():
            return True
        return request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])

    def build(self):
        return MyWidget()

    def img_to_jpg(self,file):
        if file[-4:] == '.png':
            print(file)
            img = Image.open(file).convert('RGB')
            img_conv = file.replace(file[-4:], '_converted.jpg')
            img.save(img_conv)
            return self.show_dialog()
        elif file[-5:] == '.jpeg':
            img = Image.open(file[0]).convert('RGB')
            img_conv = file.replace(file[-5:], '_converted.jpg')
            img.save(img_conv)
            return self.show_dialog()
        elif file[-5:] == '.webp':
            img = Image.open(file[0]).convert('RGB')
            img_conv = file.replace(file[-5:], '_converted.jpg')
            img.save(img_conv)
            return self.show_dialog()

    def show_dialog(self):
        content = Button(text='Close me!',size_hint_y=.5)
        popup = Popup(content=content,title='Success! \nFile telah diconvert ke .jpg. Silahkan cek nama file dengan akhiran converted',size_hint=(None, None), size=(600, 400),title_size=46,title_align='center',auto_dismiss=False)
        content.bind(on_press=popup.dismiss)
        popup.open()

class MyWidget(GridLayout):
    def selected(self,filename):
        try:
            self.ids.my_image.source = filename[0]
            print(filename[0],type(filename[0]))
        except:
            pass

if __name__ == "__main__":
    window = convert()
    window.run()