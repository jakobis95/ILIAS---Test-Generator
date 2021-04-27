from tkinter import *
from tkinter import ttk
from Picture_interface import picture_choice
import tkinter.font as font
import tkinter as tk



class variable_scrl_UI():
    def __init__(self, varname_list, bg_color, label_color, Label_Font, frame, StringVarList, index_dict, WIDTH, Rows, Columns, Header, header_index, column_type_list, columnwidth):
        self.bg_color = bg_color
        self.label_color = label_color
        self.Label_Font = Label_Font
        self.Rows = Rows
        self.Columns = Columns
        self.columnwidth = columnwidth
        self.StringVarList = StringVarList
        HeadingFrame = Frame(frame)
        HeadingFrame.place(relx=0, rely=0, relwidth=1, relheight=.2)

        #subframe
        mini_frame = Frame(frame)
        mini_frame.place(relx=0, rely=0.2, relwidth=1, relheight=.8)

        # Create A Canvas
        my_canvas = Canvas(mini_frame, bg=bg_color)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(mini_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        second_frame = Frame(my_canvas, bg=bg_color)

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
        Var_list = []
        rowlist = []

        # Screeninfo
        sections = 0
        for column in self.columnwidth:
            sections = sections + column

        relwidth = WIDTH / sections

        for row in range(self.Rows):
            rowlist.append(choice_row(index_dict, column_type_list, self.StringVarList, second_frame, row, relwidth , varname_list, self.Columns, self.columnwidth))

        HeadingFrame = Frame(frame)
        HeadingFrame.place(relx=0, rely=0, relwidth=1, relheight=.2)




        self.varlist = []
        self.var_name_label = []
        Y_abstand = .1


        self.var_header_label = Label(HeadingFrame, text=Header, bg=self.label_color, fg=self.bg_color)
        self.var_header_label['font'] = self.Label_Font
        self.var_header_label.place(relx=0, rely=0, relwidth=1, relheight=.5)
        relx = 0
        relw = 0
        for column in range(Columns):
            print(header_index[column])
            relw = columnwidth[column] / sections # relative breite der spaltenheader ist gleich der Auteilung der gesamtbreite (sections) durch die anzahl der sections für diese Spalte
            self.var_name_label.append(Label(HeadingFrame, text=header_index[column], bg=self.label_color, fg=self.bg_color))
            self.var_name_label[column]['font'] = self.Label_Font
            self.var_name_label[column].place(relx=relx, rely=0.5, relwidth=relw, relheight=.5)
            relx = relw + relx

class choice_column():
    def __init__(self, column_type, VarFrame, row, column, width,  TextVar):

        internal_F = Frame(VarFrame, width=width, height=30)
        internal_F.grid(row=row, column=column, pady=0, padx=0)

        if column_type == 0:
            self.entry = Entry(internal_F, textvariable=TextVar)
            self.entry.place(x=0, y=0, relwidth=1, relheight=1)
        elif column_type == 1:
            self.entry = picture_choice(TextVar, internal_F)
        elif column_type == 2:
            self.box = ttk.Combobox(internal_F, value=list(range(10)), textvariable=TextVar)
            self.box.place(x=0, y=0, relwidth=1, relheight=1)




class choice_row():
    def __init__(self, index_dict, column_type, Var_list, second_frame, row, relwidth, varname_list, columns, columnwidth):
        self.columns = columns
        self.rowlist = []
        self.Var_list = Var_list
        print("Varlist:", Var_list[19][0])
        for column in range(self.columns):
            index = index_dict[varname_list[column] .format(row + 1)]
            print(index)
            self.rowlist.append(choice_column(column_type[column], second_frame, row, column, int(relwidth * columnwidth[column]), Var_list[index][0]))


