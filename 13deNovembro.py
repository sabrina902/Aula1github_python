import flet as ft

def main(page: ft.page):
    page.title="Calculadora IMC"
    page.window.width=600
    page.window.alignment=ft.alignment.center

    def salvar(e):
        if altura_field.value!="" and peso_field.value!="":
           peso= float(peso_field.value)
           altura_metros= float(altura_field.value )/100
           imc=peso/(altura_metros ** 2)

        if imc<18.5:
            result_text.value=f"seu IMC é {imc:.2f}  - abaixo do peso!"
            result_image.src="src/baixo.png"
        elif imc<24.9:
            result_text.value=f"seu IMC é {imc:.2f}  - peso normal!"
            result_image.src="src/normal.png"
        elif imc<24.9:
            result_text.value=f"seu IMC é {imc:.2f}  - sobrepeso!"
            result_image.src="src/sobrepeso.png"
        elif imc<29.9:
            result_text.value=f"seu IMC é {imc:.2f}  - obesidade 1!"
            result_image.src="src/obesidade1.png"
        elif imc<34.9:
            result_text.value=f"seu IMC é {imc:.2f}  - obesidade 2!"
            result_image.src="src/obesidade2.png"
        elif imc<40.9:
            result_text.value=f"seu IMC é {imc:.2f}  - obesidade 3!"
            result_image.src="src/obesidade3.png"
        page.update()


    def valida_altura(e):
        if not (altura_field.value.isnumeric() and int (altura_field.value)>0):
            altura_field.error_text="insira um valor númerico pasitivo"
            altura_field.value=None
        else:
            altura_field.error_text=None
        page.update()
    
    def valida_peso(e):
        if not (peso_field.value.isnumeric() and int (peso_field.value)>0):
            peso_field.error_text="insira um valor númerico pasitivo"
            peso_field.value=None
        else:
            peso_field.error_text=None
        page.update()



    page.appbar = ft.AppBar(
        title=ft.Text( 
                     value="Calculadora IMC",
                     size=22,
                     color="white",
                     weight="bold"
                     
                     ),
        center_title=True,
        bgcolor="#4CADE4"
        
        )
    altura_field= ft.TextField(
        label="Altura (cm)",
        width=300,
        hint_text="Por favor insira sua Altura",
        on_change=valida_altura
    )

    peso_field= ft.TextField(
        label="Peso (kg)",
        width=300,
        hint_text="Por favor insira seu peso",
        on_change=valida_peso
    )
    
    result_text= ft.Text(
    value="insira as informações para começar!",
    size=22,
    width=150
    )
    
    result_image=ft.Image(src="src/imc.png", width=150,height='150')
    salvar_button=ft.ElevatedButton(on_click=salvar)

    page.add(
        ft.Row(
            [
                    ft.Column(
                            controls=[
                                    ft.Row([ result_text,result_image],
                                           alignment=ft.MainAxisAlignment.CENTER
                                           ),
                                            altura_field,
                                            peso_field,
                                            salvar_button

                                    
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
                
        )
            
    )
ft.app(main)