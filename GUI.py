import tkinter as tkr

root = tkr.Tk()
root.configure(bg="white")
root.geometry("800x500")

def menu():
    list = root.place_slaves()
    for l in list:
        l.destroy()
    list = root.pack_slaves()
    for l in list:
        l.destroy()

    button1 = tkr.Button(root, text="Magazyn", font=30, bd=8, bg="white", relief="raised",command=ustawienia_graczy)
    button1.place(relx=0.5, rely=0.35, relheight=0.1, relwidth=0.3, anchor='n')

    button2 = tkr.Button(root, text="Zwierzaki", font=30, bd=8, bg="white", relief="raised",command = ustawienia)
    button2.place(relx=0.5, rely=0.5, relheight=0.1, relwidth=0.3, anchor='n')

    button3 = tkr.Button(root, text="Rozmieszczenie", font=30, bd=8, bg="white", relief="raised")
    button3.place(relx=0.5, rely=0.65, relheight=0.1, relwidth=0.3, anchor='n')

def ustawienia_graczy():
    list = root.place_slaves()
    for l in list:
        l.destroy()

    button1 = tkr.Button(root, text="2", font=30,bd=8, bg="white",relief = "raised")
    button1.place(relx=0.5, rely=0.85, relheight=0.1, relwidth=0.3, anchor='n')

    button2 = tkr.Button(root, text="1", font=30, bd=8, bg="white",relief = "raised")
    button2.place(relx=0.2, rely=0.85, relheight=0.1, relwidth=0.3, anchor='n')

    button3 = tkr.Button(root, text="3", font=30,bd=8, bg="white",relief = "raised")
    button3.place(relx=0.8, rely=0.85, relheight=0.1, relwidth=0.3, anchor='n')


def ustawienia():
    list = root.place_slaves()
    for l in list:
        l.destroy()

    text = tkr.Label(root, text="Stan poczatkowy", font=30, bd=8, bg="white", relief="raised")
    text.place(relx=0.2, rely=0.1, relheight=0.1, relwidth=0.3, anchor='n')

    bilans_nr = tkr.Spinbox(root,from_= 10, to_=1000,increment=10, bd=8, bg="white", relief="raised")
    bilans_nr.place(relx=0.45, rely=0.1, relheight=0.1, relwidth=0.1, anchor='n')

    ok = tkr.Button(root, text="Zapisz", font=30, bd=8, bg="white", relief="raised")
    ok.place(relx=0.8, rely=0.85, relheight=0.1, relwidth=0.3, anchor='n')

    sound = tkr.Label(root, text="Dzwiek ", font=30, bd=8, bg="white", relief="raised")
    sound.place(relx=0.2, rely=0.2, relheight=0.1, relwidth=0.3, anchor='n')

    sound_on = tkr.Button(root, text="ON", font=30, bd=8, bg="white", relief="raised")
    sound_on.place(relx=0.45, rely=0.2, relheight=0.1, relwidth=0.1, anchor='n')

    sound_off = tkr.Button(root, text="OFF", font=30, bd=8, bg="white", relief="raised")
    sound_off.place(relx=0.55, rely=0.2, relheight=0.1, relwidth=0.1, anchor='n')

menu()

root.mainloop()
