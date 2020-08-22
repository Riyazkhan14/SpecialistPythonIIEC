import pyttsx3
import os
engine = pyttsx3.init()
engine.setProperty('rate', 120)    
engine.setProperty('volume', 2)
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', en_voice_id)

while True:
                
               pyttsx3.speak("Welcome to Windows software opener tool.\nHere you will be asked to choose your choice to open a program.\nPress 1 for Network Properties\nPress 2 for Notepad\nPress 3 for Calculator\nPress 4 for Microsoft Paint")

               x = int(input("Enter your choice to run a program : "))

               pyttsx3.speak(" you have pressed" )
               pyttsx3.speak(str(x ))
               if x == 1 or x==2 or x==3 or x == 4 :
                   pyttsx3.speak("we are trying to open")
               else:
                   pyttsx3.speak(str(x))
                   pyttsx3.speak("This number is not avaible in Menu")

               if int (x )== 1:
                   pyttsx3.speak("Network properties" )
                   pyttsx3.speak("Please Wait" )
               elif (x )== 2:
                   pyttsx3.speak("Windows Notepad" )
                   pyttsx3.speak("Please Wait" )
               elif (x ) == 3:
                   pyttsx3.speak("Windows Calcuator" )
                   pyttsx3.speak("Please Wait" )
               elif (x)== 4:
                  pyttsx3.speak("Microsoft Paint" )
                  pyttsx3.speak("Please Wait" )
               
               else:
                   pyttsx3.speak("Kindly choose correct number " )
                

               if int(x)== 1:
                   os.system("ncpa.cpl" )
                   break
               elif int(x)== 2:
                   os.system("notepad")
                   break
               elif int (x )== 3:
                   os.system ("calc")
                   break
               elif int (x)== 4:
                   os.system ("mspaint")
                   break
               else:
                   pyttsx3.speak("Would you like to add new  number and programe")
          

    
