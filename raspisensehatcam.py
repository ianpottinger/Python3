import picamera, sense_hat, time, random

camera = picamera.PiCamera()
sensehat = sense_hat.SenseHat()


camera.capture('image.jpg')

camera.start_preview() #Ctrl-D to end
camera.stop_preview()

camera.sharpness = 0
camera.contrast = 0
camera.brightness = 50
camera.saturation = 0
camera.ISO = 0
camera.video_stabilization = True
camera.exposure_compensation = 0
camera.exposure_mode = 'auto'
camera.meter_mode = 'average'
camera.awb_mode = 'auto'
camera.image_effect = 'none'
camera.color_effects = None
camera.rotation = 0
camera.hflip = False
camera.vflip = False
camera.crop = (0.0, 0.0, 1.0, 1.0)
time.sleep(5)

camera.capture('image1.jpg')
time.sleep(5)
camera.capture('image2.jpg')

camera.start_preview()

for i in range(100):
    camera.brightness = i
    sleep(0.2)

camera.start_recording('video.h264')
sleep(5)
camera.stop_recording()





x = 4
y = 5
r = 19
g = 180
b = 230
sensehat.set_pixel(x, y, r, g, b)


while True:
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    sensehat.set_pixel(x, y, r, g, b)
    time.sleep(0.1)


