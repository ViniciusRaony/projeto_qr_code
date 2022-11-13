from . import db


class Usuario(db.Model):
    __tablename__ = 'Usuario'

    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(14), nullable=False, unique=True)
    nome = db.Column(db.String(45), nullable=False)
    email_pessoal = db.Column(db.String(45), nullable=False, unique=True)
    login = db.Column(db.String(45), nullable=False, unique=True)
    senha = db.Column(db.String(45), nullable=False)
    # One-to-One relationship
    funcionario = db.relationship('Funcionario', backref='usuario', lazy=True, uselist=False)
    # One-To-Many relationship
    telefone = db.relationship('Telefone', backref='usuario', lazy=True)
    # One-To-Many relationship
    rede = db.relationship('Rede', backref='usuario', lazy=True)

    def __init__(self, cpf, nome, email_pessoal, login, senha):
        self.cpf = cpf
        self.nome = nome
        self.email_pessoal = email_pessoal
        self.login = login
        self.senha = senha

    def json(self):
        return {
            'cpf': self.cpf,
            'name': self.name,
            'email_pessoal': self.email_pessoal,
            'login': self.login,
            'senha': self.senha,
        }

    def encontrar_usuario(cls, id):
        # SELECT * FROM users WHERE cpf(do db) = cpf(do parametro)
        usuario = cls.query.filter_by(id=id).first()
        if usuario:
            return usuario
        return None

    def salvar_usuario(self):
        db.session.add(self)
        db.session.commit()

    def atualizar_usuario(self, cpf, nome, email_pessoal, login, senha):
        self.cpf = cpf
        self.nome = nome
        self.email_pessoal = email_pessoal
        self.login = login
        self.senha = senha

    def deletar_usuario(self):
        db.session.delete(self)
        db.session.commit()


class Funcionario(db.Model):
    __tablename__ = 'Funcionario'

    id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(25), nullable=False)
    email_corporativo = db.Column(db.String(45), nullable=False, unique=True)
    ramal = db.Column(db.String(5), nullable=False, unique=True)
    # One-To-One
    usuario_id = db.Column(db.String(14), db.ForeignKey('usuario.id'), nullable=False)
    # One-To-Many
    cargo_id = db.Column(db.Integer, db.ForeignKey('cargo.id'), nullable=False)
    # One-To-Many
    departamento_id = db.Column(db.Integer, db.ForeignKey('departamento.id'), nullable=False)

    def __init__(self, matricula, email_corporativo, ramal):
        self.matricula = matricula
        self.email_corporativo = email_corporativo
        self.ramal = ramal

    def json(self):
        return {
            'matricula': self.matricula,
            'email_corporativo': self.email_corporativo,
            'ramal': self.ramal,
        }


class Rede(db.Model):
    __tablename__ = 'Rede'

    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(45), nullable=False)
    # One-To-Many
    usuario_id = db.Column(db.String(14), db.ForeignKey('usuario.id'), nullable=False)

    def __init__(self, link):
        self.link = link

    def json(self):
        return {
            'link': self.link,
        }


class Telefone(db.Model):
    __tablename__ = 'telefone'

    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(11), nullable=False)
    # One-To-Many
    usuario_id = db.Column(db.String(14), db.ForeignKey('usuario.id'), nullable=False)

    def __init__(self, numero):
        self.numero = numero

    def json(self):
        return {
            'numero': self.numero,
        }


class Departamento(db.Model):
    __tablename__ = 'Departamento'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(24), nullable=False)
    # One-To-Many relationship
    funcionario = db.relationship('Funcionario', backref='departamento', lazy=True)

    def __init__(self, nome):
        self.nome = nome

    def json(self):
        return {
            'nome': self.nome,
        }


class Cargo(db.Model):
    __tablename__ = 'Cargo'

    id = db.Column(db.String, primary_key=True)
    cbo = db.Column(db.String(25), nullable=False)
    # One-To-Many relationship
    funcionario = db.relationship('Funcionario', backref='cargo', lazy=True)

    def __init__(self, cbo):
        self.cbo = cbo

    def json(self):
        return {
            'cbo': self.cbo,
        }
