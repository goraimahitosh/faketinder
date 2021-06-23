import mysql.connector

from tkinter import *



class tinder:

    def __init__(self):

        self.conn=mysql.connector.connect(host="localhost", user="root", password="", database="tinder")
        self.mycursor=self.conn.cursor()

        self.root=Tk()

        self.root.minsize(300, 300)
        self.root.maxsize(300, 300)

        Label(text='Hi!!! TINDER..', bg="black", fg="red").grid(row=0, column=0)
        Label(text='Hi!!! TINDER..', bg="black", fg="red").grid(row=1, column=0)
        Label(text='Hi!!! TINDER..', bg="black", fg="red").grid(row=1, column=2)
        Label(text='Hi!!! TINDER..', bg="black", fg="red").grid(row=0, column=2)

        Label(text='Enter Email').grid(row=0, column=1)

        self.emailInput = Entry()
        self.emailInput.grid(row=1, column=1)

        Label(text="Enter Password").grid(row=2, column=1)

        self.passwordInput = Entry()
        self.passwordInput.grid(row=3, column=1)


        Button(text="Login", bg="grey", width=10, height=1, command=lambda: self.login()).grid(row=4, column=1)
        Label(text="Not a member? Register here!", fg="green").grid(row=5, column=1)
        Button(text="Register", bg="white", width=10, height=1, command=lambda: self.launchRegWindow()).grid(row=6,column=1)
        Button(text="Exit", bg="red", width=5, height=1, command=lambda: self.get_number("3")).grid(row=8, column=1)



        self.root.mainloop()

    def login(self):
        self.mycursor.execute(
            """SELECT * FROM `users` WHERE `email` LIKE '{}" AND `password` LIKE '{}'""".format(self.emailInput.get(),self.passwordInput.get()))

        user_info = self.mycursor.fetchall()

        # print(user_info)

        if len(user_info) > 0:

            print("welcome user")
            Label(text='welcome user').grid(row=0, column=0)
            self.current_user_id = user_info[0][0]
            self.cancel_window()
            # display next menu
            self.user_menu()

        else:
            print("incorrect email/password")
            self.program_menu()

    def launchRegWindow(self):
        self.cancel_window()

        Label(text='Enter Name').grid(row=0, column=0)
        name=self.userName = Entry()
        self.userName.grid(row=0, column=1)

        Label(text='Enter Email').grid(row=1, column=0)
        email=self.userEmail = Entry()
        self.userEmail.grid(row=1, column=1)

        Label(text='Enter Password').grid(row=2, column=0)
        password=self.userPassword = Entry()
        self.userPassword.grid(row=2, column=1)

        Label(text='Enter Gender').grid(row=3, column=0)
        gender=self.userGender = Entry()
        self.userGender.grid(row=3, column=1)

        Label(text='Enter Age').grid(row=4, column=0)
        age=self.userAge = Entry()
        self.userAge.grid(row=4, column=1)

        Label(text='Enter City').grid(row=5, column=0)
        city=self.userCity = Entry()
        self.userCity.grid(row=5, column=1)

        Label(text='Enter Hobbies').grid(row=6, column=0)
        hobbies=self.userHobbies = Entry()
        self.userHobbies.grid(row=6, column=1)

        Button(text="Register", command=lambda: self.mycursor.execute("""INSERT INTO `users`(`user_id`,`name`,`email`,`password`,`gender`,`age`,`city`,`hobbies`) VALUES (NULL,'{}','{}','{}','{}','{}','{}','{}')"""
                              .format(name,email,password,gender,age,city,hobbies).format(self.userName.get(), self.userEmail.get(), self.userPassword.get(), self.userGender.get(), self.userAge.get(), self.userCity.get(), self.userHobbies.get()))
                                     ).grid(row=8, column=1)
        self.conn.commit()

        self.message = Label(text="", fg="red")
        self.message.grid(row=9, column=0)

    def message(self):
        self.cancel_window()

        self.message.configure(("text"))

        self.message = Label(text="you have registered successfully", fg="red")
        self.message.grid(row=9, column=1)





        self.root.mainloop()

    def cancel_window(self):
        for i in self.root.grid_slaves():
            i.destroy()

obj=tinder()
