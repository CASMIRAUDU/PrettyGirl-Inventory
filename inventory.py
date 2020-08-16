from tkinter import *
import tkinter as tk
import tkinter.messagebox as tkMessagebox
import tkinter.ttk as ttk


root=tk.Tk()
root.title('PrettyGirl Cakes')
root.geometry('950x600')
root.resizable(width=False, height=False)
root.config(bg='blue')

# Background Image
background_image=tk.PhotoImage(file='pic12.png')
background_label = Label(root, image=background_image)
background_label.place(x=1, y=1, relwidth=1, relheight=1)


# label
product = tk.Label(root, text='Product Name',fg='maroon',bd=5, font=('arial', 16, ))
product.grid(row=0,sticky=W, pady=20,)

size = tk.Label(root, text='Size', fg='maroon', bd=5, font=('arial', 16, ))
size.grid(row=1, sticky=W, pady=20,)

price = tk.Label(root, text='Price', fg='maroon', bd=5, font=('arial', 16,))
price.grid(row=2,sticky=W, pady= 20,)

amount = tk.Label(root, text='Amount in Stock', fg='maroon', bd=5, font=('arial', 16,))
amount.grid(row=3, sticky=W, pady=15)


# Buttons
product_btn=tk.Button(root, text='Add',fg='maroon', width=14,bd=5, font=('timesnewroman'))
size_btn=tk.Button(root, text='Delete', fg='maroon', width=14,bd=5, font=('timesnewroman'))
price_btn=tk.Button(root, text='Update', fg='maroon', width=14,bd=5, font=('timesnewroman'))
amount_btn=tk.Button(root, text='Retrieve', fg='maroon', width=14,bd=5, font=('timesnewroman'))
# Buttons Placement
product_btn.grid(row=4, column=1, padx=20)
size_btn.grid(row=4, column=2, padx=20)
price_btn.grid(row=4, column=3, padx=20)
amount_btn.grid(row=4, column=4, padx=20)
# Entries
product = tk.Entry(root, textvariable=product).grid(row=0, column=1, ipadx=45, ipady=10)
size = tk.Entry(root, textvariable=size).grid(row=1, column=1, ipadx=45, ipady=10)
price = tk.Entry(root, textvariable=price).grid(row=2, column=1, ipadx=45, ipady=10)
amount = tk.Entry(root, textvariable=amount).grid(row=3, column=1, ipadx=45, ipady=10, padx=15)

# Parts List (Listbox)
parts_list = tk.Listbox(root, height=8, width=50, border=0, bd=5)
parts_list.grid(row=7, column=1, columnspan=20, rowspan=20, pady=20, padx=20,)

# Bind select
parts_list.bind('<<ListboxSelect>>',)

def quit(root):
        window.root()
exit_button = Button(root, text='Exit', fg='maroon', command=root.quit, bd=5,font=('times'))
exit_button.grid(row=40, column=4)


root.mainloop()