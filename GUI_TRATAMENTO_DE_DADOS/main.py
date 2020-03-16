# -------------- import functions ------------------
from data_processing import dataprocess
from screen import gets
# ---------------- import packages -----------------
from tkinter import *
import os 

# --------------------------------------------------

if __name__ == "__main__":
	
	class dataroute():
		def __init__(self, Entry_Data_Name,Entry_NumberLines, Entry_ChoseLines):
			self.name = Entry_Data_Name.get()
			self.numberlines = Entry_NumberLines.get()
			self.lines = Entry_ChoseLines.get()
			self.doc = doc

		def getconditions(self,doc):
			
			if chkall==1:
				for i in range(len(doc)):
					doc.append(doc[i].replace('\n','').replace(' ','').split('\t'))
    
				for i in range(len(doc)):
					for d in range(len(doc[i])):
						docl[i][d] = doc[i][d].replace(',','.')

			elif chk1 == 1 or chk2 == 1 or chk3 == 1 or chk4 == 1:
				if chk1 == 1:
					input()
			elif chk1 == 1 and chk2 == 1 and chk3 == 1 and chk4 == 1:
				input()
			elif chk1 == 1 and chk2 == 1 and chk3 == 1 and chk4 == 1:
				input()
			for i in range(len(doc)):
				docp+=doc[i]
		
			for i in range(len(doc)):
				doc.append(doc[i].replace('\n','').replace(' ','').split('\t'))
    
			for i in range(len(doc)):
				for d in range(len(doc[i])):
					docl[i][d] = doc[i][d].replace(',','.')
			

   		def process_data_btn(self,doc):
			self.doc = data_processing.read(Entry_Data_Name.get())
			dataroute.getconditions(self.doc)
	
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

	Btn_Process = Button(main_window,text='Process Data',command=process_data_btn)
	Btn_Process.grid(column=1,row=9,columnspan=2)
	lbl1.config(font=('Consolas',10),bg='#282A36',fg='#50FA7B')
	lbl2.config(font=('Consolas',10),bg='#282A36',fg='#50FA7B')
	lbl3.config(font=('Consolas',10),bg='#282A36',fg='#50FA7B')
	lbl4.config(font=('Consolas',10),bg='#282A36',fg='#50FA7B')
	Entry_Data_Name.config(width ='36',fg='#50FA7B',bg='#282A36',font=('Consolas',10) )
	main_window.config(bg='#282A36')
	main_window.mainloop()
    
    