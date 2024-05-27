from kivymd.app import MDApp
from kivy.core.text import LabelBase
import pyrebase
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
import webbrowser

# Configuração do Firebase
firebaseConfig = {
    'apiKey': "AIzaSyAZRpAINGFAgy8nFxW-IzBslyQN3PBIrV0",
    'authDomain': "calcimc-3ef39.firebaseapp.com",
    'databaseURL': "https://calcimc-3ef39-default-rtdb.firebaseio.com",
    'projectId': "calcimc-3ef39",
    'storageBucket': "calcimc-3ef39.appspot.com",
    'messagingSenderId': "575483745639",
    'appId': "1:575483745639:web:a9874d0b33024b02bacbc2",
    'measurementId': "G-TPR11T134F"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

Window.size = (350, 600)

screen_helper = '''
ScreenManager:
    LoginScreen:
    CadastroScreen:  
    CalculadoraScreen: 

<LoginScreen>:
    name: "login"
    id: login
    MDFloatLayout:
        Card:
            md_bg_color: 1, 1, 1, 1
            elevation: 2
            size_hint:.85,.9
            pos_hint: {"center_x":.5, "center_y":.5}
            radius: [4]

        Image:
            source: "images/logoimcverde.png"
            size_hint: .8, .8
            pos_hint: {"center_x":.5, "center_y":.78}

        MDLabel:
            id: login_message
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
                id: email_login
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
                id: senha_login
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
            text: "Não tem conta? Cadastre-se já!"
            font_name: "Poppins-Regular.ttf"
            theme_text_color: "Custom"
            font_size: "15sp"
            text_color: 162/255, 201/255, 86/255, 1
            pos_hint: {"center_x": .5, "center_y": .31}
            on_release:
                root.manager.transition.direction = "left"
                root.manager.current = "cadastro"

        Button:
            text: "ENTRAR"
            font_name: "Poppins-Regular.ttf"
            font_size: "20sp"
            size_hint: .5, .08
            pos_hint: {"center_x": .5, "center_y": .22}
            background_color: 0, 0, 0, 0
            canvas.before:
                Color:
                    rgb: (162/255, 201/255, 86/255, 1)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [23]
            on_release:
                print("Login realizado", email_login.text, senha_login.text)
                app.my_firebaselogin.Login(email_login.text, senha_login.text)
                root.manager.transition.direction = "right"
                root.manager.current = "calculadora"

<CadastroScreen>:
    name: "cadastro"
    id: cadastro
    MDFloatLayout:
        Card:
            md_bg_color: 1, 1, 1, 1
            elevation: 2
            size_hint:.85,.9
            pos_hint: {"center_x":.5, "center_y":.5}
            radius: [4]

        Image:
            source: "images/logoimcverde.png"
            size_hint: .8, .8
            pos_hint: {"center_x":.5, "center_y":.78}

        MDLabel:
            id: signup_message
            text: "Criar uma nova conta"
            pos_hint: {"center_x": .5, "center_y": .6}
            halign: "center"
            font_name: "Poppins-SemiBold.ttf"
            font_size: "20sp"
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
                id: email_signup
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
                id: username_signup
                hint_text: "Nome de usuário"
                size_hint: 1, None
                pos_hint: {"center_x": .5, "center_y": .5}
                height: self.minimum_height
                multiline: False
                cursor_color: 96/255, 74/255, 215/255, 1
                cursor_width: "2sp"
                foreground_color: 96/255, 74/255, 215/255, 1
                background_color: 0, 0, 0, 0
                padding: 15
                font_name: "Poppins-Regular.ttf"
                font_size: "18sp"

        MDFloatLayout:
            size_hint: .75, .08
            pos_hint: {"center_x": .5, "center_y": .28}
            canvas:
                Color:
                    rgb: (238/255, 238/255, 238/255, 1)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [25]
            TextInput:
                id: password_signup
                hint_text: "Senha(mín. 6 caracterés)"
                password: True
                size_hint: 1, None
                pos_hint: {"center_x": .5, "center_y": .5}
                height: self.minimum_height
                multiline: False
                cursor_color: 96/255, 74/255, 215/255, 1
                cursor_width: "2sp"
                foreground_color: 96/255, 74/255, 215/255, 1
                background_color: 0, 0, 0, 0
                padding: 15
                font_name: "Poppins-Regular.ttf"
                font_size: "18sp"

        MDTextButton:
            text: "Já tem conta? Faça login!"
            font_name: "Poppins-Regular.ttf"
            theme_text_color: "Custom"
            font_size: "15sp"
            text_color: 162/255, 201/255, 86/255, 1
            pos_hint: {"center_x": .5, "center_y": .21}
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "login"

        Button:
            text: "CADASTRAR"
            font_name: "Poppins-Regular.ttf"
            font_size: "20sp"
            size_hint: .5, .08
            pos_hint: {"center_x": .5, "center_y": .12}
            background_color: 0, 0, 0, 0
            canvas.before:
                Color:
                    rgb: (162/255, 201/255, 86/255, 1)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [23]
            on_release:
                print("Cadastro realizado", email_signup.text, password_signup.text)
                app.my_firebaselogin.sign_up(email_signup.text, username_signup.text, password_signup.text)
                root.manager.transition.direction = "right"
                root.manager.current = "login"

<Card@MDCard+FakeRectangularElevationBehavior>:
    size_hint: None, None
    size: "280dp", "180dp"
    pos_hint: {"center_x": .5, "center_y": .5}
    elevation: 5
    orientation: "vertical"

<CalculadoraScreen>:
    name: "calculadora"
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        Image:
            source: "images/logoimcverde.png"
            size_hint:.25,.25
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
            on_release: root.calculate(altura_m, peso_kg)
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

        MDLabel: 
            id: dicas
            text: ""
            pos_hint: {"center_x":.5, "center_y":.13}
            font_name: "Poppins-Regular.ttf"
            font_size: "12sp"
            halign: "center"       

        MDTextButton: 
            id: noticia
            text: "[u]Saiba mais[/u]"
            pos_hint: {"center_x":.5, "center_y":.05}
            font_name: "Poppins-Regular.ttf"
            theme_text_color: "Custom"
            text_color: (0, 0, 1, 1)
            font_size: "12sp"
            markup: True
            halign: "right"  
            on_release: root.on_saiba_mais_press()    

'''

class LoginScreen(Screen):
    pass

class CadastroScreen(Screen):
    pass


class CalculadoraScreen(Screen):

    def on_pre_enter(self, *args):
        if not auth.current_user:
            self.manager.current = "login"
            
    def calculate(self, altura_m, peso_kg):
        altura_text = altura_m.text.strip()
        peso_text = peso_kg.text.strip()

        if not altura_text or not peso_text:
            self.ids.resultado.text = "Insira valores válidos para altura e peso."
            self.ids.imc_condition.text = ""
        else:
            try:
                altura = float(altura_text)
                peso = float(peso_text)
                if altura == 0 or peso == 0:
                    self.ids.resultado.text = "Insira números válidos."
                    self.ids.imc_condition.text = ""
                else:
                    imc = round(peso / (altura ** 2), 2)
                    categoria = self.get_imc_category(imc)
                    self.ids.resultado.text = f'Seu IMC é de: {imc}'
                    self.ids.imc_condition.text = f'Condição: {categoria}'
                    dicas = self.get_imc_dicas(imc)
                    self.ids.dicas.text = f'Dicas:\n{dicas}'

            except ValueError:
                self.ids.resultado.text = "Insira valores numéricos válidos para altura e peso."
                self.ids.imc_condition.text = ""

    def on_saiba_mais_press(self):
        categoria = self.ids.imc_condition.text.split(":")[1].strip()  # Obtém a categoria do IMC
        link = self.get_saiba_mais_link(categoria)  # Obtém o link com base na categoria
        if link:
            webbrowser.open(link) 
            
    def get_saiba_mais_link(self, categoria):
        if categoria == "Abaixo do peso":
            return "https://www.uol.com.br/vivabem/noticias/redacao/2019/11/28/dificuldade-em-engordar-8-dicas-para-ganhar-peso-sem-comprometer-a-saude.htm"
        elif categoria == "Peso normal":
            return "https://sallet.com.br/saiba-como-manter-o-peso-ideal/"
        elif categoria == "Sobrepeso":
            return "https://ge.globo.com/eu-atleta/nutricao/noticia/nutricionista-destaca-10-habitos-que-ajudam-na-luta-contra-o-sobrepeso.ghtml"
        elif categoria == "Obesidade grau I":
            return "https://blog.winsocial.com.br/obesidade/"
        elif categoria == "Obesidade grau II":
            return "https://blog.winsocial.com.br/obesidade/"
        elif categoria == "Obesidade grau III":
            return "https://blog.winsocial.com.br/obesidade/"


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

    def get_imc_dicas(self,imc):
        if imc < 18.5:
            return "Consulte um médico para avaliar sua saúde geral.\nConsidere aumentar a ingestão de calorias com alimentos nutritivos."
        elif 18.5 <= imc < 24.9:
            return "Parabéns! Você está com um peso saudável.\nMantenha uma dieta equilibrada e pratique exercícios físicos"
        elif 25 <= imc < 29.9:
            return "Faça ajustes na dieta, como reduzir o consumo de alimentos processados e açucarados."
        elif 30 <= imc < 34.9:
            return "Estabeleça metas realistas de perda de peso e trabalhe para alcançá-las de forma sustentável."
        elif 35 <= imc < 39.9:
            return "Procure ajuda médica imediatamente para criar um plano de perda de peso seguro e eficaz."
        else:
            return "Procure ajuda médica imediatamente para criar um plano de perda de peso seguro e eficaz."
sm = ScreenManager()
sm.add_widget(LoginScreen(name="login"))
sm.add_widget(CadastroScreen(name="cadastro"))
sm.add_widget(CalculadoraScreen(name="calculadora"))

class TesteApp(MDApp):
    def build(self):
        self.my_firebaselogin = MyFirebaseLogin()
        return Builder.load_string(screen_helper)

    def on_start(self):
        self.title = "Calculadora IMC"
        self.icon = "images/logoimcverde.png"
        self.root.current = "login"

class MyFirebaseLogin:
    def Login(self, email, password):
        try:
            auth.sign_in_with_email_and_password(email, password)
            print("Login bem-sucedido")
        except:
            print("Login falhou")

    def sign_up(self, email, username, password):
        try:
            auth.create_user_with_email_and_password(email, password)
            print("Cadastro bem-sucedido")
        except:
            print("Cadastro falhou")




if __name__ == '__main__':
    TesteApp().run()
