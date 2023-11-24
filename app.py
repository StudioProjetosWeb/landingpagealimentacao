from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

# Configurações do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'diogenestrabalhoweb@gmail.com'
app.config['MAIL_PASSWORD'] = 'Diogenesgomessantos126422'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']

        msg = Message('Novo Contato da Landing Page', sender='seu-email@gmail.com', recipients=['seu-email@gmail.com'])
        msg.body = f"Nome: {nome}\nEmail: {email}\nTelefone: {telefone}"
        mail.send(msg)

        return "Obrigado pelo seu interesse! Entraremos em contato em breve."
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
