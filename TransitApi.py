import requests
import pandas as pd
from datetime import datetime
import os
from config import API_KEY 

# Lista de ciudades válidas
ciudades_validas = [
    "Bogotá, Colombia", "Cali, Colombia", "Medellín, Colombia",
    "Cajicá, Colombia", "Neiva, Colombia", "Villavicencio, Colombia"
]

# Función para obtener datos del usuario
def obtener_datos_usuario():
    placa = input("Ingrese la placa del vehículo: ").upper()
    tipo = input("Ingrese el tipo de vehículo: ").upper()
    conductor = input("Ingrese el nombre del conductor: ").strip().capitalize()
    cedula = input("Ingrese la cédula del conductor: ")
    fecha = datetime.now().strftime("%Y-%m-%d")

    # Seleccionar la ciudad de origen
    origen = seleccionar_ciudad("origen")
    if origen is None:
        return None  # Salir si no se seleccionó ciudad válida

    # Seleccionar la ciudad de destino
    destino = seleccionar_ciudad("destino")
    if destino is None:
        return None  # Salir si no se seleccionó ciudad válida

    return {
        "placa": placa,
        "tipo": tipo,
        "conductor": conductor,
        "cedula": cedula,
        "fecha": fecha,
        "origen": origen,
        "destino": destino
    }

# Función para seleccionar ciudad
def seleccionar_ciudad(tipo):
    for intentos in range(3):
        print(f"\nSeleccione la ciudad de {tipo}:")
        for i, ciudad in enumerate(ciudades_validas):
            print(f"{i + 1}. {ciudad}")
        
        try:
            opcion = int(input("Ingrese el número de la ciudad: "))
            if 1 <= opcion <= len(ciudades_validas):
                return ciudades_validas[opcion - 1]
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")

    print("Demasiados intentos. Cerrando el programa.")
    return None  # Indica que no se seleccionó ciudad válida

# Función principal
def main():
    while True:
        print("\nSeleccione una opción:")
        print("1. Ingresar datos")
        print("2. Salir")

        for intentos in range(3):
            try:
                opcion = int(input("Ingrese el número de la opción: "))
                if opcion == 1:
                    # Obtener datos del usuario
                    datos = obtener_datos_usuario()

                    if datos:  # Solo continuar si se obtuvieron datos válidos
                        # Solicitar datos a la API de Google Maps
                        url = f"https://maps.googleapis.com/maps/api/directions/json?origin={datos['origen']}&destination={datos['destino']}&key={API_KEY}&departure_time=now"
                        response = requests.get(url)
                        data = response.json()

                        # Verificar el estado de la respuesta
                        if data['status'] == 'OK':
                            # Obtener la distancia y el tiempo de viaje
                            distancia = data['routes'][0]['legs'][0]['distance']['text']
                            tiempo = data['routes'][0]['legs'][0]['duration']['text']
                            condiciones_trafico = data['routes'][0]['legs'][0]['duration_in_traffic']['text']

                            # Mostrar los resultados
                            print(f"\nOrigen: {datos['origen']}")
                            print(f"Destino: {datos['destino']}")
                            print(f"Distancia: {distancia}")
                            print(f"Tiempo Estimado: {tiempo}")
                            print(f"Condiciones de Tráfico: {condiciones_trafico}")

                            # Mostrar información del vehículo
                            print("\nInformación del Vehículo Asignado:")
                            for key, value in datos.items():
                                if key not in ['origen', 'destino']:
                                    print(f"{key.capitalize()}: {value}")

                            # Crear un DataFrame con los resultados
                            resultados = {
                                "Origen": [datos['origen']],
                                "Destino": [datos['destino']],
                                "Distancia": [distancia],
                                "Tiempo Estimado": [tiempo],
                                "Condiciones de Tráfico": [condiciones_trafico],
                                "Placa": [datos["placa"]],
                                "Tipo": [datos["tipo"]],
                                "Conductor": [datos["conductor"]],
                                "Cédula": [datos["cedula"]],
                                "Fecha": [datos["fecha"]],
                            }

                            df_resultados = pd.DataFrame(resultados)

                            # Guardar el DataFrame en un archivo Excel
                            df_resultados.to_excel("resultados_viaje.xlsx", index=False, mode='a', header=not os.path.isfile("resultados_viaje.xlsx"))
                            print("\nResultados guardados en 'resultados_viaje.xlsx'.")

                        else:
                            print("Error en la solicitud a la API:", data['status'])
                    break  # Salir del ciclo después de ingresar datos
                elif opcion == 2:
                    print("Cerrando el programa.")
                    return  # Salir del programa
                else:
                    print("Opción no válida. Intente de nuevo.")
            except ValueError:
                print("Entrada no válida. Debe ingresar un número.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
