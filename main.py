from kivy.app import App
import kivy
from kivy.uix.button import Label
import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup

kivy.require('1.10.0')

class CustomPopup(Popup):
    pass



class simple_counterApp(App):
    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()
        
    def spinner_clicked(self, value):
        if value == "Light":
            self.root.ids.store_button.background_color=(255,255,255,255)
            self.root.ids.reset_button.background_color=(200,200,200,200)
            self.root.ids.theme_button.background_color=(200,200,200,200)
            self.root.ids.count_button.background_color=(110,100,100,100)
            self.root.ids.delete_button.background_color=(100,110,100,100)
            self.root.ids.store_button.color=(0,0,0,0.5)
            self.root.ids.reset_button.color=(0,0,0,0.5)
            self.root.ids.theme_button.color=(0,0,0,0.5)
        if value == "Colored":
            self.root.ids.store_button.background_color=(1,0,1,0.4)
            self.root.ids.reset_button.background_color=(0,0,1,0.4)
            self.root.ids.theme_button.background_color=(0,0,0,0.5)
            self.root.ids.count_button.background_color=(0,255,0,0.4)
            self.root.ids.delete_button.background_color=(255,0,0,0.4)
            self.root.ids.store_button.color=(1,1,1,0.5)
            self.root.ids.reset_button.color=(1,1,1,0.5)
            self.root.ids.theme_button.color=(1,1,1,0.5)




    
    def delete(self, button):
        global num
        global i
        global zone

        num  -= 1
        if num<=-1:
            num *= 0
        self.root.ids.outputLabel.text=str(num)
        if num == 10*zone-10:
            zone-=1
            self.root.ids.outputLabel.color= (0,1,0,10)
        else:
           self.root.ids.outputLabel.color= (1,1,1,1) 

            
    def store(self, button):
        global num
        self.root.ids.Storednum.text= str(num)
        if num >= 0:
            self.root.ids.Storednum.color = (0,0,1,10)
        if num ==0:
            self.root.ids.Storednum.color = (0,1,1,10)


    def reset(self, button):
        global num
        global i
        global zone
        zone = 1
        i = 1
        num = 0
        self.root.ids.outputLabel.text= str(num)
        self.root.ids.outputLabel.color= (1,1,1,1)
        

    def count(self, button):
        global num
        global i
        global zone
        num += 1

        self.root.ids.outputLabel.text= str(num)
        if num == 10*zone:
            self.root.ids.outputLabel.color= (0,1,0,10)
            zone += 1
            
        else:
            self.root.ids.outputLabel.color= (1,1,1,1)
            
 
            

    def settings(self,button):
        pass
        

        
        




#Deklaration der Variablen--------------------------------
zone = 1
num = 0
i = 1
print(zone)


#Start der Anwendung
meineAnwendung=simple_counterApp()
print(meineAnwendung)
meineAnwendung.run()


