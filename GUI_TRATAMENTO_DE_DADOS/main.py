# -------------- import functions ------------------
from data_processing import read
from screen import gets
# ---------------- import packages -----------------
from tkinter import *
import os 

# --------------------------------------------------

main_window = Tk()
main_window.title('Fast Data Processing')
main_window.geometry('600x600')


lbl1 =  Label(main_window,text='Insert Here Your Repository Path')
lbl2 = Label(main_window,text='Processing Conditions')
lbl1.grid(column=1,row=1,padx=20)
lbl2.grid(column=1,row=2,columnspan=2)

chk1 = False
Check_Change_1 = Checkbutton(main_window,text="replace ',' to '.'", variable = chk1 )
Check_Change_1.grid(column=1,row=3)
Check_Change_1.config(font=('Consolas',10),bg='#282A36',fg='#50FA7B')

chk2 = False
Check_Change_2 = Checkbutton(main_window,text="replace ' ' to ''", variable = chk2 )
Check_Change_1.grid(column=1,row=3)
Check_Change_1.config(font=('Consolas',10),bg='#282A36',fg='#50FA7B')

chk3 = False
Check_Change_1 = Checkbutton(main_window,text="replace ',' to '.'", variable = chk1 )
Check_Change_1.grid(column=1,row=3)
Check_Change_1.config(font=('Consolas',10),bg='#282A36',fg='#50FA7B')

chk1 = False
Check_Change_1 = Checkbutton(main_window,text="replace ',' to '.'", variable = chk1 )
Check_Change_1.grid(column=1,row=3)
Check_Change_1.config(font=('Consolas',10),bg='#282A36',fg='#50FA7B')

Entry_Data_Name  = Entry(main_window)
Entry_Data_Name.grid(column=2,row=1,padx=20,pady=20)
lbl1.config(font=('Consolas',10),bg='#282A36',fg='#50FA7B')
lbl2.config(font=('Consolas',10),bg='#282A36',fg='#50FA7B')

Entry_Data_Name.config(width ='36',fg='#50FA7B',bg='#282A36',font=('Consolas',10) )
main_window.config(bg='#282A36')

main_window.mainloop()