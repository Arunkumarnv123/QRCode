from  tkinter import *
import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk , ImageDraw

class QR_Code_YT():
    def __init__(self, root):
        self.root=root
        self.root.title("Qr Code Generator")
        self.root.maxsize(1060 , 630 )
        self.root.maxsize(1060+200,600+100)
        self.root.resizable(width=False,height=False)
        self.root.configure(background="cadetblue")

        mainFrame=Frame(self.root,bd=10,width=1050,height=620,relief=RIDGE)
        mainFrame.grid( sticky='nsew')
        TitleFrame = Frame(mainFrame, bd=10, width=1050, height=100, relief=RIDGE)
        TitleFrame.grid(row=0,column=0,sticky='nsew')
        TopFrame1 = Frame(mainFrame,bg="black", bd=10, width=1050, height=540, relief=RIDGE)
        TopFrame1.grid(row=1,column=0,sticky='nsew')
        TopFrame2 = Frame(TopFrame1, bd=10, width=700,bg="blue", height=500, relief=RIDGE)
        TopFrame2.grid(row=1,column=0,sticky='nsew')
        TopFrame3 = Frame(TopFrame1, bd=10,bg="purple", width=450, height=500, relief=RIDGE)
        TopFrame3.grid(row=1,column=1,sticky='nsew')

        EnterFrame = Frame(TopFrame2, width=600, height=100, bg="orange",relief=RIDGE)
        EnterFrame.pack()
        qrcodeFrame = Frame(TopFrame2, width=600, height=400, relief=RIDGE)
        qrcodeFrame.pack()
        btnFrame = Frame(TopFrame3, bg="cadetblue", width=400, relief=RIDGE)
        btnFrame.grid(row=1,column=1)
        #===========================================================================

        def generate_qrcode():

            data=entry.get()
            if not data:
                messagebox.showerror("Error", "Enter some data")
                return
            qr = qrcode.QRCode(

                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=1

            )
            qr.add_data(data)
            qr.make(fit=True)

            qr_image = qr.make_image(fill_color="lime", back_color="green").convert("RGBA")
            overlay = Image.new("RGBA", qr_image.size)
            draw = ImageDraw.Draw(overlay)
            c_x, c_y = qr_image.width // 2, qr_image.height // 2
            radius = min(qr_image.width, qr_image.height) // 2
            for r in range(radius, 0, -1):
                alpha = int(255 * (1 - r / radius))
                color = (247, 0, 54, alpha)
                draw.ellipse(
                    (c_x - r, c_y - r, c_x + r, c_y + r),
                    fill=color,
                    outline=None

                )

            qr_image = Image.alpha_composite(qr_image, overlay)

            logo = Image.open("My-name.png")
            logo_size = (qr_image.width //2, qr_image.height // 2)
            logo = logo.resize(logo_size, Image.LANCZOS)
            logo_position = (

                (qr_image.width - logo_size[0]) // 2,
                (qr_image.height - logo_size[0]) // 2
            )
            qr_image.paste(logo, logo_position, logo)
            qr_image=qr_image.resize((200,200))
            img_tk= ImageTk.PhotoImage(qr_image)
            qr_label.config(image=img_tk ,bg="fuchsia",)
            qr_label.image=img_tk
            qq=Label(TopFrame1,text="By:- Arun Kumar N V",bg="fuchsia",font=('arial',16,'bold' ))
            qq.place(x=434,y=360)



        def save_qrcode():
            data=entry.get()
            if not data:
                messagebox.showerror("Error", "Enter some data")
                return
            qr = qrcode.QRCode(

                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=1

            )
            qr.add_data(data)
            qr.make(fit=True)

            qr_image = qr.make_image(fill_color="lime", back_color="green").convert("RGBA")
            overlay = Image.new("RGBA", qr_image.size)
            draw = ImageDraw.Draw(overlay)
            c_x, c_y = qr_image.width // 2, qr_image.height // 2
            radius = min(qr_image.width, qr_image.height) // 2
            for r in range(radius, 0, -1):
                alpha = int(255 * (1 - r / radius))
                color = (247, 212, 54, alpha)
                draw.ellipse(
                    (c_x - r, c_y - r, c_x + r, c_y + r),
                    fill=color,
                    outline=None

                )

            qr_image = Image.alpha_composite(qr_image, overlay)

            logo = Image.open("My-name.png")
            logo_size = (qr_image.width // 2, qr_image.height // 2)
            logo = logo.resize(logo_size, Image.LANCZOS)
            logo_position = (

                (qr_image.width - logo_size[0]) // 2,
                (qr_image.height - logo_size[0]) // 2
            )
            qr_image.paste(logo, logo_position, logo)
            save_path="qr_app.png"
            qr_image.save(save_path)
            messagebox.showinfo("Success",f"Qr code saved at:{save_path}")


        def reset():
            entry.delete(0,tk.END)
            qr_label.config(image="")

        def exit_program():
            result=messagebox.askyesno("Exit","Confirm if you want to exit")
            if result:
                root.destroy()

        #========================================================
        lblTitle=Label(TitleFrame,font=('arial',40,'bold' ,'underline'),text="QR Code Generator",justify='center',bg='lime',fg="aqua",width=32)
        lblTitle.pack()
        lbldisplay=Label(EnterFrame,font=('arial',20,'bold' ),text="Enter data Below to create QR Code",bg="lime",justify='center')
        lbldisplay.grid(row=0,column=0,pady=10)
        entry=Entry(EnterFrame,font=('arial',24,'bold' ),width=34,justify="center",bd=3 , bg="gray", fg="red")
        entry.grid(row=2,column=0,pady=20,padx=10)
        entry.focus()
        qr_label=Label(qrcodeFrame)
        qr_label.pack()

        #=====================================================================
        generate_btn=Button(btnFrame,font=('arial',20,'bold' ),bg="pink",text="Generate QR Code",width=20,height=2,command=generate_qrcode)
        generate_btn.grid(row=0,column=0,pady=4,padx=4)
        save_btn = Button(btnFrame, font=('arial', 20, 'bold'),bg="pink", text="Save QR Code", width=20, height=2,command=save_qrcode)
        save_btn.grid(row=1, column=0, pady=4, padx=4)
        Reset_btn = Button(btnFrame, font=('arial', 20, 'bold'),bg="pink", text="Reset", width=20, height=2,command=reset)
        Reset_btn.grid(row=2, column=0, pady=4, padx=4)
        Exit_btn = Button(btnFrame, font=('arial', 20, 'bold'),bg="pink", text="Exit", width=20, height=2,command=exit_program)
        Exit_btn.grid(row=3, column=0, pady=4, padx=4)
        lb=Label(TitleFrame,font=('arial',10,'bold' ),text="By:- Arun Kumar N V",bg="lime",justify='right')
        lb.place(x=890,y=30)

if __name__=="__main__":
    root=Tk()
    application=QR_Code_YT(root)
    root.mainloop()

