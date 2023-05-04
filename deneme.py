import tkinter as tk

root = tk.Tk()
root.geometry("300x300")

id_field = tk.Entry(root)
id_field.grid(row=0,column=0,padx=5,pady=5)




voter_id = id_field.get()
print(type(voter_id))






root.mainloop()