# countdown_timer

A python3 and tkinter based countdown timer for work interval timing

## Prerequisites

Simpleaudio library
<https://simpleaudio.readthedocs.io/en/latest/>

install using pip: `pip install simpleaudio`

## Sound sources

+ klaxon.wav <https://commons.wikimedia.org/wiki/File:WWII_submarine_dive_klaxon.ogg?uselang=en-gb>
+ tick.wav <https://commons.wikimedia.org/wiki/File:Clock_ticking.ogg> - edited using Audacity
+ brown_noise.wav - created using Audacity's generate noise function

## References

* https://tkdocs.com/shipman/
* https://tkdocs.com/tutorial/morewidgets.html#progressbar
* https://www.pythontutorial.net/tkinter/tkinter-progressbar/

## TODO

* [ ] convert to OOP
    - to enable making more timers easily
* [ ] make the brown noise wav smaller
* [ ] make it prettier
    * [ ] make all colours coherent
    * [ ] change all tk widgets to ttk to make it prettier
* [ ] change clock font to a digital clock font
* [ ] add json files for the settings so that the noises and default times can be changed
* [ ] add menus for tick noise and end signal options
* [ ] add volume controls for each noise
* [ ] change colours of buttons etc to visually fit together better
    * [ ] can i use ttk for this?
* [x] add progress bar
    * https://tkdocs.com/tutorial/morewidgets.html#progressbar
* [ ] can progress bar be put in title, or similar?
* [ ] add count up mode, a la the dr seuss timer
* [x] make jump to front of screen when timer ends

## Count Up Timer
When press start and time is 0, start counting upwards until 99:99:99
