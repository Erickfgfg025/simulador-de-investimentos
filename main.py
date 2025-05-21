import customtkinter as ctk

# Configurações iniciais
ctk.set_appearance_mode("dark")  # ou "light"
ctk.set_default_color_theme("blue")  # temas: blue, green, dark-blue

class InvestmentApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Investimentos")
        self.geometry("400x400")
        self.resizable(False, False)

        # Título
        self.label_titulo = ctk.CTkLabel(self, text="CALCULADORA DE INVESTIMENTOS", font=ctk.CTkFont(size=18, weight="bold"))
        self.label_titulo.pack(pady=(20, 10))

        # Valor investido
        self.label_valor = ctk.CTkLabel(self, text="Quanto você quer investir?")
        self.label_valor.pack()
        self.entrada_valor = ctk.CTkEntry(self, placeholder_text="Ex: 1000")
        self.entrada_valor.pack(pady=(0, 10))

        # Dias investidos
        self.label_dias = ctk.CTkLabel(self, text="Por quantos dias deseja investir?")
        self.label_dias.pack()
        self.entrada_dias = ctk.CTkEntry(self, placeholder_text="Ex: 180")
        self.entrada_dias.pack(pady=(0, 20))

        # Botão de calcular
        self.botao_calcular = ctk.CTkButton(self, text="Calcular", command=self.calcular_investimento)
        self.botao_calcular.pack(pady=10)

        # Resultado
        self.resultado_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=14))
        self.resultado_label.pack(pady=10)

    def calcular_investimento(self):
        try:
            valor_investido = float(self.entrada_valor.get())
            dias = int(self.entrada_dias.get())

            cdi_anual = 14.65
            percentual_cdi = 100

            cdi_diario = (1 + cdi_anual / 100) ** (1 / 252) - 1
            rentabilidade = (1 + cdi_diario) ** dias - 1
            rentabilidade_ajustada = rentabilidade * (percentual_cdi / 100)
            rendimento_bruto = valor_investido * rentabilidade_ajustada
            valor_final = valor_investido + rendimento_bruto

            self.resultado_label.configure(
                text=f"Valor Final: R$ {valor_final:.2f}\n"
                     f"Rendimento: R$ {rendimento_bruto:.2f}\n"
                     f"Rentabilidade: {rentabilidade_ajustada * 100:.2f}%"
            )
        except ValueError:
            self.resultado_label.configure(text="Erro nos valores. Verifique e tente novamente.")


if __name__ == "__main__":
    app = InvestmentApp()
    app.mainloop()
