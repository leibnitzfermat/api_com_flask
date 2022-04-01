
from flask import Flask
from flask_restful import Resource, Api
from resources.hotel import Hoteis, Hotel, Lista_Hoteis

app = Flask(__name__)
api = Api(app)


api.add_resource(Hoteis, '/hoteis')
api.add_resource(Lista_Hoteis, '/lista_hoteis')
api.add_resource(Hotel, '/hoteis/<string:id_hotel>')

if __name__ == '__main__':
    app.run(debug=True)

