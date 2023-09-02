import tkinter as tk



def main():
    root = tk.Tk()
    root.title('calculator')
    root.geometry("400x550")
    root.config(bg='#404040')
    
    frame =tk.Frame(root,width=400,height=300)
    frame.configure(borderwidth=5,relief='ridge')
    frame.place(x=1,y=1,width=400,height=550)
    frame.config(bg='#586F7C')
    
    number_entery = tk.Text(frame,width=50)
    number_entery.place(x=10.5,y=100,width=370,height=70)
    number_entery.config(bg='#499F68',font='Arial 20 bold')
    number_entery.configure(borderwidth=3,relief='sunken')
    
    button_number_0 =tk.Button(frame,text='0',command=lambda:number_entery.insert('end','0'))
    button_number_0.place(x=60,y=400)
    button_number_0.config(bg='#C5C6D0',font='Arial 15 bold')
    button_number_0.configure(borderwidth=2,relief='raised')
    
    button_number_dot=tk.Button(frame,text='.',command=lambda: number_entery.insert('end','.'))
    button_number_dot.place(x=100,y=400)
    button_number_dot.config(bg='#C5C6D0',font='Arial 15 bold')
    button_number_dot.configure(borderwidth=2,relief='raised')
    
    button_number_ngpo=tk.Button(frame,text='+/-',command=lambda: number_entery.insert('end','-'))
    button_number_ngpo.place(x=135,y=400)
    button_number_ngpo.config(bg='#C5C6D0',font='Arial 15 bold')
    button_number_ngpo.configure(borderwidth=2,relief='raised')
    
    button_number_eq=tk.Button(frame,text='=')
    button_number_eq.place(x=188,y=400)
    button_number_eq.config(bg='#499F68',font='Arial 15 bold')
    button_number_eq.configure(borderwidth=2,relief='raised')
    
    button_number_1=tk.Button(frame,text='1',command=lambda: number_entery.insert('end','1'))
    button_number_1.place(x=60,y=350)
    button_number_1.config(bg='#C5C6D0',font='Arial 15 bold')
    button_number_1.configure(borderwidth=2,relief='raised')
    
    button_number_2=tk.Button(frame,text='2',command=lambda: number_entery.insert('end','2'))
    button_number_2.place(x=100,y=350)
    button_number_2.config(bg='#C5C6D0',font='Arial 15 bold')
    button_number_2.configure(borderwidth=2,relief='raised')
    
    button_number_3=tk.Button(frame,text='3',command=lambda:number_entery.insert('end','3'))
    button_number_3.place(x=140,y=350)
    button_number_3.config(bg='#C5C6D0',font='Arial 15 bold')
    button_number_3.configure(borderwidth=2,relief='raised')
    
    button_number_4=tk.Button(frame,text='4',command=lambda: number_entery.insert('end','4'))
    button_number_4.place(x=60,y=300)
    button_number_4.config(bg='#C5C6D0',font='Arial 15 bold')
    button_number_4.configure(borderwidth=2,relief='raised')
    
    button_number_5=tk.Button(frame,text='5',command=lambda: number_entery.insert('end','5'))
    button_number_5.place(x=100,y=300)
    button_number_5.config(bg='#C5C6D0',font='Arial 15 bold')
    button_number_5.configure(borderwidth=2,relief='raised')
    
    button_number_6=tk.Button(frame,text='6',command=lambda:number_entery.insert('end','6'))
    button_number_6.place(x=140,y=300)
    button_number_6.config(bg='#C5C6D0',font='Arial 15 bold')
    button_number_6.configure(borderwidth=2,relief='raised')
    
    button_number_7=tk.Button(frame,text='7',command=lambda: number_entery.insert('end','7'))
    button_number_7.place(x=60,y=250)
    button_number_7.config(bg='#C5C6D0',font='Arial 15 bold')
    button_number_7.configure(borderwidth=2,relief='raised')
    
    button_number_8=tk.Button(frame,text='8',command=lambda: number_entery.insert('end','8'))
    button_number_8.place(x=100,y=250)
    button_number_8.config(bg='#C5C6D0',font='Arial 15 bold')
    button_number_8.configure(borderwidth=2,relief='raised')
    
    button_number_9=tk.Button(frame,text='9',command=lambda: number_entery.insert('end','9'))
    button_number_9.place(x=140,y=250)
    button_number_9.config(bg='#C5C6D0',font='Arial 15 bold')
    button_number_9.configure(borderwidth=2,relief='raised')
    
    button_number_delete=tk.Button(frame,text='C',command=lambda: number_entery.delete(1.0,'end'))
    button_number_delete.place(x=180,y=350)
    button_number_delete.config(bg='#C5C6D0',font='Arial 15 bold')
    button_number_delete.configure(borderwidth=2,relief='raised')
    
    button_function_add = tk.Button(frame,text='+')
    button_function_add.place(x=180,y=250)
    button_function_add.config(bg='#4682B4',font='Arial 15 bold')
    button_function_add.configure(borderwidth=2,relief='raised')
    
    button_function_subtract = tk.Button(frame,text='-')
    button_function_subtract.place(x=222,y=250)
    button_function_subtract.config(bg='#4682B4',font='Arial 15 bold')
    button_function_subtract.configure(borderwidth=2,relief='raised')
    
    button_function_division = tk.Button(frame,text='÷')
    button_function_division.place(x=180,y=300)
    button_function_division.config(bg='#4682B4',font='Arial 15 bold')
    button_function_division.configure(borderwidth=2,relief='raised')
    
    button_function_multiply = tk.Button(frame,text='x')
    button_function_multiply.place(x=220,y=300)
    button_function_multiply.config(bg='#4682B4',font='Arial 15 bold')
    button_function_multiply.configure(borderwidth=2,relief='raised')
    
    button_function_columen = tk.Button(frame,text='()',command=lambda: number_entery.insert('end','('))
    button_function_columen.place(x=220,y=350)
    button_function_columen.config(bg='#4682B4',font='Arial 15 bold')
    button_function_columen.configure(borderwidth=2,relief='raised')
    
    def display_complex_function():
        button_function_cos = tk.Button(frame,text='cos')
        button_function_cos.place(x=270,y=250)
        button_function_cos.config(bg='#4682B4',font='Arial 15 bold')
        button_function_cos.configure(borderwidth=2,relief='raised')
        
        button_function_sin = tk.Button(frame,text='sin')
        button_function_sin.place(x=330,y=250)
        button_function_sin.config(bg='#4682B4',font='Arial 15 bold')
        button_function_sin.configure(borderwidth=2,relief='raised')
        
        button_function_tan = tk.Button(frame,text='tan')
        button_function_tan.place(x=270,y=300)
        button_function_tan.config(bg='#4682B4',font='Arial 15 bold')
        button_function_tan.configure(borderwidth=2,relief='raised')
        
        button_function_sqrt = tk.Button(frame,text='sqrt')
        button_function_sqrt.place(x=325,y=300)
        button_function_sqrt.config(bg='#4682B4',font='Arial 15 bold')
        button_function_sqrt.configure(borderwidth=2,relief='raised')
        
        button_function_fact = tk.Button(frame,text='n!')
        button_function_fact.place(x=280,y=350)
        button_function_fact.config(bg='#4682B4',font='Arial 15 bold')
        button_function_fact.configure(borderwidth=2,relief='raised')
        
        button_function_log = tk.Button(frame,text='log')
        button_function_log.place(x=320,y=350)
        button_function_log.config(bg='#4682B4',font='Arial 15 bold')
        button_function_log.configure(borderwidth=2,relief='raised')
        
    def display_history():
        
        root.geometry('800x550')
        
        frame_2 =tk.Frame(root)
        frame_2.configure(borderwidth=5,relief='solid')
        frame_2.place(x=400,y=1,width=400,height=550)
        frame_2.config(bg='#586F7C')
        
        
        label = tk.Label(frame_2,text='history')
        label.pack()
        label.config(bg='#C5C6D0',font='Arial 15 bold')
        label.configure(borderwidth=1,relief='groove')
        
        text_box =tk.Text(frame_2,width=400,height=400)
        text_box.pack()
        text_box.config(bg='#C5C6D0',font='Arial 15 bold')
        
        def remove_cal():
            root.geometry('400x550')
            frame_2.destroy
        
        button_remove_history = tk.Button(frame_2,text='Close',command=remove_cal)
        button_remove_history.place(x=149,y=490)
        button_remove_history.config(bg='#4682B4',font='Arial 15 bold')
        button_remove_history.configure(borderwidth=2,relief='raised')
    
    menu = tk.Menu(root)
    menu2 = tk.Menu(menu, tearoff=0)
    menu2.add_command(label='history',command=display_history)
    menu2.add_command(label='complex functions',command=display_complex_function)
    menu2.add_command(label='Exit', command=root.destroy)
    menu.add_cascade(label='Options', menu=menu2)
    root.config(menu=menu)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    root.mainloop()
    
    
if __name__=='__main__':
    main()
    
    
