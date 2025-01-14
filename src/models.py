from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(50), nullable=False)  # Ejemplo: "Alive", "Dead", "Unknown"
    species = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    origin = db.Column(db.String(120), nullable=True)
    location = db.Column(db.String(120), nullable=True)
    image = db.Column(db.String(250), nullable=True)  # URL de la imagen del personaje

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "species": self.species,
            "gender": self.gender,
            "origin": self.origin,
            "location": self.location,
            "image": self.image,
        }

class Episode(db.Model):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    air_date = db.Column(db.String(50), nullable=True)  # Fecha de emisión
    episode_code = db.Column(db.String(50), nullable=False)  # Ejemplo: "S01E01"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "air_date": self.air_date,
            "episode_code": self.episode_code,
        }

class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    type = db.Column(db.String(50), nullable=True)  # Ejemplo: "Planet", "Space Station"
    dimension = db.Column(db.String(50), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "dimension": self.dimension,
        }

class Favorite(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=True)

    user = db.relationship('User', back_populates='favorites')
    character = db.relationship('Character')
    episode = db.relationship('Episode')
    location = db.relationship('Location')

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character": self.character.serialize() if self.character else None,
            "episode": self.episode.serialize() if self.episode else None,
            "location": self.location.serialize() if self.location else None,
        }

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    favorites = db.relationship('Favorite', back_populates='user', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "favorites": [favorite.serialize() for favorite in self.favorites],
        }
