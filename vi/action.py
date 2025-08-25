import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

user_data=speech_to_text.speech_to_text()

if "what is your name" in user_data:
    text_to_speech.text_to_speech("My name is Virtual Assistant")

elif "hello" in user_data or "hye" in user_data:
    text_to_speech.text_to_speech("hey , sir how can i help you")

elif "good morning" in user_data:
    text_to_speech.text_to_speech("good morning sir")

elif "time now" in user_data:
    current_time=datetime.datetime.now()
    Time=(str)(current_time)+"Hour:",(str)(current_time.minute)+"Minute"
    text_to_speech.text_to_speech(Time)

elif "shutdown" in user_data:
    text_to_speech.text_to_speech("ok sir")

elif "play music" in user_data:
    webbrowser.open("https://gaana.com/")
    text_to_speech.text_to_speech("gaana.com is now ready for you")

elif "play youtube" in user_data:
    webbrowser.open("https://youtube.com/")
    text_to_speech.text_to_speech("Youtube is now ready for you")

elif "open udemy" in user_data:
    webbrowser.open("https://google.com/")
    text_to_speech.text_to_speech("google is now ready for you")

elif "weather" in user_data:
    ans=weather.weather()
    text_to_speech.text_to_speech(ans)


else:
    text_to_speech.text_to_speech("I'm not able to understand")
