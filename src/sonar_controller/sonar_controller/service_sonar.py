from brping import Ping1D
import sys
import rclpy
from rclpy.node import Node
import serial
import serial.tools.list_ports
from custom_interfaces.srv import Sonar
import threading


class SonarService(Node):
    def __init__(self):
        super().__init__("sonar_service")
        self.remembered_port = None
        self.ping_device = None
        self.ping_thread = None
        self.service = self.create_service(Sonar, "sonar", self.sonar_callback)
        self.port_monitor_thread = threading.Thread(target=self.monitor_usb_port, daemon=True)
        self.port_monitor_thread.start()



 # funcion para buscar por los puertos USB el numero de serie del sonar, si coincide el numero de serie obtiene el puerto donde se ubica, ademas en esta fucnion lo que realizara sera una busqueda continua del sistema.
 #  Se realiza para cuando hay una desconexion del USB y a continuacion conectamos de nuevo pueda volver a funcionar sin que tengamos que levantar el servicio de nuevo. 
 # La busqueda se realiza de manera constante cuando no se encuentra el dispositivo con el numero de serie.


 
    def monitor_usb_port(self):
        while True:
            arduino_ports = [
                p.device
                for p in serial.tools.list_ports.comports()
                if p.serial_number == "DM00R2J8" # Numero de serie del sonar, cambiar al que se este utilizando
            ]
            if self.remembered_port not in arduino_ports:
                self.get_logger().info("USB device disconnected")
                self.ping_device = None
                self.remembered_port = None

            if not self.ping_device:
                for port in arduino_ports:
                    try:
                        ping_device = Ping1D()
                        ping_device.connect_serial(port, 115200)
                        ping_device.initialize()
                        ping_device.set_ping_enable(True)
                        self.ping_device = ping_device
                        self.remembered_port = port
                        self.get_logger().info(f"Connected to {port}")
                        break
                    except Exception as e:
                        self.get_logger().info(f"Failed to connect to {port}: {e}")
            rclpy.spin_once(self, timeout_sec=0.5)

            
     
# funcion para la comprobacion del sonar , se llama dentro de la clase Ping dada por el sonar a la funcion get_ping_enable que muestra 
# si esta activo la señal de salida acustica, que es la que se encarga de realizar la mediciones

    def sonar_callback(self, request, response):
        if self.ping_device:
            if self.ping_device.get_ping_enable:
                response.success = True
                self.get_logger().info("Sonar working")
            else:
                response.success = False
                self.get_logger().info("Sonar not working")
        return response


def main(args=None):
    rclpy.init(args=args)
    sonar_service = SonarService()
    rclpy.spin(sonar_service)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
