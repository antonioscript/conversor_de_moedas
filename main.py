import PySimpleGUI as sg
import requests

def index():
	sg.theme("DarkGreen4")
	r = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
	cotacao = r.json()
	
	dolar = cotacao["USDBRL"]["bid"] 
	euro = cotacao["EURBRL"]["bid"] 
	bit = cotacao["BTCBRL"]["bid"] 

	layout = [  
		[sg.Text("Conversor de Moedas", font="Any 24")],
		[sg.Text("")],
		[sg.Text("")],
		[sg.Text("")],
		[sg.Push(), sg.Text("Digite o Valor em Real R$", font="Any 14"), sg.Push(), sg.Input(font="Any 14", size=15, key="-VALOR-")],
		[sg.Text("")],
		[sg.Push(), sg.Text("Converter Para", font="Any 14"),sg.Push()],
		[sg.Text("")],
		[sg.Button('Dólar', font="Anya 14"), sg.Button('Euro', font="Anya 14"), sg.Button('Bitcon', font="Anya 14")],
		[sg.Text("")],
		[sg.Text("R$", font="Any 16"), sg.Input("", font="Any 14", key = "saida", size = 14, justification="center")]	  		
]

	window = sg.Window('Pick a color', layout, element_justification="center", size=(500, 500) )

	while True:                  
		event, values = window.read()
		if event == sg.WIN_CLOSED:
			break
		elif event == "Dólar":
			valor = values["-VALOR-"]
			valor1 = float(valor)
			dolar1 = float(dolar)
			conversao1 = valor1*dolar1
			window["saida"].update('{:.2f}'.format(conversao1))
		elif event == "Euro":
			valor = values["-VALOR-"]
			valor2 = float(valor)
			euro2 = float(euro)
			conversao2 = valor2*euro2
			window["saida"].update('{:.2f}'.format(conversao2))
		elif event == "Bitcon":
			valor = values["-VALOR-"]
			valor3 = float(valor)
			bit3 = float(bit)
			conversao3 = valor3*bit3
			window["saida"].update('{:.2f}'.format(conversao3))
			
index()
