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
```shell
git clone https://github.com/cervthecoder/weather_raspi.git
```
## Step 2.
Create virtualenviroment and donwload needed libraries for python.
```shell
cd weather_raspi
virtualenv weatherenv
source weatherenv/bin/activate
pip3 install django
pip3 install Adafruit_DHT
pip3 install requests
```
## Step 3.
Connect the sensor to raspberry pi (**GPIO port = 4**).s
![](https://camo.githubusercontent.com/2a3803a00eb6be6308ab309d6f91b311a3155e109e2b6f93d4c888c868008d0d/68747470733a2f2f7261772e6769746875622e636f6d2f726e696576612f506c6179696e672d776974682d53656e736f72732d2d2d5261737062657272792d50692f6d61737465722f736368656d65315f44485431312e706e67)

For more info about ports on your raspberry pi visit the <a href="https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/README.md">documentation page</a>

## Step 4.
run this command in /weather_raspi directory and go to localhost in your browser.
```shell
python3 manage.py runserver
```
You should see something like this.
![](https://github.com/cervthecoder/github_images/blob/master/Screenshot%202020-08-02%20at%2017.43.32.png)

## Step 5.
Install apache.
```shell
sudo apt update
sudo apt install apache2 -y
sudo apt-get install apache2-dev -y
sudo apt-get install apache2-mpm-worker -y
sudo apt-get install libapache2-mod-wsgi-py3 
```

## Step 6.
Configure apache. In your home directory `cd`.
```shell
nano /etc/apache2/sites-available/000-default.conf
```
Add this to the end of the file.

```conf  
 Alias /static /home/pi/weather_raspi/static
    <Directory /home/weather_raspi/weather/static> 
        Require all granted
    </Directory>
  
    <Directory /home/pi/weather_raspi/weather_raspi>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>
  
    WSGIDaemonProcess weather_raspi python-path=/home/pi/weather_raspi python-home=/home/pi/weather_raspi/weatherenv
    WSGIProcessGroup weather_raspi
    WSGIScriptAlias / /home/pi/weather_raspi/weather_raspi/wsgi.py
</VirtualHost>
  
# vim: syntax=apache ts=4 sw=4 sts=4 sr noet
```

## Step 7.
Give apache acces to our database and GPIO pins
```shell
chmod g+w ~/weather_raspi/db.sqlite3
chmod g+w ~/weather_raspi
sudo chown :www-data db.sqlite3
sudo chown :www-data ~/weather_raspi
sudo usermod -a -G gpio www-data
```

## Step 8.
Restart apache.
```
sudo service apache2 restart
```

## Step 9.
Make your page accessible from another computer. (only on your local network)
First you need to find out what is your IP adress.
```shell
ping raspberrypi.local
PING raspberrypi.local (192.168.99.99): 56 data bytes
```
`^C` (to exit the "pinging")
```shell
nano weather_raspi/weather_raspi/settings.py
```
And change this line...
```python
ALLOWED_HOSTS=[]
```
Insert there yout IP adress
```python
ALLOWED_HOSTS=['192.168.99.99']
```
To give static to apache2 (in weather_raspi directory)
```shell
python3 manage.py collectstatic
```

Now you should be able to acces the website on local network on `http://ip_adress`
![](https://github.com/cervthecoder/github_images/blob/master/Screenshot%202021-03-15%20at%2017.55.28.png?raw=true)
