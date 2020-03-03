# -------------- import functions ------------------
from data_processing import dataprocess
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
lbl3 = Label(main_window,text='Lines Number' )
lbl4 = Label(main_window,text='Lines(null = default(all lines)')

lbl1.grid(column=1,row=1,padx=20)
lbl2.grid(column=1,row=5,columnspan=2)
lbl3.grid(column=1,row=2,padx=20,pady=5)
lbl4.grid(column=1,row=3,padx=20,pady=5)

chkall = IntVar(value = 0)
Check_Change_all = Checkbutton(main_window,text="All Conditions", variable = chkall )
Check_Change_all.grid(column=1,row=6,columnspan=2)
Check_Change_all.config(font=('Consolas',10),bg='#282A36',fg='#50FA7B')

chk1 = IntVar(value = 0)
Check_Change_1 = Checkbutton(main_window,text="replace ',' to '.'", variable = chk1 )
Check_Change_1.grid(column=1,row=7)
Check_Change_1.config(font=('Consolas',10),bg='#282A36',fg='#50FA7B')

chk2 = IntVar(value = 0)
Check_Change_2 = Checkbutton(main_window,text="replace ' ' to ''", variable = chk2 )
Check_Change_2.grid(column=2,row=7)
Check_Change_2.config(font=('Consolas',10),bg='#282A36',fg='#50FA7B')

chk3 =IntVar(value = 0)
Check_Change_3 = Checkbutton(main_window,text="replace \ n", variable = chk3 )
Check_Change_3.grid(column=1,row=8)
Check_Change_3.config(font=('Consolas',10),bg='#282A36',fg='#50FA7B')

chk4 = IntVar(value = 0)
Check_Change_4 = Checkbutton(main_window,text="replace \ t", variable = chk4 )
Check_Change_4.grid(column=2,row=8)
Check_Change_4.config(font=('Consolas',10),bg='#282A36',fg='#50FA7B')

Entry_Data_Name  = Entry(main_window)
Entry_Data_Name.grid(column=2,row=1,padx=20,pady=20)

Entry_NumberLines = Entry(main_window)
Entry_NumberLines.grid(column = 2,row = 2)
Entry_NumberLines.config(width ='8',fg='#50FA7B',bg='#282A36',font=('Consolas',10) )

Entry_ChoseLines = Entry(main_window)
Entry_ChoseLines.grid(column = 2,row = 3)
Entry_ChoseLines.config(width ='8',fg='#50FA7B',bg='#282A36',font=('Consolas',10) )

lbl1.config(font=('Consolas',10),bg='#282A36',fg='#50FA7B')
lbl2.config(font=('Consolas',10),bg='#282A36',fg='#50FA7B')
lbl3.config(font=('Consolas',10),bg='#282A36',fg='#50FA7B')
lbl4.config(font=('Consolas',10),bg='#282A36',fg='#50FA7B')
Entry_Data_Name.config(width ='36',fg='#50FA7B',bg='#282A36',font=('Consolas',10) )
main_window.config(bg='#282A36')

main_window.mainloop()
if __name__ == "__main__":
	def getconditions():
		conditionall = chkall.getstate()
		if conditionall==1:
		
    
    print('ok')    
    
    