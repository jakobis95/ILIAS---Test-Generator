from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter import filedialog
#import tkFileDialog
from tkinter.scrolledtext import ScrolledText
from Time_input_UI import Test_Time_UI
from Variablen_Einfügen_UI import variable_scrl_UI
from Picture_interface import picture_choice
from PIL import Image, ImageTk
from ScrolledText_Functionality import Textformatierung

class fragen_gui():

    # test - Tobi

    def __init__(self, table_dict, fragentyp, Frame, DB_interface, ScrText, dbinhaltsliste, index_dict, bg_color='#4cc9f0', entry_color='white', label_color='#3a0ca3', button_color='#3f37c9', fg_color='#4cc9f0', *args, **kwargs):
        bg_color = '#4cc9f0'  # general Background color
        self.efg_color = '#3a0ca3'  # Entry foreground color
        self.entry_color = entry_color  # Entry Background color
        self.label_color = label_color
        self.button_color = button_color
        self.bg_color = bg_color
        self.fg_color = fg_color  # general foregroundcolor
        self.Label_Font = font.Font(family='Verdana', size=10, weight='bold') #Font definition for Labels
        self.Entry_Font = font.Font(family='Verdana', size=10, weight='normal')  # Font definition for Entrys
        self.Button_Font = font.Font(family='Verdana', size=10, weight='normal')  # Font definition for Buttons
        self.table_dict = table_dict
        self.fragentyp = fragentyp
        self.dbinhaltsliste = dbinhaltsliste[table_dict[fragentyp]] #Stringvar und der index name aus der Datenbank

        print("------", self.dbinhaltsliste)

        for i in self.dbinhaltsliste:
            i[0].set('')
        self.index_dict = index_dict[table_dict[fragentyp]] #welcher index gehört zu welchem eintrag on der Datenbank
        self.ScrText = ScrText
        self.Fragen_Window = Frame
        self.Fragen_Window.configure(bg=bg_color)
        #self.add_picture()
        self.db_I = DB_interface
        self.db_I.subscribe(self.Fill_Entrys_From_DB)
        self.titel = StringVar()
        WIDTH = int(Frame.winfo_screenwidth()/10)
        self.width = 9*WIDTH
        HEIGHT = int(Frame.winfo_screenheight() / 1.5)
        self.Fragen_Window.title("DB_List")
        self.Fragen_Window.resizable(True, True)
        self.Fragen_Window.geometry("%dx%d" % (9*WIDTH, HEIGHT))
        self.param_Frame = tk.Frame(self.Fragen_Window, bg=bg_color,bd=5)# alle Einstellungen
        self.param_Frame.place(relx=0, rely=0, relwidth=.25, relheight=1)


        self.QD_frame = tk.Frame(self.Fragen_Window, bg=bg_color, bd=5)#Fragentext mit formatierungsoptionen
        self.QD_frame.place(relx=0.25, rely=0, relwidth=.25, relheight=.4)
        self.picture_Frame_1 = tk.Frame(self.Fragen_Window, bg=bg_color, bd=5)  # Bildverwaltung für Fragentext
        self.picture_Frame_1.place(relx=0.25, rely=.4, relwidth=.25, relheight=.1)
        self.picture_Frame_2 = tk.Frame(self.Fragen_Window, bg=bg_color, bd=5)  # Bildverwaltung für Fragentext
        self.picture_Frame_2.place(relx=0.25, rely=.5, relwidth=.25, relheight=.1)
        self.picture_Frame_3 = tk.Frame(self.Fragen_Window, bg=bg_color, bd=5)  # Bildverwaltung für Fragentext
        self.picture_Frame_3.place(relx=0.25, rely=.6, relwidth=.25, relheight=.1)
        self.Speichern_Frame = tk.Frame(self.Fragen_Window, bg=bg_color, bd=5)
        self.Speichern_Frame.place(relx=0.25, rely=0.9, relwidth=.25, relheight=.1)
        self.UI_Elemente()
        self.dbinhaltsliste[self.index_dict["question_type"]][0].set(self.fragentyp)
        #Subscribe to Fragentext Funktionalotäten
        self.ScrText.subscribe(self.Fragentext_Entry.insert)

        self.Add_Entry_btn = Button(self.Speichern_Frame, text="Frage in DB erstellen", command=self.Add_data_to_DB, bg=self.button_color, fg=self.fg_color)
        self.Add_Entry_btn['font'] = self.Button_Font
        self.Add_Entry_btn.pack(side=tk.RIGHT, padx=6, anchor="e", fill=Y)

        self.Save_btn = Button(self.Speichern_Frame, text="Save Changes", command=self.Save_Change_to_DB, bg=self.button_color, fg=self.fg_color)
        self.Save_btn['font'] = self.Button_Font
        self.Save_btn.pack(side=tk.RIGHT, padx=6, anchor="e", fill=Y)

        self.text_latex = Button(self.QD_frame, text="text latex", command=self.text_latex_call, bg=self.button_color, fg=self.fg_color) #todo change Farme
        self.text_latex.place(relx=0, rely=.9, relwidth=.25, relheight=.1)
        self.text_latex['font'] = self.Button_Font

        self.text_sub = Button(self.QD_frame, text="text sub", command=self.text_sub_call, bg=self.button_color, fg=self.fg_color)#todo change Farme
        self.text_sub['font'] = self.Button_Font
        self.text_sub.place(relx=.25, rely=.9, relwidth=.25, relheight=.1)

        self.text_sup = Button(self.QD_frame, text="text sup", command=self.text_sup_call, bg=self.button_color, fg=self.fg_color)#todo change Farme
        self.text_sup['font'] = self.Button_Font
        self.text_sup.place(relx=.5, rely=.9, relwidth=.25, relheight=.1)

        self.text_italic = Button(self.QD_frame, text="text italic", command=self.text_italic_call, bg=self.button_color, fg=self.fg_color)#todo change Farme
        self.text_italic['font'] = self.Button_Font
        self.text_italic.place(relx=.75, rely=.9, relwidth=.25, relheight=.1)


        #todo var und res anzeige Frame nicht in der Klasse bestimmen
        #self.VarFrame = tk.Frame(self.Fragen_Window, bg=bg_color, bd=5)
        #self.VarFrame.place(relx=.5, rely=0, relwidth=.5, relheight=.5)
        #self.ResFrame = tk.Frame(self.Fragen_Window, bg=bg_color, bd=5)
        #self.ResFrame.place(relx=.5, rely=0.5, relwidth=.5, relheight=.5)
        #self.Variablen_interface = Variablen_UI(self.bg_color, self.label_color, self.Label_Font, self.VarFrame, self.dbinhaltsliste, self.index_dict, 3 * WIDTH, Rows=15, Columns=5, Header="Variablen", header_index=['Name.', 'Min.', 'Max', 'Präz.', 'Teilbar durch'], Type="Var")
        #self.Results_interface = Variablen_UI(self.bg_color, self.label_color, self.Label_Font, self.ResFrame, self.dbinhaltsliste, self.index_dict, 3 * WIDTH, Rows=10, Columns=6, Header="Ergebnisse", header_index=['Name.', 'Min.' , 'Max', 'Tol.', 'Punkte', 'Formel'], Type="Res")
        #self.Results_interface = Result_UI(self.ResFrame, self.q, self.index_dict)
        self.Fragen_Window.protocol("WM_DELETE_WINDOW", self.on_closing)

        #Picture interface
        #print("das soll die Varchar sein:", self.dbinhaltsliste[self.index_dict["description_img_path_1"]])
        self.image_interface_1 = picture_choice(self.dbinhaltsliste[self.index_dict["description_img_path_1"]][0], self.picture_Frame_1, self.bg_color,
                                          self.label_color, self.button_color, self.fg_color)
        self.image_interface_1.change_font(self.Label_Font, self.Entry_Font)

        self.image_interface_2 = picture_choice(self.dbinhaltsliste[self.index_dict["description_img_path_2"]][0], self.picture_Frame_2,  self.bg_color,
                                          self.label_color, self.button_color, self.fg_color)
        self.image_interface_2.change_font(self.Label_Font, self.Entry_Font)

        self.image_interface_3 = picture_choice(self.dbinhaltsliste[self.index_dict["description_img_path_3"]][0], self.picture_Frame_3,  self.bg_color,
                                          self.label_color, self.button_color, self.fg_color)
        self.image_interface_2.change_font(self.Label_Font, self.Entry_Font)



    def __del__(self):
        print("deleted")

    def on_closing(self):
        self.db_I.unsubscribe(self.Fill_Entrys_From_DB)

        self.Fragen_Window.destroy()

    def UI_Elemente(self):
        self.Title_label = Label(self.param_Frame, text=self.dbinhaltsliste[self.index_dict['question_title']][1],bg=self.label_color, fg=self.fg_color)
        self.Title_label.pack(anchor=N, fill=X, pady=(3, 0))
        self.Title_label['font'] = self.Label_Font
        self.Title_Entry = Entry(self.param_Frame, textvariable=self.dbinhaltsliste[self.index_dict['question_title']][0], bg=self.entry_color, fg=self.efg_color)
        self.Title_Entry['font'] = self.Entry_Font
        self.Title_Entry.pack(anchor=N, fill=X)

        self.Describtion_label = Label(self.param_Frame,text=self.dbinhaltsliste[self.index_dict['question_description_title']][1],bg=self.label_color, fg=self.fg_color)
        self.Describtion_label['font'] = self.Label_Font
        self.Describtion_label.pack(anchor=N, fill=X, pady=(3, 0))
        self.Describtion_Entry = Entry(self.param_Frame, textvariable=self.dbinhaltsliste[self.index_dict['question_description_title']][0], bg=self.entry_color, fg=self.efg_color)
        self.Describtion_Entry['font'] = self.Entry_Font
        self.Describtion_Entry.pack(anchor=N, fill=X)

        self.Author_label = Label(self.param_Frame, text=self.dbinhaltsliste[self.index_dict['question_author']][1], bg=self.label_color, fg=self.fg_color)
        self.Author_label['font'] = self.Label_Font
        self.Author_label.pack(anchor=N, fill=X, pady=(3, 0))
        self.Author_Entry = Entry(self.param_Frame,textvariable=self.dbinhaltsliste[self.index_dict['question_author']][0], bg=self.entry_color, fg=self.efg_color)
        self.Author_Entry['font'] = self.Entry_Font
        self.Author_Entry.pack(anchor=N, fill=X)

        self.Schwierigkeit_label = Label(self.param_Frame, text=self.dbinhaltsliste[self.index_dict['question_difficulty']][1], bg=self.label_color, fg=self.fg_color)
        self.Schwierigkeit_label['font'] = self.Label_Font
        self.Schwierigkeit_label.pack(anchor=N, fill=X, pady=(3, 0))
        self.Schwierigkeit_Entry = Entry(self.param_Frame, textvariable=self.dbinhaltsliste[self.index_dict['question_difficulty']][0], bg=self.entry_color, fg=self.efg_color, bd=1)
        self.Schwierigkeit_Entry['font'] = self.Entry_Font
        self.Schwierigkeit_Entry.pack(anchor=N, fill=X)



        self.Category_label = Label(self.param_Frame, text=self.dbinhaltsliste[self.index_dict['question_category']][1], bg=self.label_color, fg=self.fg_color)
        self.Category_label['font'] = self.Label_Font
        self.Category_label.pack(anchor=N, fill=X, pady=(3, 0))
        self.Category_Entry = Entry(self.param_Frame, textvariable=self.dbinhaltsliste[self.index_dict['question_category']][0], bg=self.entry_color, fg=self.efg_color)
        self.Category_Entry['font'] = self.Entry_Font
        self.Category_Entry.pack(anchor=N, fill=X)

        self.Typ_label = Label(self.param_Frame, text=self.dbinhaltsliste[self.index_dict['question_type']][1], bg=self.label_color, fg=self.fg_color)
        self.Typ_label['font'] = self.Label_Font
        self.Typ_label.pack(anchor=N, fill=X, pady=(3, 0))
        self.Typ_Entry = Entry(self.param_Frame, textvariable=self.dbinhaltsliste[self.index_dict['question_type']][0], bg=self.entry_color, fg=self.efg_color)
        self.Typ_Entry['font'] = self.Entry_Font
        self.Typ_Entry.pack(anchor=N, fill=X)
        self.Typ_Entry.configure(state=DISABLED)


        self.PoolTag_label = Label(self.param_Frame, text=self.dbinhaltsliste[self.index_dict['question_pool_tag']][1], bg=self.label_color, fg=self.fg_color)
        self.PoolTag_label['font'] = self.Label_Font
        self.PoolTag_label.pack(anchor=N, fill=X, pady=(3, 0))
        self.PoolTag_Entry = Entry(self.param_Frame, textvariable=self.dbinhaltsliste[self.index_dict['question_pool_tag']][0], bg=self.entry_color, fg=self.efg_color)
        self.PoolTag_Entry['font'] = self.Entry_Font
        self.PoolTag_Entry.pack(anchor=N, fill=X)

        self.Fragentext_label = Label(self.QD_frame, text=self.dbinhaltsliste[self.index_dict['question_description_main']][1], bg=self.label_color, fg=self.fg_color)
        self.Fragentext_label['font'] = self.Label_Font
        self.Fragentext_label.place(rely=0, relx=0, relwidth=1, relheight=.1)
        self.Fragentext_Entry = ScrolledText(self.QD_frame, height=6, width=65, bg=self.entry_color, fg=self.efg_color)
        self.Fragentext_Entry['font'] = self.Entry_Font
        self.Fragentext_Entry.place(rely=.1, relx=0, relwidth=1, relheight=.8)

        self.Test_Time = Test_Time_UI(self.param_Frame, self.bg_color, self.label_color, self.Label_Font)



    def Add_data_to_DB(self):
        self.dbinhaltsliste[self.index_dict['question_description_main']][0].set(self.Fragentext_Entry.get("1.0", 'end-1c'))
        self.db_I.Add_data_to_DB(self.dbinhaltsliste, self.dbinhaltsliste[3][0].get())
        print("----1 ---",self.dbinhaltsliste)
        print("----2 ---",self.dbinhaltsliste[3][0].get())



    def Save_Change_to_DB(self):

        self.dbinhaltsliste[self.index_dict['question_description_main']][0].set(self.Fragentext_Entry.get("1.0", 'end-1c'))
        self.db_I.Save_Change_to_DB(self.dbinhaltsliste)


    def Fill_Entrys_From_DB(self, db_data):
        j = 0

        for i in db_data[1][self.table_dict[self.fragentyp]]:#todo diese exception ist so nicht ok aber funktioniert erstmal um den Textbox Ihren Textzuzuweisen.
            if j == self.index_dict['question_description_main']:
                self.Fragentext_Entry.delete('1.0', 'end-1c')
                self.Fragentext_Entry.insert('1.0', i)
            else:
                self.dbinhaltsliste[j][0].set(i)
            j = j + 1
        self.image_interface_1.add_picture()
        self.image_interface_2.add_picture()
        self.image_interface_3.add_picture()
        self.dbinhaltsliste[self.index_dict["question_type"]][0].set(self.fragentyp)


    def text_latex_call(self):
        self.ScrText.text_latex(self.Fragentext_Entry)

    def text_sup_call(self):
        self.ScrText.text_sup(self.Fragentext_Entry)

    def text_italic_call(self):
        self.ScrText.text_italic(self.Fragentext_Entry)

    def text_sub_call(self):
        self.ScrText.text_sub(self.Fragentext_Entry)

class formelfrage(fragen_gui):
    def __init__(self, table_dict, Frame, DB_interface, ScrText, dbinhaltsliste, index_dict, bg_color, label_color, button_color, *args, **kwargs):
        entry_color = 'white'
        self.fragentyp = "formelfrage"
        fg_color = bg_color
        fragen_gui.__init__(self, table_dict, self.fragentyp, Frame, DB_interface, ScrText, dbinhaltsliste, index_dict, bg_color, entry_color, label_color, button_color, fg_color, *args, **kwargs)
        self.dbinhaltsliste[self.index_dict["question_type"]][0].set(self.fragentyp)
        Frame.configure(bg=bg_color)
        varname_list_variable = ["var{}_name",
                               "var{}_min",
                               "var{}_max",
                               "var{}_prec",
                               "var{}_divby",
                               "var{}_unit"]

        varname_list_result = ["res{}_name",
                            "res{}_min",
                            "res{}_max",
                            "res{}_prec",
                            "res{}_points",
                            "res{}_unit"]
        rel_width = .5
        self.VarFrame = tk.Frame(self.Fragen_Window, bg=bg_color, bd=5)
        self.VarFrame.place(relx=.5, rely=0, relwidth=rel_width, relheight=.5)
        self.width_scrl_UI = self.width * rel_width
        self.Variablen_interface = variable_scrl_UI(varname_list_variable, self.bg_color, self.label_color,
                                                    self.Label_Font, self.VarFrame, self.dbinhaltsliste,
                                                    self.index_dict, self.width_scrl_UI, Rows=15, Columns=5,
                                                    Header="Variablen",
                                                    header_index=['Name.', 'Min.', 'Max', 'Präz.', 'Teilbar durch'],
                                                    column_type_list=[0, 0, 0, 0, 0], columnwidth=(1, 1, 1, 1, 1))

        rel_width = .5
        self.ResFrame = tk.Frame(self.Fragen_Window, bg=bg_color, bd=5)
        self.ResFrame.place(relx=.5, rely=0.5, relwidth=rel_width, relheight=.5)
        self.width_scrl_UI = self.width * rel_width
        self.Results_interface = variable_scrl_UI(varname_list_result, self.bg_color, self.label_color, self.Label_Font, self.ResFrame, self.dbinhaltsliste, self.index_dict, self.width_scrl_UI, Rows=10, Columns=6, Header="Ergebnisse", header_index=['Name.', 'Min.', 'Max', 'Tol.', 'Punkte', 'Formel'], column_type_list=[0, 0, 0, 0, 0, 0], columnwidth=(1, 1, 1, 1, 1, 1))


class singlechoice(fragen_gui):
    def __init__(self, table_dict, Frame, DB_interface, ScrText, dbinhaltsliste, index_dict, bg_color, label_color, button_color, *args, **kwargs):
        entry_color = 'white'
        varname_list = ["response_{}_text",  "response_{}_img_path", "response_{}_pts"]
        self.fragentyp = "singlechoice"
        fg_color = bg_color
        fragen_gui.__init__(self, table_dict, self.fragentyp, Frame, DB_interface, ScrText, dbinhaltsliste, index_dict, bg_color, entry_color, label_color, button_color, fg_color, *args, **kwargs)
        self.response_frame = tk.Frame(self.Fragen_Window, bg=fg_color, bd=5)
        rel_width = .5
        self.response_frame.place(relx=.5, rely=0, relwidth=rel_width, relheight=1)
        self.width_scrl_UI = self.width * rel_width
        self.respose_input = variable_scrl_UI(varname_list, self.bg_color, self.label_color, self.Label_Font, self.response_frame, self.dbinhaltsliste, self.index_dict, self.width_scrl_UI, Rows=10, Columns=3, Header="Choices", header_index=['Antworttext', 'Antwort-Grafik.', 'Punkte'], column_type_list=[0, 1, 0], columnwidth=(2, 3, 1))


class multiplechoice(fragen_gui):
    def __init__(self, table_dict, Frame, DB_interface, ScrText, dbinhaltsliste, index_dict, bg_color, label_color,
                 button_color, *args, **kwargs):
        entry_color = 'white'
        varname_list = "response_{}_text","response_{}_img_path", "response_{}_pts_correct_answer","response_{}_pts_false_answer"
        fg_color = bg_color
        self.fragentyp = "multiplechoice"
        fragen_gui.__init__(self, table_dict, self.fragentyp, Frame, DB_interface, ScrText, dbinhaltsliste, index_dict,
                            bg_color, entry_color, label_color, button_color, fg_color, *args, **kwargs)
        self.response_frame = tk.Frame(self.Fragen_Window, bg=bg_color, bd=5)
        rel_width = .5
        self.response_frame.place(relx=.5, rely=0, relwidth=.5, relheight=1)
        self.width_scrl_UI = self.width * rel_width
        self.respose_input = variable_scrl_UI(varname_list, self.bg_color, self.label_color, self.Label_Font, self.response_frame,
                                              self.dbinhaltsliste, self.index_dict, self.width_scrl_UI, Rows=10,
                                              Columns=4, Header="Choices",
                                              header_index=['Antworttext', 'Antwort-Grafik.', 'Punkte','Punkteabzug'], column_type_list=[0,1,0,0], columnwidth=(2, 3, 1, 1))


class zuordnungsfrage(fragen_gui):
    def __init__(self, table_dict, Frame, DB_interface, ScrText, dbinhaltsliste, index_dict, bg_color, label_color, button_color, *args, **kwargs):
        entry_color = 'white'
        fg_color = bg_color
        self.fragentyp = "zuordnungsfrage"
        fg_color = bg_color
        varname_1 = ["definitions_response_{}_text", "definitions_response_{}_img_path"]
        varname_2 = ["terms_response_{}_text", "terms_response_{}_img_path"]
        varname_3 = ["assignment_pairs_definition_{}", "assignment_pairs_term_{}",
                            "assignment_pairs_{}_pts"]
        fragen_gui.__init__(self, table_dict, self.fragentyp, Frame, DB_interface, ScrText, dbinhaltsliste, index_dict, bg_color, entry_color, label_color, button_color, fg_color, *args, **kwargs)
        self.response_frame = tk.Frame(self.Fragen_Window, bg=bg_color, bd=5)
        rel_width = .5
        self.response_frame.place(relx=.5, rely=0, relwidth=rel_width, relheight=.3)
        self.width_scrl_UI = self.width * rel_width
        self.respose_input = variable_scrl_UI(varname_1, self.bg_color, self.label_color, self.Label_Font,
                                              self.response_frame,
                                              self.dbinhaltsliste, self.index_dict, self.width_scrl_UI, Rows=10,
                                              Columns=2, Header="Definition",
                                              header_index=['Antworttext', 'Antwort-Grafik.'], column_type_list=[0, 1],
                                              columnwidth=(3, 3))
        rel_width = .5
        self.response_frame_2 = tk.Frame(self.Fragen_Window, bg=bg_color, bd=5)
        self.width_scrl_UI = self.width * rel_width
        self.response_frame_2.place(relx=.5, rely=0.3, relwidth=rel_width, relheight=.3)
        self.respose_input_2 = variable_scrl_UI(varname_2, self.bg_color, self.label_color, self.Label_Font,
                                                self.response_frame_2,
                                                self.dbinhaltsliste, self.index_dict, self.width_scrl_UI, Rows=10,
                                                Columns=2, Header="Term",
                                                header_index=['Antworttext', 'Antwort-Grafik.'],
                                                column_type_list=[0, 1],
                                                columnwidth=(3, 3))

        rel_width = .5
        self.response_frame_3 = tk.Frame(self.Fragen_Window, bg=bg_color, bd=5)
        self.response_frame_3.place(relx=.5, rely=0.6, relwidth=rel_width, relheight=.4)
        self.width_scrl_UI = self.width * rel_width
        self.zuordnungspaare_1 = variable_scrl_UI(varname_3, self.bg_color, self.label_color, self.Label_Font,
                                                  self.response_frame_3,
                                                  self.dbinhaltsliste, self.index_dict, self.width_scrl_UI, Rows=10,
                                                  Columns=3, Header="Zuordnungspaare",
                                                  header_index=['Definition', 'Term', 'Punkte'], column_type_list=[2,2,0],
                                                  columnwidth=(4, 4, 1))

if __name__ == "__main__":
    root = tk.Tk()
    WIDTH = int(root.winfo_screenwidth() / 1.5)
    HEIGHT = int(root.winfo_screenheight() / 2)
    root.title("DB_List")
    root.resizable(False, False)
    root.geometry("%dx%d" % (WIDTH, HEIGHT))
    gesucht = 'Spannungsteiler 2'
    dbname = '../testdb.db'
    #lbl = tk.Label(text="Das ist das Main Window")
    #Fragen_Frame = Fragen_GUI(root, gesucht, dbname)
    #root.mainloop()