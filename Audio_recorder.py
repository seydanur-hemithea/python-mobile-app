# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 14:10:35 2025

@author: Seyda Nur
"""
import kivy
import wave
import pyaudio

from threading import Thread

from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.uix.relativelayout import MDRelativeLayout

from kivy.core.window import Window
Window.size=(350,300)
class AudioRecorderApp(MDApp):
    def record_audio(self):
        ### set recording parameter
        audio=pyaudio.PyAudio()
        FORMAT=pyaudio.paInt16#-32768 - +32767
        CHANNELS=1
        RATE=44100
        CHUNK=1024
        ##open stream for recording
        stream=audio.open(format=FORMAT,channels=CHANNELS,rate=RATE,
                          input=True,frames_per_buffer=CHUNK)
        #create wave file for saving recording
        wf=wave.open("recording.wav","wb")
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        #start the recording
        self.record_button.text="Recording..."
        self.recording_active=True
        
        while self.recording_active:
            data =stream.read(CHUNK)
            wf.writeframes(data)
        #stop recording
        self.record_button.text="Record"
        stream.stop_stream()
        stream.close()
        audio.terminate()
        wf.close()
        print("Recording Complated!")

    def start_recording(self,event):
        ##thread for recording the audio
        self.recording_thread=Thread(target=self.record_audio)
        self.recording_thread.start()
        self.stop_button.disabled=False
        self.record_button.disabled=True
        
    def stop_recording(self,event):
        self.recording_active=False
        #stop recording thread
        self.recording_thread.join()
        self.recording_thread=None
        
        #disable the stop button
        self.record_button.disabled=False
        self.stop_button.disabled=True
    
    def build(self):
      layout=MDRelativeLayout(md_bg_color=[255/255,0/255,0/255])
      
      self.record_button=Button(text="Record",pos_hint={"center_x":0.5,"center_y":.70},
                                   size_hint=(.4,.3),font_name="Comic",bold=True,
                                   font_size=30,background_color=(0,1,0))
      self.record_button.bind(on_press=self.start_recording)
      
      self.stop_button=Button(text="Stop Recording",pos_hint={"center_x":0.5,"center_y":.25},
                                   size_hint=(.7,.3),font_name="Comic",bold=True,
                                   font_size=30,background_color=(0,1,1),disabled=True)
      self.stop_button.bind(on_press=self.stop_recording)
                            
      layout.add_widget(self.record_button)
      layout.add_widget(self.stop_button)
      return layout
if __name__=="__main__":
    AudioRecorderApp().run()
    