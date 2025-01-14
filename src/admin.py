import os
from flask_admin import Admin
from models import db, User, Character, Episode, Location, Favorite  # Importa los modelos necesarios
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    """
    Configura el panel de administración de Flask-Admin para gestionar los modelos.
    """
    # Configuración básica del admin
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='Rick and Morty Admin', template_mode='bootstrap3')

    # Añadir modelos al panel de administración
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Character, db.session))
    admin.add_view(ModelView(Episode, db.session))
    admin.add_view(ModelView(Location, db.session))
    admin.add_view(ModelView(Favorite, db.session))

    # Nota: Puedes duplicar las líneas anteriores para agregar nuevos modelos.
