import numpy as np
import tensorflow as tf
import sys
if "Tkinter" not in sys.modules:
    from tkinter import *
model_trained=tf.keras.models.load_model('Burn_new.h5')
from tkinter import *
from tkinter.scrolledtext import ScrolledText


class GuiBinding:

    def __init__(self):

        def user_guide():
            pass

        def about():
            pass

        def select_image():
            import cv2
            import chooser
            filepath=chooser.choose()

            Rev_class={0:"1st_degree",1:"2nd_degree"}

            def mapper(val):
                return Rev_class[val]

            img=cv2.imread(filepath)
            img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            img=cv2.resize(img,(200,200))

            pred= model_trained.predict(np.array([img]))
            move_code=np.argmax(pred[0])#this func "argmax" will take the highest value from the list and print it 
            move_name=mapper(move_code)
            print(pred)
            def prediction():
                if pred==[[0.]]:
        
                    return "It is a 1st Degree \n You may put a thin layer of ointment, such as petroleum jelly or aloe vera, on the burn"
                if pred==[[1.]]:
        
                    return "It is a 2nd Degree \n Please apply SILVADENE Cream 1% on the infected area (silver sulfadiazine)"
            prediction()
            file=open("adress.txt","w")
            file.write(prediction())
            file.close()
#print("Predicted: {}".format(move_name))
        def open_camera():
            pass

        self.root = Tk()

        self.root.title('Burn Severity Detector')

        self.root.geometry('1000x700+200+0')

        background_image = PhotoImage(file="bg_image.png")
        background_label = Label(self.root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        Label(self.root, bg="blue4").pack()
        
        Button(self.root, text="A I  -  D O C", fg="Blue", font=('Times New Roman', '35', 'bold')).pack()

        Label(self.root, bg="blue4").pack()

        Button(self.root, text="Intelligent Skin Specialist", font=('Times New Roman', '25', 'bold')).pack()

        Label(self.root, bg="blue4").pack()

        self.about = Button(self.root, text="User Guide", width="20", command=user_guide)
        self.about.pack()

        Label(self.root, bg="blue4").pack()

        self.about = Button(self.root, text="Select Image", width="20", command=select_image)
        self.about.pack()

        Label(self.root, bg="blue4").pack()

        self.about = Button(self.root, text="Open Camera", width="20", command=open_camera)
        self.about.pack()

        Label(self.root, bg="blue4").pack()

        self.about = Button(self.root, text="About", width="20", command=about)
        self.about.pack()

        Label(self.root, bg="blue4").pack()


        self.message = ScrolledText(self.root, height=10, width=60)
        self.message.pack()

        self.root.mainloop()



GuiBinding()
