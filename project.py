from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
window = Tk()
window.title("Hotel Bron By ELmIn")
window.geometry("1500x1000+10+10")
window.option_add("*tearOff", FALSE)
window.iconbitmap("foto/icon")
hotels = [{"name": "Hilton", "review": "7.6 - Хорошо", "price": "207 manat - За ночь"},
          {"name": "Europe", "review": "8.5 - Очень Хорошо", "price": "244 manat - За ночь"},
          {"name": "The Venetian", "review": "6.9- Достаточно хорошо", "price": "170 manat - За ночь"}
          ]
hotels_letter = []
def Sign_in_frame():
    sign_in_frame = Frame(window, width=1500, height=900)
    sign_in_frame.place(x=0, y=0)
    sign_in_frame.config(bg="#390879")

    image = Image.open(r"foto\signin.jpg")
    resize_image = image.resize((200, 200))
    img = ImageTk.PhotoImage(resize_image)
    label1 = Label(image=img)
    label1.image = img
    label1.config(bg="#390879")
    label1.place(x=1000, y=300)




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
                        Finish_frame(gmail_get,password_get)
                        estno = 1
                if estno == 0:
                    messagebox.showerror("error", "ne pravilno vveli")

    gmail_label = Label(sign_in_frame, text="Gmail")
    gmail_label.config(bg="#390879",
                    fg="#bfff00",

            font=("Times New Roman", 24, "italic bold "))
    gmail_label.place(x=600, y=135)
    gmail_entry = Entry(sign_in_frame)
    gmail_entry.config(bg="white",
                       fg="black",
                       font=("Times New Roman", 19, "bold"),
                       width=24
                       )
    gmail_entry.place(x=600, y=170)
    password_label = Label(sign_in_frame, text="Password")
    password_label.config(
        bg="#390879",
        fg="#bfff00",
        font=("Times New Roman", 24, "italic bold "))
    password_label.place(x=600, y=219)

    sign_in_button = Button(sign_in_frame, text="sign in", command=Sign_in)
    sign_in_button.config(
            fg="black",
            bg="#bfff00"
             ,
            width=15,
            height=2,
            font=("Times New Roman", 18, "bold "))
    sign_in_button.place(x=640, y=350)
    sign_up_button = Button(sign_in_frame, text="Need to create an account ?", command=admin_user)
    sign_up_button.config(fg="black",
                   bg="#bfff00",
                   width=20,
                   height=1,
                   font=("Times New Roman", 18, " bold "))
    sign_up_button.place(x=600, y=440)
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
                          font=("Times New Roman", 19, "bold"),
                          width=22)
    password_entry.place(x=600, y=255)
    chekbtn_show = Checkbutton(sign_in_frame, text="Show password", variable=x, command=show)
    chekbtn_show.config(bg="#bfff00",fg="black",font=("Times New Roman", 18, "bold "))
    chekbtn_show.place(x=650, y=300)
    sign_in_label = Label(sign_in_frame, text="Sign in")
    sign_in_label.config(bg="#390879",
        fg="#bfff00",
        font=("Times New Roman", 30, " bold "))
    sign_in_label.place(x=680, y=80)

def admin_user():
    admin_user = Frame(window, width=1500, height=900)
    admin_user.place(x=0, y=0)
    admin_user.config(bg="#390879")


    vibor_label = Label(admin_user,text="Войти как:")
    vibor_label.config(fg="#bfff00",bg="#390879",font=("Times New Roman", 26, "italic bold ",))
    vibor_label.place(x=650,y=200)

    admin_button = Button(admin_user,text="Admin",command=Admin_frame)
    admin_button.config(bg="#390879",fg="#bfff00",font="bold",width=14,height=3)
    admin_button.place(x=530,y=300)

    user_button = Button(admin_user,text="User",command=Sign_up)
    user_button.config(bg="#390879",fg="#bfff00",font="bold",width=14,height=3)
    user_button.place(x=800,y=300)

    def Back_to_sign():
        Sign_in_frame()


    # view
    back_button = Button(admin_user, text="Back", command=Back_to_sign)
    back_button.config(bg="#390879",fg="#bfff00",font="bold",width=10,height=1)
    back_button.place(x=10, y=10)

def Admin_frame():
    admin_frame = Frame(window,width=1500,height=900)
    admin_frame.place(x=0,y=0)
    admin_frame.config(bg="#390879")
    def admin_in():
        gmail_get = gmail_entry.get()
        password_get = password_entry.get()
        print(f"{gmail_get}:{password_get}")
        if gmail_get == "elmin-admin" and password_get == "elmin2008":
            Finish_frame(gmail_get,password_get)
        elif gmail_get == "" or password_get == "":
            messagebox.showerror(title="error", message="pustoooo")
        else:
            messagebox.showerror(title="error", message="Wrong login or password")

    sign_in_button = Button(admin_frame, text="sign in", command=admin_in)
    sign_in_button.config(
        fg="#bfff00",
        bg="#390879",
        font=("bold"),
        width=15,
        height=2,
                    )
    sign_in_button.place(x=650, y=350)

    admin_label = Label(admin_frame,text="Admin sign")
    admin_label.config(fg="#bfff00",font=("Times New Roman", 30, " bold "),bg="#390879")
    admin_label.place(x=640,y=70)


    gmail_label = Label(admin_frame, text="Gmail")
    gmail_label.config(
        fg="#bfff00",
        bg="#390879",
        font=("Times New Roman", 20, "italic bold "))
    gmail_label.place(x=600, y=147)
    gmail_entry = Entry(admin_frame)
    gmail_entry.config(bg="#390879",
                       fg="white",
                       font=("Times New Roman", 19, "bold"),
                       width=24
                       )
    gmail_entry.place(x=600, y=180)

    password_label = Label(admin_frame, text="Password")
    password_label.config(bg="#390879",
                          fg="#bfff00",
                          font=("Times New Roman", 20, "bold"))
    password_label.place(x=600, y=230)

    x = IntVar()
    def show():
        print(x.get())
        if x.get() == 1:
            password_entry.config(show="")
        else:
            password_entry.config(show="*")

    password_entry = Entry(window, show="*")
    password_entry.config(bg="#390879",
                          fg="white",
                          font=("Times New Roman", 19, "bold"),
                          width=24)
    password_entry.place(x=600, y=265)
    chekbtn_show = Checkbutton(window, text="Show password", variable=x, command=show)
    chekbtn_show.config(bg="#390879", width=22,font="bold",height=1,fg="#bfff00")
    chekbtn_show.place(x=630, y=310)

    def Back_to_admin_user():
        admin_user()


    # view
    back_button = Button(admin_frame, text="Back", command=Back_to_admin_user)
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

    def Registration():
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

    registration_label = Label(start_frame, text="Registration")
    registration_label.config(fg="white",bg="#390879",
                             font=("Times New Roman", 24, "italic bold "))
    registration_label.place(x=660, y=20)
    # login
    username_label = Label(start_frame, text="Username")
    username_label.config(bg="#390879",fg="white",
                          font=("Times New Roman", 20, "italic bold "))
    username_label.place(x=670, y=100)
    username_entry = Entry(start_frame)
    username_entry.config(
                            bg="#390879",
                            fg="white",
                            font=("Times New Roman", 18, "italic bold"),
                            width=24
                                )
    username_entry.place(x=600, y=135)
    # password
    password_label = Label(start_frame, text="Password")
    password_label.config(bg="#390879",fg="white",
                          font=("Times New Roman", 22, "italic bold "))
    password_label.place(x=670, y=260)

    register_button = Button(start_frame, text="Register", command=Registration)
    register_button.config(
                            width=14,
                            height=2,
                            activeforeground="#d2dbea", bg="#390879",fg="white",font="bold")
    register_button.place(x=667, y=480)

    confirm_label = Label(start_frame, text="Confirm")
    confirm_label.config(bg="#390879",fg="white",
                         font=("Times New Roman", 24, "italic bold "))
    confirm_label.place(x=670, y=350)

    gmail_label = Label(start_frame, text="Gmail")
    gmail_label.config(bg="#390879",fg="white",font=("Times New Roman", 20, "italic bold "))
    gmail_label.place(x=690, y=175)
    gmail_entry = Entry(start_frame)
    gmail_entry.config(
        bg="#390879",
        fg="white",
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
                         fg="white",
                         font=("Times New Roman", 18, "italic bold"),
                         width=24)
    confirm_entry.place(x=600, y=390)
    password_entry = Entry(window, show="*")
    password_entry.config(bg="#390879",
                          fg="white",
                          font=("Times New Roman", 18, "italic bold"),
                          width=24)
    password_entry.place(x=600, y=300)
    chekbtn_show = Checkbutton(window, text="Show password", variable=x, command=show)
    chekbtn_show.config(bg="#390879",fg="white",width=14,height=1,font="bold")
    chekbtn_show.place(x=660, y=435)


    # view
    # control
    def Back_to_sign_in():
        Sign_in_frame()


    # view
    back_button = Button(start_frame, text="Already have an account", command=Back_to_sign_in)
    back_button.config(bg="#390879",fg="white" ,font="bold")
    back_button.place(x=638, y=550)



def Finish_frame(gmail,password):
    finish_frame = Frame(window, width=1500, height=900)
    finish_frame.place(x=0, y=0)
    finish_frame.config(bg="#390879")

    def Back_to_sign_in():
        Sign_in_frame()

    Back_button = Button(finish_frame, text="Back", command=Back_to_sign_in)
    Back_button.config(fg="#bfff00", bg="#390879", width=7, height=1, font="bold")
    Back_button.place(x=10, y=10)

    def korzina():
        korzina_frame(gmail,password)

    korzina_button = Button(finish_frame, text="Korzina", command=korzina)
    korzina_button.config(fg="#bfff00", bg="#390879", font="bold", width=14, height=3)
    korzina_button.place(x=10, y=430)


    def buy(index):
        global hotels_letter
        global hotels
        have=0


        for i in hotels_letter:
            if i["name"]==index["name"]:
                have=1
                messagebox.showerror("Ошибка", "Он уже добавлен")

        if have==0:
            messagebox.showinfo("Added", "Добавлено в корзинку")
            hotels_letter.append({"name": index["name"], "review": index["review"], "price": index["price"]})

        print(hotels_letter)
    def buy1():
        buy(hotels[0])

    def buy2():
        buy(hotels[1])

    def buy3():
        buy(hotels[2])

    def buy4():
        buy(hotels[3])

    def buy5():
        buy(hotels[4])

    frame1 = Frame(finish_frame,bg="white",width=250,height=150,highlightbackground="black",highlightthickness=1)
    frame1.place(x=300,y=150)
    review1 = Label(frame1, text= hotels[0]["review"],bg="white")
    review1.config(fg="black", font=("bold"))
    review1.place(x=10, y=10)
    buy1 = Button(frame1, text="Buy", fg="white", command=buy1)
    buy1.config(font="bold", bg="blue")
    buy1.place(x=10, y=100)
    price1 = Label(frame1, text=hotels[0]["price"],bg="white")
    price1.config(fg="black", font="bold")
    price1.place(x=10, y=50)
    label1 = Label(frame1, text=hotels[0]["name"],bg="white")
    label1.config(fg="black", font=("bold underline",15))
    label1.place(x=160, y=110)

    frame2 = Frame(finish_frame, bg="white", width=250, height=150, highlightbackground="black", highlightthickness=1)
    frame2.place(x=650, y=150)
    review2 = Label(frame2, text=hotels[1]["review"],bg="white")
    review2.config(fg="black", font="bold")
    review2.place(x=10, y=10)
    price2 = Label(frame2, text=hotels[1]["price"],bg="white")
    price2.config(fg="black", font="bold")
    price2.place(x=10, y=50)
    buy2 = Button(frame2, text="Buy", fg="white",command=buy2)
    buy2.config(font="bold", bg="blue")
    buy2.place(x=10, y=100)
    label2 = Label(frame2, text=hotels[1]["name"],bg="white")
    label2.config(fg="black", font=("bold underline",15))
    label2.place(x=150, y=110)

    frame3 = Frame(finish_frame, bg="white", width=250, height=150, highlightbackground="black", highlightthickness=1)
    frame3.place(x=1000, y=150)
    review2 = Label(frame3, text=hotels[2]["review"],bg="white")
    review2.config(fg="black", font="bold")
    review2.place(x=10, y=10)
    price2 = Label(frame3, text=hotels[2]["price"], bg="white")
    price2.config(fg="black", font="bold")
    price2.place(x=10, y=50)
    buy2 = Button(frame3, text="Buy", fg="white", command=buy3)
    buy2.config(font="bold", bg="blue")
    buy2.place(x=10, y=100)
    label2 = Label(frame3, text=hotels[2]["name"], bg="white")
    label2.config(fg="black", font=("bold underline", 15))
    label2.place(x=100, y=110)

    if len(hotels)==4:
        frame4 = Frame(finish_frame, bg="white", width=250, height=150, highlightbackground="black",
                       highlightthickness=1)
        frame4.place(x=300, y=400)
        review1 = Label(frame4, text=hotels[3]["review"], bg="white")
        review1.config(fg="black", font=("bold"))
        review1.place(x=10, y=10)
        buy1 = Button(frame4, text="Buy", fg="white", command=buy4)
        buy1.config(font="bold", bg="blue")
        buy1.place(x=10, y=100)
        price1 = Label(frame4, text=hotels[3]["price"], bg="white")
        price1.config(fg="black", font="bold")
        price1.place(x=10, y=50)
        label1 = Label(frame4, text=hotels[3]["name"], bg="white")
        label1.config(fg="black", font=("bold underline", 15))
        label1.place(x=100, y=110)
    if len(hotels) == 5:
        frame4 = Frame(finish_frame, bg="white", width=250, height=150, highlightbackground="black",
                       highlightthickness=1)
        frame4.place(x=300, y=400)
        review1 = Label(frame4, text=hotels[3]["review"], bg="white")
        review1.config(fg="black", font=("bold"))
        review1.place(x=10, y=10)
        buy1 = Button(frame4, text="Buy", fg="white", command=buy4)
        buy1.config(font="bold", bg="blue")
        buy1.place(x=10, y=100)
        price1 = Label(frame4, text=hotels[3]["price"], bg="white")
        price1.config(fg="black", font="bold")
        price1.place(x=10, y=50)
        label1 = Label(frame4, text=hotels[3]["name"], bg="white")
        label1.config(fg="black", font=("bold underline", 15))
        label1.place(x=100, y=110)

        frame5 = Frame(finish_frame, bg="white", width=250, height=150, highlightbackground="black",
                       highlightthickness=1)
        frame5.place(x=650, y=400)
        review1 = Label(frame5, text=hotels[4]["review"], bg="white")
        review1.config(fg="black", font=("bold"))
        review1.place(x=10, y=10)
        buy1 = Button(frame5, text="Buy", fg="white", command=buy5)
        buy1.config(font="bold", bg="blue")
        buy1.place(x=10, y=100)
        price1 = Label(frame5, text=hotels[4]["price"], bg="white")
        price1.config(fg="black", font="bold")
        price1.place(x=10, y=50)
        label1 = Label(frame5, text=hotels[4]["name"], bg="white")
        label1.config(fg="black", font=("bold underline", 15))
        label1.place(x=100, y=110)
    if len(hotels) > 5:
        messagebox.showerror("error","Переполнено")
        frame4 = Frame(finish_frame, bg="white", width=250, height=150, highlightbackground="black",
                       highlightthickness=1)
        frame4.place(x=300, y=400)
        review1 = Label(frame4, text=hotels[3]["review"], bg="white")
        review1.config(fg="black", font=("bold"))
        review1.place(x=10, y=10)
        buy1 = Button(frame4, text="Buy", fg="white", command=buy4)
        buy1.config(font="bold", bg="blue")
        buy1.place(x=10, y=100)
        price1 = Label(frame4, text=hotels[3]["price"], bg="white")
        price1.config(fg="black", font="bold")
        price1.place(x=10, y=50)
        label1 = Label(frame4, text=hotels[3]["name"], bg="white")
        label1.config(fg="black", font=("bold underline", 15))
        label1.place(x=100, y=110)

        frame5 = Frame(finish_frame, bg="white", width=250, height=150, highlightbackground="black",
                       highlightthickness=1)
        frame5.place(x=650, y=400)
        review1 = Label(frame5, text=hotels[4]["review"], bg="white")
        review1.config(fg="black", font=("bold"))
        review1.place(x=10, y=10)
        buy1 = Button(frame5, text="Buy", fg="white", command=buy5)
        buy1.config(font="bold", bg="blue")
        buy1.place(x=10, y=100)
        price1 = Label(frame5, text=hotels[4]["price"], bg="white")
        price1.config(fg="black", font="bold")
        price1.place(x=10, y=50)
        label1 = Label(frame5, text=hotels[4]["name"], bg="white")
        label1.config(fg="black", font=("bold underline", 15))
        label1.place(x=100, y=110)


    def Add():
        Add_frame(gmail,password)

    def Edit():
        Edit_frame(gmail,password)

    def Delete():
        Delete_frame(gmail,password)

    if gmail == "elmin-admin" and password == "elmin2008":
        add_button = Button(finish_frame,text="Add",command=Add)
        add_button.config(fg="#bfff00",bg="#390879",font="bold",width=14,height=3)
        add_button.place(x=10,y=100)

        edit_button = Button(finish_frame,text="Edit",command=Edit)
        edit_button.config(fg="#bfff00",bg="#390879",font="bold",width=14,height=3)
        edit_button.place(x=10,y=210)

        delete_button = Button(finish_frame, text="Delete", command=Delete)
        delete_button.config(fg="#bfff00", bg="#390879",font="bold",width=14,height=3)
        delete_button.place(x=10, y=320)


def Star_frame2():
    start_frame2 = Frame(window, width=1028, height=768)
    start_frame2.place(x=0, y=0)

    def Back():
        Sign_in_frame()


    # view
    back_button = Button(start_frame2, text="Back", command=Back)
    back_button.config(bg="red", fg="black")
    back_button.place(x=30, y=150)

    welcome_label = Label(start_frame2, text="Welcome")
    welcome_label.config(bg="black",
                         fg="#ff3399",
                         font=("Times New Roman", 16, "italic bold "))
    welcome_label.place(x=200, y=100)

Sign_in_frame()


def korzina_frame(gmail,password):
    korzina_frame = Frame(window, width=1500, height=900)
    korzina_frame.place(x=0, y=0)
    korzina_frame.config(bg="#390879")


    def Back_to_finish_frame():
        Finish_frame(gmail,password)
    def buy(index):
        global hotels_letter
        global hotels
        have=0


        for i in hotels_letter:
            if i["name"]==index["name"]:
                have=1
                messagebox.showerror("Ошибка", "Он уже добавлен")

        if have==0:
            messagebox.showinfo("Added", "Добавлено в корзинку")
            hotels_letter.append({"name": index["name"], "review": index["review"], "price": index["price"]})

        print(hotels_letter)

    def close(index):
        global hotels_letter
        for i in hotels_letter:
            if i["name"] == index["name"]:
                hotels_letter.remove(i)
                messagebox.showinfo("deleted", "Успешно удален")
                Finish_frame(gmail, password)

    def close1():
        close(hotels_letter[0])

    def close2():
        close(hotels_letter[1])

    def close3():
        close(hotels_letter[2])

    def close4():
        close(hotels_letter[3])

    def close5():
        close(hotels_letter[4])

    Back_button = Button(korzina_frame, text="Back", command=Back_to_finish_frame)
    Back_button.config(fg="#bfff00", bg="#390879", width=7, height=1, font="bold")
    Back_button.place(x=10, y=10)

    korzina_label = Label(text="Корзина")
    korzina_label.config(bg="#390879",fg="#bfff00",font=("Times New Roman", 34, "italic bold "))
    korzina_label.place(x=620,y=30)




    if len(hotels_letter) == 1:
        frame1 = Frame(korzina_frame,bg="white",width=250,height=150,highlightbackground="black",highlightthickness=1)
        frame1.place(x=300,y=150)
        review1 = Label(frame1, text=hotels_letter[0]["review"],bg="white")
        review1.config(fg="black", font="bold")
        review1.place(x=10, y=10)
        buy1 = Button(frame1, text="Х", fg="white", command=close1)
        buy1.config(font="bold", bg="blue")
        buy1.place(x=10, y=100)
        price1 = Label(frame1, text=hotels_letter[0]["price"],bg="white")
        price1.config(fg="black", font="bold")
        price1.place(x=10, y=50)
        label1 = Label(frame1, text=hotels_letter[0]["name"],bg="white")
        label1.config(fg="black", font=("bold underline",15))
        label1.place(x=160, y=110)
    if len(hotels_letter) == 2:
        frame1 = Frame(korzina_frame,bg="white",width=250,height=150,highlightbackground="black",highlightthickness=1)
        frame1.place(x=300,y=150)
        review1 = Label(frame1, text=hotels_letter[0]["review"],bg="white")
        review1.config(fg="black", font=("bold"))
        review1.place(x=10, y=10)
        buy1 = Button(frame1, text="Х", fg="white", command=close1)
        buy1.config(font="bold", bg="blue")
        buy1.place(x=10, y=100)
        price1 = Label(frame1, text=hotels_letter[0]["price"],bg="white")
        price1.config(fg="black", font="bold")
        price1.place(x=10, y=50)
        label1 = Label(frame1, text=hotels_letter[0]["name"],bg="white")
        label1.config(fg="black", font=("bold underline",15))
        label1.place(x=160, y=110)


        frame2 = Frame(korzina_frame, bg="white", width=250, height=150, highlightbackground="black", highlightthickness=1)
        frame2.place(x=650, y=150)
        review2 = Label(frame2, text=hotels_letter[1]["review"],bg="white")
        review2.config(fg="black", font="bold")
        review2.place(x=10, y=10)
        price2 = Label(frame2, text=hotels_letter[1]["price"],bg="white")
        price2.config(fg="black", font="bold")
        price2.place(x=10, y=50)
        buy2 = Button(frame2, text="Х", fg="white",command=close2)
        buy2.config(font="bold", bg="blue")
        buy2.place(x=10, y=100)
        label2 = Label(frame2, text=hotels_letter[1]["name"],bg="white")
        label2.config(fg="black", font=("bold underline",15))
        label2.place(x=150, y=110)
    if len(hotels_letter) == 3:
        frame1 = Frame(korzina_frame, bg="white", width=250, height=150, highlightbackground="black",
                       highlightthickness=1)
        frame1.place(x=300, y=150)
        review1 = Label(frame1, text=hotels_letter[0]["review"], bg="white")
        review1.config(fg="black", font=("bold"))
        review1.place(x=10, y=10)
        buy1 = Button(frame1, text="Х", fg="white", command=close1)
        buy1.config(font="bold", bg="blue")
        buy1.place(x=10, y=100)
        price1 = Label(frame1, text=hotels_letter[0]["price"], bg="white")
        price1.config(fg="black", font="bold")
        price1.place(x=10, y=50)
        label1 = Label(frame1, text=hotels_letter[0]["name"], bg="white")
        label1.config(fg="black", font=("bold underline", 15))
        label1.place(x=160, y=110)

        frame2 = Frame(korzina_frame, bg="white", width=250, height=150, highlightbackground="black",
                       highlightthickness=1)
        frame2.place(x=650, y=150)
        review2 = Label(frame2, text=hotels_letter[1]["review"], bg="white")
        review2.config(fg="black", font="bold")
        review2.place(x=10, y=10)
        price2 = Label(frame2, text=hotels_letter[1]["price"], bg="white")
        price2.config(fg="black", font="bold")
        price2.place(x=10, y=50)
        buy2 = Button(frame2, text="Х", fg="white", command=close2)
        buy2.config(font="bold", bg="blue")
        buy2.place(x=10, y=100)
        label2 = Label(frame2, text=hotels_letter[1]["name"], bg="white")
        label2.config(fg="black", font=("bold underline", 15))
        label2.place(x=150, y=110)


        frame3 = Frame(korzina_frame, bg="white", width=250, height=150, highlightbackground="black", highlightthickness=1)
        frame3.place(x=1000, y=150)
        review2 = Label(frame3, text=hotels_letter[2]["review"],bg="white")
        review2.config(fg="black", font="bold")
        review2.place(x=10, y=10)
        price2 = Label(frame3, text=hotels_letter[2]["price"], bg="white")
        price2.config(fg="black", font="bold")
        price2.place(x=10, y=50)
        buy2 = Button(frame3, text="Х", fg="white", command=close3)
        buy2.config(font="bold", bg="blue")
        buy2.place(x=10, y=100)
        label2 = Label(frame3, text=hotels_letter[2]["name"], bg="white")
        label2.config(fg="black", font=("bold underline", 15))
        label2.place(x=100, y=110)

    if len(hotels_letter) == 4:
        frame1 = Frame(korzina_frame, bg="white", width=250, height=150, highlightbackground="black",
                       highlightthickness=1)
        frame1.place(x=300, y=150)
        review1 = Label(frame1, text=hotels_letter[0]["review"], bg="white")
        review1.config(fg="black", font=("bold"))
        review1.place(x=10, y=10)
        buy1 = Button(frame1, text="Х", fg="white", command=close1)
        buy1.config(font="bold", bg="blue")
        buy1.place(x=10, y=100)
        price1 = Label(frame1, text=hotels_letter[0]["price"], bg="white")
        price1.config(fg="black", font="bold")
        price1.place(x=10, y=50)
        label1 = Label(frame1, text=hotels_letter[0]["name"], bg="white")
        label1.config(fg="black", font=("bold underline", 15))
        label1.place(x=160, y=110)

        frame2 = Frame(korzina_frame, bg="white", width=250, height=150, highlightbackground="black",
                       highlightthickness=1)
        frame2.place(x=650, y=150)
        review2 = Label(frame2, text=hotels_letter[1]["review"], bg="white")
        review2.config(fg="black", font="bold")
        review2.place(x=10, y=10)
        price2 = Label(frame2, text=hotels_letter[1]["price"], bg="white")
        price2.config(fg="black", font="bold")
        price2.place(x=10, y=50)
        buy2 = Button(frame2, text="Х", fg="white", command=close2)
        buy2.config(font="bold", bg="blue")
        buy2.place(x=10, y=100)
        label2 = Label(frame2, text=hotels_letter[1]["name"], bg="white")
        label2.config(fg="black", font=("bold underline", 15))
        label2.place(x=150, y=110)

        frame3 = Frame(korzina_frame, bg="white", width=250, height=150, highlightbackground="black",
                       highlightthickness=1)
        frame3.place(x=1000, y=150)
        review2 = Label(frame3, text=hotels_letter[2]["review"], bg="white")
        review2.config(fg="black", font="bold")
        review2.place(x=10, y=10)
        price2 = Label(frame3, text=hotels_letter[2]["price"], bg="white")
        price2.config(fg="black", font="bold")
        price2.place(x=10, y=50)
        buy2 = Button(frame3, text="Х", fg="white", command=close3)
        buy2.config(font="bold", bg="blue")
        buy2.place(x=10, y=100)
        label2 = Label(frame3, text=hotels_letter[2]["name"], bg="white")
        label2.config(fg="black", font=("bold underline", 15))
        label2.place(x=100, y=110)

        frame4 = Frame(korzina_frame, bg="white", width=250, height=150, highlightbackground="black",
                       highlightthickness=1)
        frame4.place(x=300, y=400)
        review1 = Label(frame4, text=hotels_letter[3]["review"], bg="white")
        review1.config(fg="black", font=("bold"))
        review1.place(x=10, y=10)
        buy1 = Button(frame4, text="Х", fg="white", command=close4)
        buy1.config(font="bold", bg="blue")
        buy1.place(x=10, y=100)
        price1 = Label(frame4, text=hotels_letter[3]["price"], bg="white")
        price1.config(fg="black", font="bold")
        price1.place(x=10, y=50)
        label1 = Label(frame4, text=hotels_letter[3]["name"], bg="white")
        label1.config(fg="black", font=("bold underline", 15))
        label1.place(x=100, y=110)
    if len(hotels_letter) == 5:
        frame1 = Frame(korzina_frame, bg="white", width=250, height=150, highlightbackground="black",
                       highlightthickness=1)
        frame1.place(x=300, y=150)
        review1 = Label(frame1, text=hotels_letter[0]["review"], bg="white")
        review1.config(fg="black", font=("bold"))
        review1.place(x=10, y=10)
        buy1 = Button(frame1, text="Х", fg="white", command=close1)
        buy1.config(font="bold", bg="blue")
        buy1.place(x=10, y=100)
        price1 = Label(frame1, text=hotels_letter[0]["price"], bg="white")
        price1.config(fg="black", font="bold")
        price1.place(x=10, y=50)
        label1 = Label(frame1, text=hotels_letter[0]["name"], bg="white")
        label1.config(fg="black", font=("bold underline", 15))
        label1.place(x=160, y=110)

        frame2 = Frame(korzina_frame, bg="white", width=250, height=150, highlightbackground="black",
                       highlightthickness=1)
        frame2.place(x=650, y=150)
        review2 = Label(frame2, text=hotels_letter[1]["review"], bg="white")
        review2.config(fg="black", font="bold")
        review2.place(x=10, y=10)
        price2 = Label(frame2, text=hotels_letter[1]["price"], bg="white")
        price2.config(fg="black", font="bold")
        price2.place(x=10, y=50)
        buy2 = Button(frame2, text="Х", fg="white", command=close2)
        buy2.config(font="bold", bg="blue")
        buy2.place(x=10, y=100)
        label2 = Label(frame2, text=hotels_letter[1]["name"], bg="white")
        label2.config(fg="black", font=("bold underline", 15))
        label2.place(x=150, y=110)

        frame3 = Frame(korzina_frame, bg="white", width=250, height=150, highlightbackground="black",
                       highlightthickness=1)
        frame3.place(x=1000, y=150)
        review2 = Label(frame3, text=hotels_letter[2]["review"], bg="white")
        review2.config(fg="black", font="bold")
        review2.place(x=10, y=10)
        price2 = Label(frame3, text=hotels_letter[2]["price"], bg="white")
        price2.config(fg="black", font="bold")
        price2.place(x=10, y=50)
        buy2 = Button(frame3, text="Х", fg="white", command=close3)
        buy2.config(font="bold", bg="blue")
        buy2.place(x=10, y=100)
        label2 = Label(frame3, text=hotels_letter[2]["name"], bg="white")
        label2.config(fg="black", font=("bold underline", 15))
        label2.place(x=100, y=110)

        frame4 = Frame(korzina_frame, bg="white", width=250, height=150, highlightbackground="black",
                       highlightthickness=1)
        frame4.place(x=300, y=400)
        review1 = Label(frame4, text=hotels_letter[3]["review"], bg="white")
        review1.config(fg="black", font=("bold"))
        review1.place(x=10, y=10)
        buy1 = Button(frame4, text="Х", fg="white", command=close4)
        buy1.config(font="bold", bg="blue")
        buy1.place(x=10, y=100)
        price1 = Label(frame4, text=hotels_letter[3]["price"], bg="white")
        price1.config(fg="black", font="bold")
        price1.place(x=10, y=50)
        label1 = Label(frame4, text=hotels_letter[3]["name"], bg="white")
        label1.config(fg="black", font=("bold underline", 15))
        label1.place(x=100, y=110)

        frame5 = Frame(korzina_frame, bg="white", width=250, height=150, highlightbackground="black",
                       highlightthickness=1)
        frame5.place(x=650, y=400)
        review1 = Label(frame5, text=hotels_letter[4]["review"], bg="white")
        review1.config(fg="black", font=("bold"))
        review1.place(x=10, y=10)
        buy1 = Button(frame5, text="Х", fg="white", command=close5)
        buy1.config(font="bold", bg="blue")
        buy1.place(x=10, y=100)
        price1 = Label(frame5, text=hotels_letter[4]["price"], bg="white")
        price1.config(fg="black", font="bold")
        price1.place(x=10, y=50)
        label1 = Label(frame5, text=hotels_letter[4]["name"], bg="white")
        label1.config(fg="black", font=("bold underline", 15))
        label1.place(x=100, y=110)
    # if len(hotels_letter) > 5:
    #     messagebox.showerror("error", "Переполнено")

def Delete_frame(gmail,password):
    Delete_frame = Frame(window, width=1500, height=900)
    Delete_frame.place(x=0, y=0)
    Delete_frame.config(bg="#390879")
    def Delete_back_to_finish():
        Finish_frame(gmail,password)

    back_button = Button(Delete_frame, text="Back", command=Delete_back_to_finish)
    back_button.config(bg="#390879", fg="#bfff00", font="bold", width=10, height=1)
    back_button.place(x=10, y=10)

    def delete1():
        deleted_film = delete_entry.get()
        have=0
        for i in hotels:
            if deleted_film.lower() == i["name"].lower():
                have=1
                hotels.remove(i)
                messagebox.showinfo("deleter", "Успешно удален")
                Finish_frame(gmail, password)
        if have == 0:
            messagebox.showerror("Error","Не найден")
    delete_label = Label(Delete_frame)
    delete_label.config(text="Delete Hotel: ", bg="#390879", fg="#bfff00",
                       font=("Times New Roman", 30, " bold ")
                       )
    delete_label.place(x=640, y=150)

    delete_entry = Entry(Delete_frame)
    delete_entry.config(bg="white", fg="black",
                        font=("Times New Roman", 20, "italic  "),
                        width=24
                        )
    delete_entry.place(x=600, y=250)

    delete_button = Button(Delete_frame, command=delete1)
    delete_button.config(text="Delete", bg="#390879", fg="#bfff00",
                      font=("Open Sans", 20, "bold italic "))
    delete_button.place(x=700, y=350)
def Edit_frame(gmail,password):
    Edit_frame = Frame(window, width=1500, height=900)
    Edit_frame.place(x=0, y=0)
    Edit_frame.config(bg="#390879")

    def Edit_back_to_finish():
        Finish_frame(gmail,password)

    back_button = Button(Edit_frame, text="Back", command=Edit_back_to_finish)
    back_button.config(bg="#390879", fg="#bfff00", font="bold", width=10, height=1)
    back_button.place(x=10, y=10)
    def Edit_name():
        old = edit_entry_name.get()
        new = edit_entry_change.get()
        have=0
        for i in hotels:
            if old.title() == i["name"].title():
                have=1
                i["name"] = new.title()
                messagebox.showinfo("changed","Успешно изменено")
                Finish_frame(gmail, password)
        if have == 0:
            messagebox.showerror("Ошибка","Такого отеля нет")

    edit_label = Label(Edit_frame)
    edit_label.config(text="Edit Hotel", bg="#390879", fg="#bfff00",
                       font=("Times New Roman", 30, " bold ")
                       )
    edit_label.place(x=620, y=60)

    edit_label_name = Label(Edit_frame)
    edit_label_name.config(text="Название отеля:", bg="#390879", fg="#bfff00",
                       font=("Times New Roman", 22, " bold ")
                      )
    edit_label_name.place(x=420, y=200)

    edit_entry_name = Entry(Edit_frame)
    edit_entry_name.config(bg="white", fg="black",
                      font=("Open Sans", 18, "bold italic "),
                      width=24
                      )

    edit_entry_name.place(x=650, y=205)

    edit_label_change = Label(Edit_frame)
    edit_label_change.config(text="Поменять  на :", bg="#390879", fg="#bfff00",
                      font=("Times New Roman", 22 ,"bold")
                      )
    edit_label_change.place(x=420, y=255)

    edit_entry_change = Entry(Edit_frame)
    edit_entry_change.config(bg="white", fg="black",
                       font=("Open Sans", 18, "bold italic "),
                       width=24
                       )
    edit_entry_change.place(x=650, y=260)

    edit_button = Button(Edit_frame, command=Edit_name)
    edit_button.config(text="Edit", bg="#390879", fg="#bfff00", width=12, height=2,
                    font=("Open Sans", 16, "bold italic "))
    edit_button.place(x=620, y=330)


def Add_frame(gmail,password):
    Add_frame = Frame(window, width=1500, height=900)
    Add_frame.place(x=0, y=0)
    Add_frame.config(bg="#390879")

    def Add_back_to_finish():
        Finish_frame(gmail,password)

    back_button = Button(Add_frame, text="Back", command=Add_back_to_finish)
    back_button.config(bg="#390879", fg="#bfff00", font="bold", width=10, height=1)
    back_button.place(x=10, y=10)

    def add():
        name_get = name_entry.get()
        review_get = review_entry.get()
        price_get = price_entry.get()
        if name_get == "" or review_get == "" or price_get == "":
            messagebox.showerror("error", "Пустоо")
        else:
            hotels.append({"name":name_get,"review":review_get,"price":price_get})
            messagebox.showinfo(message="Успешно Добавлено")
            Finish_frame(gmail,password)

    name_entry = Entry(Add_frame)
    name_entry.config(bg="white",
        fg="black",
        font=("Times New Roman", 18, "italic bold"),
        width=28)
    name_entry.place(x=610,y=205)

    name_label = Label(Add_frame,text="Name: ")
    name_label.config(fg="#bfff00",bg="#390879",font=("Times New Roman", 20, " bold "))
    name_label.place(x=500,y=200)

    review_label = Label(Add_frame,text="review: ")
    review_label.config(fg="#bfff00",bg="#390879", font=("Times New Roman", 20, " bold "))
    review_label.place(x=505, y=270)

    review_entry = Entry(Add_frame)
    review_entry.config(bg="white",
                 fg="black",
                 font=("Times New Roman", 18, "italic bold"),
                 width=28)
    review_entry.place(x=610, y=275)

    price_label = Label(Add_frame,text="price: ")
    price_label.config(fg="#bfff00",bg="#390879", font=("Times New Roman", 20, " bold "))
    price_label.place(x=505, y=340)

    price_entry = Entry(Add_frame)
    price_entry.config(bg="white",
                  fg="black",
                  font=("Times New Roman", 18, "italic bold"),
                  width=28)
    price_entry.place(x=610, y=345)

    add_label = Label(Add_frame,text="Add Hotel")
    add_label.config(fg="#bfff00",bg="#390879",font=("Times New Roman", 30, " bold "))
    add_label.place(x=670,y=100)

    add_button = Button(Add_frame,text="Add Hotel",command=add)
    add_button.config(bg="#390879",fg="#bfff00",font=("Open Sans", 21, "bold italic "))
    add_button.place(x=700,y=420)


window.mainloop()