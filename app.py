from flask import Flask,render_template,request,redirect,url_for,flash

app = Flask(__name__)

app.config['SECRET_KEY']='una_clave_secreta_muy_larga_y_dificil_de_advinar'
@app.route('/')
def main():
    return render_template('base.html')

@app.route('/animales')
def ani():
    return render_template('animales.html')

@app.route('/Vehiculos')
def vei():
    return render_template('vehiculos.html')

@app.route('/Maravillas')
def mav():
    return render_template('Maravillas.html')

@app.route('/AcercaDe')
def Ace():
    return render_template('AcercaDe.html')

@app.route('/registrate')
def Regi():
    return render_template('registrate.html')

@app.route('/iniciaSes')
def Inicia():
    return render_template('iniciaSes.html')

@app.route('/obtenerinfo',methods=("GET","POST"))
def Obt():
    error=None
    if request.method == "POST":
        NombreCompleto=request.form["NombreCompleto"]
        Dia=request.form["Dia"]
        Mes=request.form["Mes"]
        Año = int(request.form["Año"])
        Genero=request.form["Genero"]
        email=request.form["email"]
        Contra=request.form["Contra"]
        ContraPru=request.form["ContraPru"]
        tel=request.form["tel"]

        if Contra != ContraPru:
            error = "La contraseña no coincide"
        
        if Año > 2006:
            error ="Eres menor de edad"

        if error is not None:
            flash(error, "error")
            return render_template("registrate.html")
        else:
            flash(f"Registro exitoso para el usuario: {NombreCompleto}", "success")
            return render_template("base.html")
        
if __name__ == '__main__':
    app.run(debug=True)
