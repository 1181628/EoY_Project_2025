import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()
root.title("")
root.geometry("520x750+300+90")

#image = Image.open("a_name.png")
#image = image.resize((100,100), Image.LANCZOS)
#image = ImageTk.PhotoImage(image)

#laybel image
#laybel title subtitle
#bugs

#-----------setting-----------
total = 0
maximum_cards = 10
maximum_stats = 25
minimum_stats = 1
image_label = ""
user_catalogue = {}
existed_catalogue = {}
frames = {}
window = {}
card = {}
sort_list = {}
sorted_catalogue = {}
error_flag = {"flag": "no"}
parent_frame = {}
sort = "Alphabetical"
last_sort = {"sort_by": "Sort by..."}
general_catalogue = {}
reverse_flag = tk.BooleanVar(value=True)

image = Image.open("1.png")
image = image.resize((100,100), Image.LANCZOS)
Blazegolem = ImageTk.PhotoImage(image)

image = Image.open("2.png")
image = image.resize((100,100), Image.LANCZOS)
Dawnmirage = ImageTk.PhotoImage(image)

image = Image.open("3.png")
image = image.resize((100,100), Image.LANCZOS)
Frostste = ImageTk.PhotoImage(image)

image = Image.open("4.png")
image = image.resize((100,100), Image.LANCZOS)
Moldvine = ImageTk.PhotoImage(image)

image = Image.open("5.png")
image = image.resize((100,100), Image.LANCZOS)
Vexscream = ImageTk.PhotoImage(image)

image = Image.open("6.png")
image = image.resize((100,100), Image.LANCZOS)
Vortexwing = ImageTk.PhotoImage(image)

image = Image.open("7.png")
image = image.resize((100,100), Image.LANCZOS)
Wispghoul = ImageTk.PhotoImage(image)

image = Image.open("8.png")
image = image.resize((100,100), Image.LANCZOS)
Nightraid = ImageTk.PhotoImage(image)

image = Image.open("9.png")
image = image.resize((100,100), Image.LANCZOS)
Angryblow = ImageTk.PhotoImage(image)

image = Image.open("10.png")
image = image.resize((100,100), Image.LANCZOS)
Thelastone = ImageTk.PhotoImage(image)

def create_image_buttons():
    images = [Blazegolem, Dawnmirage, Frostste, Moldvine, Vexscream,
             Vortexwing, Wispghoul, Nightraid, Angryblow, Thelastone]    
    for i, img in enumerate(images):
        btn = tk.Button(root, image=img, command=lambda i=i: select_image(i))
        btn.pack()

def select_image(index):
    images = [Blazegolem, Dawnmirage, Frostste, Moldvine, Vexscream,
             Vortexwing, Wispghoul, Nightraid, Angryblow, Thelastone]
    image_label.config(image=images[index])
    image_label.image = images[index]

def upload_catalogue():
    with open('user_catalogue_file.txt', 'r') as usercatalogueFile:
        for line in usercatalogueFile:
            if line.strip():
                name, stats = line.strip().split(':', 1)
                values = [int(item.strip()) for item in stats.split(',')]
                user_catalogue[name.strip()] = values
    with open('existed_catalogue.txt', 'r') as existedcatalogueFile:
        for line in existedcatalogueFile:
            if line.strip():
                name, stats = line.strip().split(':', 1)
                values = [int(item.strip()) for item in stats.split(',')]
                existed_catalogue[name.strip()] = values

def save_catalogue():
    with open('user_catalogue_file.txt', 'w') as usercatalogueFile:
        for name, stats in user_catalogue.items():
            each = f"{name}: {','.join(map(str, stats))}\n"
            usercatalogueFile.write(each)

def close_root():
    root.destroy()

def end_page():
    save_catalogue()
    root = tk.Toplevel()
    root.title("Over look")
    root.geometry("300x500+800+90")
    #label title
    for name, stats in user_catalogue.items():
        label = tk.Label(root, text=f"{name}: {stats}")
        label.pack()
    confirm_button = tk.Button(root, text="Confirm", command=close_root)
    confirm_button.pack()

def save_exit():
    response = messagebox.askquestion("Save & Exit", "Are you sure you want to end your program? (We will automatically save your catalogue)")
    if response == "yes":
        end_page()
    else:
        return

#----------sub functions----------    
def error_popup(invalids):
    error_flag["flag"] = "yes"
    if invalids == 1:
        messagebox.showerror("Error", "You have reached the maximum number of cards!")
    elif invalids == 2:
        messagebox.showerror("Error", "This card name already exists in the existing catalogue!")
    elif invalids == 3:
        messagebox.showerror("Error", "This card name already exists in your catalogue!")
    elif invalids == 4:
        messagebox.showerror("Error", "All stats must be integers!")
    elif invalids == 5:
        messagebox.showerror("Error", f"Strength must be between {minimum_stats} and {maximum_stats}!")
    elif invalids == 6:
        messagebox.showerror("Error", f"Speed must be between {minimum_stats} and {maximum_stats}!")
    elif invalids == 7:
        messagebox.showerror("Error", f"Stealth must be between {minimum_stats} and {maximum_stats}!")
    elif invalids == 8:
        messagebox.showerror("Error", f"Cunning must be between {minimum_stats} and {maximum_stats}!")


def check_invalid(action):
    if action == 3:
        if (card["name"].get() in existed_catalogue.keys()):
            error_popup(2)
            return
        if (card["name"].get() in user_catalogue.keys()):
            error_popup(3)
            return
    elif action == 4:
        if (card["name"] in existed_catalogue.keys()):
            error_popup(2)
            return
        if (card["name"] in user_catalogue.keys()):
            error_popup(3)
            return
    if action == 3:
        try:
            strength = int(card["strength"].get())
            speed = int(card["speed"].get())
            stealth = int(card["stealth"].get())
            cunning = int(card["cunning"].get())
        except ValueError:
            error_popup(4)
            return
        if (strength > maximum_stats) or (strength < minimum_stats):
            error_popup(5)
            return
        if (speed > maximum_stats) or (speed < minimum_stats):
            error_popup(6)
            return
        if (stealth > maximum_stats) or (stealth < minimum_stats):
            error_popup(7)
            return
        if (cunning > maximum_stats) or (cunning < minimum_stats):
            error_popup(8)
            return

def check_invalid_len():
    if len(user_catalogue) == maximum_cards:
        error_popup(1)
        error_flag["flag"] = "yes"

def go_back():
    if ("catalogue" in frames):
        frames["catalogue"].destroy()
        del frames["catalogue"]
    if "manage" in frames:
        frames["manage"].destroy()
        del frames["manage"]
    if "sort" in frames:
        frames["sort"].destroy()
        del frames["sort"]
    if "print" in frames:
        frames["print"].destroy()
        del frames["print"]

def find_card(entry):
    if entry in general_catalogue.keys():
        card["name"] = entry
        card_detail(1)
    else:
        messagebox.showinfo("Invalid Entry", f"There is no card named '{entry}' in the catalogue.")

def sort_card(sort_action, reverse_flag):
    sort = sort_list["sort_combo"].get()
    if "catalogue" in frames:
        frames["catalogue"].destroy()
        del frames["catalogue"]    
    if sort_list["sort_combo"].get() == "Sort by...":
        if sort_action == 6:
            sort = last_sort["sort_by"]
        else:
            if last_sort["sort_by"] == "Sort by...":
                sort = "Alphabetical"
            else:
                sort = last_sort["sort_by"]
            sort = "Alphabetical"
    if sort_action == 7:
        reverse_flag.set(not reverse_flag.get())
        reverse = reverse_flag.get()
        reverse2 = (not reverse_flag.get())
    else: 
        reverse_flag2 = tk.BooleanVar(value=True)
        reverse = reverse_flag2.get()
        reverse2 = (not reverse_flag2.get())
    if sort == "Alphabetical":
        sorted_catalogue = dict(sorted(general_catalogue.items(), key=lambda name: name[0].casefold(), reverse=reverse2))
    elif sort == "Total scored":
        sorted_catalogue = dict(sorted(general_catalogue.items(), key=lambda name: name[1][4], reverse=reverse))
    elif sort == "Strength":
        sorted_catalogue = dict(sorted(general_catalogue.items(), key=lambda name: name[1][0], reverse=reverse))
    elif sort == "Speed":
        sorted_catalogue = dict(sorted(general_catalogue.items(), key=lambda name: name[1][1], reverse=reverse))
    elif sort == "Stealth":
        sorted_catalogue = dict(sorted(general_catalogue.items(), key=lambda name: name[1][2], reverse=reverse))
    elif sort == "Cunning":
        sorted_catalogue = dict(sorted(general_catalogue.items(), key=lambda name: name[1][3], reverse=reverse))
    last_sort["sort_by"] = sort
    general_catalogue.clear()
    general_catalogue.update(sorted_catalogue)
    label_catalogue(6) 

def inside_frame_label(action):
    if action in (1, 2):
        frame_key = "sort"
    elif "manage" in frames:
        frame_key = "manage"
    else:
        return
    if frame_key not in frames:
        frames[frame_key] = tk.Frame(root, bg="grey")
        frames[frame_key].pack()
        frames[frame_key].grid_propagate(False)
    parent_frame = frames[frame_key]
    find_label = tk.Label(parent_frame, text="Find the card...")
    find_entry = tk.Entry(parent_frame)
    find_button = tk.Button(parent_frame, text="Find", command=lambda:find_card(find_entry.get()))
    sort_list["sort_combo"] = ttk.Combobox(parent_frame, 
                                                     values=["Alphabetical", "Total scored", "Strength", "Speed", "Stealth", "Cunning"])
    sort_list["sort_combo"].set("Sort by...")
    sort_button = tk.Button(parent_frame, text="Sort", command=lambda:sort_card(6, reverse_flag))
    reverse_button = tk.Button(parent_frame, text="↑↓", command=lambda:sort_card(7, reverse_flag))
    go_back_button = tk.Button(parent_frame, text="Go back", command=go_back)
    find_label.pack()
    find_entry.pack()
    find_button.pack()
    sort_list["sort_combo"].pack()
    reverse_button.pack()
    sort_button.pack()
    go_back_button.pack()

#----------main functions----------
def confirm_action(action):
    if (action != 1) and (action != 2) and (action != 6):
        check_invalid(action)
        if error_flag["flag"] == "yes":
            return
        #card_detail(action)
    if action == 3:
        strength = int(card["strength"].get())
        speed = int(card["speed"].get())
        stealth = int(card["stealth"].get())
        cunning = int(card["cunning"].get())
        total = strength + speed + stealth + cunning
        user_catalogue[card["name"].get()] = [strength, speed, stealth, cunning, total]
    elif action == 4:
        user_catalogue[card["name"]] = existed_catalogue[card["name"]]
    elif action == 5:
        del user_catalogue[card["name"]]
        #bug
    save_catalogue()
    if "window2" in window:
        window["window2"].destroy()
        #bug

def cancel_action():
    response = messagebox.askquestion("Cancel", "Are you sure you want to stop editing this card?")
    if response == "yes":
        window["window2"].destroy()
    else:
        return

def card_detail(action):
    window["window2"] = tk.Toplevel(root)
    window["window2"].title(card["name"])
    window["window2"].geometry("300x500+800+90")
    name_label = tk.Label(window["window2"], text=card["name"])
    image = tk.Label(root, image=card["name"])
    image.pack()
    strength_label = tk.Label(window["window2"], text=f"Strength: {general_catalogue[card['name']][0]}")
    speed_label = tk.Label(window["window2"], text=f"Speed: {general_catalogue[card['name']][1]}")
    stealth_label = tk.Label(window["window2"], text=f"Stealth: {general_catalogue[card['name']][2]}")
    cunning_label = tk.Label(window["window2"], text=f"Cunning: {general_catalogue[card['name']][3]}")
    totalscore_label = tk.Label(window["window2"], text=f"Total scores: {general_catalogue[card['name']][4]}")
    confirm_button = tk.Button(window["window2"], text="Confirm", command=lambda: confirm_action(action))
    confirm_button.pack()
    if (action != 1) and (action != 2) and (action != 6):
        cancel_button = tk.Button(window["window2"], text="Cancel", command=cancel_action)
        cancel_button.pack()
    name_label.pack()
    strength_label.pack()
    speed_label.pack()
    stealth_label.pack()
    cunning_label.pack()
    totalscore_label.pack()

def add_new_card():
    check_invalid_len()
    if error_flag["flag"] == "yes":
        return
    error_flag["flag"] = "no"
    window["window2"] = tk.Toplevel(root)
    window["window2"].title("Make your own card")
    window["window2"].geometry("300x500+800+90")
    name_label = tk.Label(window["window2"], text="Name:")
    card["name"] = tk.Entry(window["window2"])
    strength_label = tk.Label(window["window2"], text="Strength:")
    card["strength"] = tk.Entry(window["window2"])
    speed_label = tk.Label(window["window2"], text="Speed:")
    card["speed"] = tk.Entry(window["window2"])
    stealth_label = tk.Label(window["window2"], text="Stealth:")
    card["stealth"] = tk.Entry(window["window2"])
    cunning_label = tk.Label(window["window2"], text="Cunning:")
    card["cunning"] = tk.Entry(window["window2"])
    name_label.pack()
    card["name"].pack()
    strength_label.pack()
    card["strength"].pack()
    speed_label.pack()
    card["speed"].pack()
    stealth_label.pack()
    card["stealth"].pack()
    cunning_label.pack()
    card["cunning"].pack()
    select_button = tk.Button(root, text="Select Image", command=select_image)
    select_button.pack()
    confirm_button = tk.Button(window["window2"], text="Confirm", command=lambda: confirm_action(3))
    confirm_button.pack()
    cancel_button = tk.Button(window["window2"], text="Cancel", command=cancel_action)
    cancel_button.pack()

def label_catalogue(action):
    #error
    if action == 4:
        check_invalid_len()
        if error_flag["flag"] == "yes":
            return
    error_flag["flag"] = "no"
    frames["catalogue"] = tk.Frame(root, bg="grey")
    frames["catalogue"].pack()
    frames["catalogue"].grid_propagate(False)
    text_label = tk.Label(frames["catalogue"], text=f"Your Monster Card Catalogue: {len(user_catalogue)}/10")
    text_label.pack()
    if (action == 1) or (action == 5):
        general_catalogue.update(user_catalogue)
    elif (action == 2) or (action == 4):
        general_catalogue.update(existed_catalogue)
    for name, stats in general_catalogue.items():
        cards_button = tk.Button(frames["catalogue"], text=name, command=lambda name=name:(card.update({"name": name}), card_detail(action)))
        cards_button.pack()
        if action == 5:
            label = tk.Label(frames["catalogue"], text=" ", bg="red")
            label.pack()
            #may be bug here
    inside_frame_label(action)

def manage_user_catalogue():
    frames["manage"] = tk.Frame(root, bg="grey")
    frames["manage"].pack()
    frames["manage"].grid_propagate(False)
    add_new_button = tk.Button(frames["manage"], text="Make your own card", command=add_new_card)
    add_new_button.pack()
    add_exist_button = tk.Button(frames["manage"], text="Add from existing cards", command=lambda:label_catalogue(4))
    add_exist_button.pack()
    delete_button = tk.Button(frames["manage"], text="Removing a card", command=lambda:label_catalogue(5))
    delete_button.pack()
    go_back_button = tk.Button(frames["manage"], text="Go back", command=go_back)
    go_back_button.pack()

#----------main code----------
upload_catalogue()
user_catalogue = dict(sorted(user_catalogue.items(), key=lambda name: name[0].lower()))
existed_catalogue = dict(sorted(existed_catalogue.items(), key=lambda name: name[0].lower()))
for name, stats in user_catalogue.items():
        total = total + sum(stats[:4])

frames["title"] = tk.Frame(root, bg="grey")
frames["title"].pack()
frames["title"].grid_propagate(False)
title_label = tk.Label(frames["title"], text="Monster Card Game Digital Catalogue")
title_label.pack()
text_label = tk.Label(frames["title"], text="——————————————————————————————————————————")
subtitle_label = tk.Label(frames["title"], text="Choose what you want to do:")
subtitle_label.pack()

frames["inform"] = tk.Frame(root, bg="grey")
frames["inform"].pack()
frames["inform"].grid_propagate(False)
text_label = tk.Label(frames["inform"], text=f"Your Monster Card Catalogue: {len(user_catalogue)}/10")
text_label.pack()
text_label = tk.Label(frames["inform"], text=f"Your Monster Card's Stats': {total}")
text_label.pack()

frames["button"] = tk.Frame(root, bg="grey")
frames["button"].pack()
frames["button"].grid_propagate(False)
user_catalogue_button = tk.Button(frames["button"], text="View your card catalogue", command=lambda: label_catalogue(1))
user_catalogue_button.pack()
exist_catalogue_button = tk.Button(frames["button"], text="View existing card's catalogue", command=lambda: label_catalogue(2))
exist_catalogue_button.pack()
manage_catalogue_button = tk.Button(frames["button"], text="Manage your card catalogue", command=manage_user_catalogue)
manage_catalogue_button.pack()
exit_button = tk.Button(root, text="Save & Exit", command=save_exit)
exit_button.pack()


#action1 : label user catalgoue
#action2 : label existed catalgoue
#action3 : made and add new cards
#action4 : label existed catalgoue and add from existed cards
#action5 : label user catalgoue and delete cards
#action6 : label cards that was beeing sorted and also used to mark no reverse
#action7 : used to mark as reversed

root.mainloop()