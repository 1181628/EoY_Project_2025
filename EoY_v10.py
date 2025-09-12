def select_image(direction, image_label, image_name_label):    
    if direction == "left":
        image_number["current"] =  image_number["current"] - 1
        if image_number["current"] < 8:
            image_number["current"] = 20
    elif direction == "right":
        image_number["current"] = image_number["current"] + 1
        if image_number["current"] > 20:
            image_number["current"] = 8
    
    image_label.config(image=image_dictionary[image_number["current"]])
    image_label.image = image_dictionary[image_number["current"]]
    
    image_name_label.config(text=f"Selected: image{image_number['current']}")



def add_new_card():
    check_invalid_len()
    if error_flag["flag"] == "yes":
        return
    error_flag["flag"] = "no"
    window["window2"] = tk.Toplevel(root, bg="white")
    window["window2"].title("Make your own card")
    window["window2"].geometry("340x600+800+90")

    frames["labeling"] = tk.Frame(window["window2"], bg="#f2d243")
    frames["labeling"].place(x=5, y=5, height=590, width=330)
    frames["labeling"].grid_propagate(False)    
    
    image_label = tk.Label(window["window2"])
    image_label.pack(pady=5)
    image_label.config(image=image_dictionary[image_number["current"]])
    image_label.image = image_dictionary[image_number["current"]]
    
    image_name_label = tk.Label(window["window2"], text=f"Selected: image{image_number['current']}",
                              font=("Arial", 12), fg="blue")
    image_name_label.pack(pady=5)
    
    select_left_button = tk.Button(window["window2"], text="◀", 
        command=lambda: select_image("left", image_label, image_name_label),
        font=themes["card"]["font"], bg=themes["exit"]["bg"], fg=themes["exit"]["fg"], 
        width=themes["exit"]["width"], relief=themes["relief"])
    select_left_button.pack()

    select_right_button = tk.Button(window["window2"], text="▶", 
        command=lambda: select_image("right", image_label, image_name_label),
        font=themes["card"]["font"], bg=themes["exit"]["bg"], fg=themes["exit"]["fg"], 
        width=themes["exit"]["width"], relief=themes["relief"])
    select_right_button.pack()




image_number = {"current": 8}
image_label = ""
