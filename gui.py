
import tkinter as tk


def calculate():
    bill = float(entry.get())
    tip = bill * 0.15
    total = bill + tip

    result.config(text=f"Tip: ${tip:.2f}   Total: ${total:.2f}")


root = tk.Tk()
root.title("Tip Calculator")

tk.Label(root, text="Bill amount:").pack(padx=10, pady=(10, 0))
entry = tk.Entry(root)
entry.pack(padx=10, pady=4)

tk.Button(root, text="Calculate 15% tip", command=calculate).pack(padx=10, pady=4)

result = tk.Label(root, text="Tip: $0.00   Total: $0.00", font=("Arial", 12))
result.pack(padx=10, pady=10)

root.mainloop()
