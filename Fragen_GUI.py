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
import numpy as np
import pandas as pd
from pandas.core.reshape.util import cartesian_product

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

        self.Add_Entry_btn = Button(self.Speichern_Frame, text="Neue Frage erstellen", command=self.Add_data_to_DB, bg=self.button_color, fg=self.fg_color)
        self.Add_Entry_btn['font'] = self.Button_Font
        self.Add_Entry_btn.pack(side=tk.RIGHT, padx=6, anchor="e", fill=Y)

        self.Save_btn = Button(self.Speichern_Frame, text="Änderungen Speichern", command=self.Save_Change_to_DB, bg=self.button_color, fg=self.fg_color)
        self.Save_btn['font'] = self.Button_Font
        self.Save_btn.pack(side=tk.RIGHT, padx=6, anchor="e", fill=Y)

        self.calc_val_range_btn = Button(self.Speichern_Frame, text=" Wertebereich\nberechnen", command=self.calculate_value_range_function, bg=self.button_color, fg=self.fg_color)
        self.calc_val_range_btn['font'] = self.Button_Font
        self.calc_val_range_btn.pack(side=tk.RIGHT, padx=6, anchor="e", fill=Y)

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

        self.Extra_Einstellungen_Frame = Frame(self.param_Frame, bg=self.bg_color)
        self.Extra_Einstellungen_Frame.pack(anchor=N, fill=X, pady=(3, 0))

    def Add_data_to_DB(self):
        self.dbinhaltsliste[self.index_dict['question_description_main']][0].set(self.Fragentext_Entry.get("1.0", 'end-1c'))
        self.db_I.Add_data_to_DB(self.dbinhaltsliste, self.dbinhaltsliste[3][0].get())



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


    def calculate_value_range_function(self):
        # Wertebereich berechnen

        self.number_of_variables = 15
        self.number_of_results = 10
        self.var_res_combined_min_entries_list = []
        self.var_res_combined_max_entries_list = []
        self.var_prec_entry_list = []
        self.res_min_entry_list = []
        self.res_max_entry_list = []

        ############# VARIABLEN UND ERGEBNISSE _MIN SAMMLUNG
        for i in range(self.number_of_variables):
            self.var_res_combined_min_entries_list.append(self.dbinhaltsliste[self.index_dict["var" + str(i+1) + "_min"]][0])
        for j in range(self.number_of_results):
            self.var_res_combined_min_entries_list.append(self.dbinhaltsliste[self.index_dict["res" + str(j+1) + "_min"]][0])

        ############# VARIABLEN UND ERGEBNISSE _MAX SAMMLUNG
        for m in range(self.number_of_variables):
            self.var_res_combined_max_entries_list.append(self.dbinhaltsliste[self.index_dict["var" + str(m+1) + "_max"]][0])
        for n in range(self.number_of_results):
            self.var_res_combined_max_entries_list.append(self.dbinhaltsliste[self.index_dict["res" + str(n+1) + "_max"]][0])

        ############# VARIABLEN _PREC SAMMLUNG
        for u in range(self.number_of_variables):
            self.var_prec_entry_list.append(self.dbinhaltsliste[self.index_dict["var" + str(u+1) + "_prec"]][0])

        ############# ERGEBNISSE _MIN SAMMLUNG
        for v in range(self.number_of_results):
            self.res_min_entry_list.append(self.dbinhaltsliste[self.index_dict["res" + str(v+1) + "_min"]][0])

        ############# ERGEBNISSE _MAX SAMMLUNG
        for w in range(self.number_of_results):
            self.res_max_entry_list.append(self.dbinhaltsliste[self.index_dict["var" + str(w+1) + "_max"]][0])



        for i in range(self.number_of_results):
            if self.dbinhaltsliste[self.index_dict["res" + str(i+1) + "_formula"]][0].get() != "":
                fragen_gui.calculate_value_range_from_formula_in_GUI(self, self.dbinhaltsliste[self.index_dict["res" + str(i+1) + "_formula"]][0], self.var_res_combined_min_entries_list, self.var_res_combined_max_entries_list, self.var_prec_entry_list, self.dbinhaltsliste[self.index_dict["res" + str(i+1) + "_min"]][0], self.dbinhaltsliste[self.index_dict["res" + str(i+1) + "_max"]][0], self.dbinhaltsliste[self.index_dict["res" + str(i+1) + "_prec"]][0], self.res_min_entry_list, self.res_max_entry_list)


    def calculate_value_range_replace_formula_numpy(self, formula, var_res_combined_min_entries_list, var_res_combined_max_entries_list, res_min_entries_list, res_max_entries_list):

        self.formula = formula.get()
        self.formula_var_replaced = formula.get().replace('$', '_')
        self.formula_var_replaced = self.formula_var_replaced.replace('^', '**')


        self.np_variables_translator_dict = {"pi": "np.pi",
                                   ",": ".",
                                   "^": "**",
                                   "e": "*10**",

                                   "sin": "np.sin",
                                   "cos": "np.cos",
                                   "tan": "np.tan",
                                   "arcsin": "np.arcsin",
                                   "arccos": "np.arccos",
                                   "arctan": "np.arctan",

                                   "sinh": "np.sinh",
                                   "cosh": "np.cosh",
                                   "tanh": "np.tanh",
                                   "arcsinh": "np.arcsinh",
                                   "arccosh": "np.arccosh",
                                   "arctanh": "np.arctanh",

                                   "sqrt": "np.sqrt",
                                   "abs": "np.abs",
                                   "ln": "np.ln",
                                   "log": "np.log",

                                   "_v1": " row['a'] ",
                                   "_v2": " row['b'] ",
                                   "_v3": " row['c'] ",
                                   "_v4": " row['d'] ",
                                   "_v5": " row['e'] ",
                                   "_v6": " row['f'] ",
                                   "_v7": " row['g'] ",
                                   "_v8": " row['h'] ",
                                   "_v9": " row['i'] ",
                                   "_v10": " row['j'] ",
                                   "_v11": " row['k'] ",
                                   "_v12": " row['l'] ",
                                   "_v13": " row['m'] ",
                                   "_v14": " row['n'] ",
                                   "_v15": " row['o'] "}

        self.np_results_translator_dict = {

                                   "_r1": " row['p'] ",
                                   "_r2": " row['q'] ",
                                   "_r3": " row['r'] ",
                                   "_r4": " row['s'] ",
                                   "_r5": " row['t'] ",
                                   "_r6": " row['u'] ",
                                   "_r7": " row['v'] ",
                                   "_r8": " row['w'] ",
                                   "_r9": " row['x'] ",
                                   "_r10": " row['y'] "}

        print("----------------------")
        #print("Übernehme Formel aus Eingabefeld:")
        print("---> ", self.formula, end="", flush=True)
        #print("Prüfe auf Grenzen")


        def replace_var(match):
            return self.np_variables_translator_dict[match.group(0)]

        def replace_res(match):
            return self.np_results_translator_dict[match.group(0)]



        self.formula_var_replaced = re.sub('|'.join(r'\b%s\b' % re.escape(s) for s in self.np_variables_translator_dict),replace_var, self.formula_var_replaced)


        #for key in self.np_variables_translator_dict.keys():
        #    self.formula_var_replaced = self.formula_var_replaced.replace(key, self.np_variables_translator_dict[key])

        self.formula_res_replaced = re.sub('|'.join(r'\b%s\b' % re.escape(s) for s in self.np_results_translator_dict),replace_res, self.formula_var_replaced)


        print(" --- ", "NUMPY: ", self.formula_res_replaced)

        #for key in self.np_results_translator_dict.keys():
        #    self.formula_res_replaced = self.formula_res_replaced.replace(key, self.np_results_translator_dict[key])



        for i in range(len(var_res_combined_min_entries_list)):
            if "$v" + (str(i+1)) in formula.get() and var_res_combined_min_entries_list[i].get() != "" and var_res_combined_max_entries_list[i].get() != "":
                self.formula = self.formula_var_replaced


                for j in range(len(res_min_entries_list)):
                    if "$r" + (str(j+1)) in formula.get():
                        if res_min_entries_list[j].get() != "" and res_max_entries_list[j].get() != "":

                            #print("Grenzen verfügbar! --> Ersetze alle Symbole mit numpy-symoblik")

                            self.formula = self.formula_res_replaced

                        else:
                            self.formula = "NaN"


            if "$r" + (str(i+1)) in formula.get() and var_res_combined_min_entries_list[i].get() != "" and var_res_combined_max_entries_list[i].get() != "":
                self.formula = self.formula_res_replaced


        return self.formula


    def calculate_value_range_from_formula_in_GUI(self, formula, var_res_combined_min_entries_list, var_res_combined_max_entries_list, var_prec_entries_list,  res_min_entry, res_max_entry, res_prec_entry, res_min_entries_list, res_max_entries_list):


        def value_range_lower_upper_bounds(var_res_combined_min_entries_list, var_res_combined_max_entries_list, var_lower_bound_list, var_upper_bound_list):

                for u in range(len(var_res_combined_min_entries_list)):
                    if var_res_combined_min_entries_list[u] != "":
                        if bool(re.search(r'\d', var_res_combined_min_entries_list[u].get())) == True and bool(re.search(r'\d', var_res_combined_max_entries_list[u].get())) == True:
                            try:
                                var_lower_bound_list[u], var_upper_bound_list[u] = int(var_res_combined_min_entries_list[u].get()), int(var_res_combined_max_entries_list[u].get())
                            except ValueError:
                                var_lower_bound_list[u], var_upper_bound_list[u] = float(var_res_combined_min_entries_list[u].get()), float(var_res_combined_max_entries_list[u].get())
                        else:
                            var_lower_bound_list[u], var_upper_bound_list[u] = 0, 0

        def min_max(col):
            return pd.Series(index=['min', 'max'], data=[col.min(), col.max()])


        # Alle Formeln berechnen die KEIN $r enthalten (nur variablen)


        self.var1_lower, self.var1_upper = 0, 0
        self.var2_lower, self.var2_upper = 0, 0
        self.var3_lower, self.var3_upper = 0, 0
        self.var4_lower, self.var4_upper = 0, 0
        self.var5_lower, self.var5_upper = 0, 0
        self.var6_lower, self.var6_upper = 0, 0
        self.var7_lower, self.var7_upper = 0, 0
        self.var8_lower, self.var8_upper = 0, 0
        self.var9_lower, self.var9_upper = 0, 0
        self.var10_lower, self.var10_upper = 0, 0
        self.var11_lower, self.var11_upper = 0, 0
        self.var12_lower, self.var12_upper = 0, 0
        self.var13_lower, self.var13_upper = 0, 0
        self.var14_lower, self.var14_upper = 0, 0
        self.var15_lower, self.var15_upper = 0, 0

        self.res1_lower, self.res1_upper = 0, 0
        self.res2_lower, self.res2_upper = 0, 0
        self.res3_lower, self.res3_upper = 0, 0
        self.res4_lower, self.res4_upper = 0, 0
        self.res5_lower, self.res5_upper = 0, 0
        self.res6_lower, self.res6_upper = 0, 0
        self.res7_lower, self.res7_upper = 0, 0
        self.res8_lower, self.res8_upper = 0, 0
        self.res9_lower, self.res9_upper = 0, 0
        self.res10_lower, self.res10_upper = 0, 0



        self.new_list = []
        self.new_list2 = []
        self.set_nr_of_var_index = []

        self.var_prec_entry_list_values = []

        self.lower_list = [self.var1_lower, self.var2_lower, self.var3_lower, self.var4_lower, self.var5_lower,
                           self.var6_lower, self.var7_lower, self.var8_lower, self.var9_lower, self.var10_lower,
                           self.var11_lower, self.var12_lower, self.var13_lower, self.var14_lower, self.var15_lower,
                           self.res1_lower, self.res2_lower, self.res3_lower, self.res4_lower, self.res5_lower,
                           self.res6_lower, self.res7_lower, self.res8_lower, self.res9_lower, self.res10_lower]

        self.upper_list = [self.var1_upper, self.var2_upper, self.var3_upper, self.var4_upper, self.var5_upper,
                           self.var6_upper, self.var7_upper, self.var8_upper, self.var9_upper, self.var10_upper,
                           self.var11_upper, self.var12_upper, self.var13_upper, self.var14_upper, self.var15_upper,
                           self.res1_upper, self.res2_upper, self.res3_upper, self.res4_upper, self.res5_upper,
                           self.res6_upper, self.res7_upper, self.res8_upper, self.res9_upper, self.res10_upper]

        ############# ERGEBNISSE _MAX SAMMLUNG
        self.res_formula_entry_list = []
        for i in range(self.number_of_results):
            self.res_formula_entry_list.append(self.dbinhaltsliste[self.index_dict["res" + str(i+1) + "_formula"]][0])

        self.new_dict = {"row['a']": 'a',
                         "row['b']": 'b',
                         "row['c']": 'c',
                         "row['d']": 'd',
                         "row['e']": 'e',
                         "row['f']": 'f',
                         "row['g']": 'g',
                         "row['h']": 'h',
                         "row['i']": 'i',
                         "row['j']": 'j',
                         "row['k']": 'k',
                         "row['l']": 'l',
                         "row['m']": 'm',
                         "row['n']": 'n',
                         "row['o']": 'o',
                         "row['p']": 'p',
                         "row['q']": 'q',
                         "row['r']": 'r',
                         "row['s']": 's',
                         "row['t']": 't',
                         "row['u']": 'u',
                         "row['v']": 'v',
                         "row['w']": 'w',
                         "row['x']": 'x',
                         "row['y']": 'y' }

        self.list_index_dict = {'a': 0,
                                'b': 1,
                                'c': 2,
                                'd': 3,
                                'e': 4,
                                'f': 5,
                                'g': 6,
                                'h': 7,
                                'i': 8,
                                'j': 9,
                                'k': 10,
                                'l': 11,
                                'm': 12,
                                'n': 13,
                                'o': 14,
                                'p': 15,
                                'q': 16,
                                'r': 17,
                                's': 18,
                                't': 19,
                                'u': 20,
                                'v': 21,
                                'w': 22,
                                'x': 23,
                                'y': 24,
                                }

        values = []

        # Number of values per range
        N = 5

        # ersetzt formel durch numpy expressions: z.B. 2^5 -> 2**5, $v1*2+$v3 -> row[a] *2+ row[c]
        self.formula_1_numpy_expression = fragen_gui.calculate_value_range_replace_formula_numpy(self, formula, var_res_combined_min_entries_list, var_res_combined_max_entries_list, res_min_entries_list, res_max_entries_list)


        if self.formula_1_numpy_expression != None and self.formula_1_numpy_expression != "NaN":

            # neue formel wird nach leerzeichen gesplittet um einzelne 'row[a]' durch 'a' zu ersetzen
            self.new_list = self.formula_1_numpy_expression.split(' ')




            self.exp_as_func = eval('lambda row: ' + self.formula_1_numpy_expression)

            # self.exp_as_func is not iterable, therefore it is assigned to function[]
            functions = [self.exp_as_func]

            value_range_lower_upper_bounds(var_res_combined_min_entries_list, var_res_combined_max_entries_list, self.lower_list, self.upper_list)



            # ersetzen: 'row[a]' -> 'a' als neue Liste
            for i in range(len(self.new_list)):
                if "row" in self.new_list[i]:
                    if self.new_dict[self.new_list[i]] not in self.new_list2:
                        self.new_list2.append(self.new_dict[self.new_list[i]])

            self.set_nr_of_var_index = sorted(self.new_list2)

            self.max_index_nr = self.list_index_dict[self.set_nr_of_var_index[-1]] + 1


            # Berechnung der Formel. "linspace" erstellt "N" Werte zwischen zwei Grenzen -> linspace(0,10,N) N=11 --> 0,1,2,3,4,5,6,7,8,9,10
            for p in range(len(self.set_nr_of_var_index)):
                values.append(np.linspace(self.lower_list[self.list_index_dict[self.set_nr_of_var_index[p]]], self.upper_list[self.list_index_dict[self.set_nr_of_var_index[p]]], N))


            df = pd.DataFrame(cartesian_product(values), index=self.set_nr_of_var_index).T



            if res_prec_entry.get() != "":
                self.var_prec_highest_value = res_prec_entry.get()
            else:
                for i in range(len(var_prec_entries_list)):
                    self.var_prec_entry_list_values.append(var_prec_entries_list[i].get())

                self.var_prec_highest_value = max(self.var_prec_entry_list_values)





            #pd.options.display.float_format = '{:,.3f}'.format


            for i, f in enumerate(functions):
                df[f'f_{i + 1}'] = df.apply(f, axis=1)


            df1 = df.apply(pd.to_numeric, errors='coerce')

            #print(df1)
            #print()
            print(" --- ", "min: ", df1.apply(min_max).iloc[0]['f_1'], " max: ",df1.apply(min_max).iloc[1]['f_1'])
            #print(df1.apply(min_max).iloc[0]['f_1'])
            #print(df1.apply(min_max).iloc[1]['f_1'])
            #print("////////////////////////")


            self.res_min_calc_value = df1.apply(min_max).iloc[0]['f_1']
            self.res_max_calc_value = df1.apply(min_max).iloc[1]['f_1']




            #"{:.2f}".format(a_float)
            #res_min_entry.delete(0, END)
            res_min_entry.set(str("{:.2f}".format(self.res_min_calc_value)))
            #res_max_entry.delete(0, END)
            res_max_entry.set(str(self.res_max_calc_value))





            # Prüfen ob $r.. in Formeln enthalten
            for i in range(len(self.res_formula_entry_list)):
                for j in range(1,10):
                    if "$r" + str(j) in str(self.res_formula_entry_list[i].get()):
                        print("$r" + str(j) + " found!", self.res_formula_entry_list[i].get())

                        if self.res_min_entry_list[j-1].get() != "" and self.res_max_entry_list[j-1].get() != "":
                            print("---", self.res_min_entry_list[j-1].get(), self.res_max_entry_list[j-1].get())



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
                            "res{}_tol",
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
        self.Results_interface = variable_scrl_UI(varname_list_result, self.bg_color, self.label_color, self.Label_Font, self.ResFrame, self.dbinhaltsliste, self.index_dict, self.width_scrl_UI, Rows=10, Columns=7, Header="Ergebnisse", header_index=['Name.', 'Min.', 'Max', 'Präz.', 'Tol.', 'Punkte', 'Formel'], column_type_list=[0, 0, 0, 0, 0, 0, 0], columnwidth=(1, 1, 1, 1, 1, 1, 1))


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
        self.response_input = variable_scrl_UI(varname_list, self.bg_color, self.label_color, self.Label_Font, self.response_frame, self.dbinhaltsliste, self.index_dict, self.width_scrl_UI, Rows=10, Columns=3, Header="Choices", header_index=['Antworttext', 'Antwort-Grafik.', 'Punkte'], column_type_list=[0, 1, 0], columnwidth=(2, 3, 1))

        self.checkbox_frame = tk.Frame(self.response_frame, bg=fg_color, bd=5)
        self.checkbox_frame.place(relx=0, rely=.9, relwidth=.9, relheight=.1)

        self.shuffle_answers_check = Checkbutton(self.checkbox_frame, text="Fragen mischen",
                                                 variable=self.dbinhaltsliste[self.index_dict["shuffle_answers"]][0],
                                                 onvalue=1, offvalue=0, bg=self.label_color, fg=self.bg_color)
        self.shuffle_answers_check['font'] = self.Label_Font
        self.shuffle_answers_check.place(relx=0, rely=0, relwidth=.3, relheight=1)

        self.picture_preview_pixel_label = Label(self.checkbox_frame, text="Bildpreviewbreite in Pixel: ", anchor='w',
                                                 bg=self.label_color, fg=self.bg_color)
        self.picture_preview_pixel_label['font'] = self.Label_Font
        self.picture_preview_pixel_label.place(relx=0.6, rely=0, relwidth=.4, relheight=.5)

        self.picture_preview_pixel = Entry(self.checkbox_frame, text="Bild-Previewbreite in Pxl",
                                           textvariable=self.dbinhaltsliste[self.index_dict["picture_preview_pixel"]][
                                               0], fg=self.bg_color)
        self.picture_preview_pixel['font'] = self.Entry_Font
        self.picture_preview_pixel.place(relx=0.6, rely=0.5, relwidth=.4, relheight=.5)

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
        self.response_input.update_pictures()
        self.dbinhaltsliste[self.index_dict["question_type"]][0].set(self.fragentyp)

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
        self.response_input = variable_scrl_UI(varname_list, self.bg_color, self.label_color, self.Label_Font, self.response_frame,
                                              self.dbinhaltsliste, self.index_dict, self.width_scrl_UI, Rows=10,
                                              Columns=4, Header="Antwortmöglichkeiten",
                                              header_index=['Antworttext', 'Antwort-Grafik.', 'Punkte','Punkteabzug'], column_type_list=[0,1,0,0], columnwidth=(2, 3, 1, 1))

        self.checkbox_frame = tk.Frame(self.response_frame, bg=fg_color, bd=5)
        self.checkbox_frame.place(relx=0, rely=.9, relwidth=.9, relheight=.1)

        self.shuffle_answers_check = Checkbutton(self.checkbox_frame, text="Fragen mischen",
                                                 variable=self.dbinhaltsliste[self.index_dict["shuffle_answers"]][0],
                                                 onvalue=1, offvalue=0,bg=self.label_color, fg=self.bg_color)
        self.shuffle_answers_check['font'] = self.Label_Font
        self.shuffle_answers_check.place(relx=0, rely=0, relwidth=.3, relheight=1)

        self.multiple_row_answ_check = Checkbutton(self.checkbox_frame, text="Mehrzeilige Antworten",
                                                 variable=self.dbinhaltsliste[self.index_dict["multiple_row_answ"]][0],
                                                 onvalue=1, offvalue=0,bg=self.label_color, fg=self.bg_color)
        self.multiple_row_answ_check['font'] = self.Label_Font
        self.multiple_row_answ_check.place(relx=0.3, rely=0, relwidth=.3, relheight=1)

        self.picture_preview_pixel_label = Label(self.checkbox_frame, text="Bildpreviewbreite in Pixel: ",anchor='w',  bg=self.label_color, fg=self.bg_color)
        self.picture_preview_pixel_label['font'] = self.Label_Font
        self.picture_preview_pixel_label.place(relx=0.6, rely=0, relwidth=.4, relheight=.5)

        self.picture_preview_pixel = Entry(self.checkbox_frame, text="Bild-Previewbreite in Pxl",
                                                   textvariable=self.dbinhaltsliste[self.index_dict["picture_preview_pixel"]][0], fg=self.bg_color)
        self.picture_preview_pixel['font'] = self.Entry_Font
        self.picture_preview_pixel.place(relx=0.6, rely=0.5, relwidth=.4, relheight=.5)

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
        self.response_input.update_pictures()
        self.dbinhaltsliste[self.index_dict["question_type"]][0].set(self.fragentyp)

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
        self.response_input = variable_scrl_UI(varname_1, self.bg_color, self.label_color, self.Label_Font,
                                              self.response_frame,
                                              self.dbinhaltsliste, self.index_dict, self.width_scrl_UI, Rows=10,
                                              Columns=2, Header="Definition",
                                              header_index=['Antworttext', 'Antwort-Grafik.'], column_type_list=[0, 1],
                                              columnwidth=(3, 3))
        rel_width = .5
        self.response_frame_2 = tk.Frame(self.Fragen_Window, bg=bg_color, bd=5)
        self.width_scrl_UI = self.width * rel_width
        self.response_frame_2.place(relx=.5, rely=0.3, relwidth=rel_width, relheight=.3)
        self.response_input_2 = variable_scrl_UI(varname_2, self.bg_color, self.label_color, self.Label_Font,
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

        self.shuffle_answers_check = Checkbutton(self.param_Frame, text="Antworten mehreren Fragen zuordnen",
                                                 variable=self.dbinhaltsliste[self.index_dict["asignment_mode"]][0],
                                                 onvalue=1, offvalue=0, bg=self.label_color, fg=self.bg_color)
        self.shuffle_answers_check['font'] = self.Label_Font
        self.shuffle_answers_check.place(relx=0, rely=.75, relwidth=1, relheight=.09)

        self.picture_preview_pixel_label = Label(self.param_Frame, text="Bildpreviewbreite in Pixel: ", anchor='w',
                                                 bg=self.label_color, fg=self.bg_color)
        self.picture_preview_pixel_label['font'] = self.Label_Font
        self.picture_preview_pixel_label.place(relx=0, rely=.85, relwidth=1, relheight=.05)

        self.picture_preview_pixel = Entry(self.param_Frame, text="Bild-Previewbreite in Pxl",
                                           textvariable=self.dbinhaltsliste[self.index_dict["picture_preview_pixel"]][
                                               0], fg=self.bg_color)
        self.picture_preview_pixel['font'] = self.Entry_Font
        self.picture_preview_pixel.place(relx=0, rely=0.9, relwidth=1, relheight=.05)

    def Fill_Entrys_From_DB(self, db_data):
        j = 0

        for i in db_data[1][self.table_dict[
            self.fragentyp]]:  # todo diese exception ist so nicht ok aber funktioniert erstmal um den Textbox Ihren Textzuzuweisen.
            if j == self.index_dict['question_description_main']:
                self.Fragentext_Entry.delete('1.0', 'end-1c')
                self.Fragentext_Entry.insert('1.0', i)
            else:
                self.dbinhaltsliste[j][0].set(i)
            j = j + 1
        self.image_interface_1.add_picture()
        self.image_interface_2.add_picture()
        self.image_interface_3.add_picture()
        self.response_input.update_pictures()
        self.response_input_2.update_pictures()
        self.zuordnungspaare_1.update_pictures()
        self.dbinhaltsliste[self.index_dict["question_type"]][0].set(self.fragentyp)

class formelfrage_permutation(fragen_gui):
    def __init__(self, table_dict, Frame, DB_interface, ScrText, dbinhaltsliste, index_dict, bg_color, label_color, button_color, *args, **kwargs):
        entry_color = 'white'
        self.fragentyp = "formelfrage_permutation"
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
                            "res{}_unit",
                               "perm_var_symbol_{}",
                               "perm_var_value_{}"]
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
        self.Results_interface = variable_scrl_UI(varname_list_result, self.bg_color, self.label_color, self.Label_Font,
                                                  self.ResFrame, self.dbinhaltsliste, self.index_dict,
                                                  self.width_scrl_UI, Rows=10, Columns=8, Header="Ergebnisse",
                                                  header_index=['Name.', 'Min.', 'Max', 'Tol.', 'Punkte', 'Formel', 'permut\nsymbol', 'permut\nwerte'],
                                                  column_type_list=[0, 0, 0, 0, 0, 0, 0, 0], columnwidth=(1, 1, 1, 1, 1, 1, 1, 1))


if __name__ == "__main__":
    from ScrolledText_Functionality import Textformatierung
    from DB_interface import DB_Interface

    from XML_class import XML_Interface
    root = tk.Tk()
    # WIDTH = int(root.winfo_screenwidth())
    # HEIGHT = int(root.winfo_screenheight())
    # root.title("Fragengenerator")
    # root.resizable(True, True)
    # root.geometry("%dx%d" % (WIDTH, HEIGHT))

    # Farben und Schriften Definitionen
    Label_Font = font.Font(family='Verdana', size=10, weight='bold')  # Font definition for Labels
    Entry_Font = font.Font(family='Verdana', size=10, weight='normal')  # Font definition for Entrys
    Button_Font = font.Font(family='Verdana', size=10, weight='normal')  # Font definition for Buttons
    table_list = ['formelfrage', 'singlechoice', 'multiplechoice', 'zuordnungsfrage', 'testeinstellungen', 'testeinstellungen']  # hier sind die Namen der Table drinne die verwendet werden können
    bg_color = '#4cc9f0'  # general Background color
    efg_color = '#3a0ca3'  # Entry foreground color
    entry_color = 'white'  # Entry Background color
    label_color = '#3a0ca3'
    button_color = '#3f37c9'
    fg_color = '#4cc9f0'  # general foregroundcolor
    table_dict = {'formelfrage': 0, 'singlechoice': 1, 'multiplechoice': 2, 'zuordnungsfrage': 3, 'testeinstellungen': 4, 'testeinstellungen': 5}

    mydb_name = 'generaldb.db'  # Datenbank mit allen Fragentypen
    mytempdb_name = 'generaldb2.db'  # Kopie der originalen Datenbank
    WIDTH = int(root.winfo_screenwidth())

    DBI = DB_Interface(mydb_name, mytempdb_name, table_dict, table_list)
    index_info = DBI.get_index_info()
    table_index_list = index_info[0]
    table_index_dict = index_info[1]
    xml_interface = XML_Interface(DBI, table_dict, table_index_list, table_index_dict)


    # zu Testzwecken die singlechoice Frage aus der DB holen und ein singlechoice Fragen Fenster öffnen
    work_window = Toplevel()
    work_window.title("Testfrage1")
    ScrText = Textformatierung()
    print("Hier wir in zukunft eine single Choice Frage geöffnet")
    work_on_question = singlechoice(table_dict, work_window, DBI, ScrText, table_index_list,
                                    table_index_dict, bg_color, label_color, button_color)

    DBI.get_question("Testfrage1", 1)
    #test_conf = Testeinstellungen(DBI, table_index_list[4], table_index_dict[4], table_dict['testeinstellungen'], WIDTH, Label_Font, Entry_Font, Button_Font, bg_color, entry_color, label_color, button_color, fg_color)
    root.mainloop()