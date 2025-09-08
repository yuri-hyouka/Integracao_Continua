from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_exchange_rate():
    """Busca a taxa USD-BRL em tempo real"""
    try:
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        response = requests.get(url).json()
        return float(response["USDBRL"]["bid"])
    except Exception as e:
        print("Erro ao buscar cotação:", e)
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    taxa = get_exchange_rate()
    if request.method == "POST" and taxa:
        try:
            valor = float(request.form["valor"])
            direcao = request.form["direcao"]

            if direcao == "brl_to_usd":
                convertido = round(valor / taxa, 2)
                resultado = f"R${valor:.2f} = US${convertido:.2f} (1 USD = R${taxa:.2f})"
            else:
                convertido = round(valor * taxa, 2)
                resultado = f"US${valor:.2f} = R${convertido:.2f} (1 USD = R${taxa:.2f})"
        except ValueError:
            resultado = "Digite um valor numérico válido!"
    
    return render_template("index.html", resultado=resultado, taxa=taxa)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)