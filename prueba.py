import requests

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class GeoAPI:
 API_KEY = "d81015613923e3e435231f2740d5610b"
 LAT = "-35.836948753554054"
 LON = "-61.870523905384076"

@classmethod
def is_hot_in_pehuajo(cls):
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?lat={cls.LAT}&lon={cls.LON}&appid={cls.API_KEY}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                temperature = data["main"]["temp"] - 273.15  #to C

                if temperature > 28:
                    return True
                else:
                    return False
            else:
                print("--- Error en la conexion ---")
                return False
        except requests.exceptions.RequestException as errorserv:
            print("--- Error en la conexión --- ", errorserv)
            return False
        



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd

_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"], "quantity": [3, 10, 0, 5]})

def is_product_available(product_name, quantity):
    if product_name not in _PRODUCT_DF['product_name'].values:
        print("El producto no existe")
        return False

    stock = _PRODUCT_DF.loc[_PRODUCT_DF['product_name'] == product_name, 'quantity'].item()

    # Verificar si hay suficiente stock disponible
    if stock >= quantity:
        return True
    else:
        return False
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1", "heladoFrozen"]

def validate_discount_code(discount_code):
    for code in _AVAILABLE_DISCOUNT_CODES:
        return any(sum(a.lower() != b.lower() for a, b in zip(discount_code, code)) < 3 for code in _AVAILABLE_DISCOUNT_CODES)

#comparamos los codigos caracter por caracter ignorando uppercases. Dependiendo si la diferencia es mayor o menor a 3 retorna un booleano diferente,
#con el any busque una logica que permita al programa identificar si al menos uno de los valores generados fue True