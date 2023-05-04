import sys
import rclpy
from rclpy.node import Node
from custom_interfaces.srv import Sonar , SerialNumber


#Este script realiza una simple peticion al servicio para ver la respuesta del servicio, imprime por pantalla los resultados de la peticion
 
class Sonarasync(Node):
    def __init__(self):
        super().__init__("sonar_client_async")
        self.client=self.create_client(SerialNumber,"get_serial_number")
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("service not avaliable,waiting again....")
 # Funcion para la realizacion de la peticion            
    def send_request(self):
        request_serial = SerialNumber.Request()
        request_serial.serial_number = str(sys.argv[1])
        self.future=self.client.call_async(request_serial)



def main(args=None):
    rclpy.init(args=args)
    move_client= Sonarasync()
    move_client.send_request()

    while rclpy.ok():
        rclpy.spin_once(move_client)
        if move_client.future.done():
            try:
                response= move_client.future.result()
            except Exception as e:
                move_client.get_logger().info(
                    f"Service call failes {e}"
                )
            else:
                move_client.get_logger().info(
                    f"Result of check {response.success}"
                )
                
            break
        move_client.destroy_node()
        rclpy.shutdown()

if __name__=="__main__":
    main()