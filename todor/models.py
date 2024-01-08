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