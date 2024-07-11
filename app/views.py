from flask import jsonify, request
from app.models import Maquinaria

def index():
    response = {'message':'Hola Mundo API-REST Flask'}
    return jsonify(response)

def get_all_maquinaria():
    maquinarias = Maquinaria.get_all()
    return jsonify([Maquinaria.serialize() for Maquinaria in maquinarias])

def get_maquinaria(id_maquinaria):
    maquinaria = Maquinaria.get_by_id(id_maquinaria)
    if not maquinaria:
        return jsonify({'message': 'Product not found'}), 404
    return jsonify(maquinaria.serialize())

def create_maquinaria():
    #obtengo los datos enviados en formato json - convierte en un diccionario python
    data = request.json
    #PROCESO DE VALIDACION 
    #if(data['title']==''):
    #    return jsonify({'message':'El campo titulo es obligatorio'}), 500    
    new_maquinaria = Maquinaria(None,data['brand'],data['name'],data['model'],data['release_date'],data['banner'])
    new_maquinaria.save()
    response = {'message':'Maquinaria creada con exito'}
    return jsonify(response) , 201

def update_maquinaria(id_maquinaria):
    maq = Maquinaria.get_by_id(id_maquinaria)
    if not maq:
        return jsonify({'message': 'Product not found'}), 404
    data = request.json
    maq.brand = data['brand']
    maq.name = data['name']
    maq.model= data['model']
    maq.release_date = data['release_date']
    maq.banner = data['banner']
    maq.save()
    return jsonify({'message': 'Maquinaria updated successfully'})

def delete_maquinaria(id_maquinaria):
    maquinaria = Maquinaria.get_by_id(id_maquinaria)
    if not maquinaria:
        return jsonify({'message': 'Maquinaria not found'}), 404
    maquinaria.delete()
    return jsonify({'message': 'Maquinaria deleted successfully'})
