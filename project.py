from tkinter import *
from tkinter import messagebox
# from PIL import ImageTk,Image
window = Tk()
window.title("Hotel Bron By eLmIn")
window.geometry("1500x1000+10+10")
window.option_add("*tearOff", FALSE)

def Sign_in_frame():
    sign_in_frame = Frame(window, width=1500, height=900)
    sign_in_frame.place(x=0, y=0)
    sign_in_frame.config(bg="#390879")




    # control
    def Sign_in():
        gmail_get = gmail_entry.get()
        password_get = password_entry.get()
        if gmail_get == "" or password_get == "": #or "@gmail.com" not in gmail_get:
            messagebox.showerror("error", "pustoo")
        elif "@gmail.com" not in gmail_get:
            messagebox.showerror("error", "nepravilniy gmail")
        else:
            with open("account.txt", "a") as file:
                with open("account.txt", "r") as file:
                    account = file.readlines()
                estno = 0
                for user in account:
                    proverka = gmail_get + ":" + password_get + "\n"
                    if proverka in user:
                        finish_frame(gmail_get,password_get)
                        estno = 1
                if estno == 0:
                    messagebox.showerror("error", "ne pravilno vveli")

    gmail_button = Label(sign_in_frame, text="Gmail")
    gmail_button.config(bg="#390879",
                    fg="#bfff00",

            font=("Times New Roman", 24, "italic bold "))
    gmail_button.place(x=600, y=135)
    gmail_entry = Entry(sign_in_frame)
    gmail_entry.config(bg="white",
                       fg="black",
                       font=("Times New Roman", 18, "italic  "),
                       width=24
                       )
    gmail_entry.place(x=600, y=170)
    password_button = Label(sign_in_frame, text="Password")
    password_button.config(
        bg="#390879",
        fg="#bfff00",
        font=("Times New Roman", 24, "italic bold "))
    password_button.place(x=600, y=219)

    sign_in = Button(sign_in_frame, text="sign in", command=Sign_in)
    sign_in.config(
            fg="#390879",
            bg="#bfff00"
             ,
            width=15,
            height=2,
            activeforeground="#d2dbea",font=("Times New Roman", 18, "italic bold "))
    sign_in.place(x=640, y=350)
    sign_up = Button(sign_in_frame, text="Need to create an account ?", command=aduser)
    sign_up.config(fg="#390879",
                   bg="#bfff00",
                   width=25,
                   height=1,
                   font=("Times New Roman", 16, "italic bold "))
    sign_up.place(x=600, y=440)
    x = IntVar()

    #
    def show():
        print(x.get())
        if x.get() == 1:
            password_entry.config(show="")
        else:
            password_entry.config(show="*")

    password_entry = Entry(sign_in_frame, show="*")
    password_entry.config(bg="white",
                          fg="black",
                          font=("Times New Roman", 19, "italic bold"),
                          width=22)
    password_entry.place(x=600, y=255)
    chekbtn = Checkbutton(sign_in_frame, text="Show password", variable=x, command=show)
    chekbtn.config(bg="#bfff00",fg="#390879",font=("Times New Roman", 16, "italic bold "))
    chekbtn.place(x=650, y=300)
    s_label = Label(sign_in_frame, text="Sign in")
    s_label.config(bg="#390879",
        fg="#bfff00",
        font=("Times New Roman", 30, " bold "))
    s_label.place(x=680, y=80)

#


# def register():
#     Sign_up()

def aduser():
    aduser_frame = Frame(window, width=1500, height=900)
    aduser_frame.place(x=0, y=0)
    aduser_frame.config(bg="#390879")


    vibor = Label(aduser_frame,text="Войти как:")
    vibor.config(fg="#bfff00",bg="#390879",font=("Times New Roman", 26, "italic bold ",))
    vibor.place(x=650,y=200)

    knopka1 = Button(aduser_frame,text="Admin",command=admin)
    knopka1.config(bg="brown",fg="white",width=17,height=3)
    knopka1.place(x=550,y=300)

    knopka2 = Button(aduser_frame,text="User",command=Sign_up)
    knopka2.config(bg="brown",fg="white",width=17,height=3)
    knopka2.place(x=800,y=300)

    def Back3():
        Sign_in_frame()


    # view
    back_button = Button(aduser_frame, text="Back", command=Back3)
    back_button.config(bg="red",fg="white",font="bold",width=10,height=1)
    back_button.place(x=10, y=10)

def admin():
    admin_frame = Frame(window,width=1500,height=900)
    admin_frame.place(x=0,y=0)
    admin_frame.config(bg="#390879")
    def admin_in():
        gmail_get = adgmail_entry.get()
        password_get = password_entry.get()
        print(f"{gmail_get}:{password_get}")
        if gmail_get == "elmin-admin" or password_get == "elmin2008":
            finish_frame(gmail_get,password_get)
        elif gmail_get == "" or password_get == "":
            messagebox.showerror(title="error", message="pustoooo")
        else:
            messagebox.showerror(title="error", message="Wrong login or password")

    sign_in = Button(admin_frame, text="sign in", command=admin_in)
    sign_in.config(
        fg="#bfff00",
        bg="#390879",
        width=15,
        height=2,
        activeforeground="#d2dbea", font="bold")
    sign_in.place(x=650, y=350)

    admintxt = Label(admin_frame,text="Admin sign")
    admintxt.config(fg="#bfff00",font=("Times New Roman", 30, " bold "),bg="#390879")
    admintxt.place(x=640,y=70)


    adgmail_button = Label(admin_frame, text="Gmail")
    adgmail_button.config(
        fg="#bfff00",
        bg="#390879",
        font=("Times New Roman", 20, "italic bold "))
    adgmail_button.place(x=600, y=147)
    adgmail_entry = Entry(admin_frame)
    adgmail_entry.config(bg="#390879",
                       fg="black",
                       font=("Times New Roman", 18, "italic  "),
                       width=24
                       )
    adgmail_entry.place(x=600, y=180)

    adpassword_button = Label(admin_frame, text="Password")
    adpassword_button.config(bg="#390879",
        fg="#bfff00",
        font=("Times New Roman", 20, "italic bold "))
    adpassword_button.place(x=600, y=230)

    x = IntVar()
    def show():
        print(x.get())
        if x.get() == 1:
            password_entry.config(show="")
        else:
            password_entry.config(show="*")

    password_entry = Entry(window, show="*")
    password_entry.config(bg="#390879",
                          fg="#bfff00",
                          font=("Times New Roman", 19, "italic bold"),
                          width=22)
    password_entry.place(x=600, y=265)
    chekbtn2 = Checkbutton(window, text="Show password", variable=x, command=show)
    chekbtn2.config(bg="#390879", width=22,height=1,fg="#bfff00")
    chekbtn2.place(x=650, y=310)

    def Back4():
        aduser()


    # view
    back_button = Button(admin_frame, text="Back", command=Back4)
    back_button.config(bg="#390879",fg="#bfff00",font="bold",width=10,height=1)
    back_button.place(x=10, y=10)


def Sign_up():
    start_frame = Frame(window, width=1500, height=900)
    start_frame.place(x=0, y=0)
    start_frame.config(bg="#390879")
    # from PIL import ImageTk, Image
    # image = Image.open(r"icon_images2\hotel.jpg")
    # resize_image = image.resize((1500, 900))
    # img = ImageTk.PhotoImage(resize_image)
    # label1 = Label(image=img)
    # label1.image = img
    # label1.place(x=0, y=0)

    def Sign_in2():
        gmail_get = gmail_entry.get()
        password_get = password_entry.get()
        confirm_get = confirm_entry.get()
        if gmail_get == "" or password_get == "" or confirm_get == "":  # or "@gmail.com" not in gmail_get:
            messagebox.showerror("error", "pusto")
        elif "@gmail.com" not in gmail_get:
            messagebox.showerror("error", "neverniy gmail")
        elif confirm_get != password_get:
            messagebox.showerror("error", "neverniy confirm")
        else:
            with open("account.txt", "a") as file:
                file.write(f"{gmail_get}:{password_get}\n")
            messagebox.showinfo(message="reqistraciya uspeshna")
            Sign_in_frame()

    registrator_label = Label(start_frame, text="Registration")
    registrator_label.config(fg="white",bg="#390879",
                             font=("Times New Roman", 24, "italic bold "))
    registrator_label.place(x=660, y=20)
    # login
    login_button = Label(start_frame, text="Username")
    login_button.config(bg="#390879",fg="white",
        font=("Times New Roman", 20, "italic bold "))
    login_button.place(x=670, y=100)
    login_entry = Entry(start_frame)
    login_entry.config(
        bg="#390879",
        fg="black",
        font=("Times New Roman", 18, "italic bold"),
        width=24
    )
    login_entry.place(x=600, y=135)
    # password
    password_button = Label(start_frame, text="Password")
    password_button.config(bg="#390879",fg="white",
        font=("Times New Roman", 22, "italic bold "))
    password_button.place(x=670, y=260)

    sign_in = Button(start_frame, text="Register", command=Sign_in2)
    sign_in.config(
        width=14,
        height=2,
        activeforeground="#d2dbea", bg="#390879",fg="white",font="bold")
    sign_in.place(x=667, y=480)
    confirm_button = Label(start_frame, text="Confirm")
    confirm_button.config(bg="#390879",fg="white",
        font=("Times New Roman", 24, "italic bold "))
    confirm_button.place(x=670, y=350)
    gmail_label = Label(start_frame, text="Gmail")
    gmail_label.config(bg="#390879",fg="white",font=("Times New Roman", 20, "italic bold "))
    gmail_label.place(x=690, y=175)
    gmail_entry = Entry(start_frame)
    gmail_entry.config(
        bg="#390879",
        fg="black",
        font=("Times New Roman", 18, "italic bold"),
        width=24
    )
    gmail_entry.place(x=600, y=210)

    x = IntVar()

    #
    def show():
        print(x.get())
        if x.get() == 1:
            confirm_entry.config(show="*")
            password_entry.config(show="*")
        else:
            confirm_entry.config(show="")
            password_entry.config(show="")

    confirm_entry = Entry(window, show="*")
    confirm_entry.config(bg="#390879",
                         fg="black",
                         font=("Times New Roman", 18, "italic bold"),
                         width=24)
    confirm_entry.place(x=600, y=390)
    password_entry = Entry(window, show="*")
    password_entry.config(bg="#390879",
                          fg="black",
                          font=("Times New Roman", 18, "italic bold"),
                          width=24)
    password_entry.place(x=600, y=300)
    chekbtn = Checkbutton(window, text="Show password", variable=x, command=show)
    chekbtn.config(bg="#390879",fg="white",width=14,height=1,font="bold")
    chekbtn.place(x=660, y=435)


    # view
    # control
    def Back():
        Sign_in_frame()


    # view
    back_button = Button(start_frame, text="Already have an account", command=Back)
    back_button.config(bg="#390879",fg="white" ,font="bold")
    back_button.place(x=638, y=550)



def finish_frame(gmail,password):
    finish_frame = Frame(window, width=1500, height=900)
    finish_frame.place(x=0, y=0)



    def Back():
        Sign_in_frame()
    Back = Button(finish_frame,text="Back to sign",command=Back)
    Back.config(fg="white",bg="brown",width=10,height=1,font="bold")
    Back.place(x=10,y=10)

    def korzinka():
        korzina_frame(gmail,password)

    def buy1():
        with open("otel.txt", "a") as file1:
            with open("otel.txt", "r") as file:
                account = file.read()
                if "\nReview 7.6 - well \nPrice: 207 manat - one night\nHilton***" in account:
                    messagebox.showerror("error","Уже добавили")
                else:
                    file1.write("\nReview 7.6 - well \nPrice: 207 manat - one night\nHilton***")
                    messagebox.showinfo("Added","Успешно добавлено")

    def buy2():
        with open("otel.txt", "a") as file1:
            with open("otel.txt", "r") as file:
                account = file.read()
                if "\nReview 8.5 - Very well\nPrice: 244 manat - one night\nEurope***" in account:
                    messagebox.showerror("error", "Уже добавили")
                else:
                    file1.write("\nReview 8.5 - Very well\nPrice: 244 manat - one night\nEurope***")
                    messagebox.showinfo("Added", "Успешно добавлено")

    def buy3():
        with open("otel.txt", "a") as file1:
            with open("otel.txt", "r") as file:
                account = file.read()
                if "\nReview 6.9 - Well enough\nPrice: 170 manat - one night\nThe Venetian***" in account:
                    messagebox.showerror("error", "Уже добавили")
                else:
                    file1.write("\nReview 6.9 - Well enough\nPrice: 170 manat - one night\nThe Venetian***")
                    messagebox.showinfo("Added", "Успешно добавлено")

    def buy4():
        with open("otel.txt", "a") as file1:
            with open("otel.txt", "r") as file:
                account = file.read()
                if "\nReview 8.2 - Very well\nPrice: 228 manat - one night\nLas Vegas***" in account:
                    messagebox.showerror("error", "Уже добавили")
                else:
                    file1.write("\nReview 8.2 - Very well\nPrice: 228 manat - one night\nLas Vegas***")
                    messagebox.showinfo("Added", "Успешно добавлено")

    def buy5():
        with open("otel.txt", "a") as file1:
            with open("otel.txt", "r") as file:
                account = file.read()
                if "\nReview:9\nPrice:300 manat\nDubai\n" in account:
                    messagebox.showerror("error", "Уже добавили")
                else:
                    file1.write("\nReview:9\nPrice:300 manat\nDubai\n")
                    messagebox.showinfo("Added", "Успешно добавлено")



    frame1=Frame(finish_frame,bg="white",width=250,height=150,highlightbackground="black",highlightthickness=1)
    frame1.place(x=300,y=150)
    review1 = Label(frame1, text="Review 7.6 ",bg="white")
    review1.config(fg="black", font="bold")
    review1.place(x=70, y=10)
    buy1 = Button(frame1, text="Buy", fg="white", command=buy1)
    buy1.config(font="bold", bg="blue")
    buy1.place(x=10, y=100)
    price1 = Label(frame1, text="Price: 207 manat",bg="white")
    price1.config(fg="black", font="bold")
    price1.place(x=50, y=50)
    label1 = Label(frame1, text="Hilton***",bg="white")
    label1.config(fg="black", font=("bold underline",15))
    label1.place(x=160, y=110)

    frame2 = Frame(finish_frame, bg="white", width=250, height=150, highlightbackground="black", highlightthickness=1)
    frame2.place(x=650, y=150)
    review2 = Label(frame2, text="Review 8.5 ",bg="white")
    review2.config(fg="black", font="bold")
    review2.place(x=70, y=10)
    price2 = Label(frame2, text="Price: 244 manat",bg="white")
    price2.config(fg="black", font="bold")
    price2.place(x=50, y=50)
    buy2 = Button(frame2, text="Buy", fg="white",command=buy2)
    buy2.config(font="bold", bg="blue")
    buy2.place(x=10, y=100)
    label2 = Label(frame2, text="Europe***",bg="white")
    label2.config(fg="black", font=("bold underline",15))
    label2.place(x=150, y=110)

    frame3 = Frame(finish_frame, bg="white", width=250, height=150, highlightbackground="black", highlightthickness=1)
    frame3.place(x=1000, y=150)
    review2 = Label(frame3, text="Review 6.9",bg="white")
    review2.config(fg="black", font="bold")
    review2.place(x=70, y=10)
    price2 = Label(frame3, text="Price: 170 manat", bg="white")
    price2.config(fg="black", font="bold")
    price2.place(x=50, y=50)
    buy2 = Button(frame3, text="Buy", fg="white", command=buy3)
    buy2.config(font="bold", bg="blue")
    buy2.place(x=10, y=100)
    label2 = Label(frame3, text="The Venetian***", bg="white")
    label2.config(fg="black", font=("bold underline", 15))
    label2.place(x=100, y=110)



    frame4 = Frame(finish_frame, bg="white", width=250, height=150, highlightbackground="black", highlightthickness=1)
    frame4.place(x=300, y=400)
    review2 = Label(frame4, text="Review 8.2",bg="white")
    review2.config(fg="black", font="bold")
    review2.place(x=70, y=10)
    price2 = Label(frame4, text="Price: 228 manat", bg="white")
    price2.config(fg="black", font="bold")
    price2.place(x=50, y=50)
    buy2 = Button(frame4, text="Buy", fg="white", command=buy4)
    buy2.config(font="bold", bg="blue")
    buy2.place(x=10, y=100)
    label2 = Label(frame4, text="Las Vegas***", bg="white")
    label2.config(fg="black", font=("bold underline", 15))
    label2.place(x=120, y=110)

    frame5 = Frame(finish_frame, bg="white", width=250, height=150, highlightbackground="black", highlightthickness=1)
    frame5.place(x=650, y=400)
    review2 = Label(frame5, text="Review:9", bg="white")
    review2.config(fg="black", font="bold")
    review2.place(x=10, y=10)
    price2 = Label(frame5, text="Price:300 manat", bg="white")
    price2.config(fg="black", font="bold")
    price2.place(x=10, y=50)
    buy2 = Button(frame5, text="Buy", fg="white", command=buy5)
    buy2.config(font="bold", bg="blue")
    buy2.place(x=10, y=100)
    label2 = Label(frame5, text="Dubai", bg="white")
    label2.config(fg="black", font=("bold underline", 15))
    label2.place(x=100, y=110)


    korzina = Button(finish_frame, text="ticket", command=korzinka)
    korzina.config(fg="white", bg="blue", font="bold", height=1)
    korzina.place(x=10, y=250)

    with open("account.txt","r")as file:
        remember=file.read()
        if f"{gmail}:{password}" not in remember:
            add_button = Button(finish_frame,text="Add",command=Add_frame)
            add_button.config(fg="white",bg="brown")
            add_button.place(x=10,y=100)



def Star_frame2():
    start_frame2 = Frame(window, width=1028, height=768)
    start_frame2.place(x=0, y=0)

    def Back():
        Sign_in_frame()

    # def next():
    #     finish_frame(gmail,password)

    # view
    back_button = Button(start_frame2, text="Back", command=Back)
    back_button.config(bg="red", fg="black")
    back_button.place(x=30, y=150)
    back_button = Button(start_frame2, text="next", command=next)
    back_button.config(bg="red", fg="white")
    back_button.place(x=200, y=150)
    welcome_label = Label(start_frame2, text="Welcome")
    welcome_label.config(bg="black",
                         fg="#ff3399",
                         font=("Times New Roman", 16, "italic bold "))
    welcome_label.place(x=200, y=100)





Sign_in_frame()


def korzina_frame(gmail,password):
    korzina_frame = Frame(window, width=1500, height=900)
    korzina_frame.place(x=0, y=0)
    with open("otel.txt","a") as file:
        with open("otel.txt","r")as file2:
            read=file2.read()
            if "\nReview 7.6 - well \nPrice: 207 manat - one night\nHilton***" in read:
                frame1 = Frame(korzina_frame, bg="white", width=250, height=150, highlightbackground="black",
                               highlightthickness=1)
                frame1.place(x=300, y=150)
                review1 = Label(frame1, text="Review 7.6 ", bg="white")
                review1.config(fg="black", font="bold")
                review1.place(x=70, y=10)
                price1 = Label(frame1, text="Price: 207 manat", bg="white")
                price1.config(fg="black", font="bold")
                price1.place(x=50, y=50)
                label1 = Label(frame1, text="Hilton***", bg="white")
                label1.config(fg="black", font=("bold underline", 15))
                label1.place(x=160, y=110)
            if "\nReview 8.5 - Very well\nPrice: 244 manat - one night\nEurope***" in read:
                frame2 = Frame(korzina_frame, bg="white", width=250, height=150, highlightbackground="black",
                               highlightthickness=1)
                frame2.place(x=650, y=150)
                review2 = Label(frame2, text="Review 8.5 ", bg="white")
                review2.config(fg="black", font="bold")
                review2.place(x=70, y=10)
                price2 = Label(frame2, text="Price: 244 manat", bg="white")
                price2.config(fg="black", font="bold")
                price2.place(x=50, y=50)
                label2 = Label(frame2, text="Europe***", bg="white")
                label2.config(fg="black", font=("bold underline", 15))
                label2.place(x=150, y=110)
            if "\nReview 6.9 - Well enough\nPrice: 170 manat - one night\nThe Venetian***" in read:
                frame3 = Frame(korzina_frame, bg="white", width=250, height=150, highlightbackground="black",
                               highlightthickness=1)
                frame3.place(x=1000, y=150)
                review2 = Label(frame3, text="Review 6.9", bg="white")
                review2.config(fg="black", font="bold")
                review2.place(x=70, y=10)
                price2 = Label(frame3, text="Price: 170 manat", bg="white")
                price2.config(fg="black", font="bold")
                price2.place(x=50, y=50)
                label2 = Label(frame3, text="The Venetian***", bg="white")
                label2.config(fg="black", font=("bold underline", 15))
                label2.place(x=100, y=110)
            if "\nReview 8.2 - Very well\nPrice: 228 manat - one night\nLas Vegas***" in read:
                frame4 = Frame(korzina_frame, bg="white", width=250, height=150, highlightbackground="black",
                               highlightthickness=1)
                frame4.place(x=300, y=400)
                review2 = Label(frame4, text="Review 8.2", bg="white")
                review2.config(fg="black", font="bold")
                review2.place(x=70, y=10)
                price2 = Label(frame4, text="Price: 228 manat", bg="white")
                price2.config(fg="black", font="bold")
                price2.place(x=50, y=50)
                label2 = Label(frame4, text="Las Vegas***", bg="white")
                label2.config(fg="black", font=("bold underline", 15))
                label2.place(x=120, y=110)
            if "\nReview:9\nPrice:300 manat\nDubai\n" in read:
                frame5 = Frame(korzina_frame, bg="white", width=250, height=150, highlightbackground="black",
                               highlightthickness=1)
                frame5.place(x=650, y=400)
                review2 = Label(frame5, text="Review:9", bg="white")
                review2.config(fg="black", font="bold")
                review2.place(x=10, y=10)
                price2 = Label(frame5, text="Price:300 manat", bg="white")
                price2.config(fg="black", font="bold")
                price2.place(x=10, y=50)

                label2 = Label(frame5, text="Dubai", bg="white")
                label2.config(fg="black", font=("bold underline", 15))
                label2.place(x=100, y=110)


        def back():
            finish_frame(gmail,password)

    back = Button(korzina_frame,text="Back",command=back)
    back.config(fg="white",bg="brown",font="bold",height=3)
    back.place(x=10,y=10)


def Add_frame():
    Add_frame = Frame(window, width=1500, height=900)
    Add_frame.place(x=0, y=0)

    def back1():
        finish_frame(gmail="elmin-admin",password="elmin2008")
    back = Button(Add_frame,text="Back",command=back1)
    back.config(fg="white",bg="brown",font="bold",height=3)
    back.place(x=10,y=10)

    def sign_in3():
        name_get = name_entry.get()
        review_get = review_entry.get()
        price_get = price_entry.get()
        if name_get == "" or review_get == "" or price_get == "":
            messagebox.showerror("error", "pustoo")
        else:
            with open("otel.txt", "a") as file:
                with open("otel.txt", "r") as file1:
                    remember=file1.read()
                    if f"\n{name_get}\n{review_get}\n{price_get}\n" in remember:
                        messagebox.showerror("error","Такое уже есть")
                    else:

                        file.write(f"\n{name_get}\n{review_get}\n{price_get}\n")
            messagebox.showinfo(message="reqistraciya uspeshna")
            Sign_in_frame()

    name_entry = Entry(Add_frame)
    name_entry.config(bg="white",
        fg="black",
        font=("Times New Roman", 18, "italic bold"),
        width=24)
    name_entry.place(x=900,y=130)

    name = Label(Add_frame,text="Введите название отеля которую хотите добавить: ")
    name.config(fg="black", font="bold")
    name.place(x=400,y=130)

    review = Label(Add_frame,text="Введите оценку отеля: ")
    review.config(fg="black", font="bold")
    review.place(x=400, y=180)

    review_entry = Entry(Add_frame)
    review_entry.config(bg="white",
                 fg="black",
                 font=("Times New Roman", 18, "italic bold"),
                 width=24)
    review_entry.place(x=640, y=180)

    price = Label(Add_frame,text="Введите стоимость отеля: ")
    price.config(fg="black", font="bold")
    price.place(x=400, y=230)

    price_entry = Entry(Add_frame)
    price_entry.config(bg="white",
                  fg="black",
                  font=("Times New Roman", 18, "italic bold"),
                  width=24)
    price_entry.place(x=670, y=230)

    labl4 = Label(Add_frame,text="Add Hotel")
    labl4.config(fg="black",font=("Comic Sans MS",24,"italic bold "))
    labl4.place(x=700,y=10)

    add_hotel = Button(Add_frame,text="Add Hotel",command=sign_in3)
    add_hotel.config(bg="red",fg="white",font="bold")
    add_hotel.place(x=700,y=330)
window.mainloop()