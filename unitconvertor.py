# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 15:14:15 2025

@author: Seyda Nur

"""
from functools import partial
from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
Window.size=(500,500)

class UnitConvertorApp(MDApp):
    def remove_everything(self):
        self.Length_button.pos_hint={"center_x":.5,"center_y":20}
        self.area_button.pos_hint={"center_x":.5,"center_y":20}
        self.BMI_button.pos_hint={"center_x":.5,"center_y":20}
        self.volume_button.pos_hint={"center_x":.5,"center_y":20}
        self.speed_button.pos_hint={"center_x":.5,"center_y":20}
        self.mass_button.pos_hint={"center_x":.5,"center_y":20}
    def add_widgets(self,SELECTIONS):
        self.SELECTIONS=SELECTIONS
        
        dropdown1=DropDown()
        for selection in self.SELECTIONS:
            bttn=Button(text=selection,size_hint_y=None,height=30)
            bttn.bind(on_release=lambda bttn:dropdown1.select(bttn.text))
            dropdown1.add_widget(bttn)
        self.main_button1=Button(text='Select',size_hint=(.3,.1),pos=(355,455),
                                 height=50)
        self.main_button1.bind(on_release=dropdown1.open)
        
        dropdown1.bind(on_select=lambda instance,x:setattr(self.main_button1,'text',x))
        self.layout.add_widget(self.main_button1)
        
        
        dropdown2=DropDown()
        for selection in self.SELECTIONS:
            bttn=Button(text=selection,size_hint_y=None,height=30)
            bttn.bind(on_release=lambda bttn:dropdown2.select(bttn.text))
            dropdown2.add_widget(bttn)
        self.main_button2=Button(text='Select',size_hint=(.3,.1),pos=(355,240),
                                 height=50)
        self.main_button2.bind(on_release=dropdown2.open)
        
        dropdown2.bind(on_select=lambda instance,x:setattr(self.main_button2,'text',x))
        self.layout.add_widget(self.main_button2)
       
        self.textinput1.pos_hint={"center_x":.3,"center_y":.65}
        self.textinput2.pos_hint={"center_x":.3,"center_y":.35}
    def calculateLength(self,event):
        inputVal=self.textinput1.text
        inputUnit=self.main_button1.text
        outputUnit=self.main_button2.text
        
        result=round(inputVal*self.unitDict[inputUnit]/self.uintDict[outputUnit],5)
        result =str(result)
        self.textinput2.text=result
    def unit_calculator(self,title,units,event):
        self.remove_everything()
        self.title=title   
        self.titleLabel.text=self.title
        self.units=units
        self.add_widgets(self.units)
        
        
        self.convert_button.pos_hint={"center_x":.7,"center_y": .15}
        
        
    def calculateBMI(self,event):
        self.bmi_label.text=""
        self.height=self.height_input.text
        self.weight=self.weight_input.text
        self.weight=int(self.weight)
        self.height=int(self.height)
        
        self.height=self.height*self.height
        
        if(self.weight!=""and self.height!=1):
            self.bmi=round((self.weight/self.height)*10000,3)
            if self.bmi<18:
                print("You are underweight")
                self.bmi=str(self.bmi)
                self.bmi_label.text=self.bmi+"  Underweight"
                self.bmi_label.pos_hint={"center_x":.5,"center_y":.20}
            elif self.bmi>24:
                print("You are overweight")
                self.bmi=str(self.bmi)
                self.bmi_label.text=self.bmi+"  Overweight"
                self.bmi_label.pos_hint={"center_x":.5,"center_y":.20}
            else:
                print("You are Normal")
                self.bmi=str(self.bmi)
                self.bmi_label.text=self.bmi+"  Normalweight"
                self.bmi_label.pos_hint={"center_x":.5,"center_y":.20}
    def bmi_calculator(self,event):
        self.remove_everything()
        self.titleLabel.text="BMI Calculator"
        #height
        self.height_label=Label(text="Height(cm)",pos_hint={"center_x":.35,"center_y":.70},
                                size_hint=(1,1),font_size=30,color=(0,0,0))
        self.layout.add_widget(self.height_label)
        self.height_input=TextInput(text="",pos_hint={"center_x":.7,"center_y":.70},
                                    size_hint=(.3,None),height=48,font_size=29,foreground_color=(0,.5,0),
                                    font_name="Comic")
        self.layout.add_widget(self.height_input)
        #weight
        self.weight_label=Label(text="Weight(kg)",pos_hint={"center_x":.35,"center_y":.50},
                                size_hint=(1,1),font_size=30,color=(0,0,0))
        self.layout.add_widget(self.weight_label)
        self.weight_input=TextInput(text="",pos_hint={"center_x":.7,"center_y":.50},
                                    size_hint=(.3,None),height=48,font_size=29,foreground_color=(0,.5,0),
                                    font_name="Comic")
        self.layout.add_widget(self.weight_input)
        
        self.BMI_convertButton=Button(text="Calculate",pos_hint={"center_x":.5,"center_y":.35},
                                      size_hint=(.2,.1),size=(75,75),font_name="Comic",bold=True,
                                      font_size=24,background_color=(0,0,0)
                                      )
        self.BMI_convertButton.bind(on_press=self.calculateBMI)
        self.layout.add_widget(self.BMI_convertButton)
    def build(self):
    
        self.layout=MDRelativeLayout(md_bg_color=[255/255,0/255,0/255])
        self.length_units=[
            "milimeter","centimeter","meter","kilometer"
            ]
        self.temperature_units=[
            "celcius","fahrenheit"
            ]
        self.area_units=[
            "square meter","square kilometer","square centimeter","square milimeter","are","hectare"
            ]
        self.volume_units=[
            "cubic meter","cubic centimeter","litre","mililitre","gallon"
            ]
        self.weight_units=[
            "miligram","gram","kilogram"
            ]
        self.titleLabel=Label(text="Choose your Convertor",
                              pos_hint={"center_x":0.5,"center_y":.94},
                              size_hint=(1,1),
                              font_size=40,color=(1,1,0),font_name="Comic")
        self.BMI_button=Button(text="BMI",pos_hint={"center_x":.28,"center_y":.75},
                                     size_hint=(.23,.17),font_name="Comic",bold=True,
                                     font_size=30,background_color=(0,1,0))
        self.BMI_button.bind(on_press=self.bmi_calculator)
        self.bmi_label=Label(text="",pos_hint={"center_x":.35,"center_y":.50},
                             size_hint=(1,1),font_size=30,color=(0,0,0))
        self.layout.add_widget(self.bmi_label)
        self.Length_button=Button(text="Length",pos_hint={"center_x":.68,"center_y":.75},
                                     size_hint=(.23,.17),font_name="Comic",bold=True,
                                     font_size=30,background_color=(0,1,0))
        self.Length_button.bind(on_press=partial(self.unit_calculator,"Length Calculator",self.length_units))
        
        self.area_button=Button(text="Area",pos_hint={"center_x":.28,"center_y":.50},
                                     size_hint=(.23,.17),font_name="Comic",bold=True,
                                     font_size=30,background_color=(0,1,0))
        self.area_button.bind(on_press=partial(self.unit_calculator,"Area Calculator",self.area_units))
        self.volume_button=Button(text="Volume",pos_hint={"center_x":.68,"center_y":.50},
                                     size_hint=(.23,.17),font_name="Comic",bold=True,
                                     font_size=30,background_color=(0,1,0))
        self.speed_button=Button(text="Speed",pos_hint={"center_x":.28,"center_y":.25},
                                     size_hint=(.23,.17),font_name="Comic",bold=True,
                                     font_size=30,background_color=(0,1,0))
        self.mass_button=Button(text="Mass",pos_hint={"center_x":.68,"center_y":.25},
                                     size_hint=(.23,.17),font_name="Comic",bold=True,
                                     font_size=30,background_color=(0,1,0))
        self.textinput1=TextInput(text="",pos_hint={"center_x":.2,"center_y":65},
                                  size_hint=(.3,None),height=48,font_size=29,
                                  foreground_color=(0,.5,0),font_name="Comic")
        self.layout.add_widget(self.textinput1)
        self.textinput2=TextInput(text="",pos_hint={"center_x":.2,"center_y":35},
                                  size_hint=(.3,None),height=48,font_size=29,
                                  foreground_color=(0,.5,1),font_name="Comic")
        self.layout.add_widget(self.textinput2)
        self.convert_button=Button(text="Convert",pos_hint={"center_x":.7,"center_y":15},
                                     size_hint=(.20,.15),font_name="Comic",bold=True,
                                     font_size=30,background_color=(0,1,0))
        self.convert_button.bind(on_press=self.calculateLength)
        
        self.layout.add_widget(self.convert_button)
        
        self.UnitDict={
            "milimetre":0.001,
            "centimeter":0.01,
            "meter":0.1,
            "kilometer":1
            }
        
       
        self.layout.add_widget(self.titleLabel)
        self.layout.add_widget(self.BMI_button)
        self.layout.add_widget(self.Length_button)
        self.layout.add_widget(self.area_button)
        self.layout.add_widget(self.volume_button)
        self.layout.add_widget(self.speed_button)
        self.layout.add_widget(self.mass_button)
        
        return self.layout
if __name__=="__main__":
    UnitConvertorApp().run()
