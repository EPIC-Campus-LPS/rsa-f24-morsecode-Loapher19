from playsound import playsound
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)
# Bit overcomplicated but much more modular, applicable in the real world, and it seemed more fun then doing it normally
# well not too applicable in the real world cuz it still uses my actual filepaths but still :] you think i know how to find those?
# Maybe in the future if i ever release this publicly ill either get sounds from the cloud or have the user provide their own filepaths
class Morse:
    def __init__(self, morsestring):
        self.morsestring = morsestring
    
    def __str__(self):
        return self._morsestring
        
    @property
    def morsestring(self):
        return self._morsestring
    
    @morsestring.setter
    def morsestring(self, morsestring):
        for i in morsestring:
            if i not in [".","-"," ","/"]:
                raise ValueError("Invalid character in morse code.")
        self._morsestring = morsestring
    
    @classmethod
    def play(cls, morse):
        morsestring = str(morse)
        for i in morsestring:
            if i == ".":
                playsound('/home/liams/Downloads/morseshort.mp3',False)
                time.sleep(0.3)
            elif i == "-":
                playsound('/home/liams/Downloads/morselong.mp3',False)
                time.sleep(0.3)
            elif i in [" ","/"]:
                time.sleep(0.3)
            else:
                raise ValueError("Tried to play nonexistent character in morse code")
    
    @classmethod
    def translate(cls, eng):
        morse = ""
        table = Morse.morsetable()
        for i in eng:
            try:
                morse += table[i]
                morse += " "
            except KeyError:
                raise ValueError("Tried to translate an unsupported character to morse code.")
        return Morse(morse)
    
    @classmethod
    def morsetable(cls):
        table = {
            " ": "/",
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            "0": "-----",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----."
        }
        return table
    
Morse.play(Morse.translate("HYMENOPUS CORONATUS"))