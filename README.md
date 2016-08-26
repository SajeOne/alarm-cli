# alarm-cli
Linux CLI App for Simple Alarms

![cli](https://u.teknik.io/0g6fE.png "Terminal Interface")

## About
alarm-cli is a python based CLI alarm program designed for Linux(Other OS' not tested). It features a simple interface for creating alarms allowing for quick reminders to be replaced without getting off track of your work. This was the entire design principle of alarm-cli, an app I could use to set reminders quickly and forget I had set them.

# Commands
`Ex. alarm-cli <command>`
```
set - Set a new alarm
list - Show list of currently set alarms
del - delete an alarm
clear - delete alarms that have passed
daemon - start alarm watcher
stop - stops alarm watcher
```

# Installation
#### If you are on Arch Linux you can use the PKGBUILD to install alarm-cli (makepkg -irs)

#### Otherwise..

```
git clone https://github.com/SajeOne/alarm-cli.git
cd alarm-cli
python setup.py install --optimize=1 # May require root privileges (sudo)
alarm-cli -h
```

## Third Party Licenses

`alarm.wav`
Credit to [Thoribass](https://soundcloud.com/thoribass)

https://creativecommons.org/licenses/by/3.0/
