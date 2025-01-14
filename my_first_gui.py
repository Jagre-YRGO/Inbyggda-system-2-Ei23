import guizero as gz

print('starting gui app')

def increment_number():
    print('button pushed!')
    number_text.value = str(int(number_text.value) + int(increment_value_box.value))

#start app
app = gz.App(title='my first gui')

#populate app with widgets
number_text = gz.Text(app,text='0',size=50)
my_button = gz.PushButton(app, text='increment',command=increment_number)
increment_value_box = gz.TextBox(app,text='1')

#display app
app.display()

print('hej då!')