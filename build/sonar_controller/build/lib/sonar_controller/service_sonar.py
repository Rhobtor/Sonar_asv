
from brping import Ping1D
import sys
import rclpy
from rclpy.node import Node
import serial
import serial.tools.list_ports
from custom_interfaces.srv import Sonar

class SonarServicie(Node):
    def __init__(self):
        super().__init__("sonar_service")
        self.remeber= None
        self._puerto_serial = None
        # self.working= Ping1D() 
        self.serial_port_find_arduino()  #cambiar el usb si es necesario
        self.service=self.create_service(
            Sonar,
            "sonar",
            self.sonar_callback
        )
    
    def serial_port_find_arduino(self):
        for pinfo in serial.tools.list_ports.comports():
             if pinfo.serial_number == "DM00R2J8":
                # self.working.connect_serial(pinfo.device,115200)
                self._puerto_serial = serial.Serial(pinfo.device)
                self.remeber= pinfo.device
                break
        if not self._puerto_serial :
            # No se ha encontrado el dispositivo con el número de serie especificado
            # Se podría generar una excepción o imprimir un mensaje de error
            raise IOError("Could not find an arduino - is it plugged in?")
            # pass 

    def sonar_callback(self,request,response):
        self.working = Ping1D()
        self.working.connect_serial(self.remeber, 115200)    #cambiar el usb si es necesario
        
        if self._puerto_serial:
            # for pinfo in serial.tools.list_ports.comports():
            #     if pinfo.serial_number == "DM00R2J8":
            #         self.working= Ping1D()
            #         self.working.connect_serial(pinfo.device,115200)
            #         break
            # if not self.working:
            #     # No se ha encontrado el dispositivo con el número de serie especificado
            #     # Se podría generar una excepción o imprimir un mensaje de error
            #     raise IOError("Could not find an arduino - is it plugged in?")
            #     # pass 

            
            if self.working:
                    self.get_logger().info("sonar already working")
                    response.success=True
                    
                
                
            if not self.working:
                response.success=False
                self.get_logger().info("sonar wasnt working")
                    
        

        return response    
        

def main(args=None):
    rclpy.init(args=args)
    move_service= SonarServicie()
    rclpy.spin(move_service)
    rclpy.shutdown()
if __name__=="__main__":
    main()