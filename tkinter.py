# importing modules
import tkinter as tk
import time
import webbrowser
import urllib


# definitions
# physis topics
def ph_electc():
    ph_elec = Toplevel()
    ph_elec.title('Electricity')
    web_bt = Button(ph_elec, text='More information \n on web', font=('Claibri', 20),
                    command=lambda: webbrowser.open('https://en.wikipedia.org/wiki/Electricity')).pack()


def pl_opticsc():
    pl_optic = Toplevel()
    pl_optic.title('Optics')
    web_bt = Button(pl_optic, text='More information \n on web', font=('Claibri', 20),
                    command=lambda: webbrowser.open('https://en.wikipedia.org/wiki/Optics')).pack()


def pl_mechc():
    pl_mech = Toplevel()
    pl_mech.title('Mechanics')
    web_bt = Button(pl_mech, text='More information \n on web', font=('Claibri', 20),
                    command=lambda: webbrowser.open('')).pack()


def pl_thermc():
    pl_therm = Toplevel()
    pl_therm.title('Thermodynamics')
    web_bt = Button(pl_therm, text='More information \n on web', font=('Claibri', 20),
                    command=lambda: webbrowser.open('')).pack()


def pl_magc():
    pl_mag = Toplevel()
    pl_mag.title('Magnetism')
    web_bt = Button(pl_mag, text='More information \n on web', font=('Claibri', 20),
                    command=lambda: webbrowser.open('')).pack()


def pl_modpc():
    ph_ = Toplevel()
    ph_elec.title('')
    web_bt = Button(ph_, text='More information \n on web', font=('Claibri', 20),
                    command=lambda: webbrowser.open('')).pack()


def pl_spacec():
    pl_space = Toplevel()
    pl_space.title('')
    web_bt = Button(pl_space, text='More information \n on web', font=('Claibri', 20),
                    command=lambda: webbrowser.open('')).pack()


# chem topics
def cl_orgc():
    cl_org = Toplevel()
    cl_org.title('')
    web_bt = Button(cl_org, text='More information \n on web', command=lambda: webbrowser.open('')).pack()


def ph_():
    ph_ = Toplevel()
    ph_elec.title('')
    web_bt = Button(ph_, text='More information \n on web', command=lambda: webbrowser.open('')).pack()


def cl_nucc():
    cl_nuc = Toplevel()
    cl_nuc.title('')
    web_bt = Button(cl_nuc, text='More information \n on web', command=lambda: webbrowser.open('')).pack()


def cl_inorgc():
    cl_inorg = Toplevel()
    cl_inorg.title('')
    web_bt = Button(cl_inorg, text='More information \n on web', command=lambda: webbrowser.open('')).pack()


def cl_elecc():
    cl_elec = Toplevel()
    cl_elec.title('')
    web_bt = Button(cl_elec, text='More information \n on web', command=lambda: webbrowser.open('')).pack()


# bio topics
def ph_():
    ph_ = Toplevel()
    ph_elec.title('')
    web_bt = Button(ph_, text='More information \n on web', command=lambda: webbrowser.open('')).pack()


def ph_():
    ph_ = Toplevel()
    ph_elec.title('')
    web_bt = Button(ph_, text='More information \n on web', command=lambda: webbrowser.open('')).pack()


def ph_():
    ph_ = Toplevel()
    ph_elec.title('')
    web_bt = Button(ph_, text='More information \n on web', command=lambda: webbrowser.open('')).pack()


def ph_():
    ph_ = Toplevel()
    ph_elec.title('')
    web_bt = Button(ph_, text='More information \n on web', command=lambda: webbrowser.open('')).pack()


# math topics
def ph_():
    ph_ = Toplevel()
    ph_elec.title('')
    web_bt = Button(ph_, text='More information \n on web', command=lambda: webbrowser.open('')).pack()


def ph_():
    ph_ = Toplevel()
    ph_elec.title('')
    web_bt = Button(ph_, text='More information \n on web', command=lambda: webbrowser.open('')).pack()


def ph_():
    ph_ = Toplevel()
    ph_elec.title('')
    web_bt = Button(ph_, text='More information \n on web', command=lambda: webbrowser.open('')).pack()


def ph_():
    ph_ = Toplevel()
    ph_elec.title('')
    web_bt = Button(ph_, text='More information \n on web', command=lambda: webbrowser.open('')).pack()


def ph_():
    ph_ = Toplevel()
    ph_elec.title('')
    web_bt = Button(ph_, text='More information \n on web', command=lambda: webbrowser.open('')).pack()


def ph_():
    ph_ = Toplevel()
    ph_elec.title('')
    web_bt = Button(ph_, text='More information \n on web', command=lambda: webbrowser.open('')).pack()


def ph_():
    ph_ = Toplevel()
    ph_elec.title('')
    web_bt = Button(ph_, text='More information \n on web', command=lambda: webbrowser.open('')).pack()


# sub-header learn
def phy_buttonlc():
    pl_elect = Button(main_window, text='Electricity', font=('Claibri', 15), padx=32, bg='#0760f0', command=ph_electc)
    pl_elect.grid(row=2, column=5)
    pl_optics = Button(main_window, text='Optics', font=('Claibri', 15), padx=48, bg='#0760f0', command=pl_opticsc)
    pl_optics.grid(row=3, column=5)
    pl_mech = Button(main_window, text='Mechanics', font=('Claibri', 15), padx=30, bg='#0760f0', command=pl_mechc)
    pl_mech.grid(row=4, column=5)
    pl_therm = Button(main_window, text='Thermodynamics', font=('Claibri', 15), bg='#0760f0', command=pl_thermc)
    pl_therm.grid(row=5, column=5)
    pl_mag = Button(main_window, text='Magnetism', font=('Claibri', 15), padx=30, bg='#0760f0', command=pl_magc)
    pl_mag.grid(row=6, column=5)
    pl_modp = Button(main_window, text='Modern Physics', font=('Claibri', 15), padx=10, bg='#0760f0', command=pl_modpc)
    pl_modp.grid(row=7, column=5)
    pl_space = Button(main_window, text='Astrophysics', font=('Claibri', 15), padx=25, bg='#0760f0', command=pl_spacec)
    pl_space.grid(row=8, column=5)


def chem_buttonlc():
    cl_org = Button(main_window, text='Organic Chemistry', font=('Claibri', 15), padx=10, bg='#1cb021', command=cl_orgc)
    cl_org.grid(row=2, column=6)
    cl_phy = Button(main_window, text='Physical Chemistry', font=('Claibri', 15), padx=10, bg='#1cb021')
    cl_phy.grid(row=3, column=6)
    cl_nuc = Button(main_window, text='Nuclear Chemistry', font=('Claibri', 15), padx=10, bg='#1cb021', command=cl_nucc)
    cl_nuc.grid(row=4, column=6)
    cl_inorg = Button(main_window, text='Inorganic Chemistry', font=('Claibri', 15), padx=5, bg='#1cb021',
                      command=cl_inorgc)
    cl_inorg.grid(row=5, column=6)
    cl_elec = Button(main_window, text='Electrochemistry', font=('Claibri', 15), padx=20, bg='#1cb021',
                     command=cl_elecc)
    cl_elec.grid(row=6, column=6)


def bio_buttonlc():
    bl_plant = Button(main_window, text='Plant biology', font=('Claibri', 15), padx=20, bg='#f00717')
    bl_plant.grid(row=9, column=5)
    bl_anim = Button(main_window, text='Animal biology', font=('Claibri', 15), padx=15, bg='#f00717')
    bl_anim.grid(row=10, column=5)
    bl_class = Button(main_window, text='Classification', font=('Claibri', 15), padx=20, bg='#f00717')
    bl_class.grid(row=11, column=5)
    bl_mic = Button(main_window, text='Micro Biology', font=('Claibri', 15), padx=18, bg='#f00717')
    bl_mic.grid(row=12, column=5)


def math_buttonlc():
    ml_arith = Button(main_window, text='Arithmetic', font=('Calibri', 15), padx=40, bg='#ebff0f')
    ml_arith.grid(row=9, column=6)
    ml_alge = Button(main_window, text='Algebra', font=('Calibri', 15), padx=55, bg='#ebff0f')
    ml_alge.grid(row=10, column=6)
    ml_trig = Button(main_window, text='Trigonometry', font=('Calibri', 15), padx=30, bg='#ebff0f')
    ml_trig.grid(row=11, column=6)
    ml_combi = Button(main_window, text='Combinotrics', font=('Calibri', 15), padx=30, bg='#ebff0f')
    ml_combi.grid(row=12, column=6)
    ml_stat = Button(main_window, text='Statistics', font=('Calibri', 15), padx=45, bg='#ebff0f')
    ml_stat.grid(row=13, column=6)
    ml_calc = Button(main_window, text='Calculus', font=('Calibri', 15), padx=45, bg='#ebff0f')
    ml_calc.grid(row=14, column=6)
    ml_geo = Button(main_window, text='Geometry', font=('Calibri', 15), padx=40, bg='#ebff0f')
    ml_geo.grid(row=15, column=6)


def gk_buttonlc():
    gkl_spo = Button(main_window, text='Sports', font=('Calibri', 15), padx=10).pack()
    gkl_ear = Button(main_window, text='Earth', font=('Calibri', 15), padx=10).pack()
    gkl_spac = Button(main_window, text='Space', font=('Calibri', 15), padx=10).pack()
    gkl_pol = Button(main_window, text='Politics', font=('Calibri', 15), padx=10).pack()
    gkl_hum = Button(main_window, text='Humanities', font=('Calibri', 15), padx=10).pack()
    gkl_ = Button(main_window, text='', font=('Calibri', 15), padx=10).pack()


# sub-headernotes
def new_notec():
    return


def open_prevc():
    return


# headers
def learn_button():
    phy_buttonl = Button(main_window, text="Physics", font=('Arial Bold', 10), padx=67, pady=27, command=phy_buttonlc,
                         bg='#0760f0')
    phy_buttonl.grid(column=0, row=5, rowspan=2)

    chem_buttonl = Button(main_window, text="Chemistry", font=('Arial Bold', 10), padx=60, pady=27,
                          command=chem_buttonlc, bg='#1cb021')
    chem_buttonl.grid(column=0, row=7, rowspan=2)

    bio_buttonl = Button(main_window, text="Biology", font=('Arial Bold', 10), padx=68, pady=29, command=bio_buttonlc,
                         bg='#f00717')
    bio_buttonl.grid(column=0, row=9, rowspan=2)

    math_buttonl = Button(main_window, text="Mathematics", font=('Arial Bold', 10), padx=52, pady=29,
                          command=math_buttonlc, bg='#ebff0f')
    math_buttonl.grid(column=0, row=11, rowspan=2)

    gk_buttonl = Button(main_window, text="General knowledge", font=('Arial Bold', 10), padx=30, pady=29,
                        command=gk_buttonlc, bg='#804bab')
    gk_buttonl.grid(column=0, row=13, rowspan=2)


def notes_button():
    new_note_button = Button(main_window, text='New note', font=('Arial Bold', 10), padx=68, pady=21, command=new_notec)
    new_note_button.grid(row=5, column=2)
    open_prev_button = Button(main_window, text='Open Previous notes', font=('Arial Bold', 10), padx=33, pady=21,
                              command=open_prevc)
    open_prev_button.grid(row=6, column=2)


# main program
main_window = Tk()
main_window.geometry('1050x650')
main_window.title('Digital book')

welcome = Label(main_window, text="   Welcome to Digital Book   ", font=('Arial Bold', 30), fg='white', bg='black', )
welcome.grid(column=0, row=0, columnspan=3)

mode = Label(main_window, text="Choose mode", font=('Arial Bold', 25), fg='green')
mode.grid(column=0, row=1, columnspan=3)

exit_button = Button(main_window, text='Exit program', font=('Arial Bold', 10), padx=20, pady=47, bg='red', fg='white',
                     command=main_window.destroy)
exit_button.grid(row=2, column=4, rowspan=3)

# headers
learn_button = Button(main_window, text='Learn', font=('Arial Bold', 15), padx=70, pady=40, command=learn_button,
                      bg='grey')
learn_button.grid(column=0, row=2, rowspan=3)

notes_button = Button(main_window, text='Notes', font=('Arial Bold', 15), padx=70, pady=40, command=notes_button,
                      bg='grey')
notes_button.grid(column=2, row=2, rowspan=3)

main_window.mainloop()

'''
#sub-header test
def phy_buttontc():
    phyt=Toplevel()
    phyt.title('Physics Test')
def chem_buttontc():
    chemt=Toplevel()
    chemt.title('Chemistry Test')
def bio_buttontc():
    biot=Toplevel()
    biot.title('Biology Test')
def math_buttontc():
    matht=Toplevel()
    matht.title('Mathematics Test')
def gk_buttontc():
    gkt=Toplevel()
    gkt.title('General Knowledge Test')

def test_button():
    phy_buttont=Button(main_window,text="Physics",font=('Arial Bold',10),padx=67,pady=20,command=phy_buttontc)
    phy_buttont.grid(column=1,row=5)

    chem_buttont=Button(main_window,text="Chemistry",font=('Arial Bold',10),padx=60,pady=20,command=chem_buttontc)
    chem_buttont.grid(column=1,row=6)

    bio_buttont=Button(main_window,text="Biology",font=('Arial Bold',10),padx=68,pady=21,command=bio_buttontc)
    bio_buttont.grid(column=1,row=7)

    math_buttont=Button(main_window,text="Mathematics",font=('Arial Bold',10),padx=52,pady=20,command=math_buttontc)
    math_buttont.grid(column=1,row=8)

    gk_buttont=Button(main_window,text="General knowledge",font=('Arial Bold',10),padx=30,pady=20,command=gk_buttontc)
    gk_buttont.grid(column=1,row=9)

test_button=Button(main_window,text='Test',font=('Arial Bold',15),padx=70,pady=40,command=test_button,bg='grey')
test_button.grid(column=1,row=2,rowspan=2)'''
####################
'''
byjus.com/chemistry/
5-calculator
6 above
7above
8-icons,images,exit button
9 image app
10 status bar
11 frames
12 radiobuttons
13 message box
14new window
15 open files dialog box
16 sliders
17 check box
18 drop down menu
19,20 database
'''