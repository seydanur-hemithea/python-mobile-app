# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:33:56 2025

@author: Seyda nur
"""
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.uix.relativelayout import MDRelativeLayout
from translate import Translator
from kivy.core.window import Window
Window.size=(500,600)

class MyApp(MDApp):
    def translateText(self,event):
        self.errorLabel.text=""
        var1=self.textInput1.text
        if(var1!=""):
            translator=Translator(from_lang=self.main_button1.text,to_lang=self.main_button2.text)
            try:
                translation=translator.translate(var1)
                self.textInput2.text=""
                self.textInput2.text=translation
            except:
                self.errorLabel.text="Network Error or Invalid Text"
        else:
            self.errorLabel.text="No text to Translate"
            self.errorLabel.pos_hint={"center_x":0.5,"center_y":.80}
            
    def build(self):
        layout=MDRelativeLayout(md_bg_color=[173/255,216/255,230/255])
        self.titleLabel=Label(text="Translator Application",pos_hint={"center_x":0.5,"center_y":.94},
                              size_hint=(1,1),font_size=50,color=(1,0,0),font_name="Calibri")
        self.textInput1=TextInput(text="",pos_hint={"center_x":0.5,"center_y":.65},
                              size_hint=(1,None),height=150,font_size=29,
                              foreground_color=(0,0.5,0),font_name="Calibri"
                              ,hint_text="Enter the text to translate")
        self.textInput2=TextInput(text="",pos_hint={"center_x":0.5,"center_y":.30},
                              size_hint=(1,None),height=150,font_size=29,foreground_color=(0,0.5,0),
                              font_name="Calibri",readonly=True)
        self.translate_button=Button(text="Translate",pos_hint={"center_x":0.5,"center_y":.50},
                                     size_hint=(.25,.1),size=(75,75),
                                     font_size=29,background_color=(0,1,0),on_press=self.translateText)
        self.choice=["English","German","French","Russian","Arabic","Turkish"]
        self.dropdown1=DropDown()
        for choice in self.choice:
            btton=Button(text=choice,size_hint_y=None,height=30)
            btton.bind(on_release=lambda btton:self.dropdown1.select(btton.text))
            self.dropdown1.add_widget(btton)
        
        
        self.main_button1=Button(text="English",size_hint=(None,None),
                                pos=(100,690),height=50)
        self.main_button1.bind(on_release=self.dropdown1.open)
        
        self.dropdown1.bind(on_select=lambda instance,x:setattr(self.main_button1,"text",x))
        
        layout.add_widget(self.main_button1)
        ###dropdown2
        self.dropdown2=DropDown()
        for choice in self.choice:
            btton=Button(text=choice,size_hint_y=None,height=30)
            btton.bind(on_release=lambda btton:self.dropdown2.select(btton.text))
            self.dropdown2.add_widget(btton)
        
        
        self.main_button2=Button(text="English",size_hint=(None,None),
                                pos=(100,365),height=50)
        self.main_button2.bind(on_release=self.dropdown2.open)
        
        self.dropdown2.bind(on_select=lambda instance,x:setattr(self.main_button2,"text",x))
        
        layout.add_widget(self.main_button2)
        
        self.errorLabel=Label(text="",pos_hint={"center_x":.5,"center_y":.80},
                                     size_hint=(1,1),font_size=25,color=(0,0,1))
        layout.add_widget(self.titleLabel)
        layout.add_widget(self.textInput1)
        layout.add_widget(self.textInput2)
        layout.add_widget(self.translate_button)
        layout.add_widget(self.errorLabel)
     
        
        
        return layout
    
    
if __name__=="__main__":
    MyApp().run()