from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from pygame import *
from mutagen.mp3 import MP3

#------Ventana y Frames---------
ventana = Tk()
ventana.title("ReMusic")
ventana.resizable(False,False)
frame = Frame()
frame.config(bg="#5fcde4")
frame.pack()



#-----------Variables----------
canciones = ""
CancionDi = ""
control = False
mixer.init()

#----------Imagnes--------
imaryu = Image.open("C:/Users/ADMIN/Documents/Vs/Python/PythonTem1/ProYO/ReproductorMusIc/Resourses/RyoImg2.jpeg")
imaryu = imaryu.resize((400,400), Image.LANCZOS)
imaryu = ImageTk.PhotoImage(imaryu)

gifryu = Image.open("C:/Users/ADMIN/Documents/Vs/Python/PythonTem1/ProYO/ReproductorMusIc/Resourses/RyoImg1.jpeg")
gifryu = gifryu.resize((400,400),Image.LANCZOS)
gifryu = ImageTk.PhotoImage(gifryu)


SongMa= Image.open("C:/Users/ADMIN/Documents/Vs/Python/PythonTem1/ProYO/ReproductorMusIc/Resourses/SongMas.png")
SongMa = ImageTk.PhotoImage(SongMa)
reproCan= Image.open("C:/Users/ADMIN/Documents/Vs/Python/PythonTem1/ProYO/ReproductorMusIc/Resourses/play.png")
reproCan = ImageTk.PhotoImage(reproCan)
pauseUnpa= Image.open("C:/Users/ADMIN/Documents/Vs/Python/PythonTem1/ProYO/ReproductorMusIc/Resourses/PauseUnpau.png")
pauseUnpa = ImageTk.PhotoImage(pauseUnpa)
AvanSong = Image.open("C:/Users/ADMIN/Documents/Vs/Python/PythonTem1/ProYO/ReproductorMusIc/Resourses/AvanzarSong.png")
AvanSong = ImageTk.PhotoImage(AvanSong)
regreSong = Image.open("C:/Users/ADMIN/Documents/Vs/Python/PythonTem1/ProYO/ReproductorMusIc/Resourses/RetrocederSong.png")
regreSong =ImageTk.PhotoImage(regreSong)
subiVo = Image.open("C:/Users/ADMIN/Documents/Vs/Python/PythonTem1/ProYO/ReproductorMusIc/Resourses/SubirVolu.png")
subiVo = ImageTk.PhotoImage(subiVo)
bajaVo = Image.open("C:/Users/ADMIN/Documents/Vs/Python/PythonTem1/ProYO/ReproductorMusIc/Resourses/BajarVolu.png")
bajaVo = ImageTk.PhotoImage(bajaVo)

#----------Funciones----------
def abrirCan():
    global CancionDi
    global canciones
    global pos
    global n
    pos = 0
    n = 0
    
    CancionDi = filedialog.askopenfilenames(title="Abrir Cancion",filetypes=[("Archivo MP3","*.mp3")])
    nombre()
    
def nombre():
    global pos
    global n
    global CancionDi
    global canciones
    n = len(CancionDi)
    canciones = CancionDi[pos]
    nombreCanAc = canciones.split("/")
    nombreCanAc = nombreCanAc[-1]
    nombreCan.config(text=nombreCanAc,wraplength=400,justify=LEFT) 
    cantidadCan.config(text=f"Canciones cargadas: {n}")
        
def repro():
    global canciones
    global pos
    global n
    global x
    mixer.music.load(canciones)
    mixer.music.set_volume(1)
    mixer.music.play()
    can = MP3(canciones)
    tiempo = can.info.length
    x = int(tiempo)
    ryu.config(image=gifryu)
    cantidadCan.config(text=f"CANCION {pos + 1} DE {n}")    

def retroceder():
    global pos
    global n
    if pos > 0:
        pos = pos -1
    else:
        pos = 0
    nombre()
    repro()
    cantidadCan.config(text=f"CANCION {pos + 1} DE {n}")
       
def avanzar():
    global pos
    global n
    if pos == n -1 :
        pos = 0
    else:
        pos += 1
    nombre()
    repro()
    cantidadCan.config(text=f"CANCION {pos + 1} DE {n}")
    
def pau():
    global control
    if control==False:
        mixer.music.pause()
        control = True
        
    elif control:
        mixer.music.unpause()
        control=False
def subirvolumen():
    volumen = mixer.music.get_volume()
    nuevoVolumen = min(1.0,volumen + 0.1)
    mixer.music.set_volume(nuevoVolumen) 

def bajarVolumen():
    volumen = mixer.music.get_volume()
    nuevoVolumen = max(0.0,volumen - 0.1)
    mixer.music.set_volume(nuevoVolumen)   
 
        
#---------Img Repro------------
ryu = Label(frame,image=imaryu)
ryu.grid(row =0,column=0,columnspan=7,padx=10,pady=10)     

#------------Botones----------
nombreCan = Label(frame, text="CANCION (NO SELECCIONADA)",bg="#5fcde4",fg="#fff",font="Normal")
nombreCan.grid(row = 1, column=0, columnspan=7,padx=3,pady=3)
cantidadCan = Label(frame,text="0/0",bg="#5fcde4",fg="#fff",font="Normal")
cantidadCan.grid(row = 2,column=0,columnspan=7,padx=3,pady=3)
abrir = Button(frame,image=SongMa,command=abrirCan,borderwidth=0,bg="#5fcde4")
abrir.grid(row=3,column=0, padx=5,pady=5)
reproducir = Button(frame,image=reproCan,command=repro,borderwidth=0,bg="#5fcde4")
reproducir.grid(row=3,column=1,padx=5,pady=5)
regresarCan = Button(frame,command=retroceder,image=regreSong,borderwidth=0,bg="#5fcde4")
regresarCan.grid(row=3,column=2,padx=5,pady=5)
pausarUnpa = Button(frame,command=pau,image=pauseUnpa,borderwidth=0,bg="#5fcde4")
pausarUnpa.grid(row=3,column=3,padx=5,pady=5)
avanzarCan = Button(frame,command=avanzar,image=AvanSong,borderwidth=0,bg="#5fcde4")
avanzarCan.grid(row=3,column=4,padx=5,pady=5)
subirVolumen = Button(frame,command=subirvolumen,image=subiVo,borderwidth=0,bg="#5fcde4")
subirVolumen.grid(row=3,column=5,padx=5,pady=5)
BajarVolumen = Button(frame,command=bajarVolumen,image=bajaVo,borderwidth=0,bg="#5fcde4")
BajarVolumen.grid(row=3,column=6,padx=5,pady=5)

"""tiempo = Label(frame,bg="#5fcde4",text="0")
tiempo.grid(row=2,column=0,padx=2,pady=2)"""


ventana.mainloop()