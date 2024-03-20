import paho.mqtt.client as mqtt
import time

# Định nghĩa các hàm callback khi kết nối thành công và nhận tin nhắn
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Kết nối thành công!")
        client.subscribe("topic/test")  # Đăng ký nhận tin nhắn từ topic "topic/test"
    else:
        print("Kết nối không thành công. Mã trạng thái:", rc)

def on_message(client, userdata, msg):
    print("Nhận được tin nhắn từ topic", msg.topic + ": " + str(msg.payload.decode()))

# Khởi tạo một client MQTT
client = mqtt.Client(client_id="your_client_id")  # Thay "your_client_id" bằng một định danh duy nhất cho client của bạn

# Thiết lập các hàm callback
client.on_connect = on_connect
client.on_message = on_message

# Kết nối tới broker (thay đổi địa chỉ broker và cổng tùy vào cấu hình của bạn)
client.connect("broker.example.com", 1883, 60)

# Bắt đầu vòng lặp để duy trì kết nối và xử lý tin nhắn
client.loop_start()

# Gửi một số tin nhắn đến broker
for i in range(5):
    client.publish("topic/test", "Message " + str(i+1))
    time.sleep(1)  # Đợi 1 giây giữa các lần gửi tin nhắn

# Đợi một chút trước khi thoát
time.sleep(2)

# Dừng client và đóng kết nối
client.loop_stop()
client.disconnect()
