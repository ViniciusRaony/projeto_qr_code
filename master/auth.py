from flask import Blueprint, render_template, request, flash, redirect, url_for

from . import db
from .models import Usuario
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario = Usuario.query.filter_by(email=email).first()
        if usuario:
            if check_password_hash(usuario.senhar, senha):
                flash('Logado com sucesso', category='sucess')
            else:
                flash('Senha incorreta, tente novamente.', category='error')
        else:
            flash('Emal inexistente.', category='error')

    return render_template('login.html', text="Testing")  # Passar valores para o template


@auth.route('/qr-code', methods=['GET', 'POST'])
def qr_code():
    return render_template('qr_code.html')


@auth.route('/cartao-customizar', methods=['GET', 'POST'])
def cartao_customizar():
    return render_template('cartao_customizar.html')


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email_pessoal = request.form.get('email')
        nome = request.form.get('nome')
        senha1 = request.form.get('senha1')
        senha2 = request.form.get('senha2')

        usuario = Usuario.query.filter_by(email_pessoal=email_pessoal).first()
        if usuario:
            flash('Email já cadastrado.', category='error')
        elif senha1 != senha2:
            flash('Password precisam ser iguais.', category='error')
        else:
            novo_usuario = Usuario(email_pessoal=email_pessoal, nome=nome,
                                   senha=generate_password_hash(senha1, method='sha256'))
            db.session.add(novo_usuario)
            db.session.commit()
            flash('Conta criada com sucesso!', category='error')
            return redirect(url_for('views.home'))

    return render_template('sign_up.html')
