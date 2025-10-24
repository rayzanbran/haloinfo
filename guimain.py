from tkinter import *
from tkinter import ttk
import haloinfohelper

root = Tk()
root.title("haloinfo")
root.geometry('300x150')
root.resizable(width=True, height=True)

mainframe = ttk.Frame(padding=5)
mainframe.grid(row=0, column=0, sticky=(N, S, E, W))

# Logic
def get_halo_info(*args):
    global halopedia_link_label_var
    global halo_name_label_var
    global halopedia_link_label_var

    print(f"Selected: {selected_halo.get()}")
    halo_name_label_var.set(haloinfohelper.gethalo(selected_halo.get()))
    halo_release_date_label_var.set(haloinfohelper.get_release_date(selected_halo.get()))
    halopedia_link_label_var.set(haloinfohelper.get_halopedia_link(selected_halo.get()))

def copy_link_to_clipboard(*args):
    root.clipboard_append(halopedia_link_label_var.get())
    root.update()

# Telling the window elements to expand with the window size
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)

# Creating and placing the radio button menu that will have all the halo game names
button_label_var = StringVar(value="Choose a Halo")
halo_button = ttk.Menubutton(mainframe, text=button_label_var.get(), style="TMenubutton", padding=5)
halo_button.grid(column=0, row=0, sticky=(N, E, W))

halo_names_menu = Menu()

selected_halo = StringVar()

for option in haloinfohelper.get_keys():
    halo_names_menu.add_radiobutton(label = haloinfohelper.gethalo(option), value=option, variable = selected_halo, command=get_halo_info) # command = get_halo_info

halo_button['menu'] = halo_names_menu

# Create labels that will display the information about the game
# And set stringvars that will be able to change and update the labels automatically
halo_name_label_var = StringVar()
halo_name_label = ttk.Label(mainframe, textvariable = halo_name_label_var, padding=5)
halo_name_label.grid(column=0, row=1, sticky=(N, S))

halo_release_date_label_var = StringVar()
halo_release_date_label = ttk.Label(mainframe, textvariable = halo_release_date_label_var, padding=5)
halo_release_date_label.grid(column=0, row=2, sticky=(N, S))

halopedia_link_label_var = StringVar()
halopedia_link_label = ttk.Label(mainframe, textvariable = halopedia_link_label_var, padding=5)
halopedia_link_label.grid(column=0, row=3, sticky=(N, S))

# Button for copying the Halopedia link to the clipboard
# because ttk labels cannot be selected...sigh...
halopedia_link_copy_button = ttk.Button(mainframe, text= 'Copy Link', command=copy_link_to_clipboard)
halopedia_link_copy_button.grid(column=0, row=4, sticky=(N, S))

# Run the program
root.mainloop()