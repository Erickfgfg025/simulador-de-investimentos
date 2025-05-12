from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class InvestmentCalculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)

        self.add_widget(Label(text="CALCULADORA DE INVESTIMENTOS", font_size=20, color=(1, 1, 0, 1)))

        self.add_widget(Label(text="Quanto você quer investir?", color=(1, 0, 0, 1)))
        self.entrada_valor = TextInput(hint_text="Ex: 1000", multiline=False, input_filter='float')
        self.add_widget(self.entrada_valor)

        self.add_widget(Label(text="Por quantos dias deseja investir?", color=(1, 0, 0, 1)))
        self.entrada_dias = TextInput(hint_text="Ex: 180", multiline=False, input_filter='int')
        self.add_widget(self.entrada_dias)

        self.resultado_label = Label(text="", font_size=18)
        self.add_widget(self.resultado_label)

        botao = Button(text="Calcular", size_hint=(1, 0.3))
        botao.bind(on_press=self.calcular_investimento)
        self.add_widget(botao)

    def calcular_investimento(self, instance):
        try:
            valor_investido = float(self.entrada_valor.text)
            dias = int(self.entrada_dias.text)

            cdi_anual = 14.65
            percentual_cdi = 100

            cdi_diario = (1 + cdi_anual / 100) ** (1 / 252) - 1
            rentabilidade = (1 + cdi_diario) ** dias - 1
            rentabilidade_ajustada = rentabilidade * (percentual_cdi / 100)
            rendimento_bruto = valor_investido * rentabilidade_ajustada
            valor_final = valor_investido + rendimento_bruto

            self.resultado_label.text = f"Valor Final: R$ {valor_final:.2f}"
        except:
            self.resultado_label.text = "Erro nos valores. Verifique e tente novamente."


class InvestmentApp(App):
    def build(self):
        return InvestmentCalculator()


if __name__ == '__main__':
    InvestmentApp().run()