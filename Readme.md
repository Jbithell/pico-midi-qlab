# USB Midi Trigger Buttons for Pi Pico

CircuitPython project that creates a go-button trigger for QLab/other Midi triggered sources. 

## Development 

Press and hold BootSel on the Pico then insert the microusb, enabling and drag the .uf2 firmware file onto the drive. Once this is done loaded, you'll need to drag the lib folder and the boot.py and code.py files across. The device will reboot and then run. 

Because this project disables the file storage system on the Pico, if you want to make further changes you'll need to install the flash_nuke.uf2 firmware first. 