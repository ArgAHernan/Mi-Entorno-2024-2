from flask import Flask
from flask_cors import CORS
#from app.views import index, get_all_products, get_product, create_product, update_product, delete_product
#para no tener que importar una por una los nombres de las funciones, * = trae todas.

from app.views import	*
from app.database import init_app

#inicializacion de la aplicacion con flask
app = Flask(__name__) #representa el modulo actual
CORS(app)
init_app(app)
#registrar una ruta asociada a una vista
#app.route('/helloworld', methods=['GET'])(index)

app.route('/productos/', methods=['GET'])(get_all_maquinaria)
app.route('/productos/', methods=['POST'])(create_maquinaria)
app.route('/productos/', methods=['GET'])(get_maquinaria)
app.route('/productos/', methods=['PUT'])(update_maquinaria)
app.route('/productos/', methods=['DELETE'])(delete_maquinaria)


if __name__ == '__main__': #levanta el servidor de flask
    app.run(debug=True)
