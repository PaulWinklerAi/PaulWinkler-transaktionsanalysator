import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import pandas as pd
from main import read_transactions, convert_currency, analyze_expenses

# Global DataFrame
df = None

# Läs in och visa transaktionsfilen
def load_file():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        df = read_transactions(file_path)
        if df is not None:
            messagebox.showinfo("Info", "Fil laddad!")
        else:
            messagebox.showerror("Fel", "Det gick inte att läsa in filen.")

# Visa utgifter per kategori och valuta
def show_expenses_per_category():
    global df
    if df is None:
        messagebox.showerror("Fel", "Ingen fil laddad.")
        return
    
    output_text.delete(1.0, tk.END)  # Rensa texten i textrutan
    
    # Analysera utgifter per kategori
    categories = df.groupby("Kategori")
    total_in_sek = 0

    for category, transactions in categories:
        output_text.insert(tk.END, f"Kategori: {category}\n")
        total_in_category = 0
        currencies = transactions["Valuta"].unique()  # Hämta unika valutor i kategorin
        for currency in currencies:
            output_text.insert(tk.END, f"Valuta: {currency}\n")
            category_currency_data = transactions[transactions["Valuta"] == currency]
            for index, row in category_currency_data.iterrows():
                amount_in_sek = convert_currency(row["Belopp"], row["Valuta"])
                total_in_category += amount_in_sek
                output_text.insert(tk.END, f"  Belopp: {row['Belopp']} {currency} -> {amount_in_sek:.2f} SEK\n")
        
        output_text.insert(tk.END, f"Totalt belopp i SEK för {category}: {total_in_category:.2f} SEK\n\n")
        total_in_sek += total_in_category
    
    output_text.insert(tk.END, f"\nTotalt belopp i SEK för alla kategorier: {total_in_sek:.2f} SEK")

# Spara den uppdaterade transaktionsfilen
def save_updated_file():
    global df
    if df is None:
        messagebox.showerror("Fel", "Ingen fil laddad.")
        return
    
    # Spara uppdaterade transaktioner
    save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if save_path:
        df["Belopp i SEK"] = df.apply(lambda row: convert_currency(row["Belopp"], row["Valuta"]), axis=1)
        df.to_csv(save_path, index=False)
        messagebox.showinfo("Info", "Uppdaterad fil sparad!")

# GUI Uppsättning
root = tk.Tk()
root.title("Transaktionsanalysator")
root.geometry("800x600") 
root.configure(bg="#f5f5f5") 

# Texten i GUI
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10, relief="flat", background="#007aff", foreground="white")
style.configure("TLabel", font=("Helvetica", 14), background="#f5f5f5")
style.configure("TText", font=("Helvetica", 12), padding=10, relief="flat", height=20, width=80)  # Justera storleken på textrutan

# Knapp för att ladda fil
load_button = ttk.Button(root, text="Ladda transaktionsfil", command=load_file)
load_button.pack(pady=20)

# Knapp för att visa utgifter per kategori
show_button = ttk.Button(root, text="Visa utgifter per kategori", command=show_expenses_per_category)
show_button.pack(pady=20)

# Knapp för att spara uppdaterad fil
save_button = ttk.Button(root, text="Spara uppdaterad fil", command=save_updated_file)
save_button.pack(pady=20)

# Textfält för att visa resultat
output_text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12), height=20, width=80)  # Större storlek på textrutan
output_text.pack(pady=20)
output_text.configure(state="normal")  # Gör så att vi kan skriva i textfältet

# Starta GUI
root.mainloop()
