import tkinter as tk 
from tkinter import ttk

def main():
    root = tk.Tk() # Main Window
    root.title("Store Manager")
    root.geometry("500x500")
    root.iconbitmap("store-icon.ico")

    ### Sale Order Button ###
    addSaleButton = tk.Button(root, text="+ Sale", command=add_sale)
    addSaleButton.pack()
    delSaleButton = tk.Button(root, text="- Sale", command=del_sale)
    delSaleButton.pack()

    ### Search Label/Entry ###
    searchLabel = tk.Label(root, text="Search: ")
    searchLabel.pack()
    searchEntry = tk.Entry(root)
    searchEntry.pack()

    ### Sales Order List (Tree) ###
    orderTree = ttk.Treeview(root, columns=("ID", "Date"))
    orderTree.heading("ID", text="ID")
    orderTree.heading("Date", text="Date")
    orderTree["show"] = "headings"
    orderTree.pack()

    ### Display number of Sales ###
    totalOrdersLabel = tk.Label(root, text="Total: ")
    totalOrdersLabel.pack()
    totalOrdersValue = tk.Label(root, text="0")
    totalOrdersValue.pack()

    root.mainloop() # Main Event Loop

def add_sale():
    print("Clicked add sale button!")

def del_sale():
    print("Clicked delete sale button!")

if __name__ == '__main__':
    main()