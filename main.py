import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to generate the CSR
def generate_csr():
   country = entry_country.get()
   state = entry_state.get()
   locality = entry_locality.get()
   organization = entry_organization.get()
   org_unit = entry_org_unit.get()
   common_name = entry_common_name.get()
   email = entry_email.get()
   key_out = entry_key_out.get()
   csr_out = entry_csr_out.get()

   # OpenSSL command to generate CSR
   command = [
       'openssl', 'req', '-new',
       '-newkey', 'rsa:2048',
       '-nodes',
       '-keyout', key_out,
       '-out', csr_out,
       '-subj', f"/C={country}/ST={state}/L={locality}/O={organization}/OU={org_unit}/CN={common_name}/emailAddress={email}"
   ]

   try:
       subprocess.run(command, check=True)
       messagebox.showinfo("Success", "CSR Generated Successfully!")
   except subprocess.CalledProcessError as e:
       messagebox.showerror("Error", f"Error Generating CSR:\n{e}")

# Function to browse files for key and csr output
def browse_key_out():
   filename = filedialog.asksaveasfilename(defaultextension=".pem", filetypes=[("PEM Files", "*.pem")])
   if filename:
       entry_key_out.delete(0, tk.END)
       entry_key_out.insert(0, filename)

def browse_csr_out():
   filename = filedialog.asksaveasfilename(defaultextension=".csr", filetypes=[("CSR Files", "*.csr")])
   if filename:
       entry_csr_out.delete(0, tk.END)
       entry_csr_out.insert(0, filename)

# Set up the main application window
root = tk.Tk()
root.title("CSR Generator")

# Define the layout
tk.Label(root, text="Country (C):").grid(row=0, column=0, sticky=tk.W)
entry_country = tk.Entry(root)
entry_country.grid(row=0, column=1)
entry_country.insert(0, 'US')

tk.Label(root, text="State (ST):").grid(row=1, column=0, sticky=tk.W)
entry_state = tk.Entry(root)
entry_state.grid(row=1, column=1)
entry_state.insert(0, 'MO')

tk.Label(root, text="Locality (L):").grid(row=2, column=0, sticky=tk.W)
entry_locality = tk.Entry(root)
entry_locality.grid(row=2, column=1)
entry_locality.insert(0, 'Maryland Heights')

tk.Label(root, text="Organization (O):").grid(row=3, column=0, sticky=tk.W)
entry_organization = tk.Entry(root)
entry_organization.grid(row=3, column=1)
entry_organization.insert(0, 'Poly')

tk.Label(root, text="Organizational Unit (OU):").grid(row=4, column=0, sticky=tk.W)
entry_org_unit = tk.Entry(root)
entry_org_unit.grid(row=4, column=1)
entry_org_unit.insert(0, 'Poly')

tk.Label(root, text="Common Name (CN):").grid(row=5, column=0, sticky=tk.W)
entry_common_name = tk.Entry(root)
entry_common_name.grid(row=5, column=1)

tk.Label(root, text="Email Address:").grid(row=6, column=0, sticky=tk.W)
entry_email = tk.Entry(root)
entry_email.grid(row=6, column=1)
entry_email.insert(0, 'Andrew.Schnur@EdwardJones.com')

tk.Label(root, text="Key Output File:").grid(row=7, column=0, sticky=tk.W)
entry_key_out = tk.Entry(root)
entry_key_out.grid(row=7, column=1)
tk.Button(root, text="Browse...", command=browse_key_out).grid(row=7, column=2)

tk.Label(root, text="CSR Output File:").grid(row=8, column=0, sticky=tk.W)
entry_csr_out = tk.Entry(root)
entry_csr_out.grid(row=8, column=1)
tk.Button(root, text="Browse...", command=browse_csr_out).grid(row=8, column=2)

tk.Button(root, text="Generate CSR", command=generate_csr).grid(row=9, column=0, columnspan=3)

# Run the Tkinter main loop
root.mainloop()