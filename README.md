# MyRaspberryPi
This is my Raspberry-dedicated repository, with all the projects and tests I'll do on it!

## Setup:
In case I forget something about the first setup or something about the Raspberry Pi OS I'll write a small guide (**ATTENTION**: I'm using a Raspberry Pi 4 model B with 2 GB of RAM, with other models the setup MAY be different):

- Control integrity and clean components if dirty (with A LOT of caution and on your own risk);
- Install Raspberry imager on your PC;
- Install Raspberry Pi OS on a micro SD, better if during configuration you set Raspberry Pi Connect and put your router informations so it automatically connects to it after the setup (without formatting, if invisible in file manager it's a good sign, Raspberry imager will find it);
- When finished, Raspberry imager will automatically remove (not fisically) the micro SD safely without it having conflicts with windows files (as Raspberry Pi OS is a derivate of Linux and Windows doesn't recognize Linux's files);
- Remove fisically the micro SD from the PC;
- Put it in the Raspberry before powering it on;
- Power the Raspberry on (remember to check the voltage and amperage of the charger);
- If you configured Raspberry Pi Connect and your router informations, you're in! No need to do complicate things;
- If you don't, it's a little bit harder...

## Connect to your Raspberry Pi (without imager)
### On displays:
Just wait for the setup of the OS to be finished and connect to your router using it's password
### Headless (without using monitors or other types of displays):
You need to connect to Wi-Fi, that's for sure the first thing to do (you could do that with a LAN cable or by commands on your micro SD), then, to connect to your PC use SSH, if you didn't enable SSH during the configuration too, well, you're stupid. What? You really expected to connect into it with magic tricks? You now have to delete everything inside the micro SD and reinstall the OS again because it's impossible to connect to a headless Raspberry without SSH enabled.

## Conclusion:
Good! Now you should be in, whether by Raspberry Pi Connect or by the other methods. After the setup, you can access the display by Raspberry Pi Connect if you're going headless. Now you have a very useful second mini PC for all your projects and tests, or it could be used to learn how OS like Linux and derivates (such as Raspberry Pi OS itself) work or for endless other types of uses. The possibilities are truly infinite with this small yet powerful tool!
