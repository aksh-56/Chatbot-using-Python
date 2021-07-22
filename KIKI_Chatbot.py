import pyttsx3
import datetime   
import speech_recognition as sr
import wikipedia
import webbrowser
import pyaudio
engine= pyttsx3.init('sapi5')        
voices= engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    return 
def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning mam!!")
    elif hour>=12 and hour<16:
        speak("Good afternoon mam!!")
    else:
        speak("Good evening mam!! ")
    speak("kiki to your service!,what can i do for you? ")
    return
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening.....")
        try:
            audio=r.listen(source)
            text=r.recognize_google(audio,language="en-in")
            speak('you said,'+text)
            
        except:
            speak('pardon, please say again')
            text=takecommand()
    return text
    
def main():
    wishMe()
#if name == 'main':
#  main()
    while True:
        text=takecommand().lower()
        speak('you said,'+text)
        if 'wikipedia' in text:
          speak ("Searching wikipedia!!.....")    
          text=text.replace("wikipedia"," ")
          results=wikipedia.summary(text,sentences=2)
          speak("according to wikipedia")
          speak(results)
          print(results)
        elif 'open youtube' in text:
           webbrowser.open("youtube.com")  
        elif 'open google' in text:
           webbrowser.open("google.com")  
        elif 'open facebook' in text:
           webbrowser.open("facebook.com") 
        elif 'open netflix' in text:
           webbrowser.open("netflix.com")     
           
        elif 'time' in text:
            strtime=datetime.datetime.now().strftime("%H hours;%M minits and ;%S seconds")
            speak("mam,the time is" +strtime)
        elif 'exit' in text:
            speak("SEE you soon!; GOOD BYE")
            break
    
if __name__ == '__main__':
 main()