import sys
import rclpy
from rclpy.node import Node
from custom_interfaces.srv import Sonar

class Sonarasync(Node):
    def __init__(self):
        super().__init__("sonar_client_async")
        self.client=self.create_client(Sonar,"sonar")
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("service not avaliable,waiting again....")
        
    def send_request(self):
        request = Sonar.Request()
        # request.value= bool(sys.argv[1])
        self.future=self.client.call_async(request)



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
                    f"Result of check {response.message}"
                )
                move_client.get_logger().info(
                    f"Result of check {response.success}"
                )
                
            break
        move_client.destroy_node()
        rclpy.shutdown()

if __name__=="__main__":
    main()