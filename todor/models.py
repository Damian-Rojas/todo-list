from todor import db

# Creaci{on del modelo del usuario
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique= True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    # Constructor del modelo
    def __init__(self, username, password):
        self.username=username
        self.password=password

    # Obtener datos
    def __repr__(self):
        return f'<User: {self.username}>' 
    


# Creación del modelo del usuario
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)# Se crea relacion con el usuario
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.Text)
    state= db.Column(db.Boolean, default=False)

    # Constructor del modelo
    def __init__(self, created_by, title, desc, state=False):
        self.created_by=created_by
        self.title=title
        self.desc=desc
        self.state=state
        


    # Obtener datos
    def __repr__(self):
        return f'<Todo: {self.title}>' 