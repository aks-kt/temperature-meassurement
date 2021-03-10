import board
import adafruit_mlx90614 as mlx
import busio as io

i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
sensor = mlx.MLX90614(i2c)

obj_temp = "{:.2f}".format(sensor.object_temperature)
with open('test.txt', 'w', encoding='utf-8') as f:
	f.write("Nhiet do: {} do C".format(obj_temp))
	f.close()
print("Nhiet do: ", obj_temp, " do C")
