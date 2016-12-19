# alarm-cli
Linux CLI App for Simple Alarms

![cli](https://i.imgur.com/JriT6Mv.png "Terminal Interface")

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
#### If you are on Arch Linux:
```
wget https://gist.githubusercontent.com/SajeOne/a14763247157f02c6ad82006f6104adf/raw/2921f115d3902f64e11ede733897f3b170e3b6fc/alarm-cli-pkgbuild -O PKGBUILD
makepkg -irs
```

#### Otherwise:

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
