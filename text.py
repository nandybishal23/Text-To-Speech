from logging import StrFormatStyle
from gtts import gTTS  

import os 
  
given_text = 'Hey Bishal Good Morning. Hope you have a nice Good Day'  

language = 'en'  

output = gTTS(given_text,lang=language)   

output.save("result_output.mp3") 

os.system("start result_output.mp3") 
