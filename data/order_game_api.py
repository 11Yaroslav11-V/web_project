from flask import jsonify, Blueprint, request
import datetime
from data import db_session
from data.order_game import Order

blueprint = Blueprint('order_game_api', __name__, template_folder='templates')


@blueprint.route('/api/order')
def get_order():
    db_sess = db_session.create_session()
    order = db_sess.query(Order).all()
    return jsonify({'order': [item.to_dict(
        only=('id', 'company', 'game_name', 'status',
              'created_date', )) for item in order]})


@blueprint.route('/api/order/<int:order_id>', methods=['GET'])
def get_one_order(order_id):
    db_sess = db_session.create_session()
    order = db_sess.query(Order).get(order_id)
    if not order:
        return jsonify({'error': 'Not found'})
    return jsonify({'order': order.to_dict(
        only=('id', 'company', 'game_name', 'status',
              'created_date'))})


@blueprint.route('/api/order', methods=['POST'])
def create_order():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in ['company', 'game_name', 'status']):
        return jsonify({'error': 'Bad request'})

    db_sess = db_session.create_session()
    order = Order(
        company=request.json['company'],
        game_name=request.json['game_name'],
        status=request.json['status'])
    db_sess.add(order)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/order/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    db_sess = db_session.create_session()
    order = db_sess.query(Order).get(order_id)
    if not order:
        return jsonify({'error': 'Not found'})
    db_sess.delete(order)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/order/<int:order_id>', methods=['PUT'])
def edit_order_status(order_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    db_sess = db_session.create_session()
    order = db_sess.query(Order).get(order_id)
    if not order:
        return jsonify({'error': 'Not found'})
    order.status = request.json['status']

    db_sess.commit()
    return jsonify({'success': 'OK'})


