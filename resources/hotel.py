from os import sep
from flask_restful import Resource


hoteis = [
    {
        'id_hotel': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Belo Horizonte'
    },
    {
        'id_hotel': 'bravo',
        'nome': 'Bravo Hotel',
        'estrelas': 2.3,
        'diaria': 420.34,
        'cidade': 'São Paulo'
    },
    {
        'id_hotel': 'delta',
        'nome': 'Delta Hotel',
        'estrelas': 3.3,
        'diaria': 420.34,
        'cidade': 'Rio de janeiro'
    },
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}
    

nomes = []
for i in range(len(hoteis)):
    nomes.append(hoteis[i]['nome'])
class Lista_Hoteis(Resource):
    def get(self):
        return nomes
            
    
class Hotel(Resource):
    def get(self, id_hotel):
        for hotel in hoteis:
            if hotel['id_hotel'] == id_hotel:
                return hotel
        return {'message': 'Hotel not found.'}, 404    
    
    def post(self, id_hotel):
        pass
    
    def put(self, id_hotel):
        pass
    
    def delete(self, id_hotel):
        pass