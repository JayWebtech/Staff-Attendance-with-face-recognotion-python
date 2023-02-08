import mysql.connector
import cv2
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.uix.popup import Popup

cam = cv2.VideoCapture(0)
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  db = "staff_database",
)
Window.size = (600,500)

class Intro(Screen):
    pass

class Login(Screen):
    def do_login(self, loginText, passwordText):
        if loginText == 'admin' and passwordText =='admin':
            self.manager.current = 'Admin'
        else:
            popup = Popup(title='Login Alert', content=Label(text='Incorrect Login Combination'),size_hint=(None, None), size=(400, 150))
            popup.open()

class Admin(Screen):
    pass

class Register(Screen):
    def register(self, email, name, staff_id):
        pass
    def snap(self,staff_id):
        cv2.namedWindow('Staff Pasport')
        img_counter = 0
        # while loop
        while True:
            # intializing the frame, ret
            ret, frame = cam.read()
            # if statement
            if not ret:
                print('failed to grab frame')
                break
            #to get continuous live video feed from my laptops webcam
            k  = cv2.waitKey(1)
            # if the escape key is been pressed, the app will stop
            if k%256 == 27:
                print('escape hit, closing the app')
                break
            # if the spacebar key is been pressed
            cv2.imshow('test', frame)
            # screenshots will be taken
            elif k%256  == 32:
                # the format for storing the images scrreenshotted
                # saves the image as a png file
                cv2.imwrite(staff_id+".png", frame)
                print('screenshot taken')
                # the number of images automaticallly increases by 1
                img_counter += 1

        # release the camera
        cam.release()

        # stops the camera window
        cam.destoryAllWindows()

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("kv_files/window.kv")

class MyApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
	MyApp().run()