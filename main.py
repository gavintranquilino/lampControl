from gpiozero import DigitalOutputDevice
from time import sleep
from discord import Client

base = DigitalOutputDevice(17)


class Lamp:
    def __init__(self):
        self.delay_time = 0.1
        self.state = False

    def change_state(self, switch):
        if switch:
            base.on()
        elif not switch:
            base.off()
        else:
            pass


lamp = Lamp()
client = Client()


@client.event
async def on_ready():
    print("Logged in")


@client.event
async def on_message(message):

    if message.content == "lamp on":
        lamp.state = True
        lamp.change_state(lamp.state)
        await message.channel.send("Light turned on")
        print("Light turned on")

    elif message.content == "lamp off":
        lamp.state = False
        lamp.change_state(lamp.state)
        await message.channel.send("Light turned off")
        print("Light turned off")

    if (
        "<@450414958421868554>" in message.content
        or "<@!450414958421868554>" in message.content
    ):
        await message.channel.send("Flashing light")
        print("Light turned on")

        for i in range(4):
            if lamp.state:
                lamp.change_state(False)
                sleep(lamp.delay_time)
                lamp.change_state(True)
                sleep(lamp.delay_time)
            else:
                lamp.change_state(True)
                sleep(lamp.delay_time)
                lamp.change_state(False)
                sleep(lamp.delay_time)


if __name__ == "__main__":
    with open("token.0", "r") as f:
        token = f.read()
        client.run(token)
