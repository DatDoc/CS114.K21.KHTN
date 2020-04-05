import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

import requests
HEIGHT = 600
WIDTH = 800
root = tk.Tk()
root.title("Current weather")
def format_response(weather_infor):
	try:		# use try in case the user type the name that NOT VALID
		name = weather_infor['name']
		condition = weather_infor['weather'][0]['description']
		temperature = weather_infor['main']['temp']
		humidity = weather_infor['main']['humidity']
		output_str =  'City : %s \nCondition: %s \nTemperature : %s celsius\nHumidity : %s\n' % (name, condition, temperature, humidity)
	except:
		output_str = "please type again!!!"

	return output_str

def open_icon(icon):

    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png'))

    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img

def get_weather(city):
	weather_key = 'a04d860843675aebff2701a3d43d9c95' #api key 
	url = 'https://api.openweathermap.org/data/2.5/weather' 
	params = {'q' : city, 'appid' : weather_key, 'units' : 'metric'}
	response = requests.get(url, params = params)
	weather_infor = response.json()
	lower_label['text'] = format_response(weather_infor)

	icon_name = weather_infor['weather'][0]['icon']
	open_icon(icon_name)


canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()
 
background_img = tk.PhotoImage(file = 'mountain.png')
background_label = tk.Label(root, image = background_img)
background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

upper_frame = tk.Frame(root, bg = '#33E1FF', bd = 5)
upper_frame.place(relx = 0.5, rely = 0.1, relheight = 0.1, relwidth = 0.75, anchor = 'n')


button = tk.Button(upper_frame,text = "find",bg = 'gray', command = lambda: get_weather(entry.get()))
button.place(relx= 0.66, relwidth = 0.34 , relheight = 1)

entry = tk.Entry(upper_frame, font = 40)
entry.place(relheight = 1, relwidth = 0.65)

lower_frame = tk.Frame(root, bg= '#33E1FF', bd = 5)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.65, anchor = 'n')

lower_label = tk.Label(lower_frame, font = ('Times New Roman', 30) )
lower_label.place(relheight = 1, relwidth =1)


weather_icon = tk.Canvas(lower_frame)
weather_icon.place(relx=0.4, rely=0.7, relwidth=0.2, relheight=0.3)

root.mainloop()
