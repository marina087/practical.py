from gtts import gTTS



def textTOAudio(str):
     audio = gTTS(str)
     audio.save('example.mp3')
     

textTOAudio ('this audio is generated using TTS module of by marina ') 