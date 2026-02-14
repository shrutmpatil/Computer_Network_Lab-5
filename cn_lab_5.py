import tkinter as tk
from tkinter import messagebox
import math

def get_ip_class(first_octet):
    if 1 <= first_octet <= 126:
        return "A"
    elif 128 <= first_octet <= 191:
        return "B"
    elif 192 <= first_octet <= 223:
        return "C"
    elif 224 <= first_octet <= 239:
        return "D"
    elif 240 <= first_octet <= 255:
        return "E"
    else:
        return "Invalid"

def ip_details():
    ip = entry.get().strip()
    parts = ip.split(".")

    # Clear previous result
    result_text.delete(1.0, tk.END)

    if len(parts) != 4:
        messagebox.showerror("Error", "Invalid IP Address Format")
        return

    try:
        parts = [int(part) for part in parts]
        if not all(0 <= part <= 255 for part in parts):
            raise ValueError
    except:
        messagebox.showerror("Error", "Invalid IP Address")
        return

    first_octet = parts[0]
    ip_class = get_ip_class(first_octet)

    if ip_class == "Invalid":
        messagebox.showerror("Error", "Invalid IP Address")
        return

    output = f"IP Address: {ip}\n"
    output += f"Class of IP Address: {ip_class}\n\n"

    if ip_class == "A":
        net_bits = 8
        host_bits = 24
        networks = 2**7 - 2
        hosts = 2**24 - 2
        start_range = "1.0.0.0"
        end_range = "126.255.255.255"
        subnet_mask = "255.0.0.0"

    elif ip_class == "B":
        net_bits = 16
        host_bits = 16
        networks = 2**14
        hosts = 2**16 - 2
        start_range = "128.0.0.0"
        end_range = "191.255.255.255"
        subnet_mask = "255.255.0.0"

    elif ip_class == "C":
        net_bits = 24
        host_bits = 8
        networks = 2**21
        hosts = 2**8 - 2
        start_range = "192.0.0.0"
        end_range = "223.255.255.255"
        subnet_mask = "255.255.255.0"

    elif ip_class == "D":
        result_text.insert(tk.END, "Class D is reserved for Multicasting.")
        return

    elif ip_class == "E":
        result_text.insert(tk.END, "Class E is reserved for Experimental purposes.")
        return

    output += f"Number of NetID bits: {net_bits}\n"
    output += f"Number of HostID bits: {host_bits}\n"
    output += f"Number of networks supported: {networks}\n"
    output += f"Number of hosts per network: {hosts}\n"
    output += f"Start range: {start_range}\n"
    output += f"End range: {end_range}\n"
    output += f"Default Subnet Mask: {subnet_mask}\n"

    result_text.insert(tk.END, output)


# ===== GUI Setup =====
root = tk.Tk()
root.title("IPv4 Class Analyzer")
root.geometry("500x450")
root.resizable(False, False)

title_label = tk.Label(root, text="IPv4 Address Classification", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

entry_label = tk.Label(root, text="Enter IPv4 Address:")
entry_label.pack()

entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=5)

calc_button = tk.Button(root, text="Calculate", command=ip_details, width=15)
calc_button.pack(pady=10)

result_text = tk.Text(root, height=15, width=60)
result_text.pack(pady=10)

root.mainloop()