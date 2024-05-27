from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (350, 600)

kv = '''
<CalculadoraScreen>:
MDFloatLayout:
    md_bg_color: 1, 1, 1, 1
    Image:
        source: "images/logoimcverde.png"
        size_hint:.18,.18
        pos_hint: {"center_x":.5, "center_y":.92}
    MDLabel:
        text: "Insira seus dados"
        pos_hint: {"center_x":.5, "center_y":.82}
        font_name: "Poppins-SemiBold.ttf"
        font_size: "28sp"
        halign: "center"
    MDFloatLayout:
        size_hint:.9,.1
        pos_hint: {"center_x":.5, "center_y":.7}
        canvas:
            Color:
                rgb: (238/255, 238/255, 238/255, 1)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [6]
    MDLabel:
        id: peso_kg_label
        text: "Kg"
        pos_hint: {"center_x":.55, "center_y":.7}
        font_name: "Poppins-SemiBoldItalic.ttf"
        font_size: "22sp"
        padding_x: "12sp"
    TextInput:
        id: peso_kg
        hint_text: "Insira seu peso em Kg"
        size_hint:.9, None
        pos_hint: {"center_x":.65, "center_y":.7}
        font_name: "Poppins-Regular.ttf"
        height: self.minimum_height
        font_size: "20sp"
        hint_text_color: (170/255, 170/255, 170/255, 1)
        background_color: 1, 1, 1, 0
        padding: 18
        cursor_color: 0, 0, 0, 1
        multiline: False

    MDFloatLayout:
        size_hint:.9,.1
        pos_hint: {"center_x":.5, "center_y":.55}
        canvas:
            Color:
                rgb: (238/255, 238/255, 238/255, 1)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [6]
    MDLabel:
        id: altura_m_label
        text: "m"
        pos_hint: {"center_x":.55, "center_y":.55}
        font_name: "Poppins-SemiBoldItalic.ttf"
        font_size: "22sp"
        padding_x: "12sp"
    TextInput:
        id: altura_m
        hint_text: "Insira sua altura em metros(ex.:1.80)"
        size_hint:.9, None
        pos_hint: {"center_x":.58, "center_y":.55}
        font_name: "Poppins-Regular.ttf"
        height: self.minimum_height
        font_size: "15sp"
        hint_text_color: (170/255, 170/255, 170/255, 1)
        background_color: 1, 1, 1, 0
        padding: 18
        cursor_color: 0, 0, 0, 1
        multiline: False  

    MDLabel:
        id: resultado_label
        text: "Resultado"
        pos_hint: {"center_x":.5, "center_y":.45}
        font_name: "Poppins-Regular.ttf"
        font_size: "22sp"
        halign: "center"

    MDLabel:
        id: imc_condition
        text: ""
        pos_hint: {"center_x": .5, "center_y": .2}
        font_name: "Poppins-Regular.ttf"
        font_size: "20sp"
        halign: "center"

    Button:
        text: "Calcular"
        size_hint:.9,.1
        pos_hint: {"center_x":.5, "center_y":.30}
        font_name: "Poppins-Regular.ttf"
        font_size: "22sp"
        halign: "center"
        background_color: 1, 1, 1, 0
        on_release: app.calculate(altura_m, peso_kg)
        canvas.before:
            Color:
                rgb: (162/255, 201/255, 86/255, 1)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [6]
    MDLabel:
        id: resultado
        text: ""
        pos_hint: {"center_x":.5, "center_y":.4}
        font_name: "Poppins-Regular.ttf"
        font_size: "22sp"
        halign: "center"
'''

class CalculadoraIMC(MDApp):
    def build(self):
        return Builder.load_string(kv)

    def calculate(self, altura_m, peso_kg):
        if altura_m.text != "" and peso_kg.text != "":
            try:
                p = float(altura_m.text)
                r = float(peso_kg.text)
                imc = round(r / (p ** 2), 2)
                categoria = self.get_imc_category(imc)
                self.root.ids.resultado.text = f'Seu IMC é de: {imc}'
                self.root.ids.imc_condition.text = f'Condição: {categoria}'
            except ValueError:
                self.root.ids.resultado.text = "Insira valores numéricos válidos."
                self.root.ids.imc_condition.text = ""

    def get_imc_category(self, imc):
        # Adicione aqui a lógica para retornar a categoria do IMC com base no valor do IMC.
        # Por exemplo:
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Peso normal "
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        elif 30 <= imc < 34.9:
            return "Obesidade grau I"
        elif 35 <= imc < 39.9:
            return "Obesidade grau II"
        else:
            return "Obesidade grau III"

if __name__ == "__main__":
    CalculadoraIMC().run()