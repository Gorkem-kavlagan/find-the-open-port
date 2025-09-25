import socket
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

def portlari_tara():
    hedef_ip = giris_ip.get()
    try:
        baslangic_portu = int(giris_baslangic_port.get())
        bitis_portu = int(giris_bitis_port.get())
    except ValueError:
        yazi_sonuc.insert(tk.END, "Lütfen geçerli port numaraları girin.\n")
        return

    yazi_sonuc.delete("1.0", tk.END)  
    yazi_sonuc.insert(tk.END, f"{hedef_ip} üzerinde portlar aranıyor...\n")

    pencere.update() 

    for port in range(baslangic_portu, bitis_portu + 1):
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soket.settimeout(0.01)
        sonuc = soket.connect_ex((hedef_ip, port))
        if sonuc == 0:
            yazi_sonuc.insert(tk.END, f"{port} numaralı port açık\n")
        soket.close()

    yazi_sonuc.insert(tk.END, "Tarama tamamlandı.\n")


pencere = tk.Tk()
pencere.title("Port Tarayıcı")
pencere.geometry("400x400")


ttk.Label(pencere, text="Hedef IP:").pack(pady=5)
giris_ip = ttk.Entry(pencere, width=30)
giris_ip.pack()

ttk.Label(pencere, text="Başlangıç Portu:").pack(pady=5)
giris_baslangic_port = ttk.Entry(pencere, width=30)
giris_baslangic_port.pack()

ttk.Label(pencere, text="Bitiş Portu:").pack(pady=5)
giris_bitis_port = ttk.Entry(pencere, width=30)
giris_bitis_port.pack()


buton_tara = ttk.Button(pencere, text="Taramayı Başlat", command=portlari_tara)
buton_tara.pack(pady=10)


yazi_sonuc = scrolledtext.ScrolledText(pencere, width=45, height=10)
yazi_sonuc.pack(pady=10)

pencere.mainloop()
