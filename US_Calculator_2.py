from tkinter import*
 
main = Tk()
main.title("Calculator")
main.resizable(width = False, height = False )
#mengatur size apknya
main.geometry("360x400+460+40")

operator = "" #variable kosng untuk melakukan operasi perhitungan
input_value = StringVar() #untuk menyimpan string input nilai
display_text = Entry(main, font=('arial',20,"bold"),textvariable=input_value,bd=30, insertwidth=4,bg="powder blue",justify=RIGHT)
# apayang ingin kita tampilkan dan settingannya, kita pingin menampilkan input_value yang diketikkan oleh user
display_text.grid(columnspan=4) #menentukan banyak column yang mau kta pakai

# Row 1 [7,8,9,+]
btn_7 = Button(main,padx=16,bd=8,bg="salmon",fg="white",font=("arial",20,"bold"),text="7")
btn_7.grid(row=1,column=0)

btn_8 = Button(main,padx=16,bd=8,bg="salmon",fg="white",font=("arial",20,"bold"),text="8")
btn_8.grid(row=1,column=1)

btn_9 = Button(main,padx=16,bd=8,bg="salmon",fg="white",font=("arial",20,"bold"),text="9")
btn_9.grid(row=1,column=2)

btn_add = Button(main,padx=16,bd=8,bg="salmon",fg="white",font=("arial",20,"bold"),text="+")
btn_add.grid(row=1,column=3)

# Row 2 [4,5,6,-]
btn_4 = Button(main,padx=16,bd=8,bg="salmon",fg="white",font=("arial",20,"bold"),text="4")
btn_4.grid(row=2,column=0)

btn_5 = Button(main,padx=16,bd=8,bg="salmon",fg="white",font=("arial",20,"bold"),text="5")
btn_5.grid(row=2,column=1)

btn_6 = Button(main,padx=16,bd=8,bg="salmon",fg="white",font=("arial",20,"bold"),text="6")
btn_6.grid(row=2,column=2)

btn_minus = Button(main,padx=16,bd=8,bg="salmon",fg="white",font=("arial",20,"bold"),text="-")
btn_minus.grid(row=2,column=3)

# Row 3 [1,2,3],
btn_1 = Button(main,padx=16,bd=8,bg="salmon",fg="white",font=("arial",20,"bold"),text="1")
btn_1.grid(row=3,column=0)

btn_2 = Button(main,padx=16,bd=8,bg="salmon",fg="white",font=("arial",20,"bold"),text="2")
btn_2.grid(row=3,column=1)

btn_3 = Button(main,padx=16,bd=8,bg="salmon",fg="white",font=("arial",20,"bold"),text="3")
btn_3.grid(row=3,column=2)

btn_multiple = Button(main,padx=16,bd=8,bg="salmon",fg="white",font=("arial",20,"bold"),text="*")
btn_multiple.grid(row=3,column=3)

# Row 3 [0,c,=,/],
btn_0 = Button(main,padx=16,bd=8,bg="salmon",fg="white",font=("arial",20,"bold"),text="0")
btn_0.grid(row=4,column=0)

btn_C = Button(main,padx=16,bd=8,bg="salmon",fg="white",font=("arial",20,"bold"),text="C")
btn_C.grid(row=4,column=1)

btn_equals = Button(main,padx=16,bd=8,bg="salmon",fg="white",font=("arial",20,"bold"),text="=")
btn_equals.grid(row=4,column=2)

btn_div = Button(main,padx=16,bd=8,bg="salmon",fg="white",font=("arial",20,"bold"),text=chr(247))
btn_div.grid(row=4,column=3)


main.mainloop() #untuk run apk