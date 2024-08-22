Using optical character recognition to convert text to morse code 

Tools used:
  Esp 32 cam
  Esp 8266
  Vibration Motor
  
Software Used:
  Arduino IDE
  Python :
    Pytesseract 
    OpenCV

We used the example arduino script to upload the esp32 cam video an IP. We grabbed the video feed in python and use pytesseract and opencv to get each character . We then used pyserial to send that data to an esp8266 which was connected to the vibration motor that generated the output morse code
