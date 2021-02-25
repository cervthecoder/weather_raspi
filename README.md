# weather_raspi

My app for displaying info of humidity and temperature from my raspi and dht11 sensor using django and python, also implementing outside temperature, humidity and pressure.

## What you need
1. Raspbeerry pi 0-4
![](https://images-na.ssl-images-amazon.com/images/I/91zSu44%2B34L._SL1500_.jpg)
2. DHT11 or DHT22 sensor
![](https://lankatronics.com/image/cache/catalog/Sub%20categories/Temperature%20Sensors%20and%20Modules/DHT11-2-700x700.jpg)
3. Bread board and jumper cables or you can solder it directly on raspberry pi.
## Step 1.
You need to download the code from github.
```
git clone https://github.com/cervthecoder/weather_raspi.git
```
## Step 2.
Donwload needed libraries for python.
```
pip3 install django
pip3 install Adafruit_DHT
```
## Step 3.
Connect the sensor to raspberry pi (**GPIO port = 4**).s
![](https://camo.githubusercontent.com/2a3803a00eb6be6308ab309d6f91b311a3155e109e2b6f93d4c888c868008d0d/68747470733a2f2f7261772e6769746875622e636f6d2f726e696576612f506c6179696e672d776974682d53656e736f72732d2d2d5261737062657272792d50692f6d61737465722f736368656d65315f44485431312e706e67)

For more info about ports on your raspberry pi visit the <a href="https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/README.md">documentation page</a>

## Step 4.
run this command in /weather_raspi directory and go to localhost in your browser.
```
python3 manage.py runserver
```
You should see something like this.
![alt text](https://github.com/cervthecoder/github_images/blob/master/Screenshot%202020-08-02%20at%2017.43.32.png)

