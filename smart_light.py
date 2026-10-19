print("welcome to python")

class SmartLight:
    def __init__(self):
        self.is_on = False
        self.brightness = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_brightness(self, brightness):
        self.brightness = brightness

light = SmartLight()

light.turn_on()
light.set_brightness(75)

print("Light on:", light.is_on)
print("Brightness:", light.brightness)

light.turn_off()
print("Light on:", light.is_on)
