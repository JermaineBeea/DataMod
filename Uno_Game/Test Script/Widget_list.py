import tkinter as tk
from tkinter import ttk

# Sample data
data = {
    'dave': [(0, 'blue'), (1, 'red'), (1, 'blue'), (2, 'red')],
    'mat': [(6, 'yellow'), (2, 'white'), (6, 'blue'), (0, 'yellow')]
}

def populate_treeview(tree):
    # Clear existing data
    for item in tree.get_children():
        tree.delete(item)
    
    # Insert data into the treeview
    for name, values in data.items():
        for index, color in values:
            tree.insert("", "end", values=(name, index, color))

# Create the main window
root = tk.Tk()
root.title("Data Representation")

# Create a Treeview widget
columns = ('Name', 'Index', 'Color')
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.heading('Name', text='Name')
tree.heading('Index', text='Index')
tree.heading('Color', text='Color')

# Add a scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)

# Layout
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Populate the Treeview with data
populate_treeview(tree)

# Start the Tkinter main loop
root.mainloop()

