from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import requests

# Función para obtener la ubicación basada en la IP
def obtener_ubicacion(ip):
    try:
        print(f"Consultando ubicación para IP: {ip}")
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        print(response.text)  # Imprime la respuesta completa de la API
        data = response.json()
        ciudad = data.get("city", "Desconocida")
        region = data.get("region", "Desconocida")
        pais = data.get("country", "Desconocido")
        loc = data.get("loc", "Desconocida")
        return f"{ciudad}, {region}, {pais} ({loc})"
    except Exception as e:
        return f"Error al obtener ubicación: {str(e)}"

# Función para registrar datos de visitantes
def registrar_visita(client_ip, user_agent, ubicacion):
    with open("visitas.txt", "a") as file:
        file.write(f"{datetime.now()} - IP: {client_ip} - Ubicación: {ubicacion} - User-Agent: {user_agent}\n")

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Obtener la IP del cliente
        client_ip = self.client_address[0]
        # Obtener el User-Agent del cliente
        user_agent = self.headers.get('User-Agent')
        # Obtener la ubicación del cliente
        ubicacion = obtener_ubicacion(client_ip)

        # Registrar la visita
        registrar_visita(client_ip, user_agent, ubicacion)

        # Responder al cliente
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Gracias por tu visita!")

# Configurar y ejecutar el servidor
def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor corriendo en http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
