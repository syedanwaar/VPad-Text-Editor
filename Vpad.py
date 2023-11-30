from ctypes.wintypes import WORD
from operator import mod
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, font, colorchooser, filedialog
import os

main_application=tk.Tk()
main_application.title("Vpad")
main_application.iconbitmap('./icons/icon.ico')
main_application.geometry('1000x600')# plan for rechange


#################################### main menu #######################################
main_menu=tk.Menu(main_application)
### File Menu
# File icons
new_icon=tk.PhotoImage(file="./icons/new.png")
open_icon=tk.PhotoImage(file="./icons/open.png")
save_icon=tk.PhotoImage(file="./icons/save.png")
save_as_icon=tk.PhotoImage(file="./icons/save_as.png")
exit_icon=tk.PhotoImage(file="./icons/exit.png")
# File 
file=tk.Menu(main_menu,tearoff=False)

### Edit Menu
# Edit icons
copy_icon=tk.PhotoImage(file="./icons/copy.png")
paste_icon=tk.PhotoImage(file="./icons/paste.png")
cut_icon=tk.PhotoImage(file='./icons/cut.png')
clear_all_icon=tk.PhotoImage(file='./icons/clear_all.png')
find_icon=tk.PhotoImage(file='./icons/find.png')
# Edit
edit=tk.Menu(main_menu,tearoff=False)

### View Menu
# View Icons
tool_bar_icon=tk.PhotoImage(file='./icons/tool_bar.png')
status_bar_icon=tk.PhotoImage(file='./icons/status_bar.png')
# View
view=tk.Menu(main_menu,tearoff=False)

#### Color Theme Menu
# ColorTheme Icon
light_default_icon=tk.PhotoImage(file="./icons/light_default.png")
light_plus_icon=tk.PhotoImage(file='./icons/light_plus.png')
dark_icon=tk.PhotoImage(file='./icons/dark.png')
red_icon=tk.PhotoImage(file='./icons/red.png')
monokai_icon=tk.PhotoImage(file='./icons/monokai.png')
night_blue_icon=tk.PhotoImage(file='./icons/night_blue.png')
theme_choice=tk.StringVar()
color_icons=(light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)
color_dict={
    "Light Default":("#000000","#ffffff"),
    "Light Plus":("#474747","#e0e0e0"),
    "Dark":("#c4c4c4","#2d2d2d"),
    "Red":("#2d2d2d","#ffe8e8"),
    "Monokai":("#d3b774","#474747"),
    "Night Blue":("#ededed","#6b9dc2")
}
# color theme
color_theme=tk.Menu(main_menu,tearoff=False)

### Adding Submenus to main menu
main_menu.add_cascade(label="File",menu=file)
main_menu.add_cascade(label="Edit",menu=edit)
main_menu.add_cascade(label="View",menu=view)
main_menu.add_cascade(label="Color Theme",menu=color_theme)
# ------------------------&&&&&&&&&&& end main nenu &&&&&&&&&&&&-----------------------


#################################### toolbar #######################################
tool_bar=ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)

## fontbox
font_tuple=font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family, state='readonly')
font_box['values']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,sticky=tk.W,padx=5,ipady=2)

## sizebox
size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
font_size['values']=tuple(i for i in range(8,81,2))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5,ipady=2)

## Bold button
bold_icon=tk.PhotoImage(file="./icons/bold.png")
bold_btn=ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0,column=2,padx=3)

## Italic button
italic_icon=tk.PhotoImage(file="./icons/italic.png")
italic_btn=ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0,column=3,padx=3)

## Italic button
underline_icon=tk.PhotoImage(file="./icons/underline.png")
underline_btn=ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0,column=4,padx=3)

## font color button
font_color_icon=tk.PhotoImage(file="./icons/font_color.png")
font_color_btn=ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=3)

## align left
align_left_icon=tk.PhotoImage(file="./icons/align_left.png")
align_left_btn=ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=3)

## align center button
align_center_icon=tk.PhotoImage(file="./icons/align_center.png")
align_center_btn=ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=3)

## align right button
align_right_icon=tk.PhotoImage(file="./icons/align_right.png")
align_right_btn=ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=3)
# ------------------------&&&&&&&&&&& end toolbar &&&&&&&&&&&&-----------------------


#################################### text editor #######################################
text_editor=tk.Text(main_application)
text_editor.config(wrap='word')

scroll_bar=tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

###### font family and font size functionality
current_font_family="Arial"
current_font_size=12

def change_font(event=None):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_fontsize(event=None):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.config(font=(current_font_family, current_font_size))

font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>",change_fontsize)

###### Buttons functionality

# Bold button functionality
def change_bold():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'bold':
        text_editor.config(font=(current_font_family,current_font_size,'normal'))
    elif text_property.actual()['weight'] == 'normal':
        text_editor.config(font=(current_font_family,current_font_size,'bold'))

bold_btn.configure(command=change_bold)

# Italic button functionaliy
def change_italic():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.config(font=(current_font_family,current_font_size,'italic'))
    elif text_property.actual()['slant'] == 'italic':
        text_editor.config(font=(current_font_family,current_font_size,'roman'))

italic_btn.config(command=change_italic)

# Underline button functionaliy
def change_underline():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.config(font=(current_font_family,current_font_size,'underline'))
    elif text_property.actual()['underline'] == 1:
        text_editor.config(font=(current_font_family,current_font_size,'normal'))

underline_btn.config(command=change_underline)

# change font color functionality
def change_font_color():
    color_var=colorchooser.askcolor()
    text_editor.config(fg=color_var[1])

font_color_btn.config(command=change_font_color)

### Align Functionality

# right align functionality
def align_right():
    text_content=text_editor.get(1.0,tk.END)
    text_editor.tag_config(tk.RIGHT,justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,tk.RIGHT)

align_right_btn.config(command=align_right)

# center align functionality
def align_center():
    text_content=text_editor.get(1.0,tk.END)
    text_editor.tag_config(tk.CENTER,justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,tk.CENTER)
    
align_center_btn.config(command=align_center)

# left align functionality
def align_left():
    text_content=text_editor.get(1.0,tk.END)
    text_editor.tag_config(tk.LEFT,justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')
    
align_left_btn.config(command=align_left)

text_editor.configure(font=("Arial",12))
# ------------------------&&&&&&&&&&& end text editor &&&&&&&&&&&&-----------------------


#################################### statusbar #######################################
status_bar=ttk.Label(main_application,text=f"Characters : {0} Words : {0}")
status_bar.pack(side=tk.BOTTOM)

text_changed=False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        content=text_editor.get(1.0,'end-1c')
        status_bar.config(text=f"Characters : {len(content)} Words : {len(content.split())}")
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>",changed)
# ------------------------&&&&&&&&&&& end statusbar &&&&&&&&&&&&-----------------------


#################################### main menu functionality #######################################
## global url variable
url=""

### file Commands

## new functionality
def new_file(event=None):
    global url
    url=""
    text_editor.delete(1.0,tk.END)
    main_application.title("Untitled")
file.add_command(label="New", image=new_icon, compound=tk.LEFT, accelerator="Ctrl+N",command=new_file)

## Open functionality
def open_file(event=None):
    global url
    url= filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File", filetypes=(("Text files","*.txt"),("All Files","*.*")))
    try:
        with open(url,'r', encoding='utf-8') as f:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,f.read(),tk.END)
    except Exception:
        return
    main_application.title(os.path.basename(url))

file.add_command(label="Open", image=open_icon, compound=tk.LEFT, accelerator="Ctrl+O", command=open_file)

## save functionality
def save_file(event=None):
    global url
    try:
        if url:
            with open(url,'w',encoding='utf-8') as f:
                content=str(text_editor.get(1.0,tk.END))
                f.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension=".txt",filetypes=(("Text Files",'*.txt'),("All Files",'*.*')))
            content=text_editor.get(1.0, tk.END)
            url.write(content)
            url.close()
    except:
        return
file.add_command(label="Save", image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S', command=save_file)

## save as functionality
def save_as(event=None):
    global url
    try:
        content=str(text_editor.get(1.0,tk.END))
        url=filedialog.asksaveasfile(mode="w",defaultextension='.txt',filetypes=(('Text Files',"*.txt"),("All Files",'*.*')))
        url.write(content)
        url.close()
    except:
        return
file.add_command(label='Save As', image=save_as_icon, compound=tk.LEFT, accelerator="Ctrl+Alt+S", command=save_as)
file.add_separator()

## exit functionality
def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel("Warning", "Do you want to save the file ?")
            if mbox is True:
                if url:
                    content=str(text_editor.get(1.0,tk.END))
                    with open(url, 'w', encoding='utf-8') as f:
                        f.write(content)
                else:
                    content=str(text_editor.get(1.0,tk.END))
                    url=filedialog.asksaveasfile(mode='w',defaultextension=".txt", filetypes=(("Text Files","*.txt"),("All Files","*.*")))
                    url.write(content)
                    url.close()
                main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return
file.add_command(label="Exit",image=exit_icon, compound=tk.LEFT, accelerator="Ctrl+Q", command=exit_func)

### Edit Commands
edit.add_command(label="Copy", image=copy_icon, compound=tk.LEFT, accelerator="Ctrl+C",command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label="Paste", image=paste_icon, compound=tk.LEFT, accelerator="Ctrl+V",command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="Cut", image=cut_icon, compound=tk.LEFT, accelerator="Ctrl+X", command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label="Clear All", image=clear_all_icon, compound=tk.LEFT, accelerator="Ctrl+Alt+X", command=lambda:text_editor.delete(1.0,tk.END))

## Find Functionality
def find_func(event=None):
    def find():
        word= str(text_find_input.get())
        text_editor.tag_remove('match','1.0',tk.END)
        matches=0
        if word:
            start_pos="1.0"
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match",f"{start_pos}",end_pos)
                start_pos=end_pos
                text_editor.tag_config("match",foreground="Red",background="Yellow")

    def replace():
        word=str(text_find_input.get())
        replace_text=str(text_replace_input.get())
        content=str(text_editor.get(1.0,tk.END))
        content=content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,content,tk.END)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry("450x250+400+200")
    find_dialogue.title("Find")
    find_dialogue.resizable(0,0)
    ## Find frame
    find_frame=ttk.LabelFrame(find_dialogue,text="Find/Replace")
    find_frame.pack(pady=30)
    ## Labels
    text_find_label=ttk.Label(find_frame,text="Find : ")
    text_replace_label=ttk.Label(find_frame,text="Replace : ")
    ## Entry
    text_find_input=ttk.Entry(find_frame,width=35)
    text_replace_input=ttk.Entry(find_frame,width=35)
    ## Buttons
    find_btn=ttk.Button(find_frame,text="Find",command=find)
    replace_btn=ttk.Button(find_frame,text="Replace",command=replace)
    ## Grids
    # Label Grid
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)
    # Entry Grid
    text_find_input.grid(row=0,column=1,padx=4,pady=4)
    text_replace_input.grid(row=1,column=1,padx=4,pady=4)
    # Button Grid
    find_btn.grid(row=2,column=0,padx=8,pady=4)
    replace_btn.grid(row=2,column=1,padx=8,pady=4)

    find_dialogue.mainloop()

edit.add_command(label="Find", image=find_icon, compound=tk.LEFT, accelerator="Ctrl+F",command=find_func)

### View checkbuttons
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(expand=True,fill=tk.BOTH)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True

view.add_checkbutton(label="Tool Bar", variable=show_toolbar, onvalue=1, offvalue=0 ,image=tool_bar_icon, compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label='Status Bar', variable=show_statusbar ,onvalue=1, offvalue=0, image=status_bar_icon, compound=tk.LEFT, command=hide_statusbar)

### Color theme commands

def change_theme():
    chosen_theme=theme_choice.get()
    color_tuple=color_dict.get(chosen_theme)
    fg_color,bg_color=color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,foreground=fg_color)

count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icons[count],compound=tk.LEFT,variable=theme_choice, command=change_theme)
    count+=1
# ------------------------&&&&&&&&&&& end main menu functionality &&&&&&&&&&&&-----------------------
main_application.config(menu=main_menu)

### Binding Shortcut keys
main_application.bind("<Control-n>",new_file)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Alt-s>", save_as)
main_application.bind("<Control-q>",exit_func)
main_application.bind("<Control-f>",find_func)

main_application.mainloop()