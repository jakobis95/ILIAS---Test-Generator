from tkinter import *
import tkinter as tk
import tkinter.font as font
from DB_Treeview import UI
from DB_interface import DB_Interface
#from XML_class import xml_interface
from ScrolledText_Functionality import Textformatierung
class Main(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        #XML related data

        print("hier habe ich etwas geschrieben damit wir sehen was passiert wenn ich das jetzt auch eine ebenfalls geänderte GitHub pusche")






        # Farben und Schriften Definitionen
        Label_Font = font.Font(family='Verdana', size=10, weight='bold')  # Font definition for Labels
        Entry_Font = font.Font(family='Verdana', size=10, weight='normal')  # Font definition for Entrys
        Button_Font = font.Font(family='Verdana', size=10, weight='normal')  # Font definition for Buttons
        self.table_list = ['formelfrage', 'singlechoice', 'multiplechoice',
                           'zuordnungsfrage']  # hier sind die Namen der Table drinne die verwendet werden können
        bg_color = '#4cc9f0'  # general Background color
        efg_color = '#3a0ca3'  # Entry foreground color
        entry_color = 'white'  # Entry Background color
        label_color = '#3a0ca3'
        button_color = '#3f37c9'
        fg_color = '#4cc9f0'  # general foregroundcolor
        table_dict = {'formelfrage': 0, 'singlechoice': 1, 'multiplechoice': 2, 'zuordnungsfrage': 3}

        mydb_name = 'generaldb.db'         #Datenbank mit allen Fragentypen
        mytempdb_name = 'generaldb2.db' #Kopie der originalen Datenbank
        Left_Top_Frame = tk.Frame(bg=bg_color, bd=20)
        Left_Top_Frame.place(relx=0, rely=0, relwidth=.8, relheight=.5)
        Left_Bottom_Frame = tk.Frame(bg=bg_color, bd=20)
        Left_Bottom_Frame.place(relx=0, rely=0.5, relwidth=.8, relheight=.5)
        Right_Menu_Frame = tk.Frame(bg=bg_color, bd=20)
        Right_Menu_Frame.place(relx=.8, rely=0.0, relwidth=.2, relheight=1)

        WIDTH = int(root.winfo_screenwidth())

        DBI = DB_Interface(mydb_name, mytempdb_name, root, table_dict, self.table_list)
        index_info = DBI.get_index_info()
        table_index_list = index_info[0]
        table_index_dict = index_info[1]
        print("das ist in Main", table_index_list)
        DBT = UI(table_dict, DBI, Left_Top_Frame, WIDTH, 0, table_index_list, table_index_dict, "Fragendatenbank", bg_color, button_color, label_color, Button_Font, Label_Font)
        Test_T = UI(table_dict, DBI, Left_Bottom_Frame, WIDTH, 2, table_index_list, table_index_dict, "Fragenauswahl für Test", bg_color, button_color, label_color, Button_Font, Label_Font)
        mytempdb_name = '../tempdb.db'

        # XML_interface erstellen, diese Klasse muss die DBI kennen. Daher wird dieses übergeben
        # XML_interface = xml_interface(DBI)

        #Menue
        Menu_lbl = Label(Right_Menu_Frame, text="Menü", bg=label_color, fg=bg_color)
        Menu_lbl['font'] = Label_Font
        Menu_lbl.pack(side="top", fill=X)
        new_question = Button(Right_Menu_Frame, text="neue Frage", bg=button_color, fg=bg_color, command=DBT.choose_qt_typ)
        new_question['font'] = Button_Font
        new_question.pack(side="top", fill=X)
        add_question = Button(Right_Menu_Frame, text="Frage zu für Test auswählen", bg=button_color, fg=bg_color, command=DBT.add_data_to_testdb)
        add_question['font'] = Button_Font
        add_question.pack(side="top", fill=X)
        excel_import = Button(Right_Menu_Frame, text="Fragen aus Excel", bg=button_color, fg=bg_color)
        excel_import['font'] = Button_Font
        excel_import.pack(side="top", fill=X)
        datenbank_og = Button(Right_Menu_Frame, text="Datenbank wählen", bg=button_color, fg=bg_color)
        datenbank_og['font'] = Button_Font
        datenbank_og.pack(side="top", fill=X)
        test_lbl = Label(Right_Menu_Frame, text="Test Menü", bg=label_color, fg=bg_color)
        test_lbl['font'] = Label_Font
        test_lbl.pack(side="top", fill=X)
        #create_Test = Button(Right_Menu_Frame, text="Test aus Auswahl erstellen", bg=button_color, fg=bg_color, command=self.Test_aus_auswahl_erstellem)
        #create_Test['font'] = Button_Font
        #create_Test.pack(side="top", fill=X)
        create_Test_excel = Button(Right_Menu_Frame, text="Test aus Excel erstellen", bg=button_color, fg=bg_color)
        create_Test_excel['font'] = Button_Font
        create_Test_excel.pack(side="top", fill=X)
        #Put_btn = tk.Button(bottom_Frame, text="Add to Test")
        #Put_btn.place(relx=0, rely=0)

    #def test_aus_auswahl_erstellen(self): # hier werden die Funktionalitäten aufgerufen um einen Test zu erstellen
        #self.table_list #liste mit den 4 tabeln
        #mytempdb_name #datenbank name nicht der von Temp

if __name__ == "__main__":


    root = tk.Tk()
    WIDTH = int(root.winfo_screenwidth() / 1.25)
    HEIGHT = int(root.winfo_screenheight() / 2)
    root.title("Fragengenerator")
    root.resizable(True, True)
    root.geometry("%dx%d" % (WIDTH, HEIGHT))
    main = Main(root)
    main.pack()
    root.mainloop()