from kivy.core.text import LabelBase
from kivymd.app import MDApp 
from kivy.lang import Builder 
from kivy.core.window import Window

Window.size = (350, 600)

kv = '''
MDFloatLayout:
    md_bg_color: 1, 1, 1, 1
    Image:
        source: "logoimcverde.png"
        size_hint: .18, .18
        pos_hint: {"center_x": .5, "center_y": .92}
    MDLabel:
        text: "Insira seus dados"
        pos_hint: {"center_x": .5, "center_y": .82}
        font_name: "Poppins-SemiBold.ttf"
        font_size: "28sp"
        halign: "center"
    MDFloatLayout:
        size_hint: .9, .1
        pos_hint: {"center_x": .5, "center_y": .7}
        canvas:
            Color:
                rgb: (238/255, 238/255, 238/255, 1)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [6]
    MDLabel:
        text: "Kg"
        pos_hint: {"center_x": .55, "center_y": .7}
        font_name: "Poppins-SemiBoldItalic.ttf"
        font_size: "22sp"
        padding_x: "12sp"
    TextInput:
        id: peso_kg
        hint_text: "Insira seu peso em Kg"
        size_hint: .9, None
        pos_hint: {"center_x": .65, "center_y": .7}
        font_name: "Poppins-Regular.ttf"
        height: self.minimum_height
        font_size: "20sp"
        hint_text_color: (170/255, 170/255, 170/255, 1)
        background_color: 1, 1, 1, 0
        padding: 18
        cursor_color: 0, 0, 0, 1
        multiline: False

    MDFloatLayout:
        size_hint: .9, .1
        pos_hint: {"center_x": .5, "center_y": .55}
        canvas:
            Color:
                rgb: (238/255, 238/255, 238/255, 1)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [6]
    MDLabel:
        text: "m"
        pos_hint: {"center_x": .55, "center_y": .55}
        font_name: "Poppins-SemiBoldItalic.ttf"
        font_size: "22sp"
        padding_x: "12sp"
    TextInput:
        id: altura_m
        hint_text: "Insira sua altura em metros"
        size_hint: .9, None
        pos_hint: {"center_x": .58, "center_y": .55}
        font_name: "Poppins-Regular.ttf"
        height: self.minimum_height
        font_size: "19sp"
        hint_text_color: (170/255, 170/255, 170/255, 1)
        background_color: 1, 1, 1, 0
        padding: 18
        cursor_color: 0, 0, 0, 1
        multiline: False  

    MDLabel:
        text: "Resultado"
        pos_hint: {"center_x": .5, "center_y": .45}
        font_name: "Poppins-Regular.ttf"
        font_size: "22sp"
        halign: "center"         


'''

class CalculadoraIMC(MDApp):
    def build(self):
        return Builder.load_string(kv)
    
if __name__ == "__main__":
    CalculadoraIMC().run()