import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import webbrowser
from pyzbar.pyzbar import decode

class QRScannerNode(Node):
    def __init__(self):
        super().__init__('qr_scanner_node')
        
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10)
        
        self.br = CvBridge()
        self.link_opened = False
        
        self.get_logger().info("QR Scanner Node started. Looking for QR codes...")

    def image_callback(self, msg):
        frame = self.br.imgmsg_to_cv2(msg, "bgr8")
        
        # Detect and decode the QR code using PyZbar
        decoded_objects = decode(frame)
        
        for obj in decoded_objects:
            data = obj.data.decode('utf-8')
            self.get_logger().info(f"QR Code Scanned! Text: {data}")
            
            # Open the browser only once if it's a valid link
            if not self.link_opened and data.startswith("http"):
                self.get_logger().info("Opening link in web browser...")
                webbrowser.open(data)
                self.link_opened = True
        
        cv2.imshow("Robot Camera View", frame)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    qr_scanner = QRScannerNode()
    
    try:
        rclpy.spin(qr_scanner)
    except KeyboardInterrupt:
        pass
        
    qr_scanner.destroy_node()
    cv2.destroyAllWindows()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
