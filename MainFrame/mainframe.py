from tkinter import *
import tkinter as tk
from tkinter import ttk
from Logica.logica import *
from Logica.logica import raizcuadrada
import math



root= tk.Tk()
root.title("Calculadora V1.0")
root.geometry("+500+80")
root.columnconfigure(0,weigh=1)
root.rowconfigure(0, weight=1)




# --MainFrame Desing--

 # --MainFrame Style--
MainStyle= ttk.Style()
MainStyle.configure('MainS.TFrame', background="green3")



mainframe= ttk.Frame(root,style="MainS.TFrame") 
mainframe.grid(column=0,row=0, sticky="NSEW")
mainframe.columnconfigure(0,weight=1)
mainframe.columnconfigure(1,weight=1)
mainframe.columnconfigure(2,weight=1)
mainframe.columnconfigure(3,weight=1)
mainframe.columnconfigure(4,weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
# --window creation and positions--

 # --Label Style--

LabelStyle_Ecuacion=ttk.Style()
LabelStyle_Ecuacion.configure('Label_Style_Ecua.TLabel', font= "arial 15", anchor="e")

LabelResultado=ttk.Style()
LabelResultado.configure('Label_Result.TLabel', font="arial 45", anchor="e")


Ecuacion= StringVar()
label_Ecuacion= ttk.Label(mainframe, textvariable=Ecuacion, style='Label_Style_Ecua.TLabel')
label_Ecuacion.grid(column=0, row=0, columnspan=5, sticky="NSEW")

Resultado= StringVar()
label_Resultado= ttk.Label(mainframe, textvariable=Resultado, style='Label_Result.TLabel')
label_Resultado.grid(column=0, row=1, columnspan=5, sticky="NSEW")

#-- Button Creation--
 
 #--Button Style--
StyleButton=ttk.Style()
StyleButton.configure('Button_numbers.TButton', font="arial 25", width="6", background="green3", relief="flat")

StyleDelete=ttk.Style()
StyleDelete.configure('Button_delete.TButton', font="arial 25", width="6", background="green3", relief="flat")

StyleBother=ttk.Style()
StyleBother.configure('Button_other.TButton', font="arial 25", width="6", background="green3", relief="flat")



Button0= ttk.Button(mainframe,text="0", style="Button_numbers.TButton", command=lambda: datos("0", Ecuacion ,Resultado))
Button1= ttk.Button(mainframe,text="1", style="Button_numbers.TButton", command=lambda: datos("1", Ecuacion ,Resultado))
Button2= ttk.Button(mainframe,text="2", style="Button_numbers.TButton", command=lambda: datos("2", Ecuacion ,Resultado))
Button3= ttk.Button(mainframe,text="3", style="Button_numbers.TButton", command=lambda: datos("3", Ecuacion ,Resultado))
Button4= ttk.Button(mainframe,text="4", style="Button_numbers.TButton", command=lambda: datos("4", Ecuacion ,Resultado))
Button5= ttk.Button(mainframe,text="5", style="Button_numbers.TButton", command=lambda: datos("5", Ecuacion ,Resultado))
Button6= ttk.Button(mainframe,text="6", style="Button_numbers.TButton", command=lambda: datos("6", Ecuacion ,Resultado))
Button7= ttk.Button(mainframe,text="7", style="Button_numbers.TButton", command=lambda: datos("7", Ecuacion ,Resultado))
Button8= ttk.Button(mainframe,text="8", style="Button_numbers.TButton", command=lambda: datos("8", Ecuacion ,Resultado))
Button9= ttk.Button(mainframe,text="9", style="Button_numbers.TButton", command=lambda: datos("9", Ecuacion ,Resultado))

Button_delete= ttk.Button(mainframe, text=chr(9003), style="Button_delete.TButton",command=lambda: borrar(Ecuacion))
Button_delete_all= ttk.Button(mainframe, text="C", style="Button_other.TButton",command=lambda:limpiar(Ecuacion,Resultado))
Button_parentesis= ttk.Button(mainframe, text="(", style="Button_other.TButton", command=lambda: datos("(", Ecuacion ,Resultado))
Button_close_parentesis= ttk.Button(mainframe, text=")", style="Button_other.TButton", command=lambda: datos(")", Ecuacion ,Resultado))
Button_Sqroot= ttk.Button(mainframe, text="√", style="Button_other.TButton",command=lambda: raizcuadrada(Ecuacion, Resultado))
Button_division= ttk.Button(mainframe, text=chr(247), style="Button_other.TButton", command=lambda: datos("/", Ecuacion ,Resultado))
Button_multi= ttk.Button(mainframe, text="*", style="Button_other.TButton", command=lambda: datos("*", Ecuacion ,Resultado))
Button_sum= ttk.Button(mainframe, text="+", style="Button_other.TButton", command=lambda: datos("+", Ecuacion ,Resultado))
Button_rest= ttk.Button(mainframe, text="-", style="Button_other.TButton", command=lambda: datos("-", Ecuacion ,Resultado))
Button_point= ttk.Button(mainframe, text=".", style="Button_other.TButton", command=lambda: datos(".", Ecuacion ,Resultado))
Button_equal= ttk.Button(mainframe, text="=", style="Button_other.TButton", command=lambda: datos("=", Ecuacion ,Resultado))




# Button Style
#Style_button_number= ttk.Style() 
#Style_button_number.configure()


# --Positions--
 # Position in row 2
Button_Sqroot.grid(column=0,row=2, sticky="NSEW")
Button_parentesis.grid(column=1,row=2, sticky="NSEW")
Button_close_parentesis.grid(column=2, row=2, sticky="NSEW")
Button_delete_all.grid(column=3,row=2, sticky="NSEW")
Button_delete.grid(column=4, row=2, sticky="NSEW")

 # Position in row 3
Button7.grid(column=0, row=3, sticky="NSEW")
Button8.grid(column=1, row=3, sticky="NSEW")
Button9.grid(column=2, row=3, sticky="NSEW")
Button_division.grid(column=3,row=3, sticky="NSEW")
 
 # Position in row 4
Button4.grid(column=0, row=4, sticky="NSEW")
Button5.grid(column=1, row=4, sticky="NSEW")
Button6.grid(column=2, row=4, sticky="NSEW")
Button_multi.grid(column=3, row=4, sticky="NSEW")
 
 # Position in row 5
Button1.grid(column=0, row=5, sticky="NSEW")
Button2.grid(column=1, row=5, sticky="NSEW")
Button3.grid(column=2, row=5, sticky="NSEW")
Button_point.grid(column=3, row=5, sticky="NSEW")

 # Especial position
  # Config position columun
Button0.grid(column=0,row=6, columnspan=2,sticky="WNSE")
Button_equal.grid(column=2,row=6, columnspan=4, sticky="NSEW")
  
  # Config position row
Button_sum.grid(column=4 , row=3, rowspan=2, sticky="NSEW")
Button_rest.grid(column=4 , row=5, sticky="NSEW")




