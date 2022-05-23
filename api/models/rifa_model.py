from . import db

class Rifa(db.Model):
    __tablename__ = 'Rifa'

    id      = db.Column(db.Integer,primary_key=True, autoincrement=True)
    nombre  = db.Column(db.String(80))
    imagen  = db.String(db.String(120))

    tickets = db.relationship(
        'Ticket',
        backref='Rifa',
        lazy='dynamic'
    )

    def __repr__(self) -> str:
        return "Rifa: {}".format(self.nombre)