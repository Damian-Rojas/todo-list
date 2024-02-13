from flask import (
   Blueprint, render_template, request, url_for, redirect, flash, session, g 
)
# Objeto G, puede servir para guardar algun valor como por ejemplo las cookies


# Para generar y chequear los password
from werkzeug.security import generate_password_hash, check_password_hash

from .models import User
from todor import db

bp=Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('register/', methods=('GET','POST'))
def register():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
         
        user=User(username, generate_password_hash(password))

        error=None

        user_name=User.query.filter_by(username=username).first()
        if user_name==None:
            db.session.add(user)
            db.session.commit()
            return  redirect(url_for('auth.login'))
        else:
            error= f'El usuario {username} ya esta registrado'
        flash(error)
        

    return render_template('auth/register.html')


@bp.route('login/', methods=('GET','POST'))
def login():
        if request.method=='POST':
            username=request.form['username']
            password=request.form['password']

            error=None

            #Validar datos
            user=User.query.filter_by(username=username).first()
            if user==None:
                 error='Nombre de ussuario incorrecto'
            elif not check_password_hash(user.password, password):
                 error='Contraseña incorrecta'
                 
            # Iniciar sesion
            if error is None:
                session.clear() # Limpia sesion
                session['user_id']=user.id # Se guarda en la clave de la sesion la el Id del usuario
                return  redirect(url_for('todo.index'))
    
            flash(error)


        return render_template('auth/login.html')

# Función verificar si el usuario que inicia Sesion
@bp.before_app_request #Ejecuta la función en cada petición
def load_logged_in_used():
    user_id=session.get('user_id') #Obtiene el id del usuario que tiene la sesion

    if user_id is None:
        g.user=None
    else:
        g.user=User.query.get_or_404(user_id)
          

@bp.route('logout/')
def logout():
     session.clear()
     return redirect(url_for('index'))


import functools
# Funcion decoradora para inicio de sesion, sino tiene inicio de sesion a autenticación del usuario
def login_required(view):
    @functools.wraps(view)
    def wraps_view(** kwargs):
         if g.user is None:
              return redirect(url_for('auth.login'))
         return view(**kwargs)
    return wraps_view

     
     
     