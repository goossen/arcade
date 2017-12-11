#arcade

A RetroPie based arcade cabinet.

## Basics
An RPi running the RetroPie distribution is housed in a homemade arcade cabinet.  The RPi also controls the lights, monitor and speaker, using a PIR motion sensor and relay.

![Outside](https://raw.github.com/goossen/arcade/master/arcade-out.jpg)

### Cabinet Design and Build
The cabinet was build using 3/4" MDF, and the design was based on available templates.  See http://www.koenigs.dk/mame/eng/draw.htm.  The joystick and buttons are connected to a RPi USB input.  The cabinet also houses a 22" widescreen led monitor and computer speakers.  It was necessary to add a ground loop isolater to reduce speaker feedback.

![Insides](https://raw.github.com/goossen/arcade/master/arcade-in.jpg)

### Motion Sensing
The motion_sensing.py Python script reads from a PIR sensor when motion is detected.  If no motion is sensed for 10 minutes, then the power to the monitor, speaker and led strip lights is turned off.
