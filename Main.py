from tkinter import *
import tkinter as tk
import tkinter.font as font
from DB_Treeview import UI
from DB_interface import DB_Interface
from XML_class import XML_Interface
from Taxonomie_interface import TAX_Interface
from Test_Klassen import Testeinstellungen_TRV
from tkinter import filedialog
from DB_creator import generate_db
from ScrolledText_Functionality import Textformatierung
class Main(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.pname = StringVar() #Strinvariable für die Poolname-eingabe

        # Farben und Schriften Definitionen
        self.Label_Font = font.Font(family='Verdana', size=10, weight='bold')  # Font definition for Labels
        self.Entry_Font = font.Font(family='Verdana', size=10, weight='normal')  # Font definition for Entrys
        self.Button_Font = font.Font(family='Verdana', size=10, weight='normal')  # Font definition for Buttons
        self.bg_color = '#4cc9f0'  # general Background color
        #self.fg_color = '#3a0ca3'  # Entry foreground color
        self.entry_color = 'white'  # Entry Background color
        self.label_color = '#3a0ca3'
        self.button_color = '#3f37c9'
        self.fg_color = '#4cc9f0'  # general foregroundcolor
        self.WIDTH = int(root.winfo_screenwidth())  # Monitorauflösung in Pixel in der Breite


        # Datenbank mit allen Fragentypen/ wenn nicht vorhanden muss mit DB_creator_Testbed erstellt werden
        mydb_name = 'generaldb.db'
        # Kopie der originalen Datenbankstrucktur und wird als temporärer Speicher für Fragen die als Test verwendet werden sollen benutzt
        mytempdb_name = 'generaldb2.db'
        # hier sind die Namen der Table drinne die verwendet werden können
        self.table_list = ['formelfrage', 'singlechoice', 'multiplechoice', 'zuordnungsfrage',
                           'formelfrage_permutation',
                           'testeinstellungen']
        # hier kann der Index des entsprechenden Table namens in self.table_list bestimmt werden
        self.table_dict = {'formelfrage': 0, 'singlechoice': 1, 'multiplechoice': 2, 'zuordnungsfrage': 3, 'formelfrage_permutation' : 4 , 'testeinstellungen': 5}

        # initialisierung des Datenbank interface, hier sind alle Funktionen untergebracht die mit der Datenbank Kommunikation zutun haben/ mehr informationen in DB_interface.py
        self.DBI = DB_Interface(mydb_name, mytempdb_name, self.table_dict, self.table_list)
        #Für jeden table in der Datenbank werden die Spaltenbeschriftungen ausgelesen und eine Textvariable erstellt
        self.index_info = self.DBI.get_index_info()
        self.table_index_list = self.index_info[0]
        self.table_index_dict = self.index_info[1]

        # XML_Interface erstellen, diese Klasse muss die DBI kennen. Daher wird dieses übergeben
        self.xml_interface = XML_Interface(self.DBI, self.table_dict, self.table_index_list, self.table_index_dict)

        tax_interface = TAX_Interface(self.bg_color, self.button_color, self.label_color, self.Button_Font,
                                      self.Label_Font)
        #Aufteilung des Startbildschirm in 3 Frames
        #Frame für die Fragen-Datenbank UI
        Left_Top_Frame = tk.Frame(bg=self.bg_color, bd=20)
        Left_Top_Frame.place(relx=0, rely=0, relwidth=.8, relheight=.5)
        #Frame für die Temporäre Datenbank UI
        Left_Bottom_Frame = tk.Frame(bg=self.bg_color, bd=20)
        Left_Bottom_Frame.place(relx=0, rely=0.5, relwidth=.8, relheight=.5)
        #Menü
        Right_Menu_Frame = tk.Frame(bg=self.bg_color, bd=20)
        Right_Menu_Frame.place(relx=.8, rely=0.0, relwidth=.2, relheight=1)


        #Fragen-Datenbank UI in Left_Top_Frame öffnen
        DBT = UI(self.table_dict, self.DBI, Left_Top_Frame, self.WIDTH, 0, self.table_index_list, self.table_index_dict, "Fragendatenbank", self.bg_color, self.button_color, self.label_color, self.Button_Font, self.Label_Font)
        #Temporäre-Datenbank UI in Left_Bottom_Frame öffnen
        Test_T = UI(self.table_dict, self.DBI, Left_Bottom_Frame, self.WIDTH, 2, self.table_index_list, self.table_index_dict, "Fragenauswahl für Test", self.bg_color, self.button_color, self.label_color, self.Button_Font, self.Label_Font)

        #Menue
        Menu_lbl = Label(Right_Menu_Frame, text="Menü", bg=self.label_color, fg=self.bg_color)
        Menu_lbl['font'] = self.Label_Font
        Menu_lbl.pack(side="top", fill=X)
        new_question = Button(Right_Menu_Frame, text="neue Frage", bg=self.button_color, fg=self.bg_color, command=DBT.choose_qt_typ)
        new_question['font'] = self.Button_Font
        new_question.pack(side="top", fill=X)
        add_question = Button(Right_Menu_Frame, text="Frage zu Test hinzufügen", bg=self.button_color, fg=self.bg_color, command=DBT.add_data_to_testdb)
        add_question['font'] = self.Button_Font
        add_question.pack(side="top", fill=X)
        excel_import = Button(Right_Menu_Frame, text="Fragen aus Excel importieren", bg=self.button_color, fg=self.bg_color, command=self.xml_interface.excel_import_to_db)
        excel_import['font'] = self.Button_Font
        excel_import.pack(side="top", fill=X)
        excel_export_to_xlsx = Button(Right_Menu_Frame, text="Datenbank exportieren", bg=self.button_color, fg=self.bg_color, command= lambda: self.xml_interface.excel_export_to_xlsx(self, self.table_index_dict, self.table_list))
        excel_export_to_xlsx['font'] = self.Button_Font
        excel_export_to_xlsx.pack(side="top", fill=X)
        datenbank_og = Button(Right_Menu_Frame, text="Datenbank wählen", bg=self.button_color, fg=self.bg_color, command=self.DB_Manager_UI)
        datenbank_og['font'] = self.Button_Font
        datenbank_og.pack(side="top", fill=X)
        taxonomy_settings = Button(Right_Menu_Frame, text="Taxonomie bearbeiten", bg=self.button_color, fg=self.bg_color, command=tax_interface.edit_tax_of_existing_ilias_pool_file)
        taxonomy_settings['font'] = self.Button_Font
        taxonomy_settings.pack(side="top", fill=X)
        help_btn = Button(Right_Menu_Frame, text="Hilfe", bg=self.button_color,
                                   fg=self.bg_color, command=self.help_window)
        help_btn['font'] = self.Button_Font
        help_btn.pack(side="top", fill=X)
        test_lbl = Label(Right_Menu_Frame, text="Test Menü", bg=self.label_color, fg=self.bg_color)
        test_lbl['font'] = self.Label_Font
        test_lbl.pack(side="top", fill=X)
        create_Test = Button(Right_Menu_Frame, text="Test erstellen", bg=self.button_color, fg=self.bg_color, command=self.create_Test_Menu)
        create_Test.pack(side="top", fill=X)
        create_Test['font'] = self.Button_Font
        create_Pool = Button(Right_Menu_Frame, text="Pool erstellen", bg=self.button_color, fg=self.bg_color, command=self.Poolname_eingabe_menu)
        create_Pool['font'] = self.Button_Font
        create_Pool.pack(side="top", fill=X)


    def help_window(self):
        work_window = Toplevel(bg=self.bg_color)
        work_window.geometry("%dx%d+%d+%d" % (WIDTH / 1.5, WIDTH / 5, WIDTH / 2, WIDTH / 4))
        Menu_lbl = Label(work_window,
                         text="Auswahl einer Frage in der Datenbank geshieht durch einmaliges drücken der linken Maustaste.\n Es kann Shift oder Str gedrücktgehalten werden um mehrere Fragen gleichzeitig zu Makieren.\n Ihre auswahl können Sie entweder zu einem Test hinzufügen über den Button im Menü auf der rechte Seite oder Löschen ", bg=self.label_color,
                         fg="white", anchor="w")
        Menu_lbl['font'] = self.Label_Font
        Menu_lbl.place(relx=.1, rely=.05, relwidth=1, relheight=.2)
        Menu_lbl_2 = Label(work_window,
                         text="Bearbeiten Sie eine bereits erstellte Frage durch einen Doppelklick auf die Zeile in der Fragenübersicht.",
                         bg=self.label_color,
                         fg="white", anchor="w")
        Menu_lbl_2['font'] = self.Label_Font
        Menu_lbl_2.place(relx=.1, rely=.3, relwidth=1, relheight=.2)
        Menu_lbl_2 = Label(work_window,
                           text="Die Suche sucht nach ganzen begriffen oder Textteilen in allen 6 Spalten.\n Um wieder alle fragen sehen zu könne drücken Sie zurücksetzen."
                           ,bg=self.label_color,
                           fg="white", anchor="w")
        Menu_lbl_2['font'] = self.Label_Font
        Menu_lbl_2.place(relx=.1, rely=.55, relwidth=1, relheight=.2)

    def New_DB_window(self):
        work_window = Toplevel(bg=self.bg_color)
        work_window.geometry("%dx%d+%d+%d" % (WIDTH / 1.5, WIDTH / 5, WIDTH / 2, WIDTH / 4))
        Menu_lbl = Label(work_window,
                         text="Auswahl einer Frage in der Datenbank geshieht durch einmaliges drücken der linken Maustaste.\n Es kann Shift oder Str gedrücktgehalten werden um mehrere Fragen gleichzeitig zu Makieren.\n Ihre auswahl können Sie entweder zu einem Test hinzufügen über den Button im Menü auf der rechte Seite oder Löschen ", bg=self.label_color,
                         fg="white", anchor="w")
        Menu_lbl['font'] = self.Label_Font
        Menu_lbl.place(relx=.1, rely=.05, relwidth=1, relheight=.2)
        Menu_lbl_2 = Label(work_window,
                         text="Bearbeiten Sie eine bereits erstellte Frage durch einen Doppelklick auf die Zeile in der Fragenübersicht.",
                         bg=self.label_color,
                         fg="white", anchor="w")
        Menu_lbl_2['font'] = self.Label_Font
        Menu_lbl_2.place(relx=.1, rely=.3, relwidth=1, relheight=.2)
        Menu_lbl_2 = Label(work_window,
                           text="Die Suche sucht nach ganzen begriffen oder Textteilen in allen 6 Spalten. Um wieder alle fragen sehen zu könne drücken Sie zurücksetzen."
                           ,bg=self.label_color,
                           fg="white", anchor="w")
        Menu_lbl_2['font'] = self.Label_Font
        Menu_lbl_2.place(relx=.1, rely=.55, relwidth=1, relheight=.2)


    #Testmenü wird als neue Instanz aufgerufen wenn der Test_erstellen_Button gedrückt wird, diese Klasse befindet sich in Test_Klassen.py
    def create_Test_Menu(self):
        Test_TRV = Testeinstellungen_TRV(self.DBI, self.xml_interface, self.table_index_list[5], self.table_index_dict[5],
                                         self.table_dict['testeinstellungen'], self.WIDTH, self.Label_Font, self.Entry_Font, self.Button_Font,
                                         self.bg_color, self.entry_color, self.label_color, self.button_color, self.fg_color)
    def Poolname_eingabe_menu(self):
        Poolmenu = Pool_Name(self.xml_interface, self.WIDTH, self.Label_Font, self.Entry_Font, self.Button_Font,
                                         self.bg_color, self.entry_color, self.label_color, self.button_color, self.fg_color)
    def DB_Manager_UI(self):
        self.textvar = StringVar()
        self.work_window = Toplevel()
        width = self.WIDTH
        name = StringVar()
        self.work_window.title("Datenbankauswahl")
        self.work_window.resizable(True, True)
        self.work_window.geometry("%dx%d+%d+%d" % (width / 6, width / 12, width / 2, width / 4))
        Choose_DB = Button(self.work_window, text="Datenbank auswählen", bg=self.button_color, fg=self.bg_color,
                             command=self.Choose_DB)
        Choose_DB['font'] = self.Button_Font
        Choose_DB.pack(side="top", fill=X)
        DB_name = Label(self.work_window, textvariable= self.textvar)
        DB_name['font'] = self.Entry_Font
        DB_name.pack(side="top", fill=X)
        self.Open_DB = Button(self.work_window, text="Datenbank Öffnen", bg=self.button_color, fg=self.bg_color,
                           command=lambda: self.DBI.change_DB(self.file.name))
        self.Open_DB['font'] = self.Button_Font
        self.Open_DB.pack(side="top", fill=X)
        Paltzhalter = Label(self.work_window,bg=self.bg_color)
        Paltzhalter.pack(side="top", fill=X)
        New_DB = Button(self.work_window, text="Neue Datenbank erstellen", bg=self.button_color, fg=self.bg_color,
                        command=lambda: self.create_DB(name))
        New_DB['font'] = self.Button_Font
        New_DB.pack(side="top", fill=X)
        New_DB_name = Entry(self.work_window, textvariable=name, fg=self.bg_color)
        New_DB_name['font'] = self.Label_Font
        New_DB_name.pack(side="top", fill=X)
        # self.Open_DB.bind('<ButtonRelease-1>', self.destroy_DB_Manager_UI)

    def destroy_DB_Manager_UI(self, e):
        self.work_window.destroy()

    def create_DB(self, name_var):
        name = name_var.get()
        name = name + ".db"
        print(name)
        new_DB = generate_db(name)

    def Choose_DB(self):
        self.file = filedialog.askopenfile(parent=self.work_window, mode='rb', title='Choose a file')
        print("dieser Pfad wurde zurückgegeben:", self.file.name)
        self.textvar.set(self.file.name)

class Pool_Name():
    def __init__(self, xml_interface, width, label_font, entry_font, Button_Font, bg_color, entry_color, label_color, button_color, fg_color):
        self.xml_interface = xml_interface
        self.Label_pfont = font.Font(family='Verdana', size=15, weight='bold')
        self.Entry_pfont = font.Font(family='Verdana', size=15, weight='normal')
        self.active = False  # Aktivitätsflag für Such Eingabefeld
        self.pname = StringVar()
        work_window_basis = Toplevel()
        work_window_basis.geometry("%dx%d+%d+%d" % (width / 6, width / 12, width / 2, width / 4))
        work_window_basis.title("Fragenpool erstellen")
        work_window = Frame(work_window_basis, bd=10 ,bg=bg_color)
        work_window.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.Poolname = Entry(work_window, textvariable=self.pname, fg="grey")
        self.Poolname.place(relx=0, rely=0, relwidth=1, relheight=.5)
        self.Poolname['font'] = self.Entry_pfont
        self.pname.set("Poolname eingeben")
        create_Pool2 = Button(work_window, text="Pool erstellen", bg=button_color, fg=bg_color,
                              command=lambda: self.create_Fragenpool(work_window_basis))
        create_Pool2['font'] = Button_Font
        create_Pool2.place(relx=0, rely=0.5, relwidth=1, relheight=.5)
        create_Pool2['font'] = self.Label_pfont
        self.Poolname.bind('<FocusIn>', self.delete_placeholder)
        self.Poolname.bind('<FocusOut>', self.delete_placeholder)

    def delete_placeholder(self, e):
        if len(self.pname.get()) < 1 & self.active == True:
            self.pname.set("Poolname eingeben")
            self.Poolname.configure(fg="grey")
            self.active = False
        elif self.active == False:
            self.pname.set("")
            self.Poolname.configure(fg="black")
            self.active = True

    def create_Fragenpool(self, work_window_basis):
        work_window_basis.destroy()
        self.xml_interface.create_test_or_pool(self.pname, "ilias_pool")
        self.pname.set("Poolname eingeben")

if __name__ == "__main__":


    root = tk.Tk()
    WIDTH = int(root.winfo_screenwidth() / 1.25)
    HEIGHT = int(root.winfo_screenheight() / 2)
    root.title("Fragengenerator")
    root.resizable(True, True)
    root.geometry("%dx%d" % (WIDTH, HEIGHT))
    #dieses Programm läuft in einer Main Klasse die hier erstellt wird
    main = Main(root)
    main.pack()
    root.mainloop()