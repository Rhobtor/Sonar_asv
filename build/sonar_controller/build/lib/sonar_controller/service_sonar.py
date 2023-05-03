
# # # from brping import Ping1D
# # # import sys
# # # import rclpy
# # # from rclpy.node import Node
# # # import serial
# # # import serial.tools.list_ports
# # # from custom_interfaces.srv import Sonar

# # # class SonarServicie(Node):
# # #     def __init__(self):
# # #         super().__init__("sonar_service")
# # #         self.sonar= None
# # #         self.remeber= None
# # #         self.serial_port = None
# # #         # self.working= Ping1D() 
# # #         # self.serial_port_find_arduino()  #cambiar el usb si es necesario
# # #         self.service=self.create_service(
# # #             Sonar,
# # #             "sonar",
# # #             self.sonar_callback
# # #         )
    
# # #     def serial_port_find_arduino(self):
# # #         for pinfo in serial.tools.list_ports.comports():
# # #              if pinfo.serial_number == "DM00R2J8":
# # #                 # self.working.connect_serial(pinfo.device,115200)
# # #                 self.serial_port = serial.Serial(pinfo.device)
# # #                 return pinfo.device
                
# # #         if not self.serial_port :
# # #             # No se ha encontrado el dispositivo con el número de serie especificado
# # #             # Se podría generar una excepción o imprimir un mensaje de error
# # #             raise IOError("Could not find an arduino - is it plugged in?")
# # #             # pass 

# # #     def sonar_callback(self,request,response):
# # #         # self.working = Ping1D()
# # #         # self.working.connect_serial(self.remeber, 115200)    #cambiar el usb si es necesario
        
# # #         # if self._puerto_serial:
# # #         #     # for pinfo in serial.tools.list_ports.comports():
# # #         #     #     if pinfo.serial_number == "DM00R2J8":
# # #         #     #         self.working= Ping1D()
# # #         #     #         self.working.connect_serial(pinfo.device,115200)
# # #         #     #         break
# # #         #     # if not self.working:
# # #         #     #     # No se ha encontrado el dispositivo con el número de serie especificado
# # #         #     #     # Se podría generar una excepción o imprimir un mensaje de error
# # #         #     #     raise IOError("Could not find an arduino - is it plugged in?")
# # #         #     #     # pass 

            
# # #         #     if self.working:
# # #         #             self.get_logger().info("sonar already working")
# # #         #             response.success=True
                    
                
                
# # #         #     if not self.working:
# # #         #         response.success=False
# # #         #         self.get_logger().info("sonar wasnt working")
                    
        

# # #         # return response    
# # #         if self.sonar:
# # #             self.get_logger().info("Sonar is already working")
# # #             response.success = True
# # #         else:
# # #             try:
# # #                 self.serial_port = serial.Serial(
# # #                     port=self.serial_port_find_arduino(),
# # #                     baudrate=115200,
# # #                     timeout=1.0
# # #                 )
# # #             except (serial.SerialException, IOError) as e:
# # #                 self.get_logger().error(f"Error connecting to device: {e}")
# # #                 response.success = False
# # #             else:
# # #                 self.sonar = Ping1D()
# # #                 self.sonar.connect_serial(self.serial_port)
# # #                 self.get_logger().info("Sonar connected")
# # #                 response.success = True

# # #         return response

# # # def main(args=None):
# # #     rclpy.init(args=args)
# # #     move_service= SonarServicie()
# # #     rclpy.spin(move_service)
# # #     rclpy.shutdown()
# # # if __name__=="__main__":
# # #     main()


# # from brping import Ping1D
# # import sys
# # import rclpy
# # from rclpy.node import Node
# # import serial
# # import serial.tools.list_ports
# # from custom_interfaces.srv import Sonar


# # class SonarServicie(Node):
# #     def __init__(self):
# #         super().__init__("sonar_service")
# #         self._working = None
# #         self._serial_port = None
# #         self._serial_number = "DM00R2J8"  # cambiar al número de serie correcto
# #         self._create_service()

# #     def _create_service(self):
# #         self.service = self.create_service(
# #             Sonar,
# #             "sonar",
# #             self._sonar_callback
# #         )

# #     def _find_serial_port(self):
# #         for pinfo in serial.tools.list_ports.comports():
# #             if pinfo.serial_number == self._serial_number:
# #                 self._serial_port = pinfo.device
# #                 break
# #         if not self._serial_port:
# #             raise IOError("Could not find an arduino - is it plugged in?")

# #     def _connect_ping1d(self):
# #         if not self._serial_port:
# #             self._find_serial_port()
# #         if not self._working:
# #             self._working = Ping1D()
# #             self._working.connect_serial(self._serial_port, 115200)

# #     def _disconnect_ping1d(self):
# #         if self._working:
# #             self._working.disconnect_serial()
# #             self._working = None

# #     def _sonar_callback(self, request, response):
# #         self._disconnect_ping1d()  # Cerrar cualquier conexión serial existente
# #         self._connect_ping1d()  # Abrir una nueva conexión serial

# #         if self._working:
# #             self.get_logger().info("Sonar is working")
# #             response.success = True
# #         else:
# #             self.get_logger().info("Sonar is not working")
# #             response.success = False

# #         return response


# # def main(args=None):
# #     rclpy.init(args=args)
# #     sonar_service = SonarServicie()
# #     rclpy.spin(sonar_service)
# #     sonar_service._disconnect_ping1d()  # Cerrar la conexión serial antes de salir
# #     rclpy.shutdown()


# # if __name__ == "__main__":
# #     main()


# from brping import Ping1D
# import sys
# import rclpy
# from rclpy.node import Node
# import serial
# import serial.tools.list_ports
# from custom_interfaces.srv import Sonar

# class SonarService(Node):
#     def __init__(self):
#         super().__init__("sonar_service")
#         self.working = False
#         self.serial_port = None
#         self.device_serial_number = "DM00R2J8"  # cambiar esto si es necesario

#         # crea el servicio
#         self.service = self.create_service(
#             Sonar,
#             "sonar",
#             self.sonar_callback
#         )

#         # verifica si el dispositivo está conectado en la inicialización
#         self.check_device_connection()

#     def check_device_connection(self):
#         """Verifica si el dispositivo está conectado y actualiza el estado en consecuencia."""
#         port_info = serial.tools.list_ports.grep(self.device_serial_number)
#         if port_info:
#             # el dispositivo está conectado
#             self.serial_port = port_info.device
#             self.working = True
#             self.get_logger().info("Sonar working.")
#         else:
#             # el dispositivo no está conectado
#             self.serial_port = None
#             self.working = False
#             self.get_logger().info("Sonar not working.")

#     def sonar_callback(self, request, response):
#         if self.working:
#             response.success = True
#             self.get_logger().info("Sonar already working.")
#         else:
#             response.success = False
#             self.get_logger().info("Sonar not working.")

#         return response

#     def update(self):
#         """Método que se ejecuta periódicamente para verificar el estado del dispositivo."""
#         self.check_device_connection()

# def main(args=None):
#     rclpy.init(args=args)
#     sonar_service = SonarService()

#     # crea un temporizador que se ejecutará cada 2 segundos para verificar el estado del dispositivo
#     timer_period = 2.0  # en segundos
#     timer = sonar_service.create_timer(timer_period, sonar_service.update)

#     try:
#         rclpy.spin(sonar_service)
#     except KeyboardInterrupt:
#         pass

#     sonar_service.destroy_node()
#     rclpy.shutdown()

# if __name__ == "__main__":
#     main()







# from brping import Ping1D
# import sys
# import rclpy
# from rclpy.node import Node
# import serial
# import serial.tools.list_ports
# from custom_interfaces.srv import Sonar

# class SonarService(Node):
#     def __init__(self):
#         super().__init__("sonar_service")
#         self.serial_port = None
#         self.sonar = None
#         self.serial_port_find_arduino()  # cambiar el USB si es necesario
#         self.service = self.create_service(Sonar, "sonar", self.sonar_callback)

#     def serial_port_find_arduino(self):
#         for pinfo in serial.tools.list_ports.comports():
#             if pinfo.serial_number == "DM00R2J8":
#                 self.serial_port = pinfo.device
#                 break
#         if not self.serial_port:
#             # No se ha encontrado el dispositivo con el número de serie especificado
#             # Se podría generar una excepción o imprimir un mensaje de error
#             self.get_logger().error("Could not find an arduino - is it plugged in?")
#             return False
#         return True

#     def sonar_callback(self, request, response):
#         if not self.serial_port_find_arduino():
#             response.success = False
#             response.message = "Sonar not working - arduino not found"
#             return response
        
#         if not self.sonar:
#             try:
#                 # self.sonar = Ping1D(self.serial_port)
#                 self.sonar = Ping1D()
#                 self.sonar.connect_serial(self.serial_port, 115200)
#             except Exception as e:
#                 self.get_logger().error(f"Could not initialize sonar: {e}")
#                 response.success = False
#                 response.message = "Sonar not working - initialization error"
#                 return response

        
#         # try:
#         #     self.serial_port_find_arduino()  # Busca el dispositivo y conecta al sonar
#         # if self.sonar and self.sonar.get_ping_enable():
#         #     self.get_logger().info("Sonar is working")
#         #     response.success = True
#         # else:
#         #     self.get_logger().info("Sonar is not working")
#         #     response.success = False
       

        




#         try:
#             self.sonar.initialize()
#         except Exception as e:
#             self.get_logger().error(f"Could not initialize sonar: {e}")
#             response.success = False
#             response.message = "Sonar not working - initialization error"
#             return response

#         if not self.sonar.get_ping_enable():
#             self.get_logger().error("Sonar not working - no response from device")
#             response.success = False
#             response.message = "Sonar not working - no response from device"
#             return response
        
#         self.get_logger().info("Sonar working")
#         response.success = True
#         response.message = "Sonar working"
#         return response    





# def main(args=None):
#     rclpy.init(args=args)
#     sonar_service = SonarService()


#     try:
#         rclpy.spin(sonar_service)
#     except KeyboardInterrupt:
#         pass

#     sonar_service.destroy_node()
#     rclpy.shutdown()



# if __name__ == "__main__":
#     main()


# from brping import Ping1D
# import sys
# import rclpy
# from rclpy.node import Node
# import serial
# import serial.tools.list_ports
# from custom_interfaces.srv import Sonar

# class SonarServicie(Node):
#     def __init__(self):
#         super().__init__("sonar_service")
#         self.remeber = None
#         self._puerto_serial = None
#         self.working = None
#         self.serial_port_find_arduino()
#         self.service = self.create_service(
#             Sonar,
#             "sonar",
#             self.sonar_callback
#         )
    
#     def serial_port_find_arduino(self):
#         for pinfo in serial.tools.list_ports.comports():
#             if pinfo.serial_number == "DM00R2J8":
#                 self._puerto_serial = serial.Serial(pinfo.device)
#                 self.remeber = pinfo.device
#                 break
#         if not self._puerto_serial :
#             raise IOError("Could not find an arduino - is it plugged in?")
    
#     def sonar_callback(self, request, response):
#         self.working = Ping1D()
#         try:
#             self.working.connect_serial(self.remeber, 115200)
#         except Exception as e:
#             response.success = False
#             self.get_logger().info("sonar not working: %s" % e)
#             return response

#         if self.working.get_ping_enable():
#             self.get_logger().info("sonar already working")
#             response.success = True
#         else:
#             response.success = False
#             self.get_logger().info("sonar not working")

#         return response
    
# def main(args=None):
#     rclpy.init(args=args)
#     move_service = SonarServicie()
#     rclpy.spin(move_service)
#     rclpy.shutdown()
    
# if __name__ == "__main__":
#     main()


# from brping import Ping1D
# import sys
# import rclpy
# from rclpy.node import Node
# import serial
# import serial.tools.list_ports
# from custom_interfaces.srv import Sonar

# class SonarServicie(Node):
#     def __init__(self):
#         super().__init__("sonar_service")
#         self.remember = None
#         self._puerto_serial = None
#         self.working = None
#         self.connected = False
#         self.service = self.create_service(
#             Sonar,
#             "sonar",
#             self.sonar_callback
#         )
    
#     def serial_port_find_arduino(self):
#         for pinfo in serial.tools.list_ports.comports():
#             if pinfo.serial_number == "DM00R2J8":
#                 self._puerto_serial = serial.Serial(pinfo.device)
#                 self.remember = pinfo.device
#                 break
#         if not self._puerto_serial:
#             raise IOError("Could not find an arduino - is it plugged in?")
    
#     def sonar_callback(self, request, response):
#         self.working = Ping1D()
#         try:
#             self.working.connect_serial(self.remember, 115200)
#         except Exception as e:
#             response.success = False
#             self.get_logger().info("sonar not working: %s" % e)
#             return response

#         if self.working.get_ping_enable():
#             self.get_logger().info("sonar already working")
#             response.success = True
#         else:
#             response.success = False
#             self.get_logger().info("sonar not working")

#         return response

#     def check_serial_port(self):
#         if not self.connected:
#             for pinfo in serial.tools.list_ports.comports():
#                 if pinfo.device == self.remember:
#                     self.connected = True
#                     self.get_logger().info("USB device connected")
#                     return
#             self.get_logger().info("USB device disconnected")
#         else:
#             found = False
#             for pinfo in serial.tools.list_ports.comports():
#                 if pinfo.device == self.remember:
#                     found = True
#                     break
#             if not found:
#                 self.connected = False
#                 self.get_logger().info("USB device disconnected")

# def main(args=None):
#     rclpy.init(args=args)
#     move_service = SonarServicie()
#     try:
#         move_service.serial_port_find_arduino()
#     except IOError as e:
#         move_service.get_logger().info("Failed to find the serial port: %s" % e)
#         rclpy.shutdown()
#         return

#     while rclpy.ok():
#         rclpy.spin_once(move_service, timeout_sec=0.1)
#         move_service.check_serial_port()
        
#     move_service.get_logger().info("Exiting")
#     rclpy.shutdown()
    
# if __name__ == "__main__":
#     main()


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

    def monitor_usb_port(self):
        while True:
            arduino_ports = [
                p.device
                for p in serial.tools.list_ports.comports()
                if p.serial_number == "DM00R2J8"
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
