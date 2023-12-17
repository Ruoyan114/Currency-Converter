from forex_python.converter import CurrencyRates # provides access to currency exchange rate data.
import tkinter as tk # creating the GUI
from tkinter import ttk

c = CurrencyRates()

def result_currency_conversion(amount, from_currency, to_currency):
    """
    returns the result of the conversion
    """
    try:
        converted_rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * converted_rate
        return converted_amount
    except Exception as e:
        return str(e)

# Define the function to handle the conversion in the GUI
def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = combo_from_currency.get().upper()
        to_currency = combo_to_currency.get().upper()

        result = result_currency_conversion(amount, from_currency, to_currency)
        result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid amount.")
    except Exception as e:
        result_label.config(text=f"Error occurred: {str(e)}")


win = tk.Tk()
win.title("My Currency Converter")

label_amount = tk.Label(win, text="Enter Amount:")
label_from_currency = tk.Label(win, text="From Currency:")
label_to_currency = tk.Label(win, text="To Currency:")
result_label = tk.Label(win, text="", fg="green")

# entry field for amount
entry_amount = tk.Entry(win)

currencies = CurrencyRates().get_rates('USD')
combo_from_currency = ttk.Combobox(win, values=list(currencies.keys()))
combo_from_currency.set('USD')
combo_to_currency = ttk.Combobox(win, values=list(currencies.keys()))
combo_to_currency.set('CNY')

# the convert button
convert_button = tk.Button(win, text="Convert", command=convert_currency)

# set up the GUI
label_amount.grid(row=0, column=0)
label_from_currency.grid(row=1, column=0)
label_to_currency.grid(row=2, column=0)
entry_amount.grid(row=0, column=1)
combo_from_currency.grid(row=1, column=1)
combo_to_currency.grid(row=2, column=1)
convert_button.grid(row=3, column=0, columnspan=2)
result_label.grid(row=4, column=0, columnspan=2)

win.mainloop()
