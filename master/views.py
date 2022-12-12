from os import abort

from flask import Blueprint, render_template
from flask_login import login_required, current_user

from master.models import Usuario

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/qr_code')
@login_required
def qr_code():
    return render_template("qr_code.html", user=current_user)


@views.route('/card_cp/<int:id>', methods=['GET'])
@login_required
def render_cartao(id):
    u = Usuario.query.get(id)
    if u != current_user:
        abort(403)
    return render_template("card_cp.html", usuario=u)
