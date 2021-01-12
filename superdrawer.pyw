from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
import PIL
from PIL import Image,ImageDraw,ImageGrab,ImageTk
from tkinter import messagebox
root=Tk()
root.title('Super Drawer')
root.geometry('800x800')
brush_color="black"
def paint(e):
	brush_width='%0.0f' % float(my_slider.get())

	brush_type2=brush_type.get()

	x1=e.x-1
	y1=e.y-1
	
	x2=e.x+1
	y2=e.y+1

	my_canvas.create_line(x1,y1,x2,y2,fill=brush_color,width=brush_width,capstyle=brush_type2,smooth=True)
	

def change_brush_size(thing):
	slider_label.config(text='%0.0f' % float(my_slider.get()))
def change_brush_color():
	global brush_color
	brush_color="black"
	brush_color=colorchooser.askcolor(color=brush_color)[1]

def change_canvas_color():
	global bg_color
	bg_color="black"
	bg_color=colorchooser.askcolor(color=bg_color)[1]
	my_canvas.config(bg=bg_color)

def clear_screen():
	my_canvas.delete(ALL)
	my_canvas.config(bg='white')

	
def save_as_png():
	result=filedialog.asksaveasfilename(initialdir='C:/Users/ognjen/images',filetypes=(("png files","*.png"),("all files","*.*")))
	if result.endswith('.png'):
		pass
	else:
		result+='.png'
	result_label=Label(root,text=result)
	result_label.pack(pady=20)
	if result:
		x=root.winfo_rooty()+my_canvas.winfo_x()
		y=root.winfo_rooty()+my_canvas.winfo_y()
		x1=x+my_canvas.winfo_width()
		y1=y+my_canvas.winfo_height()
		ImageGrab.grab().crop((x,y,x1,y1)).save(result)
		
		messagebox.showinfo("Uspesno!","Slika je sacuvana uspesno!")

w=600
h=400
bgcolor='black'
my_canvas=Canvas(root,width=w,height=h,bg='white')
my_canvas.pack(pady=20)
my_canvas.bind('<B1-Motion>',paint)


brush_options_frame=Frame(root)
brush_options_frame.pack(pady=20)


brush_size_frame=LabelFrame(brush_options_frame,text='Velicina Olovke')
brush_size_frame.grid(row=0,column=0,padx=50)


my_slider=ttk.Scale(brush_size_frame,from_=1,to=100,command=change_brush_size,orient=VERTICAL,value=10)
my_slider.pack(padx=10,pady=10)

slider_label=Label(brush_size_frame,text=my_slider.get())
slider_label.pack(pady=5)


brush_type_frame=LabelFrame(brush_options_frame,text='Tip Olovke',height=400)
brush_type_frame.grid(row=0,column=1,padx=50)
brush_type=StringVar()
brush_type.set('round')

brush_type_radio1=Radiobutton(brush_type_frame,text='round ',variable=brush_type,value='round')
brush_type_radio2=Radiobutton(brush_type_frame,text='slash ',variable=brush_type,value='butt')
brush_type_radio3=Radiobutton(brush_type_frame,text='diamond ',variable=brush_type,value='projecting')
brush_type_radio1.pack(anchor=W)
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)

change_colors_frame=LabelFrame(brush_options_frame,text="Promeni Boje")
change_colors_frame.grid(row=0,column=2)


brush_color_button=Button(change_colors_frame,text="Boja Tempera",command=change_brush_color)
brush_color_button.pack(pady=10,padx=10)


canvas_color_button=Button(change_colors_frame,text="Boja Pozadine",command=change_canvas_color)
canvas_color_button.pack(pady=10,padx=10)


options_frame=LabelFrame(brush_options_frame,text="Opcije")
options_frame.grid(row=0,column=3,padx=50)

clear_button=Button(options_frame,text="Ocisti Ekran",command=clear_screen)
clear_button.pack(padx=10,pady=10)


sav_image_button=Button(options_frame,text="Sacuvaj",command=save_as_png)
sav_image_button.pack(padx=10,pady=10)





root.mainloop()
