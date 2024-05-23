from kivymd.app import MDApp
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder
from kivy.core.window import Window 

Window.size = (350, 600)

kv = '''
MDFloatLayout:
    Card:
        md_bg_color: 1, 1, 1, 1
        elevation: 5
        size_hint:.85,.9
        pos_hint: {"center_x":.5, "center_y":.5}
        radius: [10]

    Image: 
        source: "logoimcverde.png"
        size_hint: .8, .8
        pos_hint: {"center_x":.5, "center_y":.78}

    MDLabel:
        text: "Login"
        pos_hint: {"center_x": .5, "center_y": .6}
        halign: "center"
        font_name: "Poppins-SemiBold.ttf"
        font_size: "40sp"
        theme_text_color: "Custom"
        text_color: 162/255, 201/255, 86/255, 1

    MDFloatLayout:
        size_hint: .75, .08
        pos_hint: {"center_x": .5, "center_y": .48}
        canvas:
            Color:
                rgb: (238/255, 238/255, 238/255, 1)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [25]
        TextInput:
            hint_text: "Email"
            size_hint: 1, None
            pos_hint: {"center_x": .5, "center_y": .5}
            height: self.minimum_height
            multiline: False
            cursor_color: 96/255, 74/255, 215/255, 1
            cursor_width: "2sp"
            foreground_color: 96/255, 74/255, 215/255, 1
            background_color: 0, 0 , 0, 0
            padding: 15
            font_name: "Poppins-Regular.ttf"
            font_size: "18sp"

    MDFloatLayout:
        size_hint: .75, .08
        pos_hint: {"center_x": .5, "center_y": .38}
        canvas:
            Color:
                rgb: (238/255, 238/255, 238/255, 1)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [25]
        TextInput:
            hint_text: "Senha"
            password: True
            size_hint: 1, None
            pos_hint: {"center_x": .5, "center_y": .5}
            height: self.minimum_height
            multiline: False
            cursor_color: 96/255, 74/255, 215/255, 1
            cursor_width: "2sp"
            foreground_color: 96/255, 74/255, 215/255, 1
            background_color: 0, 0 , 0, 0
            padding: 15
            font_name: "Poppins-Regular.ttf"
            font_size: "18sp"

    MDTextButton:
        text: "Esqueci minha senha"
        font_name: "Poppins-Regular.ttf"
        theme_text_color: "Custom"
        text_color: 162/255, 201/255, 86/255, 1
        pos_hint: {"center_x": .5, "center_y": .31}

    Button:
        text: "ENTRAR"
        font_name: "Poppins-Regular.ttf"
        font_size: "20sp"
        size_hint: .5, .08
        pos_hint: {"center_x": .5, "center_y": .22}
        background_color: 0, 0, 0, 0
        canvas.before:
            Color:
                rgb: 162/255, 201/255, 86/255, 1
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [23]
         
'''

class Card(FakeRectangularElevationBehavior, MDFloatLayout):
    pass

class Login(MDApp):
    def build(self):
        return Builder.load_string(kv)
    
if __name__ == "__main__":
    Login().run()
