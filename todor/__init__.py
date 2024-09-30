from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Crear la extensión
db=SQLAlchemy()


def create_app():
    app=Flask (__name__)

    # cofiguracion del proyecto
    app.config.from_mapping(
        DEBUG= True,
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI="sqlite:///todolist.db"
    )

    # Inicializar la extensión 
    db.init_app(app)


    # Registrar Bluprint
    from . import todo
    app.register_blueprint(todo.bp)

    from . import auth
    app.register_blueprint(auth.bp)


    @app.route('/')
    def index():
        return render_template ('index.html')
    
    # Migra todos los modelos a la base de datos que no han sido migrados
    with app.app_context():
        db.create_all()
        
    return app