from pathlib import Path
from tkinter import Label, StringVar,Tk,Canvas,Text,Button,PhotoImage
from tkinter.constants import END,WORD
from sklearn import svm
import seaborn as sns
import pickle

#chemin d'accès aux assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title("TP9 DIABETES")
width = 600 
height = 300
 
screen_width = window.winfo_screenwidth()  
screen_height = window.winfo_screenheight() 

x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
 
window.geometry('%dx%d+%d+%d' % (width, height, x, y))
window.resizable(False, False)
window.config(cursor="dot")

result=StringVar()
result.set("------")

#import de notre modele SVM
with open('Model.pkl', 'rb') as f:
    model = pickle.load(f)
    

def predire():
    ok=False
    try:
        inputs=[[float(Prg.get(0.0,END)),float(GL.get(0.0,END)),float(Bl.get(0.0,END)),float(ST.get(0.0,END)),
                 float(Ins.get(0.0,END)),float(BMI.get(0.0,END)),float(DP.get(0.0,END)),float(AGE.get(0.0,END))]]
        ok=True
    except:
        result.set('Entrer des bonnes Valeurs')
        ok=False
    if ok:
        result.set(model.predict(inputs))
        
    
#arrière plan
canvas = Canvas(
    window,
    bg="#004c7f",
    height=300,
    width=600,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
canvas.place(x = 0, y = 0)

bg_image = PhotoImage(
    file=relative_to_assets("bg.png"))
bg = canvas.create_image(
    300,
    150,
    image=bg_image
    )

Prg = Text(
    canvas,
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    font=("sergio",10,"bold"),
    wrap=WORD,
    cursor="dot",

)
Prg.place(
    x=60,
    y=90,
    width=85,
    height=20
)
GL = Text(
    canvas,
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    font=("sergio",10,"bold"),
    wrap=WORD,
    cursor="dot",

)
GL.place(
    x=195,
    y=90,
    width=85,
    height=20
)
Bl = Text(
    canvas,
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    font=("sergio",10,"bold"),
    wrap=WORD,
    cursor="dot",

)
Bl.place(
    x=336,
    y=90,
    width=85,
    height=20
)
ST = Text(
    canvas,
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    font=("sergio",10,"bold"),
    wrap=WORD,
    cursor="dot",

)
ST.place(
    x=477,
    y=90,
    width=85,
    height=20
)

Ins = Text(
    canvas,
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    font=("sergio",10,"bold"),
    wrap=WORD,
    cursor="dot",

)
Ins.place(
    x=60,
    y=154,
    width=85,
    height=20
)
BMI = Text(
    canvas,
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    font=("sergio",10,"bold"),
    wrap=WORD,
    cursor="dot",

)
BMI.place(
    x=195,
    y=154,
    width=85,
    height=20
)
DP = Text(
    canvas,
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    font=("sergio",10,"bold"),
    wrap=WORD,
    cursor="dot",

)
DP.place(
    x=336,
    y=154,
    width=85,
    height=20
)
AGE = Text(
    canvas,
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    font=("sergio",10,"bold"),
    wrap=WORD,
    cursor="dot",

)
AGE.place(
    x=477,
    y=154,
    width=85,
    height=20
)
button_image = PhotoImage(
    file=relative_to_assets("btn.png"))
button_1 = Button(
    canvas,
    command=predire,
    image=button_image,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    activebackground="#4B2535",
    bg="#4B2535"
)
button_1.place(
    x=266,
    y=197,
    width=69,
    height=26
)

resultat=Label(
    canvas,
    textvariable=result,
    fg="red",
    bg="white",
    font=('sergio',13,'bold')
)
resultat.place(
        x=150,
        y=260,
        width=300
)

window.mainloop()
