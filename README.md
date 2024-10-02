# TransitAPI

## Descripción
TransitAPI es un proyecto diseñado para optimizar la logística y planificación de despachos mediante la integración de la API de Google. Permite calcular la distancia y el tiempo estimado entre un origen y un destino, además de gestionar datos sobre vehículos y despachos.

## Funcionalidades
- **Cálculo de Rutas**: Obtiene distancia en kilómetros y tiempo estimado entre origen y destino desde la Api de google trafic.
- **Condiciones de Tráfico**: Considera el tráfico actual para proporcionar estimaciones más precisas.
- **Gestión de Vehículos**: Permite ingresar datos de vehículos, incluyendo placa, tipo, nombre del conductor y cédula.
- **Almacenamiento de Datos**: Todos los registros se almacenan en un archivo Excel para análisis posterior.

## Tecnologías Utilizadas
- Python
- Google Maps API
- Pandas
- OpenPyXL

## Instrucciones de Uso
1. Clona el repositorio.
2. Instala las dependencias usando: pip install -r requirements.txt


3. Modifica el archivo `config.py` con tu clave de API de Google.
4. Ejecuta el archivo principal: python main.py

5. 
## Conclusiones
- **Integración Efectiva**: Este proyecto demuestra cómo integrar la API de Google para obtener datos de rutas y tiempos estimados de entrega, optimizando la logística.
- **Almacenamiento de Datos**: Los datos se almacenan en un archivo Excel para un análisis continuo.
- **Interfaz de Usuario Simple**: Facilita el ingreso de datos a través de una consola.
- **Mejoras Futuras**: Se planean análisis más profundos y una interfaz gráfica.
- **Contribuciones**: Abierto a mejoras y nuevas funcionalidades.

## Contacto
Para más información o consultas, puedes contactarme a través de:
- **Email**: jonathan.montes1@outlook.com
- **GitHub**: (https://github.com/jonathangit0320)

## Información sobre la API
Este proyecto utiliza la API de Google Maps para acceder a información sobre rutas y tiempos estimados de entrega. Asegúrate de tener una clave de API válida y habilitar los servicios requeridos en tu consola de Google Cloud.

## Licencia
Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE en este repositorio.



