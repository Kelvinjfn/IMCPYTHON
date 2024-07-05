import flet as ft

def main(page: ft.Page):
        
    def close_banner(e):
        page.banner.open = False
        page.update()

    def calcular(e):
        if peso.value=="" or altura.value=="" or genero.value=="":
            page.banner.open = True
            page.update()
        else:
            valor_peso = float(peso.value)
            valor_altura = float(altura.value)

            # Calcular IMC
            imc = valor_peso / (valor_altura * valor_altura)
            imc = float(f"{imc:.2f}")

            # Exibir o valor do IMC
            IMC.value =f"Seu IMC é {imc}"

            if genero.value == "Feminino":
                if imc < 18.5:
                    img_resultado.src = f"MULHER1.png"
                    detalhes.value = "Abaixo do Peso."
                elif 18.5 <= imc < 24.9:
                    img_resultado.src = f"MULHER1.png"
                    detalhes.value = "Peso Normal."
                elif 25 <= imc < 29.9:
                    img_resultado.src = f"MULHER2.png"
                    detalhes.value = "Sobrepeso."
                elif 30 <= imc < 34.9:
                    img_resultado.src = f"MULHER2.png"
                    detalhes.value = "Obesidade Grau 1."
                else:
                    img_resultado.src = f"MULHER2.png"
                    detalhes.value = "Obesidade Grau 2."

            else:
                if imc < 18.5:
                    img_resultado.src = f"HOMEM1.png"
                    detalhes.value = "Abaixo do Peso."
                elif 18.5 <= imc < 24.9:
                    img_resultado.src = f"HOMEM1.png"
                    detalhes.value = "Peso Normal."
                elif 25 <= imc < 29.9:
                    img_resultado.src = f"HOMEM2.png"
                    detalhes.value = "Sobrepeso."
                elif 30 <= imc < 34.9:
                    img_resultado.src = f"HOMEM2.png"
                    detalhes.value = "Obesidade Grau 1."
                else:
                    img_resultado.src = f"HOMEM2.png"
                    detalhes.value = "Obesidade Grau 2."
                
        # Limpar Campos
        peso.value = ""
        altura.value = ""
        genero.value = ""

        # Atualizar a Página
        page.update()

    
    # Configurando a página.
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MULTILINE_CHART),
        leading_width=40,
        title=ft.Text("Calculadora IMC"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT
    )
        
    page.window_width = 400
    page.window_height = 550

    # Configuração do Banner de Notificação
    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text("Preencha todos os campos!", color=ft.colors.BLACK),
        actions=[
        ft.TextButton(
            "Ok",
            on_click=close_banner,
            style=ft.ButtonStyle(color=ft.colors.BLACK)
        ),
    ],
    )

    altura = ft.TextField(label="Altura", hint_text="Por favor insira sua altura.")
    peso = ft.TextField(label="Peso", hint_text="Por favor insira seu peso.")
    genero = ft.Dropdown(
        label="Gênero",
        hint_text="Escolha seu gênero.",
        options=[
            ft.dropdown.Option("Masculino"),
            ft.dropdown.Option("Feminino"),
        ],
    )
    # Botão para calcular o IMC
    b_calcular = ft.ElevatedButton(text="Calcular IMC", on_click=calcular)

    # Exibir o IMC e Resultado
    IMC = ft.Text("Seu IMC é ...", size=30)
    detalhes = ft.Text("Insira seus dados.", size=20)

    img_capa = ft.Image(
        src=f"Capa.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    info_app_resultado = ft.Column(
        controls=[
            IMC,
            detalhes,
        ]
    )
    
    img_resultado = ft.Image(
        src=f"Capa.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    info = ft.Row(
        controls=[
            info_app_resultado,
            img_resultado,
        ]
    )


    # Layout da Página
    layout = ft.ResponsiveRow(
        [
            ft.Container(
                info,
                padding=5,
                col={"sm":4, "md":4, "xl":4},
                alignment=ft.alignment.center,
            ),
            ft.Container(
                altura,
                padding=5,
                bgcolor=ft.colors.BLACK,
                col={"sm":12, "md":3, "xl":3},
            ),
            ft.Container(
                peso,
                padding=5,
                bgcolor=ft.colors.BLACK,
                col={"sm":12, "md":3, "xl":3},
            ),
            ft.Container(
                genero,
                padding=5,
                bgcolor=ft.colors.BLACK,
                col={"sm":12, "md":3, "xl":3},
            ),
            ft.Container(
                b_calcular,
                padding=5,
                bgcolor=ft.colors.BLACK,
                col={"sm":12, "md":3, "xl":3},
            ),
        ]
    )

    page.add(layout)


ft.app(target=main)
