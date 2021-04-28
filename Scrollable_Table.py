from tkinter import *
from tkinter import ttk
from Picture_interface import picture_choice
import tkinter.font as font
import tkinter as tk

class Variablen_UI():
    def __init__(self, bg_color, label_color, Label_Font, frame, StringVarList, index_dict, WIDTH, Rows, Columns, Header, header_index, Type):
        self.bg_color = bg_color
        self.label_color = label_color
        self.Label_Font = Label_Font
        self.Rows = Rows
        self.Columns = Columns
        self.StringVarList = StringVarList
        HeadingFrame = Frame(frame)
        HeadingFrame.place(relx=0, rely=0, relwidth=1, relheight=.2)

        #subframe
        mini_frame = Frame(frame)
        mini_frame.place(relx=0, rely=0.2, relwidth=1, relheight=.8)

        # Create A Canvas
        my_canvas = Canvas(mini_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(mini_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        second_frame = Frame(my_canvas)

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
        Var_list = []
        rowlist = []

        # Screeninfo
        relwidth = WIDTH / (self.Columns * 2)
        if Type == "Var":
            for row in range(self.Rows):
                index = index_dict["var{}_name" .format(row+1)]
                #self.varlist = [] todo wozu ist das da?
                rowlist.append(Var_row(self.StringVarList, second_frame, row, relwidth, index, self.Columns))
        else:
            for row in range(self.Rows):
                if row < self.Rows-1:
                    index = index_dict["res{}_name".format(row + 1)]
                else:
                    index = index_dict["res{}_formula".format(row + 1)]
                rowlist.append(Var_row(self.StringVarList, second_frame, row, relwidth, index, self.Columns))
        HeadingFrame = Frame(frame)
        HeadingFrame.place(relx=0, rely=0, relwidth=1, relheight=.2)



        index = index_dict["var1_name"]
        self.varlist = []
        self.var_name_label = []
        Y_abstand = .1
        print("index von var_name in data ist", index)
        print("data", self.StringVarList[index][0])
        print("data", self.StringVarList[index])

        self.var_header_label = Label(HeadingFrame, text=Header, bg=self.label_color, fg=self.bg_color)
        self.var_header_label['font'] = self.Label_Font
        self.var_header_label.place(relx=0, rely=0, relwidth=1, relheight=.5)

        for i in range(Columns):
            print(header_index[i])
            self.var_name_label.append(Label(HeadingFrame, text=header_index[i], bg=self.label_color, fg=self.bg_color))
            self.var_name_label[i]['font'] = self.Label_Font
            self.var_name_label[i].place(relx=i/Columns, rely=0.5, relwidth=1/Columns, relheight=.5)



class Var_column():
    def __init__(self, VarFrame, row, column, width, TextVar):
        Y_abstand = 1/6 * (row+1)
        Row_height = 30

        internal_F = Frame(VarFrame, width=width, height=30)
        internal_F.grid(row=row, column=column, pady=0, padx=0)

        self.entry = Entry(internal_F, textvariable=TextVar, state='disabled')
        self.entry.place(x=0, y=0, relwidth=1, relheight=1)

    def enable(self):
        self.entry.configure(state='normal')

    def disable(self):
        self.entry.configure(state='disabled')

    def get_binding(self, bind, function):
        self.entry.bind(bind, function)

    def test_bind(self, e):
        print("you wrote something")


class Var_row():
    def __init__(self, Var_list, second_frame, row, relwidth, index, columns):
        self.columns = columns
        self.rowlist = []
        self.Var_list = Var_list
        for column in range(self.columns):
            self.rowlist.append(Var_column(second_frame, row, column, relwidth, Var_list[index + column][0]))
            if column == 0:
                self.rowlist[column].enable()
                self.textvar_index = index + column
        self.binder()

    def binder(self):
        self.rowlist[0].get_binding('<FocusIn>', self.binder_connector)
        self.rowlist[0].get_binding('<Leave>', self.binder_connector2)

    def binder_connector(self, e):
        print("Row is enabled")
        self.enable()

    def binder_connector2(self, e):
        print("das steht als Var im Textfeld", self.Var_list[self.textvar_index][0].get())
        if self.Var_list[self.textvar_index][0].get() == None:
            self.disable()
            print("no Var enterd")

    def enable(self):
        for i in range(self.columns):
            self.rowlist[i].enable()

    def disable(self):
        for i in range(1,self.columns):
            self.rowlist[i].disable()

zuordnungsfrage_input(varname_1, self.bg_color, self.label_color, self.Label_Font, self.response_frame,
                        self.dbinhaltsliste, self.index_dict, (3 * self.width) / 2, Rows=10,
                        Columns=2, Header="Definition",
                        header_index=['Antworttext', 'Antwort-Grafik.'],column_type_list=[0,1,0],
                        columnwidth=(3, 3))