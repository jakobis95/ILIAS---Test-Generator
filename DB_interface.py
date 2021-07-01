import sqlite3
from tkinter import *
from pathlib import Path

#Die DB_Interface Klasse regelt sämliche Datenflüsse zwischen der SQL Datenbank und allen anderen Klasse wie z.B. die UI-Klassen
#Um auf die Datenbankfunktionalitäten zuzugreifen muss eine Klasse subscribed sein zu einer der Instanz der Db_Interface
#Die Db_interface broardcastet die angeforderten Daten dann an alle subscriber und jeder sucht sich die für Ihn relevanten daten herraus
class DB_Interface():
    def __init__(self, nichtbenutzter_DB_name, tempdbname, table_dict, table_list, *args, **kwargs):
        self.listeners = []
        self.all_data = []
        self.db_data = [self.all_data, None, None, False] #broadcast data 1:  Datenbak auswahl 2:  Einzelne Frage aus Datenbank 3: daten in Temp datenbank 4:
        self.table = 'formelfrage'
        self.table_dict = table_dict
        self.table_list = table_list

        datei = open('Standard_DB_Name.txt', 'r')
        start_path = datei.read()
        my_file = Path(start_path)
        if my_file.is_file():
            dbname = start_path
        else:
            datei = open('Standard_DB_Name.txt', 'w')
            datei.write("generaldb.db")
            dbname = 'generaldb.db'
            print("Die gespeicherte Datenbank konnte nicht gefunden werden\n es wurde eine Leere Datenbank erstellt")


        # Insert Data from Database
        self.mydb = sqlite3.connect(dbname)
        self.cursor = self.mydb.cursor()
        self.mytempdb = sqlite3.connect(tempdbname)
        self.tempcursor = self.mytempdb.cursor()
        for table in self.table_list:# Temporäre Datenbank wird geleert, da hier noch daten vom letzen benutzen drinn sein können
            self.tempcursor.execute("DELETE  FROM " + table + "")
        self.mytempdb.commit()
        self.cursorlist = [self.cursor, self.cursor, self.tempcursor]
        self.dblist = [self.mydb, None, self.mytempdb]

    def change_DB(self, db_path):
        self.mydb.close()
        self.mydb = sqlite3.connect(db_path)
        self.cursor = self.mydb.cursor()
        self.cursorlist[0] = self.cursor
        self.cursorlist[1] = self.cursor
        self.dblist[0] = self.mydb
        print("new db selected:", db_path)
        self.get_complete_DB(0)
        datei = open('Standard_DB_Name.txt', 'w')
        datei.write(db_path)

    def search_DB(self, q2, id): #Suche sollte so jetzt Funktionieren
        searchterm = str(q2)
        zwischenspeicher = []
        for table in self.table_list:
            self.query = " SELECT " + self.table_index_list[self.table_dict[table]][0][1] + ", " + self.table_index_list[self.table_dict[table]][1][1] + ", " + self.table_index_list[self.table_dict[table]][2][1] + ", " + self.table_index_list[self.table_dict[table]][3][1] + ", " + self.table_index_list[self.table_dict[table]][4][1] + " FROM " + table + " Where " + self.table_index_list[self.table_dict[table]][0][1] + " LIKE '" + searchterm + "' OR " + self.table_index_list[self.table_dict[table]][1][1] + " LIKE '" + searchterm + "' OR " + self.table_index_list[self.table_dict[table]][2][1] + " LIKE '" + searchterm + "' OR " + self.table_index_list[self.table_dict[table]][3][1] + " LIKE '" + searchterm + "' "
            print("query", self.query)
            self.cursor.execute(self.query)

            zwischenspeicher.append(self.cursor.fetchall())
        print(zwischenspeicher)
        self.db_data[id] = zwischenspeicher
        self.notify()

    def does_title_exist(self, title): #todo testing required
        state = False
        print("does title exist", title)
        for table in self.table_list:
            self.query = " SELECT * FROM " + table + " WHERE " + self.table_index_list[self.table_dict[table]][3][1] + " = '" + title + "' "
            self.cursor.execute(self.query)
            vergleich = self.cursor.fetchone()
            print("das wurde in der DB gesucht", title)
            print("das wurde in der DB gefunden", vergleich)
            if vergleich:
                state = True

        return state

    def get_question(self, q2, id): #todo testing required
        zwischenspeicher = []
        for table in self.table_list:
            index = self.table_index_list[self.table_dict[table]][3][1]
            query = " SELECT * FROM " + table + " WHERE " + index + " LIKE '" + q2 + "' "

            #print(self.query)
            self.cursor.execute(query)
            test = self.cursor.fetchone()
            if test == None:
                zwischenspeicher.append("leer")
            else:
                zwischenspeicher.append(test)
        print("zwischenspeicher", zwischenspeicher)
        self.db_data[id] = zwischenspeicher
        self.og_title = self.db_data[id][0][3]
        #print(og_title)
        print(self.db_data[id])
        self.notify()

    def empty_fragenauswahl(self):
        self.db_data[1] = None
        self.notify()

    def get_index_info(self):
        self.table_index_list = [None, None, None, None, None, None] #hier sind die index_list elemtente für jeden table die den Fragentypenentsprechen zusammengefasst
        self.table_index_dict = [None, None, None, None, None, None] #hier sind die index_dict elemente für jeden table zusammengefasst
        i = 0
        for table in self.table_list:
            self.index_list = []
            self.index_dict = {}
            index = 0
            self.cursor.execute("PRAGMA table_info( " + table + " ) ")
            for row in self.cursor:
                Var = StringVar()
                q = (Var, row[1])
                d = {row[1] : index}

                self.index_dict.update(d)
                self.index_list.append(q)
                index = index + 1

            self.table_index_dict[i] = self.index_dict #liste von dictionary für jeden tabel kann mit self.table_dict[tablename] verwendet werden
            self.table_index_list[i] = self.index_list
            i = i + 1
            #print("index aus ", self.index_dict['question_type'])

        return self.table_index_list, self.table_index_dict

    def add_question_to_temp(self, item_list):
        zwischenspeicher = []
        table = "singlechoice"
        print("item:", )

        for item in item_list:
            table = item['values'][2]
            #print("Der Eintrag mit dem Titel: ", item['values'][2], ", soll kopiert werden")
            self.cursor.execute("SELECT * FROM " + table + " WHERE " + self.table_index_list[self.table_dict[table]][3][1] + " = '" + item['values'][0] + "' ")
            data = self.cursor.fetchone()
            print("data", data)
            self.tempcursor.execute("INSERT INTO " + table + " (" + self.table_index_list[self.table_dict[table]][3][1] + ") VALUES (:Titel)", {'Titel': data[3]})
            i = 0
            for item in data:
                #print("this will be copied:", item)
                self.tempcursor.execute("UPDATE " + table + " SET '" + self.table_index_list[self.table_dict[table]][i][1] + "' = :Value WHERE " + self.table_index_list[self.table_dict[table]][3][1] + " = '" + data[3] + "'", {'Value': item})
                i = i + 1
        self.mytempdb.commit()

        for table in self.table_list:
        #todo das läuft hier nicht durch database is locked heißt es
            self.query = "SELECT " + self.table_index_list[self.table_dict[table]][0][1] + ", " + self.table_index_list[self.table_dict[table]][1][1] + ", " + self.table_index_list[self.table_dict[table]][2][1] + ", " + self.table_index_list[self.table_dict[table]][3][1] + ", " + self.table_index_list[self.table_dict[table]][4][1] + " FROM " + table + ""
        #print(self.query)
            self.tempcursor.execute(self.query)
            zwischenspeicher.append(self.tempcursor.fetchall())

        self.db_data[2] = zwischenspeicher
        self.notify()

    def delete_DB_content(self, item_list, ID):
        for item in item_list:
            fragentyp = item['values'][2]
            table = fragentyp
            fragenname = item['values'][3]
            print(self.index_list[3][1])
            self.cursorlist[ID].execute(
                "DELETE  FROM " + fragentyp + " WHERE " + self.table_index_list[self.table_dict[table]][3][1] + " = '" + item['values'][
                    3] + "'") # item['values'][2] = Fragentyp und der entspricht dem Table in der Datenbank für diesen Fragentyp
            self.dblist[ID].commit()
        self.get_complete_DB(ID)
        self.notify()

    def delete_DB_testeinstellung_content(self, gesucht, ID):

        self.cursorlist[ID].execute("DELETE  FROM testeinstellungen WHERE " + self.index_list[3][1] + " = '" + gesucht + "'") # item['values'][2] = Fragentyp und der entspricht dem Table in der Datenbank für diesen Fragentyp
        self.dblist[ID].commit()
        self.get_complete_DB(ID)
        self.notify()


    def Add_data_to_DB(self, q, title):
        if self.does_title_exist(title):
            print("title existiert bereits daher konnte die Frage nicht erstellt werden")
        else:
            print("title existiert noch nicht")

            table_name = q[2][0].get() #table name ist gleich dem FragentypA
            index = self.table_dict[table_name]
            self.cursor.execute("INSERT INTO " + table_name + " (" + self.table_index_list[index][3][1] + ") VALUES (:Titel)",
                                {'Titel': q[3][0].get()})
            # print("INSERT INTO " + self.table + " (" + self.index_list[3][1] + ") VALUES (:Titel)", {'Titel': q[3][0].get()})
            self.mydb.commit()
            for i in q:
                self.cursor.execute(
                    "UPDATE " + table_name + " SET '" + i[1] + "' = :Value WHERE " + self.table_index_list[index][3][1] + " = '" +
                    q[3][0].get() + "' ", {'Value': i[0].get()})
            self.mydb.commit()
            self.get_question(q[3][0].get(), 1)
            self.get_complete_DB(0)

    def add_Changes_to_DB(self, q):
        table_name = q[2][0].get() #table name ist gleich dem FragentypA
        index = self.table_dict[table_name]
        for i in q:

            self.cursor.execute(
                "UPDATE " + table_name + " SET '" + i[1] + "' = :Value WHERE " + self.table_index_list[index][3][
                    1] + " LIKE '%" + self.db_data[1][0][3] + "%'",
                {'Value': i[0].get()})
            self.mydb.commit()
        self.get_question(q[3][0].get(), 1)
        self.get_complete_DB(0)

    def Save_Change_to_DB(self, q):

        title = q[3][0].get()
        if self.og_title == title:
               self.add_Changes_to_DB(q)
        elif self.does_title_exist(title):
            print("title existiert bereits, speichern nicht möglich")
        else:
            print("datenänderung konnte gespeichert werden")
            self.add_Changes_to_DB(q)

    def subscribe(self, listener):
        self.listeners.append(listener)

    def unsubscribe(self, listener):
        self.listeners.remove(listener)

    def get_complete_DB(self, id):
        all_data = []
        for table in self.table_list:
            if table == "testeinstellungen":
                self.query = "SELECT " + self.table_index_list[self.table_dict[table]][3][1] + " FROM " + table + ""
                print("Table", table)
            else:
                self.query = "SELECT " + self.table_index_list[self.table_dict[table]][self.table_index_dict[self.table_dict[table]]["question_title"]][1] + ", " + self.table_index_list[self.table_dict[table]][self.table_index_dict[self.table_dict[table]]["question_pool_tag"]][1] + ", " + self.table_index_list[self.table_dict[table]][self.table_index_dict[self.table_dict[table]]["question_type"]][1] + ", " + self.table_index_list[self.table_dict[table]][self.table_index_dict[self.table_dict[table]]["question_description_main"]][1] + ", " + self.table_index_list[self.table_dict[table]][self.table_index_dict[self.table_dict[table]]["date"]][1] + ", " + self.table_index_list[self.table_dict[table]][self.table_index_dict[self.table_dict[table]]["question_author"]][1] + " FROM " + table + ""
            print("Was steht im query:", self.query)
            self.cursorlist[id].execute(self.query)
            all_data.append(self.cursorlist[id].fetchall())

        self.db_data[id] = all_data
        print("all data", all_data)
        self.notify()

    def get_testeinstellungen(self, id):
        all_data = []
        for table in self.table_list:
            if table == "testeinstellungen":
                self.query = "SELECT " + self.table_index_list[self.table_dict[table]][3][1] + " FROM " + table + ""
                self.cursorlist[id].execute(self.query)
                all_data.append(self.cursorlist[id].fetchall())
        print("all data", all_data)
        self.db_data[id] = all_data
        self.notify()

    def get_dbtemp_data(self):

        print("___________________________")
        self.test_data = []
        self.question_types = ["formelfrage", "singlechoice", "multiplechoice", "zuordnungsfrage", "formelfrage_permutation"]

        # Durch alle tables suchen und Ergebnisse in einer Liste zusammenfassen
        # "extend" fügt eine Liste einer anderen zu
        for i in range(len(self.question_types)):
            self.query = "SELECT * FROM " + str(self.question_types[i]) + ""

            self.tempcursor.execute(self.query)
            self.test_data.extend((self.tempcursor.fetchall()))

        return self.test_data



    def notify(self):
        for listener in self.listeners:
            listener(self.db_data)