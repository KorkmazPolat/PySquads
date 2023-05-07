import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

class Voter:
    def __init__(self,yetgen_id,isim,soyisim,seçim,lider):
        self.yetgen_id = yetgen_id
        self.isim = isim
        self.soyisim = soyisim
        self.seçim = seçim
        self.lider = lider

    def __str__(self):
        return f"{self.yetgen_id},{self.isim},{self.soyisim},{self.seçim},{self.lider}"

voters = []

def valid_check(yetgen_id):
    file1 = open("YetkinGencler2.txt","r")
    Lines = file1.readlines()

    for line in Lines:
        if int(yetgen_id) == int(line):
            return False
    return True

def multiple_check(yetgen_id):
    # Burada kişinin daha önce oy kullanıp kullanmadığı kontrol ediliyor.
    for voter in voters:
        if voter.yetgen_id == yetgen_id:
            return True
    return False
    # Aynı kısımda kişinin yetgen üyesi olup olmadığı kontrol edilebilir.

def end_election():
    with open("oy_bilgileri","w") as f:
        for voter in voters:
            f.write(str(voter) + "\n")

    seçimler = ["Python İttifakı", "Java İttifakı"]
    liderler = ["x", "y", "z", "t"]
    lidere_göre_oy_sayilari = [[0,0],[0,0],[0,0],[0,0]] # Bu ksıım elbette lider sayısına göre güncellenecek

    for voter in voters:
        seçim = voter.seçim
        lider = voter.lider
        if seçim == "a":
            lidere_göre_oy_sayilari[liderler.index(lider)][0] += 1
        if seçim == "b":
            lidere_göre_oy_sayilari[liderler.index(lider)][1] += 1

    java_toplam = 0
    python_toplam = 0
    for i in range(len(lidere_göre_oy_sayilari)):
        java_toplam += lidere_göre_oy_sayilari[i][1]
        python_toplam += lidere_göre_oy_sayilari[i][0]
       
    toplam_oy = len(voters)
    beklenen_oy = 25

    labels = ["Seçime Katılanlar", "Seçime Katılmayanlar"]
    sizes = [toplam_oy,beklenen_oy-toplam_oy]

    x_values = ["Python İttifakı","Java İttifakı"]
    y_values = [python_toplam,java_toplam]

    fig, (axs1, ax2) = plt.subplots(1,2,figsize=(10,5))
    axs1.pie(sizes,labels=labels)
    axs1.set_title("Seçime katılım oranı")

    ax2.bar(x_values,y_values)
    ax2.set_title("Genel Oylama")


    fig, axs = plt.subplots(2,2, figsize=(10,8))
    for i in range(len(liderler)):
        row = i//2
        col = i%2
        axs[row,col].bar(seçimler, lidere_göre_oy_sayilari[i])
        axs[row,col].set_title(f"Lidere göre seçim sonuçları ({liderler[i]})")
        axs[row,col].set_xlabel("Parti")
        axs[row,col].set_ylabel("Oy sayıları") 
    plt.suptitle(f"Lidere bağlı seçim sonuçları ( Toplam Oy: {toplam_oy})", fontsize = 16)
    plt.tight_layout()
    plt.show()

def oy_ver():
    voter_id = id_field.get()
    voter_isim = isim_field.get()
    voter_soyisim = soyisim_field.get()
    voter_lider = lider_isim_field.get()

    if valid_check(voter_id):
        messagebox.showwarning("Error", "YetGen mensubu değilsiniz. Oyunuz geçerli değil.")
    elif multiple_check(voter_id):
        messagebox.showwarning("Error","Üzgünüz, sadece 1 kere oy kullanabilirsiniz.")
    else:
        voter_choice = seçim_var.get()
        voter = Voter(voter_id,voter_isim,voter_soyisim,voter_choice,voter_lider)
        voters.append(voter)
        messagebox.showinfo("Başarılı.","Oy verdiğiniz için teşekkür ederiz.")
    id_field.delete(0,tk.END)
    isim_field.delete(0,tk.END)
    soyisim_field.delete(0,tk.END)
    lider_isim_field.delete(0,tk.END)
    seçim_var.set(0)




root = tk.Tk()
root.geometry("300x285")
root.title("13 Mayıs YetGen Seçimi")


id_label = tk.Label(root, text="YetGen ID:")
id_label.grid(row=0, column=0, padx=15,pady=5)

id_field = tk.Entry(root)
id_field.grid(row=0, column=1,padx=10,pady=5)

isim_label = tk.Label(root, text="İsim:")
isim_label.grid(row=1, column=0, padx=30, pady=5)
isim_field = tk.Entry(root)
isim_field.grid(row=1, column=1, padx=10, pady=5)

soyisim_label = tk.Label(root, text="Soyisim:")
soyisim_label.grid(row=2, column=0, padx=15, pady=5)
soyisim_field = tk.Entry(root)
soyisim_field.grid(row=2, column=1, padx=10, pady=5)

lider_isim_label = tk.Label(root, text="Lider adı:")
lider_isim_label.grid(row=3, column=0, padx=15, pady=5)
lider_isim_field = tk.Entry(root)
lider_isim_field.grid(row=3, column=1, padx=10, pady=5)

seçim_label = tk.Label(root, text="Seçiminizi yapınız:")
seçim_label.grid(row=4, column=0, padx=15, pady=5)
seçim_var = tk.StringVar(root, "a")
python_button = tk.Radiobutton(root, text="Python ittifakı", variable=seçim_var, value="a")
python_button.grid(row=4, column=1, padx=15, pady=5)
java_button = tk.Radiobutton(root, text="Java ittifakı", variable=seçim_var, value="b")
java_button.grid(row=5, column=1, padx=15, pady=5)

vote_button = tk.Button(root, text="Oy ver", command=oy_ver)
vote_button.grid(row=6, column=0, padx=5, pady=5)

end_button = tk.Button(root, text="Seçimi sonlandır", command=end_election)
end_button.grid(row=6, column=1, padx=5, pady=5)

root.mainloop()