from flask import Flask, render_template, request

app = Flask (__name__,template_folder="./src/views")

# Criando uma rota
@app.route("/", methods=["GET", "POST"])
def home():
    if (request.method =="GET"):
        return render_template("index.html")
    else:
        #imprimindo dados do formulario
        if (request.form ["valor"] != "" and request.form ["frete"] != ""):

            valor_produto = request.form["valor"]
            frete = request.form["frete"]
            juros = 0.2

            if (request.form["parcelado"] == "pg_a_vista"):
                soma = float(valor_produto) + float(frete)
                return {
                    "Produto a vista": str(soma)
                }

            elif (request.form["parcelado"] == "parcelas"):
                  mult = (float(valor_produto) * juros) + float(frete) + float(valor_produto)
                  return { 
                      "Valor do produto parcelado (com juros)": str(mult)
                  }
            
            else:
                return "obrigado"

        else:
            return "Existe algum campo vazio"

#@app.route("/", methods="POST")
#def sobre():
    #return "sobre"

# Porta de erro
@app.errorhandler(404)
def not_found(error):
    return "Esta pagina não existe"

#criando porta
app.run(port=8080, debug=True)