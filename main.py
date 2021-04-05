from logging import StrFormatStyle
from gtts import gTTS  

import os 
  
given_text = ''  

with open("example.txt","r") as file:
    for line in file:
        given_text=given_text + line

language = 'en'  

output = gTTS(given_text,lang=language)   

output.save("result.mp3") 

os.system("start result.mp3") 