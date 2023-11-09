import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class RegistationApp(App):
    def build(self):
        self.title = "Registation From"
        layout = Boxlayout(orientation='vertical', padding=30, spacing=10)

        head_label = Label(text="Python Registation App", front_size=26, blod =True, height=40)
#Adding more info

        name_label = Labell(text="Name:", front_size = 18)
        self.name_input = TextInput(multiline=false, front_size = 18)
        
        email_label = Label(text="Email:", front_size = 18)
        self.email_input = TextInput(multiline=false, front_size = 18)
        password_label = Label(text="Password:", front_size = 18)
        self.password_input = TextInput(multiline=false, front_size = 18, password = True)
        repassword_label = Label(text="Re-password:", front_size = 18)
        self.repassword_input = TextInput(multiline=false, front_size = 18, password = True)

#Button Creation
        submit_button =Button(text ='Register', front_size=18)        


        Layout.add_widget(head_label)
        Layout.add_widget(name_label)
        Layout.add_widget(self.name_input)
        Layout.add_widget(email_label)
        Layout.add_widget(self.email_input)
        Layout.add_widget(password_label)
        Layout.add_widget(self.password_input)
        Layout.add_widget(repassword_label)
        Layout.add_widget(self.repassword_input)
        Layout.add_widget(submit_button)
        return layout

if __name__ == '__main__':


  RegistationApp().run()
