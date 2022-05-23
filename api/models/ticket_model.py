from . import db

class Ticket(db.Model):
    __tablename__ = 'Ticket'

    id      = db.Column(db.Integer, primary_key = True, autoincrement=True)
    number  = db.Column(db.Integer)
    sold_by = db.Column(db.String(80))
    id_rifa = db.Column(db.Integer, db.ForeignKey('Rifa.id'))

    def __repr__(self) -> str:
        return '<RifaL {}>'.format(self.number)