from flask import Flask

def create_app():
    app=Flask (__name__)

    # cofiguracion del proyecto
    app.config.from_mapping(
        DEBUG= True,
        SECRET_KEY='dev'
    )
    # Registrar Bluprint
    from . import todo
    app.register_blueprint(todo.bp)

    from . import auth
    app.register_blueprint(auth.bp)



    @app.route('/')
    def index():
        return 'Hola mundo'
        
    return app