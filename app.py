from flask import Flask,render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)