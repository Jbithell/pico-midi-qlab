# Based on the template copyright 2021 Liz Clark for Adafruit Industries - https://learn.adafruit.com/raspberry-pi-pico-led-arcade-button-midi-controller-fighter/circuitpython-code-walkthrough
# James Bithell February 2024
import board
import digitalio
import usb_midi
import adafruit_midi
import time
from adafruit_midi.note_on          import NoteOn
from adafruit_midi.note_off         import NoteOff

# Config 
buttons_pins = [board.GP6, board.GP8]
leds_pins = [board.GP7, board.GP9]
midi_notes = [60, 61]

#  MIDI setup as MIDI out device
midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

buttons = []
button_states = []
leds = []
for pin in buttons_pins:
    this_pin = digitalio.DigitalInOut(pin)
    this_pin.direction = digitalio.Direction.INPUT
    this_pin.pull = digitalio.Pull.UP
    buttons.append(this_pin)
    button_states.append(this_pin.value)
for pin in leds_pins:
    this_pin = digitalio.DigitalInOut(pin)
    this_pin.direction = digitalio.Direction.OUTPUT
    this_pin.value = True
    leds.append(this_pin)

while True:
    for i in range(len(buttons)):
        button = buttons[i]
        led = leds[i]
        #  if button is pressed...
        if button.value and button_states[i] is True:
            midi.send(NoteOn(midi_notes[i], 120))
            led.value = False
            button_states[i] = False
        #  if the button is released...
        if not button.value and button_states[i] is False:
            midi.send(NoteOff(midi_notes[i], 120))
            led.value = True
            button_states[i] = True
