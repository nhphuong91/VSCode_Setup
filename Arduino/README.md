For arduino IDE Linux installation instruction, see [here](https://www.arduino.cc/en/Guide/Linux)

# Fix "Error opening serial port"
```sh
ls -l /dev/ttyACM*
--> crw-rw---- 1 root dialout 188, 0 5 apr 23.01 ttyACM0

sudo usermod -a -G dialout <username>
```

# Fix IDE desktop icon not working
```sh
sudo chown <username> /home/<username>/Desktop/arduino-arduinoide.desktop
```
Then, double click icon to run IDE once & accept whatever it asks

