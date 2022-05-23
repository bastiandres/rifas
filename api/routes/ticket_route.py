from flask import Blueprint, jsonify, request
from api.models.ticket_model import Ticket
from backend.api.services.select_winners import returnNWinner
from flasgger import swag_from
from api.models import db
from api.schema.ticket_schema import TicketSchema

tickets_api = Blueprint('tickets', __name__)

@tickets_api.get('/')
@swag_from()
def get_all():
    ticketSch = TicketSchema(many=True)
    tickets = Ticket.query.all()
    data = ticketSch.dump(tickets)

    return jsonify(data),200


# anadido esto
@tickets_api.get('/all/<int:idRifa>')
@swag_from()
def get_all_by_id(idRifa):
    myList = []
    ticketSch = TicketSchema(many=True)
    allTickets = Ticket.query.filter(Ticket.id_rifa == int(idRifa)).all()

    return jsonify(ticketSch.dump(allTickets))


@tickets_api.post('/<int:idRifa>/new')
@swag_from()
def add_new(idRifa):
    # ticketSch = TicketSchema()
    newTicket = Ticket()
    print(idRifa)
    newTicket.id_rifa = idRifa
    newTicket.number = request.get_json()['number']
    newTicket.sold_by = request.get_json()['sold_by']
    db.session.add(newTicket)
    db.session.commit()
    return jsonify(msg='OK'),202

@tickets_api.post('/<int:idRifa>/sorteo')
@swag_from()
def sortear(idRifa):
    winners = request.get_json()['number']
    allTickets = Ticket.query.filter(Ticket.id_rifa == int(idRifa)).all()
    myList = []
    myList = returnNWinner(winners,allTickets)
    return jsonify(myList)


