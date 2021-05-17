import xml.etree.ElementTree as ET
import os
from PIL import Image
import pathlib
import shutil
import base64
from tkinter import filedialog
import pandas as pd
import shutil


class XML_Interface():


        # table_index_dict beinhaltet Daten für ALLE Fragentypen
        def __init__(self, DBI, table_dict, table_index_list, table_index_dict):
                self.DBI = DBI
                self.table_index_list = table_index_list
                self.table_index_dict = table_index_dict
                self.table_dict = table_dict



                # Forced Values
                # question_test / question_pool
                # = "question_pool"
                self.number_of_entrys = []
                self.pool_qpl_file_path_template = ""
                self.pool_qpl_file_path_output = ""
                self.qpl_file_path = ""



                #######


                print("\n")
                print("\n")
                print("\n")
                

                ############### Deklarierung der Pfade

                # Pfad des Projekts und der Module
                self.project_root_path = pathlib.Path().absolute()
                self.formelfrage_files_path = os.path.normpath(os.path.join(self.project_root_path, "ILIAS-Formelfrage"))
                self.singlechoice_files_path = os.path.normpath(os.path.join(self.project_root_path, "ILIAS-SingleChoice"))
                self.multiplechoice_files_path = os.path.normpath(os.path.join(self.project_root_path, "ILIAS-MultipleChoice"))
                self.zuordnungsfrage_files_path = os.path.normpath(os.path.join(self.project_root_path, "ILIAS-Zuordnungsfrage"))
                self.gemischte_fragentypen_files_path = os.path.normpath(os.path.join(self.project_root_path, "ILIAS-Gemischte_Fragentypen"))

                self.formelfrage_files_path_pool_output = os.path.normpath(os.path.join(self.formelfrage_files_path, "ff_ilias_pool_abgabe"))
                self.singlechoice_files_path_pool_output = os.path.normpath(os.path.join(self.singlechoice_files_path, "sc_ilias_pool_abgabe"))
                self.multiplechoice_files_path_pool_output = os.path.normpath(os.path.join(self.multiplechoice_files_path, "mc_ilias_pool_abgabe"))
                self.zuordnungsfrage_files_path_pool_output = os.path.normpath(os.path.join(self.zuordnungsfrage_files_path, "mq_ilias_pool_abgabe"))
                self.gemischte_fragentypen_files_path_pool_output = os.path.normpath(os.path.join(self.gemischte_fragentypen_files_path, "mixed_ilias_pool_abgabe"))





                # Pfad für ILIAS-Pool Dateien (zum hochladen in ILIAS)
                # Die Pfade für die qti.xml und qpl.xml werden erst zur Laufzeit bestimmt.



                #### Prüfung abgeschlossen



                ##### Pfade für Formelfrage #############################
                # Pfad für ILIAS-Test Vorlage
                self.formelfrage_test_qti_file_path_template = os.path.normpath(os.path.join(self.formelfrage_files_path, "ff_test_qti_und_tst_dateien_vorlage", "ilias_test_vorlage__qti__.xml"))
                self.formelfrage_test_tst_file_path_template = os.path.normpath(os.path.join(self.formelfrage_files_path, "ff_test_qti_und_tst_dateien_vorlage", "ilias_test_vorlage__tst__.xml"))

                # Pfad für ILIAS-Test Dateien (zum hochladen in ILIAS)
                self.formelfrage_test_qti_file_path_output = os.path.normpath(os.path.join(self.formelfrage_files_path, "ff_ilias_test_abgabe", "1604407426__0__tst_2040314", "1604407426__0__qti_2040314.xml"))
                self.formelfrage_test_tst_file_path_output = os.path.normpath(os.path.join(self.formelfrage_files_path, "ff_ilias_test_abgabe", "1604407426__0__tst_2040314", "1604407426__0__tst_2040314.xml"))
                self.formelfrage_test_img_file_path_output = os.path.normpath(os.path.join(self.formelfrage_files_path, "ff_ilias_test_abgabe", "1604407426__0__tst_2040314", "objects"))


                # Pfad für ILIAS-Pool Vorlage
                self.formelfrage_pool_qti_file_path_template = os.path.normpath(os.path.join(self.formelfrage_files_path, "ff_pool_qti_und_qpl_dateien_vorlage", "ilias_pool_vorlage__qti__.xml"))
                self.formelfrage_pool_qpl_file_path_template = os.path.normpath(os.path.join(self.formelfrage_files_path, "ff_pool_qti_und_qpl_dateien_vorlage", "ilias_pool_vorlage__qpl__.xml"))


                ##### Pfade für singlechoice #############################

                # Pfad für ILIAS-Test Vorlage
                self.singlechoice_test_qti_file_path_template = os.path.normpath(os.path.join(self.singlechoice_files_path, "sc_test_qti_und_tst_dateien_vorlage", "ilias_test_vorlage__qti__.xml"))
                self.singlechoice_test_tst_file_path_template = os.path.normpath(os.path.join(self.singlechoice_files_path, "sc_test_qti_und_tst_dateien_vorlage", "ilias_test_vorlage__tst__.xml"))

                # Pfad für ILIAS-Test Dateien (zum hochladen in ILIAS)
                self.singlechoice_test_qti_file_path_output = os.path.normpath(os.path.join(self.singlechoice_files_path, "sc_ilias_test_abgabe", "1604407426__0__tst_2040314", "1604407426__0__qti_2040314.xml"))
                self.singlechoice_test_tst_file_path_output = os.path.normpath(os.path.join(self.singlechoice_files_path, "sc_ilias_test_abgabe", "1604407426__0__tst_2040314", "1604407426__0__tst_2040314.xml"))
                self.singlechoice_test_img_file_path_output = os.path.normpath(os.path.join(self.singlechoice_files_path, "sc_ilias_test_abgabe", "1604407426__0__tst_2040314", "objects"))


                # Pfad für ILIAS-Pool Vorlage
                self.singlechoice_pool_qti_file_path_template = os.path.normpath(os.path.join(self.singlechoice_files_path, "sc_pool_qti_und_qpl_dateien_vorlage", "ilias_pool_vorlage__qti__.xml"))
                self.singlechoice_pool_qpl_file_path_template = os.path.normpath(os.path.join(self.singlechoice_files_path, "sc_pool_qti_und_qpl_dateien_vorlage", "ilias_pool_vorlage__qpl__.xml"))
                
                ##### Pfade für multiplechoice #############################

                # Pfad für ILIAS-Test Vorlage
                self.multiplechoice_test_qti_file_path_template = os.path.normpath(os.path.join(self.multiplechoice_files_path, "mc_test_qti_und_tst_dateien_vorlage", "ilias_test_vorlage__qti__.xml"))
                self.multiplechoice_test_tst_file_path_template = os.path.normpath(os.path.join(self.multiplechoice_files_path, "mc_test_qti_und_tst_dateien_vorlage", "ilias_test_vorlage__tst__.xml"))

                # Pfad für ILIAS-Test Dateien (zum hochladen in ILIAS)
                self.multiplechoice_test_qti_file_path_output = os.path.normpath(os.path.join(self.multiplechoice_files_path, "mc_ilias_test_abgabe", "1604407426__0__tst_2040314", "1604407426__0__qti_2040314.xml"))
                self.multiplechoice_test_tst_file_path_output = os.path.normpath(os.path.join(self.multiplechoice_files_path, "mc_ilias_test_abgabe", "1604407426__0__tst_2040314", "1604407426__0__tst_2040314.xml"))
                self.multiplechoice_test_img_file_path_output = os.path.normpath(os.path.join(self.multiplechoice_files_path, "mc_ilias_test_abgabe", "1604407426__0__tst_2040314", "objects"))


                # Pfad für ILIAS-Pool Vorlage
                self.multiplechoice_pool_qti_file_path_template = os.path.normpath(os.path.join(self.multiplechoice_files_path, "mc_pool_qti_und_qpl_dateien_vorlage", "ilias_pool_vorlage__qti__.xml"))
                self.multiplechoice_pool_qpl_file_path_template = os.path.normpath(os.path.join(self.multiplechoice_files_path, "mc_pool_qti_und_qpl_dateien_vorlage", "ilias_pool_vorlage__qpl__.xml"))
                
                
                ##### Pfade für zuordnungsfrage #############################

                # Pfad für ILIAS-Test Vorlage
                self.zuordnungsfrage_test_qti_file_path_template = os.path.normpath(os.path.join(self.zuordnungsfrage_files_path, "mq_test_qti_und_tst_dateien_vorlage", "ilias_test_vorlage__qti__.xml"))
                self.zuordnungsfrage_test_tst_file_path_template = os.path.normpath(os.path.join(self.zuordnungsfrage_files_path, "mq_test_qti_und_tst_dateien_vorlage", "ilias_test_vorlage__tst__.xml"))

                # Pfad für ILIAS-Test Dateien (zum hochladen in ILIAS)
                self.zuordnungsfrage_test_qti_file_path_output = os.path.normpath(os.path.join(self.zuordnungsfrage_files_path, "mq_ilias_test_abgabe", "1604407426__0__tst_2040314", "1604407426__0__qti_2040314.xml"))
                self.zuordnungsfrage_test_tst_file_path_output = os.path.normpath(os.path.join(self.zuordnungsfrage_files_path, "mq_ilias_test_abgabe", "1604407426__0__tst_2040314", "1604407426__0__tst_2040314.xml"))
                self.zuordnungsfrage_test_img_file_path_output = os.path.normpath(os.path.join(self.zuordnungsfrage_files_path, "mq_ilias_test_abgabe", "1604407426__0__tst_2040314", "objects"))


                # Pfad für ILIAS-Pool Vorlage
                self.zuordnungsfrage_pool_qti_file_path_template = os.path.normpath(os.path.join(self.zuordnungsfrage_files_path, "mq_pool_qti_und_qpl_dateien_vorlage", "ilias_pool_vorlage__qti__.xml"))
                self.zuordnungsfrage_pool_qpl_file_path_template = os.path.normpath(os.path.join(self.zuordnungsfrage_files_path, "mq_pool_qti_und_qpl_dateien_vorlage", "ilias_pool_vorlage__qpl__.xml"))
                
                
                
                ##### Pfade für gemischte Fragentypen ####################
                # Pfad für ILIAS-Test Vorlage
                self.gemischte_fragentypen_test_qti_file_path_template = os.path.normpath(os.path.join(self.gemischte_fragentypen_files_path, "mixed_test_qti_und_tst_dateien_vorlage", "ilias_test_vorlage__qti__.xml"))
                self.gemischte_fragentypen_test_tst_file_path_template = os.path.normpath(os.path.join(self.gemischte_fragentypen_files_path, "mixed_test_qti_und_tst_dateien_vorlage", "ilias_test_vorlage__tst__.xml"))

                # Pfad für ILIAS-Test Dateien (zum hochladen in ILIAS)
                self.gemischte_fragentypen_test_qti_file_path_output = os.path.normpath(os.path.join(self.gemischte_fragentypen_files_path, "mixed_ilias_test_abgabe", "1604407426__0__tst_2040314", "1604407426__0__qti_2040314.xml"))
                self.gemischte_fragentypen_test_tst_file_path_output = os.path.normpath(os.path.join(self.gemischte_fragentypen_files_path, "mixed_ilias_test_abgabe", "1604407426__0__tst_2040314", "1604407426__0__tst_2040314.xml"))
                self.gemischte_fragentypen_test_img_file_path_output = os.path.normpath(os.path.join(self.gemischte_fragentypen_files_path, "mixed_ilias_test_abgabe", "1604407426__0__tst_2040314", "objects"))


                # Pfad für ILIAS-Pool Vorlage
                self.gemischte_fragentypen_pool_qti_file_path_template = os.path.normpath(os.path.join(self.gemischte_fragentypen_files_path, "mixed_pool_qti_und_qpl_dateien_vorlage", "ilias_pool_vorlage__qti__.xml"))
                self.gemischte_fragentypen_pool_qpl_file_path_template = os.path.normpath(os.path.join(self.gemischte_fragentypen_files_path, "mixed_pool_qti_und_qpl_dateien_vorlage", "ilias_pool_vorlage__qpl__.xml"))

                


                ############### Pfad ende




        def create_test_or_pool(self, ilias_test_or_pool):
            # Daten aus DB abgreifen
            self.test_data = self.DBI.get_dbtemp_data()
            self.create_ilias_test_or_pool = ilias_test_or_pool
            self.qpl_file_path = ""
            self.tst_file_path = ""

            ###### Prüft, ob die zu erstellenden Fragen, von EINEM Fragentyp sind
            self.all_ff_questions_flag = 0
            self.all_sc_questions_flag = 0
            self.all_mc_questions_flag = 0
            self.all_mq_questions_flag = 0
            self.mixed_questions_flag = 0

            self.test_data_question_types = []



            for t in range(len(self.test_data)):
                self.test_data_question_types.append(self.test_data[t][2])



            # Zählt die Anzahl von "formelfrage" in testdaten
            # Ist die Zahl gleich der Länge der Liste, haben alle Fragen den gleichen Typ
            # "and self.test_data_question_types" prüft auf eine leere Liste
            # Wenn keine Fragen enthalten sind und keine Frage einen Fragentyp hat, wäre es ein falsches Ergebnis
            if self.test_data_question_types.count("formelfrage") == len(self.test_data_question_types) and self.test_data_question_types:
                self.all_ff_questions_flag = 1
                # höchste ID aus Ordner auslesen --  Wird benötigt um Pool-Ordner mit aufsteigender ID erstellen zu können
                self.max_id = XML_Interface.find_max_id_in_dir(self, self.formelfrage_files_path_pool_output, "formelfrage")


            elif self.test_data_question_types.count("singlechoice") == len(self.test_data_question_types) and self.test_data_question_types:
                self.all_sc_questions_flag = 1
                # höchste ID aus Ordner auslesen --  Wird benötigt um Pool-Ordner mit aufsteigender ID erstellen zu können
                self.max_id = XML_Interface.find_max_id_in_dir(self, self.singlechoice_files_path_pool_output, "singlechoice")

            elif self.test_data_question_types.count("multiplechoice") == len(self.test_data_question_types) and self.test_data_question_types:
                self.all_mc_questions_flag = 1
                # höchste ID aus Ordner auslesen --  Wird benötigt um Pool-Ordner mit aufsteigender ID erstellen zu können
                self.max_id = XML_Interface.find_max_id_in_dir(self, self.multiplechoice_files_path_pool_output, "multiplechoice")

            elif self.test_data_question_types.count("zuordnungsfrage") == len(self.test_data_question_types) and self.test_data_question_types:
                self.all_mq_questions_flag = 1
                # höchste ID aus Ordner auslesen --  Wird benötigt um Pool-Ordner mit aufsteigender ID erstellen zu können
                self.max_id = XML_Interface.find_max_id_in_dir(self, self.zuordnungsfrage_files_path_pool_output, "zuordnungsfrage")

            else:
                self.mixed_questions_flag = 1
                self.max_id = XML_Interface.find_max_id_in_dir(self, self.gemischte_fragentypen_files_path_pool_output, "gemischte_fragentypen")



            


            self.ilias_id_pool_qpl_dir = "1596569820__0__qpl_" + self.max_id
            self.ilias_id_pool_qpl_xml = "1596569820__0__qpl_" + self.max_id + ".xml"
            self.ilias_id_pool_qti_xml = "1596569820__0__qti_" + self.max_id + ".xml"

            self.formelfrage_pool_qti_file_path_output = os.path.normpath(os.path.join(self.formelfrage_files_path, "ff_ilias_pool_abgabe", "1596569820__0__qpl_" + str(self.max_id), self.ilias_id_pool_qti_xml))
            self.formelfrage_pool_qpl_file_path_output = os.path.normpath(os.path.join(self.formelfrage_files_path, "ff_ilias_pool_abgabe", "1596569820__0__qpl_" + str(self.max_id), self.ilias_id_pool_qpl_xml))
            self.formelfrage_pool_img_file_path_output        = os.path.normpath(os.path.join(self.formelfrage_files_path, "ff_ilias_pool_abgabe", "1596569820__0__qpl_" + str(self.max_id), "objects"))

            self.singlechoice_pool_qti_file_path_output = os.path.normpath(os.path.join(self.singlechoice_files_path, "sc_ilias_pool_abgabe", "1596569820__0__qpl_" + str(self.max_id), self.ilias_id_pool_qti_xml))
            self.singlechoice_pool_qpl_file_path_output = os.path.normpath(os.path.join(self.singlechoice_files_path, "sc_ilias_pool_abgabe", "1596569820__0__qpl_" + str(self.max_id), self.ilias_id_pool_qpl_xml))
            self.singlechoice_pool_img_file_path_output        = os.path.normpath(os.path.join(self.singlechoice_files_path, "sc_ilias_pool_abgabe", "1596569820__0__qpl_" + str(self.max_id), "objects"))
            
            self.multiplechoice_pool_qti_file_path_output = os.path.normpath(os.path.join(self.multiplechoice_files_path, "mc_ilias_pool_abgabe", "1596569820__0__qpl_" + str(self.max_id), self.ilias_id_pool_qti_xml))
            self.multiplechoice_pool_qpl_file_path_output = os.path.normpath(os.path.join(self.multiplechoice_files_path, "mc_ilias_pool_abgabe", "1596569820__0__qpl_" + str(self.max_id), self.ilias_id_pool_qpl_xml))
            self.multiplechoice_pool_img_file_path_output        = os.path.normpath(os.path.join(self.multiplechoice_files_path, "mc_ilias_pool_abgabe", "1596569820__0__qpl_" + str(self.max_id), "objects"))
            
            self.zuordnungsfrage_pool_qti_file_path_output = os.path.normpath(os.path.join(self.zuordnungsfrage_files_path, "mq_ilias_pool_abgabe", "1596569820__0__qpl_" + str(self.max_id), self.ilias_id_pool_qti_xml))
            self.zuordnungsfrage_pool_qpl_file_path_output = os.path.normpath(os.path.join(self.zuordnungsfrage_files_path, "mq_ilias_pool_abgabe", "1596569820__0__qpl_" + str(self.max_id), self.ilias_id_pool_qpl_xml))
            self.zuordnungsfrage_pool_img_file_path_output        = os.path.normpath(os.path.join(self.zuordnungsfrage_files_path, "mq_ilias_pool_abgabe", "1596569820__0__qpl_" + str(self.max_id), "objects"))

            self.gemischte_fragentypen_pool_qti_file_path_output = os.path.normpath(os.path.join(self.gemischte_fragentypen_files_path, "mixed_ilias_pool_abgabe", "1596569820__0__qpl_" + str(self.max_id), self.ilias_id_pool_qti_xml))
            self.gemischte_fragentypen_pool_qpl_file_path_output = os.path.normpath(os.path.join(self.gemischte_fragentypen_files_path, "mixed_ilias_pool_abgabe", "1596569820__0__qpl_" + str(self.max_id), self.ilias_id_pool_qpl_xml))
            self.gemischte_fragentypen_pool_img_file_path_output        = os.path.normpath(os.path.join(self.gemischte_fragentypen_files_path, "mixed_ilias_pool_abgabe", "1596569820__0__qpl_" + str(self.max_id), "objects"))


            # Wenn ein Test erstellt wird, ist der Pfad fix
            #Bei einem Pool, wird die ID hochgezählt



            if self.create_ilias_test_or_pool == "ilias_test":
                if self.all_ff_questions_flag == 1:
                    self.qti_file_path_output = self.formelfrage_test_qti_file_path_output
                    self.img_file_path_output = self.formelfrage_test_img_file_path_output
                    self.ff_mytree = ET.parse(self.formelfrage_test_qti_file_path_template)
                    self.tst_file_path = self.formelfrage_test_tst_file_path_output
                
                elif self.all_sc_questions_flag == 1:
                    self.qti_file_path_output = self.singlechoice_test_qti_file_path_output
                    self.img_file_path_output = self.singlechoice_test_img_file_path_output
                    self.ff_mytree = ET.parse(self.singlechoice_test_qti_file_path_template)
                    self.tst_file_path = self.singlechoice_test_tst_file_path_output
                    
                elif self.all_mc_questions_flag == 1:
                    self.qti_file_path_output = self.multiplechoice_test_qti_file_path_output
                    self.img_file_path_output = self.multiplechoice_test_img_file_path_output
                    self.ff_mytree = ET.parse(self.multiplechoice_test_qti_file_path_template)
                    self.tst_file_path = self.multiplechoice_test_tst_file_path_output

                elif self.all_mq_questions_flag == 1:
                    self.qti_file_path_output = self.zuordnungsfrage_test_qti_file_path_output
                    self.ff_mytree = ET.parse(self.zuordnungsfrage_test_qti_file_path_template)

                    self.img_file_path_output = self.zuordnungsfrage_test_img_file_path_output
                    self.tst_file_path = self.zuordnungsfrage_test_tst_file_path_output
                
                else:
                    self.qti_file_path_output = self.gemischte_fragentypen_test_qti_file_path_output
                    self.img_file_path_output = self.gemischte_fragentypen_test_img_file_path_output
                    self.ff_mytree = ET.parse(self.gemischte_fragentypen_test_qti_file_path_template)
                    self.tst_file_path = self.gemischte_fragentypen_test_tst_file_path_output

            elif self.create_ilias_test_or_pool == "ilias_pool":
                if self.all_ff_questions_flag == 1:
                    print("-------------- FF ------------")
                    self.qti_file_path_output = self.formelfrage_pool_qti_file_path_output
                    XML_Interface.create_pool_dir_from_template(self, self.formelfrage_files_path_pool_output)
                    self.ff_mytree = ET.parse(self.formelfrage_pool_qti_file_path_template)

                    self.pool_qpl_file_path_template = self.formelfrage_pool_qpl_file_path_template
                    self.pool_qpl_file_path_output = self.formelfrage_pool_qpl_file_path_output
                    self.qpl_file_path = self.formelfrage_pool_qpl_file_path_output
                    self.img_file_path_output = self.formelfrage_pool_img_file_path_output

                elif self.all_sc_questions_flag == 1:
                    print("-------------- SC ------------")
                    self.qti_file_path_output = self.singlechoice_pool_qti_file_path_output
                    XML_Interface.create_pool_dir_from_template(self, self.singlechoice_files_path_pool_output)
                    self.ff_mytree = ET.parse(self.singlechoice_pool_qti_file_path_template)

                    self.pool_qpl_file_path_template = self.singlechoice_pool_qpl_file_path_template
                    self.pool_qpl_file_path_output = self.singlechoice_pool_qpl_file_path_output
                    self.qpl_file_path = self.singlechoice_pool_qpl_file_path_output
                    self.img_file_path_output = self.singlechoice_pool_img_file_path_output
                    
                elif self.all_mc_questions_flag == 1:
                    print("-------------- MC ------------")
                    self.qti_file_path_output = self.multiplechoice_pool_qti_file_path_output
                    XML_Interface.create_pool_dir_from_template(self, self.multiplechoice_files_path_pool_output)
                    self.ff_mytree = ET.parse(self.multiplechoice_pool_qti_file_path_template)

                    self.pool_qpl_file_path_template = self.multiplechoice_pool_qpl_file_path_template
                    self.pool_qpl_file_path_output = self.multiplechoice_pool_qpl_file_path_output
                    self.qpl_file_path = self.multiplechoice_pool_qpl_file_path_output
                    self.img_file_path_output = self.multiplechoice_pool_img_file_path_output
                    
                elif self.all_mq_questions_flag == 1:
                    print("-------------- MQ ------------")
                    self.qti_file_path_output = self.zuordnungsfrage_pool_qti_file_path_output
                    XML_Interface.create_pool_dir_from_template(self, self.zuordnungsfrage_files_path_pool_output)
                    self.ff_mytree = ET.parse(self.zuordnungsfrage_pool_qti_file_path_template)

                    self.pool_qpl_file_path_template = self.zuordnungsfrage_pool_qpl_file_path_template
                    self.pool_qpl_file_path_output = self.zuordnungsfrage_pool_qpl_file_path_output
                    self.qpl_file_path = self.zuordnungsfrage_pool_qpl_file_path_output
                    self.img_file_path_output = self.zuordnungsfrage_pool_img_file_path_output

                else:
                    print("-------------- MIXED ------------")
                    self.qti_file_path_output = self.gemischte_fragentypen_pool_qti_file_path_output
                    XML_Interface.create_pool_dir_from_template(self, self.gemischte_fragentypen_files_path_pool_output)
                    self.ff_mytree = ET.parse(self.gemischte_fragentypen_pool_qti_file_path_template)

                    self.pool_qpl_file_path_template = self.gemischte_fragentypen_pool_qpl_file_path_template
                    self.pool_qpl_file_path_output = self.gemischte_fragentypen_pool_qpl_file_path_output
                    self.qpl_file_path = self.gemischte_fragentypen_pool_qpl_file_path_output
                    self.img_file_path_output = self.gemischte_fragentypen_pool_img_file_path_output


            self.ff_myroot = self.ff_mytree.getroot()
            self.id_nr = 0

            # Fragen in die XML schreiben
            for i in range(len(self.test_data)):


                if self.test_data[i][2].lower() == "formelfrage":
                    XML_Interface.ff_question_structure(self, self.test_data[i], self.table_index_dict, self.id_nr, self.pool_qpl_file_path_template, self.pool_qpl_file_path_output, self.img_file_path_output, False)

                if self.test_data[i][2].lower() == "singlechoice":
                   XML_Interface.sc_question_structure(self, self.test_data[i], self.table_index_dict, self.id_nr, self.pool_qpl_file_path_template, self.pool_qpl_file_path_output,  self.img_file_path_output)

                if self.test_data[i][2].lower() == "multiplechoice":
                   XML_Interface.mc_question_structure(self, self.test_data[i], self.table_index_dict, self.id_nr, self.pool_qpl_file_path_template, self.pool_qpl_file_path_output,  self.img_file_path_output)
                
                if self.test_data[i][2].lower() == "zuordnungsfrage":
                   XML_Interface.mq_question_structure(self, self.test_data[i], self.table_index_dict, self.id_nr, self.pool_qpl_file_path_template, self.pool_qpl_file_path_output,  self.img_file_path_output)

                if self.test_data[i][2].lower() == "formelfrage_permutation":
                    XML_Interface.ff_question_structure(self, self.test_data[i], self.table_index_dict, self.id_nr, self.pool_qpl_file_path_template, self.pool_qpl_file_path_output, self.img_file_path_output, True)


                if self.create_ilias_test_or_pool == "ilias_pool":

                    ######  Anpassung der Datei "qpl". Akualisierung des Dateinamens
                    self.mytree = ET.parse(self.qpl_file_path)
                    self.myroot = self.mytree.getroot()

                    for ident_id in self.myroot.iter('Identifier'):
                        ident_id.set('Entry', "il_0_qpl_" + str(self.max_id+str(1)))
                    self.mytree.write(self.qpl_file_path)





                self.id_nr += 1

            # Beschriebene XML im Pfad "self.qti_file_path_output" schreiben
            print(self.qti_file_path_output)
            self.ff_mytree.write(self.qti_file_path_output)
            print("TEST DONE")
            XML_Interface.replace_amp_in_xml_file(self, self.qti_file_path_output)
            


        ###### FORMELFRAGE FUNKTIONEN ################
        def ff_question_structure(self, test_data_list, table_index_dict, id_nr, pool_qpl_file_path_template , pool_qpl_file_path_output, img_file_path, activate_permutation):
                """Diese Funktion wandelt die SQL-Einträge in die .xml um, welche anschließend in ILIAS eingespielt werden kann"""


                self.pool_qpl_file_path_template = pool_qpl_file_path_template
                self.pool_qpl_file_path_output = pool_qpl_file_path_output

                self.img_file_path_output = img_file_path
                self.activate_permutation = activate_permutation

                self.perm_values_list = []

                print("PERMUTATION:", self.activate_permutation)
                print("===========")
                print(self.test_data[0][self.table_index_dict[4]['perm_var_value_1']])
                print(self.test_data[0][self.table_index_dict[4]['perm_var_symbol_1']])
                print("===========")



                if self.activate_permutation is False:
                    self.table_index = 0
                    self.perm_values_list = ["1"]

                # Wenn Permutation aktiv, dann muss Index "4" verwendet werden
                else:
                    self.table_index = 4
                    # String zu Liste konvertieren (komma getrennt)
                    self.perm_values_list = list(self.test_data[0][self.table_index_dict[4]['perm_var_value_1']].split(','))

                for i in range(len(self.perm_values_list)):
                    #self.ff_question_description_main = test_generator_modul_taxonomie_und_textformatierung.Textformatierung.format_description_text_in_xml(self, self.ff_var_use_latex_on_text_check.get(), test_data_list[table_index_dict[0]['question_description_main']])
                    # Abfrage LATEX fehlt
                    self.ff_question_description_main = XML_Interface.format_description_text_in_xml(self, test_data_list[table_index_dict[self.table_index]['question_description_main']])

                    if self.activate_permutation is True:
                        self.ff_question_description_main = self.ff_question_description_main.replace(self.test_data[0][self.table_index_dict[4]['perm_var_symbol_1']], self.perm_values_list[i])
                        print("////////////")

                        print(self.test_data[0][self.table_index_dict[4]['perm_var_symbol_1']])
                        print( self.perm_values_list[i])
                        print("////////////")

                    # Aufbau für  Fragenstruktur "TEST"
                    if self.create_ilias_test_or_pool == "ilias_test":
                        # XML Struktur aus XML Datei festlegen. Muss nur einmal angelegt werden
                        questestinterop = ET.Element('questestinterop')
                        assessment = ET.SubElement(questestinterop, 'assessment')
                        section = ET.SubElement(assessment, 'section')
                        item = ET.SubElement(section, 'item')

                    # Aufbau für  Fragenstruktur "POOL"
                    else:
                        # XML Struktur aus XML Datei festlegen. Muss nur einmal angelegt werden
                        questestinterop = ET.Element('questestinterop')
                        item = ET.SubElement(questestinterop, 'item')

                        # Zusatz für Taxonomie-Einstellungen

                        XML_Interface.set_taxonomy_for_question(self,
                                                               id_nr,
                                                               self.number_of_entrys,
                                                               item,
                                                               self.pool_qpl_file_path_template,
                                                               self.pool_qpl_file_path_output
                                                               )



                    # Struktur für den Formelfragen - Variableen/Lösungen Teil
                    # Muss für jede Frage neu angelegt/hinzugefügt werden
                    qticomment = ET.SubElement(item, 'qticomment')
                    duration = ET.SubElement(item, 'duration')
                    itemmetadata = ET.SubElement(item, 'itemmetadata')
                    presentation = ET.SubElement(item, 'presentation')

                    flow = ET.SubElement(presentation, 'flow')
                    question_description_material = ET.SubElement(flow, 'material')
                    question_description_mattext = ET.SubElement(question_description_material, 'mattext')
                    qtimetadata = ET.SubElement(itemmetadata, 'qtimetadata')


                    ### ------------------------------------------------------- XML Einträge mit Werten füllen
                     # Fragen-Titel -- "item title" in xml
                    item.set('title', test_data_list[table_index_dict[self.table_index]['question_title']])

                    # Fragen-Titel Beschreibung
                    qticomment.text = test_data_list[table_index_dict[self.table_index]['question_description_title']]

                    # Testdauer -- "duration" in xml
                    # wird keine Testzeit eingetragen, wird 1h vorausgewählt
                    duration.text = test_data_list[table_index_dict[self.table_index]['test_time']]
                    if duration.text == "":
                        duration.text = "P0Y0M0DT23H0M0S"

                    # -----------------------------------------------------------------------ILIAS VERSION
                    qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
                    fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
                    fieldlabel.text = "ILIAS_VERSION"
                    fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
                    fieldentry.text = "5.4.10 2020-03-04"
                    # -----------------------------------------------------------------------QUESTIONTYPE
                    qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
                    fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
                    fieldlabel.text = "QUESTIONTYPE"
                    fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
                    fieldentry.text = "assFormulaQuestion"
                    # -----------------------------------------------------------------------AUTHOR
                    qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
                    fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
                    fieldlabel.text = "AUTHOR"
                    fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
                    fieldentry.text = test_data_list[table_index_dict[self.table_index]['question_author']]
                    # -----------------------------------------------------------------------POINTS
                    qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
                    fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
                    fieldlabel.text = "points"
                    fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
                    fieldentry.text = str(test_data_list[table_index_dict[self.table_index]['res1_points']])

                    # Fragentitel einsetzen -- "presentation label" in xml
                    presentation.set('label', test_data_list[table_index_dict[self.table_index]['question_title']])

                    # Fragen-Text (Format) einsetzen -- "mattext_texttype" in xml -- Gibt das Format des Textes an
                    question_description_mattext.set('texttype', "text/html")

                    # Fragen-Text (Text) einsetzen   -- "mattext_texttype" in xml -- Gibt die eigentliche Fragen-Beschreibung an
                    # Wenn Bild enthalten ist, dann in Fragenbeschreibung einbetten
                    question_description_mattext.text = XML_Interface.add_picture_to_description_main(
                                                        self,
                                                        test_data_list[table_index_dict[self.table_index]['description_img_path_1']],
                                                        test_data_list[table_index_dict[self.table_index]['description_img_path_2']],
                                                        test_data_list[table_index_dict[self.table_index]['description_img_path_3']],
                                                        self.img_file_path_output,
                                                        self.ff_question_description_main, question_description_mattext, question_description_material, id_nr)




                    # ----------------------------------------------------------------------- Variable
                    XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v1", test_data_list[table_index_dict[self.table_index]['var1_min']], test_data_list[table_index_dict[self.table_index]['var1_max']], test_data_list[table_index_dict[self.table_index]['var1_prec']], test_data_list[table_index_dict[self.table_index]['var1_divby']], test_data_list[table_index_dict[self.table_index]['var1_unit']])
                    XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v2", test_data_list[table_index_dict[self.table_index]['var2_min']], test_data_list[table_index_dict[self.table_index]['var2_max']], test_data_list[table_index_dict[self.table_index]['var2_prec']], test_data_list[table_index_dict[self.table_index]['var2_divby']], test_data_list[table_index_dict[self.table_index]['var2_unit']])
                    XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v3", test_data_list[table_index_dict[self.table_index]['var3_min']], test_data_list[table_index_dict[self.table_index]['var3_max']], test_data_list[table_index_dict[self.table_index]['var3_prec']], test_data_list[table_index_dict[self.table_index]['var3_divby']], test_data_list[table_index_dict[self.table_index]['var3_unit']])
                    XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v4", test_data_list[table_index_dict[self.table_index]['var4_min']], test_data_list[table_index_dict[self.table_index]['var4_max']], test_data_list[table_index_dict[self.table_index]['var4_prec']], test_data_list[table_index_dict[self.table_index]['var4_divby']], test_data_list[table_index_dict[self.table_index]['var4_unit']])
                    XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v5", test_data_list[table_index_dict[self.table_index]['var5_min']], test_data_list[table_index_dict[self.table_index]['var5_max']], test_data_list[table_index_dict[self.table_index]['var5_prec']], test_data_list[table_index_dict[self.table_index]['var5_divby']], test_data_list[table_index_dict[self.table_index]['var6_unit']])
                    XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v6", test_data_list[table_index_dict[self.table_index]['var6_min']], test_data_list[table_index_dict[self.table_index]['var6_max']], test_data_list[table_index_dict[self.table_index]['var6_prec']], test_data_list[table_index_dict[self.table_index]['var6_divby']], test_data_list[table_index_dict[self.table_index]['var1_unit']])
                    XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v7", test_data_list[table_index_dict[self.table_index]['var7_min']], test_data_list[table_index_dict[self.table_index]['var7_max']], test_data_list[table_index_dict[self.table_index]['var7_prec']], test_data_list[table_index_dict[self.table_index]['var7_divby']], test_data_list[table_index_dict[self.table_index]['var7_unit']])
                    XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v8", test_data_list[table_index_dict[self.table_index]['var8_min']], test_data_list[table_index_dict[self.table_index]['var8_max']], test_data_list[table_index_dict[self.table_index]['var8_prec']], test_data_list[table_index_dict[self.table_index]['var8_divby']], test_data_list[table_index_dict[self.table_index]['var8_unit']])
                    XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v9", test_data_list[table_index_dict[self.table_index]['var9_min']], test_data_list[table_index_dict[self.table_index]['var9_max']], test_data_list[table_index_dict[self.table_index]['var9_prec']], test_data_list[table_index_dict[self.table_index]['var9_divby']], test_data_list[table_index_dict[self.table_index]['var9_unit']])
                    XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v10", test_data_list[table_index_dict[self.table_index]['var10_min']], test_data_list[table_index_dict[self.table_index]['var10_max']], test_data_list[table_index_dict[self.table_index]['var10_prec']], test_data_list[table_index_dict[self.table_index]['var10_divby']], test_data_list[table_index_dict[self.table_index]['var10_unit']])
                    XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v11", test_data_list[table_index_dict[self.table_index]['var11_min']], test_data_list[table_index_dict[self.table_index]['var11_max']], test_data_list[table_index_dict[self.table_index]['var11_prec']], test_data_list[table_index_dict[self.table_index]['var11_divby']], test_data_list[table_index_dict[self.table_index]['var11_unit']])
                    XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v12", test_data_list[table_index_dict[self.table_index]['var12_min']], test_data_list[table_index_dict[self.table_index]['var12_max']], test_data_list[table_index_dict[self.table_index]['var12_prec']], test_data_list[table_index_dict[self.table_index]['var12_divby']], test_data_list[table_index_dict[self.table_index]['var12_unit']])
                    XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v13", test_data_list[table_index_dict[self.table_index]['var13_min']], test_data_list[table_index_dict[self.table_index]['var13_max']], test_data_list[table_index_dict[self.table_index]['var13_prec']], test_data_list[table_index_dict[self.table_index]['var13_divby']], test_data_list[table_index_dict[self.table_index]['var13_unit']])
                    XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v14", test_data_list[table_index_dict[self.table_index]['var14_min']], test_data_list[table_index_dict[self.table_index]['var14_max']], test_data_list[table_index_dict[self.table_index]['var14_prec']], test_data_list[table_index_dict[self.table_index]['var14_divby']], test_data_list[table_index_dict[self.table_index]['var14_unit']])
                    XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v15", test_data_list[table_index_dict[self.table_index]['var15_min']], test_data_list[table_index_dict[self.table_index]['var15_max']], test_data_list[table_index_dict[self.table_index]['var15_prec']], test_data_list[table_index_dict[self.table_index]['var15_divby']], test_data_list[table_index_dict[self.table_index]['var15_unit']])


                    # ----------------------------------------------------------------------- Solution

                    XML_Interface.ff_question_results_structure(self, qtimetadata, "$r1", test_data_list[table_index_dict[self.table_index]['res1_formula']], test_data_list[table_index_dict[self.table_index]['res1_min']], test_data_list[table_index_dict[self.table_index]['res1_max']], test_data_list[table_index_dict[self.table_index]['res1_prec']], test_data_list[table_index_dict[self.table_index]['res1_tol']], test_data_list[table_index_dict[self.table_index]['res1_points']], test_data_list[table_index_dict[self.table_index]['res1_unit']], i)
                    XML_Interface.ff_question_results_structure(self, qtimetadata, "$r2", test_data_list[table_index_dict[self.table_index]['res2_formula']], test_data_list[table_index_dict[self.table_index]['res2_min']], test_data_list[table_index_dict[self.table_index]['res2_max']], test_data_list[table_index_dict[self.table_index]['res2_prec']], test_data_list[table_index_dict[self.table_index]['res2_tol']], test_data_list[table_index_dict[self.table_index]['res2_points']], test_data_list[table_index_dict[self.table_index]['res2_unit']], i)
                    XML_Interface.ff_question_results_structure(self, qtimetadata, "$r3", test_data_list[table_index_dict[self.table_index]['res3_formula']], test_data_list[table_index_dict[self.table_index]['res3_min']], test_data_list[table_index_dict[self.table_index]['res3_max']], test_data_list[table_index_dict[self.table_index]['res3_prec']], test_data_list[table_index_dict[self.table_index]['res3_tol']], test_data_list[table_index_dict[self.table_index]['res3_points']], test_data_list[table_index_dict[self.table_index]['res3_unit']], i)
                    XML_Interface.ff_question_results_structure(self, qtimetadata, "$r4", test_data_list[table_index_dict[self.table_index]['res4_formula']], test_data_list[table_index_dict[self.table_index]['res4_min']], test_data_list[table_index_dict[self.table_index]['res4_max']], test_data_list[table_index_dict[self.table_index]['res4_prec']], test_data_list[table_index_dict[self.table_index]['res4_tol']], test_data_list[table_index_dict[self.table_index]['res4_points']], test_data_list[table_index_dict[self.table_index]['res4_unit']], i)
                    XML_Interface.ff_question_results_structure(self, qtimetadata, "$r5", test_data_list[table_index_dict[self.table_index]['res5_formula']], test_data_list[table_index_dict[self.table_index]['res5_min']], test_data_list[table_index_dict[self.table_index]['res5_max']], test_data_list[table_index_dict[self.table_index]['res5_prec']], test_data_list[table_index_dict[self.table_index]['res5_tol']], test_data_list[table_index_dict[self.table_index]['res5_points']], test_data_list[table_index_dict[self.table_index]['res5_unit']], i)
                    XML_Interface.ff_question_results_structure(self, qtimetadata, "$r6", test_data_list[table_index_dict[self.table_index]['res6_formula']], test_data_list[table_index_dict[self.table_index]['res6_min']], test_data_list[table_index_dict[self.table_index]['res6_max']], test_data_list[table_index_dict[self.table_index]['res6_prec']], test_data_list[table_index_dict[self.table_index]['res6_tol']], test_data_list[table_index_dict[self.table_index]['res6_points']], test_data_list[table_index_dict[self.table_index]['res6_unit']], i)
                    XML_Interface.ff_question_results_structure(self, qtimetadata, "$r7", test_data_list[table_index_dict[self.table_index]['res7_formula']], test_data_list[table_index_dict[self.table_index]['res7_min']], test_data_list[table_index_dict[self.table_index]['res7_max']], test_data_list[table_index_dict[self.table_index]['res7_prec']], test_data_list[table_index_dict[self.table_index]['res7_tol']], test_data_list[table_index_dict[self.table_index]['res7_points']], test_data_list[table_index_dict[self.table_index]['res7_unit']], i)
                    XML_Interface.ff_question_results_structure(self, qtimetadata, "$r8", test_data_list[table_index_dict[self.table_index]['res8_formula']], test_data_list[table_index_dict[self.table_index]['res8_min']], test_data_list[table_index_dict[self.table_index]['res8_max']], test_data_list[table_index_dict[self.table_index]['res8_prec']], test_data_list[table_index_dict[self.table_index]['res8_tol']], test_data_list[table_index_dict[self.table_index]['res8_points']], test_data_list[table_index_dict[self.table_index]['res8_unit']], i)
                    XML_Interface.ff_question_results_structure(self, qtimetadata, "$r9", test_data_list[table_index_dict[self.table_index]['res9_formula']], test_data_list[table_index_dict[self.table_index]['res9_min']], test_data_list[table_index_dict[self.table_index]['res9_max']], test_data_list[table_index_dict[self.table_index]['res9_prec']], test_data_list[table_index_dict[self.table_index]['res9_tol']], test_data_list[table_index_dict[self.table_index]['res9_points']], test_data_list[table_index_dict[self.table_index]['res9_unit']], i)
                    XML_Interface.ff_question_results_structure(self, qtimetadata, "$r10", test_data_list[table_index_dict[self.table_index]['res10_formula']], test_data_list[table_index_dict[self.table_index]['res10_min']], test_data_list[table_index_dict[self.table_index]['res10_max']], test_data_list[table_index_dict[self.table_index]['res10_prec']], test_data_list[table_index_dict[self.table_index]['res10_tol']], test_data_list[table_index_dict[self.table_index]['res10_points']], test_data_list[table_index_dict[self.table_index]['res10_unit']], i)








                    # -----------------------------------------------------------------------ADDITIONAL_CONT_EDIT_MODE
                    qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
                    fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
                    fieldlabel.text = "additional_cont_edit_mode"
                    fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
                    fieldentry.text = "default"
                    # -----------------------------------------------------------------------EXTERNAL_ID
                    qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
                    fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
                    fieldlabel.text = "externalId"
                    fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
                    fieldentry.text = "5ea15be69c1e96.43933468"



                    # Wenn es sich um einen ILIAS-Test handelt, beinhaltet die XML eine Struktur mit mehreren "Zweigen"
                    # Der letzte "Zweig" --> "len(self.ff_myroot[0]) - 1" (beschreibt das letze Fach) beinhaltet die eigentlichen Fragen
                    if self.create_ilias_test_or_pool == "ilias_test":
                        self.ff_myroot[0][len(self.ff_myroot[0]) - 1].append(item)

                    # Wenn es sich um einen ILIAS-Pool handelt, beinhaltet die XML keine Struktur
                    # Die Frage kann einfach angehangen werden
                    else:
                        self.ff_myroot.append(item)







                    print(str(id_nr) + ".) Formelfrage Frage erstellt! ---> Titel: " + test_data_list[table_index_dict[0]['question_title']])
                    print(question_description_mattext.text)

                    print("\n")





        def ff_question_variables_structure(self, xml_qtimetadata,  ff_var_name, ff_var_min, ff_var_max, ff_var_prec, ff_var_divby, ff_var_unit):

                # <------------ INIT ----------->
                self.ff_var_name = ff_var_name
                self.ff_var_min = str(ff_var_min)
                self.ff_var_max = str(ff_var_max)
                self.ff_var_prec = str(ff_var_prec)
                self.ff_var_divby = str(ff_var_divby)
                self.ff_var_divby_length = len(str(self.ff_var_divby))
                self.ff_var_unit = ff_var_unit
                self.ff_var_unit_length = len(str(self.ff_var_unit))

                # <------------ FORMELFRAGE VARIABLEN STRUKTUR (in XML) ----------->
                qtimetadatafield = ET.SubElement(xml_qtimetadata, 'qtimetadatafield')
                fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
                fieldlabel.text = ff_var_name
                fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')



                # Festlegen VARIABLE-Werte
                fieldentry.text = "a:6:{" \
                              "s:9:\"precision\";i:" + str(self.ff_var_prec) + ";" \
                              "s:12:\"intprecision\";s:" + str(self.ff_var_divby_length) + ":\"" + str(self.ff_var_divby) + "\";" \
                              "s:8:\"rangemin\";d:" + str(self.ff_var_min) + ";" \
                              "s:8:\"rangemax\";d:" + str(self.ff_var_max) + ";" \
                              "s:4:\"unit\";s:0:\"\";" \
                              "s:9:\"unitvalue\";s:0:\"\";" \
                              "}"

        def ff_question_results_structure(self, xml_qtimetadata, ff_res_name, ff_res_formula, ff_res_min, ff_res_max, ff_res_prec, ff_res_tol, ff_res_points, ff_res_unit, i):

                def replace_words_in_formula(formula):

                    self.replace_words_dict = {
                        "$V": "$v",
                        "$R": "$r",
                        "=": " ",
                        "SIN": "sin",
                        "SINH": "sinh",
                        "ARCSIN": "arcsin",
                        "ASIN": "asin",
                        "ARCSINH": "arcsinh",
                        "ASINH": "asinh",
                        "COS": "cos",
                        "COSH": "cosh",
                        "ARCCOS": "arccos",
                        "ACOS": "acos",
                        "ARCCOSH": "arccosh",
                        "ACOSH": "acosh",
                        "TAN": "tan",
                        "TANH": "tanh",
                        "ARCTAN": "arctan",
                        "ATAN": "atan",
                        "ARCTANH": "arctanh",
                        "ATANH": "atanh",
                        "SQRT": "sqrt",
                        "Wurzel": "sqrt",
                        "wurzel": "sqrt",
                        "ABS": "abs",
                        "LN": "ln",
                        "LOG": "log"
                    }

                    formula = ' '.join([self.replace_words_dict.get(i,i) for i in formula.split()])

                    return formula

                # <------------ INIT ----------->
                self.ff_res_name = ff_res_name
                self.ff_res_formula = ff_res_formula
                self.ff_res_formula_length = len(str(self.ff_res_formula))
                self.ff_res_min = str(ff_res_min)
                self.ff_res_min_length = len(str(self.ff_res_min))
                self.ff_res_max = str(ff_res_max)
                self.ff_res_max_length = len(str(self.ff_res_max))
                self.ff_res_prec = str(ff_res_prec)
                self.ff_res_tol = str(ff_res_tol)
                self.ff_res_tol_length = len(str(self.ff_res_tol))

                self.ff_res_points = str(ff_res_points)
                self.ff_res_points_length = len(str(ff_res_points))
                self.ff_res_unit = ff_res_unit
                self.ff_res_unit_length = len(str(self.ff_res_unit))




                # ILIAS kann nicht mit "$Vx" statt "$vx" oder "$Rx" statt "$rx"  umgehen (kleines statt großes "V" für Variablen)
                # In der Ergebnisgleichung darf kein "=" verwendet werden! Es erscheint keine Fehlermeldung, jedoch werden die Ergebnisse
                # aus der ILIAS-Berechnung immer auf "0" gesetzt
                if self.activate_permutation is False:
                    self.ff_res_formula = replace_words_in_formula(self.ff_res_formula)

                # Wenn Permutation aktiv, dann Formeln
                else:
                    self.ff_res_formula = self.ff_res_formula.replace(self.test_data[0][self.table_index_dict[4]['perm_var_symbol_1']],self.perm_values_list[i])






                # <------------ FORMELFRAGE ERGEBNIS STRUKTUR (in XML)  ----------->
                # Hier wird die Struktur des Ergebnis-Teils (z.B. $r1) in XML geschrieben
                # Wenn der Ergebnisteil mit Einheiten verwendet wird, müssen entsprechend Daten in "resultunits" eingetragen werden
                # s for string length: "9" -> precision = "9" characters
                # rangemin: "s" for read string-like type --> "10*1000"

                qtimetadatafield = ET.SubElement(xml_qtimetadata, 'qtimetadatafield')
                fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
                fieldlabel.text = self.ff_res_name
                fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')


                # Festlegen RESULT Werte
                fieldentry.text = "a:10:{" \
                              "s:9:\"precision\";i:" + self.ff_res_prec           + ";" \
                              "s:9:\"tolerance\";s:" + str(self.ff_res_tol_length)     + ":\"" + self.ff_res_tol + "\";" \
                              "s:8:\"rangemin\";s:"  + str(self.ff_res_min_length)     + ":\"" + self.ff_res_min + "\";" \
                              "s:8:\"rangemax\";s:"  + str(self.ff_res_max_length)     + ":\"" + self.ff_res_max + "\";" \
                              "s:6:\"points\";s:"    + str(self.ff_res_points_length)  + ":\"" + self.ff_res_points + "\";" \
                              "s:7:\"formula\";s:"   + str(self.ff_res_formula_length) + ":\"" + self.ff_res_formula + "\";" \
                              "s:6:\"rating\";s:0:\"\";" \
                              "s:4:\"unit\";s:0:\"\";" \
                              "s:9:\"unitvalue\";s:0:\"\";" \
                              "s:11:\"resultunits\";a:0:{}" \
                              "}"

                print("ff_result_structure", self.ff_res_formula)

        ###### SINGLECHOICE FUNKTIONEN ##############

        def sc_question_structure(self, test_data_list, table_index_dict, id_nr, pool_qpl_file_path_template , pool_qpl_file_path_output, img_file_path):
            """Diese Funktion wandelt die SQL-Einträge in die .xml um, welche anschließend in ILIAS eingespielt werden kann"""

            self.pool_qpl_file_path_template = pool_qpl_file_path_template
            self.pool_qpl_file_path_output = pool_qpl_file_path_output

            self.img_file_path_output = img_file_path

            #self.sc_question_description_main = test_generator_modul_taxonomie_und_textformatierung.Textformatierung.format_description_text_in_xml(self, self.sc_var_use_latex_on_text_check.get(), self.sc_question_description_main)

            self.sc_question_description_main =XML_Interface.format_description_text_in_xml(self, test_data_list[table_index_dict[1]['question_description_main']])


            
            # Aufbau für  Fragenstruktur "TEST"
            if self.create_ilias_test_or_pool == "ilias_test":
                # XML Struktur aus XML Datei festlegen. Muss nur einmal angelegt werden
                questestinterop = ET.Element('questestinterop')
                assessment = ET.SubElement(questestinterop, 'assessment')
                section = ET.SubElement(assessment, 'section')
                item = ET.SubElement(section, 'item')

            # Aufbau für  Fragenstruktur "POOL"
            else:
                # XML Struktur aus XML Datei festlegen. Muss nur einmal angelegt werden
                questestinterop = ET.Element('questestinterop')
                item = ET.SubElement(questestinterop, 'item')

                # Zusatz für Taxonomie-Einstellungen

                XML_Interface.set_taxonomy_for_question(self,
                                                        id_nr,
                                                        self.number_of_entrys,
                                                        item,
                                                        self.pool_qpl_file_path_template,
                                                        self.pool_qpl_file_path_output)

            # Struktur für den SingleChoice - Fragen/Antworten Teil  -- HEADER
            # Muss für jede Frage neu angelegt/hinzugefügt werden
            qticomment = ET.SubElement(item, 'qticomment')
            duration = ET.SubElement(item, 'duration')
            itemmetadata = ET.SubElement(item, 'itemmetadata')
            presentation = ET.SubElement(item, 'presentation')
            resprocessing = ET.SubElement(item, 'resprocessing')

            # Struktur für den SingleChoice - Fragen/Antworten Teil  -- MAIN
            # Muss für jede Frage neu angelegt/hinzugefügt werden
            flow = ET.SubElement(presentation, 'flow')
            question_description_material = ET.SubElement(flow, 'material')
            question_description_mattext = ET.SubElement(question_description_material, 'mattext')
            response_lid = ET.SubElement(flow, 'response_lid')
            render_choice = ET.SubElement(response_lid, 'render_choice')

            qtimetadata = ET.SubElement(itemmetadata, 'qtimetadata')
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')

            ### ------------------------------------------------------- XML Einträge mit Werten füllen

            # Fragen-Titel -- "item title" in xml
            item.set('title', test_data_list[table_index_dict[1]['question_title']])

            # Fragen-Titel Beschreibung
            qticomment.text = test_data_list[table_index_dict[1]['question_description_title']]

            # Testdauer -- "duration" in xml
            # wird keine Testzeit eingetragen, wird 1h vorausgewählt
            duration.text = test_data_list[table_index_dict[1]['test_time']]
            if duration.text == "":
                duration.text = "P0Y0M0DT1H0M0S"

            """ Prüfen ob ILIAS Version ausgelesen werden kann"""
            # -----------------------------------------------------------------------ILIAS VERSION
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "ILIAS_VERSION"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = "5.4.14 2020-07-31"
            # -----------------------------------------------------------------------QUESTIONTYPE
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "QUESTIONTYPE"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = "SINGLE CHOICE QUESTION"
            # -----------------------------------------------------------------------AUTHOR
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "AUTHOR"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = test_data_list[table_index_dict[1]['question_author']]
            # -----------------------------------------------------------------------ADDITIONAL_CONT_EDIT_MODE
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "additional_cont_edit_mode"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = "default"
            # -----------------------------------------------------------------------EXTERNAL_ID
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "externalId"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = "5f11d3ed9af3e5.53678796"
            # -----------------------------------------------------------------------THUMB_SIZE
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "thumb_size"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = str(test_data_list[table_index_dict[1]['picture_preview_pixel']])
            # -----------------------------------------------------------------------FEEDBACK_SETTING
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "feedback_setting"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = "1"
            # -----------------------------------------------------------------------SINGLELINE
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "singleline"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = "1"

            # Fragentitel einsetzen -- "presentation label" in xml
            presentation.set('label', test_data_list[table_index_dict[1]['question_title']])

            # Fragen-Text (Format) einsetzen -- "mattext_texttype" in xml -- Gibt das Format des Textes an
            question_description_mattext.set('texttype', "text/html")

            # Fragen-Text (Text) einsetzen   -- "mattext_texttype" in xml -- Gibt die eigentliche Fragen-Beschreibung an
            # Wenn Bild enthalten ist, dann in Fragenbeschreibung einbetten
            question_description_mattext.text = XML_Interface.add_picture_to_description_main(
                                                self,
                                                test_data_list[table_index_dict[1]['description_img_path_1']],
                                                test_data_list[table_index_dict[1]['description_img_path_2']],
                                                test_data_list[table_index_dict[1]['description_img_path_3']],
                                                self.img_file_path_output,
                                                self.sc_question_description_main, question_description_mattext, question_description_material, id_nr)


            # "MCSR --> Singlechoice Identifier für xml datei
            response_lid.set('ident', "MCSR")
            response_lid.set('rcardinality', "Single")
            # TODO  mix_questions wird noch nicht in der DB gespeichert
            #render_choice.set('shuffle', self.sc_var_mix_questions.get())
            render_choice.set('shuffle', "1")



            # Antworten erstellen
            XML_Interface.sc_question_answer_structure(self, test_data_list[table_index_dict[1]['response_1_text']], test_data_list[table_index_dict[1]['response_1_pts']], test_data_list[table_index_dict[1]['response_1_img_path']], render_choice, resprocessing, item, "0")
            XML_Interface.sc_question_answer_structure(self, test_data_list[table_index_dict[1]['response_2_text']], test_data_list[table_index_dict[1]['response_2_pts']], test_data_list[table_index_dict[1]['response_2_img_path']], render_choice, resprocessing, item, "1")
            XML_Interface.sc_question_answer_structure(self, test_data_list[table_index_dict[1]['response_3_text']], test_data_list[table_index_dict[1]['response_3_pts']], test_data_list[table_index_dict[1]['response_3_img_path']], render_choice, resprocessing, item, "2")
            XML_Interface.sc_question_answer_structure(self, test_data_list[table_index_dict[1]['response_4_text']], test_data_list[table_index_dict[1]['response_4_pts']], test_data_list[table_index_dict[1]['response_4_img_path']], render_choice, resprocessing, item, "3")
            XML_Interface.sc_question_answer_structure(self, test_data_list[table_index_dict[1]['response_5_text']], test_data_list[table_index_dict[1]['response_5_pts']], test_data_list[table_index_dict[1]['response_5_img_path']], render_choice, resprocessing, item, "4")
            XML_Interface.sc_question_answer_structure(self, test_data_list[table_index_dict[1]['response_6_text']], test_data_list[table_index_dict[1]['response_6_pts']], test_data_list[table_index_dict[1]['response_6_img_path']], render_choice, resprocessing, item, "5")
            XML_Interface.sc_question_answer_structure(self, test_data_list[table_index_dict[1]['response_7_text']], test_data_list[table_index_dict[1]['response_7_pts']], test_data_list[table_index_dict[1]['response_7_img_path']], render_choice, resprocessing, item, "6")
            XML_Interface.sc_question_answer_structure(self, test_data_list[table_index_dict[1]['response_8_text']], test_data_list[table_index_dict[1]['response_8_pts']], test_data_list[table_index_dict[1]['response_8_img_path']], render_choice, resprocessing, item, "7")
            XML_Interface.sc_question_answer_structure(self, test_data_list[table_index_dict[1]['response_9_text']], test_data_list[table_index_dict[1]['response_9_pts']], test_data_list[table_index_dict[1]['response_9_img_path']], render_choice, resprocessing, item, "8")
            XML_Interface.sc_question_answer_structure(self, test_data_list[table_index_dict[1]['response_10_text']], test_data_list[table_index_dict[1]['response_10_pts']], test_data_list[table_index_dict[1]['response_10_img_path']], render_choice, resprocessing, item, "9")

            # Wenn es sich um einen ILIAS-Test handelt, beinhaltet die XML eine Struktur mit mehreren "Zweigen"
            # Der letzte "Zweig" --> "len(self.sc_myroot[0]) - 1" (beschreibt das letze Fach) beinhaltet die eigentlichen Fragen
            if self.create_ilias_test_or_pool == "ilias_test":
                self.ff_myroot[0][len(self.ff_myroot[0]) - 1].append(item)

            # Wenn es sich um einen ILIAS-Pool handelt, beinhaltet die XML keine Struktur
            # Die Frage kann einfach angehangen werden
            else:
                self.ff_myroot.append(item)


            print(str(id_nr) + ".) Singlechoice Frage erstellt! ---> Titel: " + test_data_list[table_index_dict[1]['question_title']])



        def sc_question_answer_structure(self, sc_response_var_text, sc_response_var_pts, sc_response_var_img_path,
                                          xml_render_choice, xml_resprocessing, xml_item, sc_response_counter):


            ### Bild-Daten in base64 speichern. Die XML Datei enthält die Bilder der Antworten in base64 encoded
            # "encoded64_string_raw enthält die Daten als String in der Form b'String'
            # Um die Daten in der richtigen Form zu erhalten (nur den String ohne b''), wird die Funktion .decode('utf-8') verwendet
            # Dieser String kann in der .xml Datei verwendet werden um im Ilias ein Bild zu erzeugen
            if sc_response_var_img_path != "":
                with open(sc_response_var_img_path, "rb") as image_file:
                    self.encoded64_string_raw = base64.b64encode(image_file.read())
                    self.sc_response_var_img_string_base64_encoded = self.encoded64_string_raw.decode('utf-8')

            if sc_response_var_text != "":
                response_label = ET.SubElement(xml_render_choice, 'response_label')
                question_answer_material = ET.SubElement(response_label, 'material')
                question_answer_mattext = ET.SubElement(question_answer_material, 'mattext')
                response_label.set('ident', str(sc_response_counter))
                question_answer_mattext.set('texttype', "text/plain")
                question_answer_mattext.text = sc_response_var_text

                
                if self.sc_response_var_img_string_base64_encoded != "":
                    question_answer_matimage = ET.SubElement(question_answer_material, 'matimage')

                    if str(sc_response_var_img_path.rpartition('.')[-1]) == "jpg" or str(sc_response_var_img_path.rpartition('.')[-1]) == "jpeg":
                        question_answer_matimage.set('imagtype', "image/jpeg")
                    elif str(sc_response_var_img_path.rpartition('.')[-1]) == "png":
                        question_answer_matimage.set('imagtype', "image/png")
                    elif str(sc_response_var_img_path.rpartition('.')[-1]) == "gif":
                        question_answer_matimage.set('imagtype', "image/gif")
                    else:
                        print("Bildformat ist nicht jpg/jpeg/png/gif und wird von ILIAS nicht unterstützt!")

                    question_answer_matimage.set('label', sc_response_var_img_path.rpartition('/')[-1])
                    question_answer_matimage.set('embedded', "base64")
                    question_answer_matimage.text = str(self.sc_response_var_img_string_base64_encoded)

                # --------------------------------------------------------PUNKTE FÜR ANTWORT

                respcondition = ET.SubElement(xml_resprocessing, 'respcondition')
                respcondition.set('continue', "Yes")

                conditionvar = ET.SubElement(respcondition, 'conditionvar')
                varequal = ET.SubElement(conditionvar, 'varequal')
                varequal.set('respident', "MCSR")  # MCSR --> SingleChoice Ident
                varequal.text = str(sc_response_counter)  # ID der Antwort inkrementiert für jede Antwort

                setvar = ET.SubElement(respcondition, 'setvar')
                setvar.set('action', "Add")
                setvar.text = str(sc_response_var_pts)  # Punktevergabe für die Antwort
                displayfeedback = ET.SubElement(respcondition, 'displayfeedback')
                displayfeedback.set('feedbacktype', "Response")
                displayfeedback.set('linkrefid', "response_" + str(sc_response_counter))
                # --------------------------------------------------------ZUSATZ FÜR ANTWORT

                itemfeedback = ET.SubElement(xml_item, 'itemfeedback')
                itemfeedback_flow_mat = ET.SubElement(itemfeedback, 'flow_mat')
                itemfeedback_material = ET.SubElement(itemfeedback_flow_mat, 'material')
                itemfeedback_mattext = ET.SubElement(itemfeedback_material, 'mattext')

                itemfeedback.set('ident', "response_" + str(sc_response_counter))
                itemfeedback.set('view', "All")
                itemfeedback_mattext.set('texttype', "text/plain")

        ###### MULTIPLECHOICE FUNKTIONEN ##############

        def mc_question_structure(self, test_data_list, table_index_dict, id_nr, pool_qpl_file_path_template , pool_qpl_file_path_output, img_file_path):
            """Diese Funktion wandelt die SQL-Einträge in die .xml um, welche anschließend in ILIAS eingespielt werden kann"""

            self.pool_qpl_file_path_template = pool_qpl_file_path_template
            self.pool_qpl_file_path_output = pool_qpl_file_path_output

            self.img_file_path_output = img_file_path

            # self.sc_question_description_main = test_generator_modul_taxonomie_und_textformatierung.Textformatierung.format_description_text_in_xml(self, self.sc_var_use_latex_on_text_check.get(), self.sc_question_description_main)

            self.mc_question_description_main = XML_Interface.format_description_text_in_xml(self, test_data_list[table_index_dict[2]['question_description_main']])






            # Aufbau für  Fragenstruktur "TEST"
            if self.create_ilias_test_or_pool == "ilias_test":
                # XML Struktur aus XML Datei festlegen. Muss nur einmal angelegt werden
                questestinterop = ET.Element('questestinterop')
                assessment = ET.SubElement(questestinterop, 'assessment')
                section = ET.SubElement(assessment, 'section')
                item = ET.SubElement(section, 'item')

            # Aufbau für  Fragenstruktur "POOL"
            else:
                # XML Struktur aus XML Datei festlegen. Muss nur einmal angelegt werden
                questestinterop = ET.Element('questestinterop')
                item = ET.SubElement(questestinterop, 'item')

                # Zusatz für Taxonomie-Einstellungen

                XML_Interface.set_taxonomy_for_question(self,
                                                       id_nr,
                                                       self.number_of_entrys,
                                                       item,
                                                        self.pool_qpl_file_path_template,
                                                        self.pool_qpl_file_path_output)

            # Struktur für den MultipleChoice - Fragen/Antworten Teil  -- HEADER
            # Muss für jede Frage neu angelegt/hinzugefügt werden
            qticomment = ET.SubElement(item, 'qticomment')
            duration = ET.SubElement(item, 'duration')
            itemmetadata = ET.SubElement(item, 'itemmetadata')
            presentation = ET.SubElement(item, 'presentation')
            resprocessing = ET.SubElement(item, 'resprocessing')

            # Struktur für den MultipleChoice - Fragen/Antworten Teil  -- MAIN
            # Muss für jede Frage neu angelegt/hinzugefügt werden
            flow = ET.SubElement(presentation, 'flow')
            question_description_material = ET.SubElement(flow, 'material')
            question_description_mattext = ET.SubElement(question_description_material, 'mattext')
            response_lid = ET.SubElement(flow, 'response_lid')
            render_choice = ET.SubElement(response_lid, 'render_choice')

            qtimetadata = ET.SubElement(itemmetadata, 'qtimetadata')
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')

            ### ------------------------------------------------------- XML Einträge mit Werten füllen

            # Fragen-Titel -- "item title" in xml
            item.set('title', test_data_list[table_index_dict[2]['question_title']])

            # Fragen-Titel Beschreibung
            qticomment.text = test_data_list[table_index_dict[2]['question_description_title']]

            # Testdauer -- "duration" in xml
            # wird keine Testzeit eingetragen, wird 1h vorausgewählt
            duration.text = test_data_list[table_index_dict[2]['test_time']]
            if duration.text == "":
                duration.text = "P0Y0M0DT1H0M0S"

            """ Prüfen ob ILIAS Version ausgelesen werden kann"""
            # -----------------------------------------------------------------------ILIAS VERSION
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "ILIAS_VERSION"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = "5.4.14 2020-07-31"
            # -----------------------------------------------------------------------QUESTIONTYPE
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "QUESTIONTYPE"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = "MULTIPLE CHOICE QUESTION"
            # -----------------------------------------------------------------------AUTHOR
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "AUTHOR"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = test_data_list[table_index_dict[2]['question_author']]
            # -----------------------------------------------------------------------ADDITIONAL_CONT_EDIT_MODE
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "additional_cont_edit_mode"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = "default"
            # -----------------------------------------------------------------------EXTERNAL_ID
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "externalId"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = "5f11d3ed9af3e5.53678796"
            # -----------------------------------------------------------------------THUMB_SIZE
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "thumb_size"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = str(test_data_list[table_index_dict[2]['picture_preview_pixel']])
            # -----------------------------------------------------------------------FEEDBACK_SETTING
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "feedback_setting"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = "1"
            # -----------------------------------------------------------------------SINGLELINE
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "singleline"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = "1"

            # Fragentitel einsetzen -- "presentation label" in xml
            presentation.set('label', test_data_list[table_index_dict[2]['question_title']])

            # Fragen-Text -- "mattext_texttype" in xml -- Gibt das Format des Textes an
            question_description_mattext.set('texttype', "text/html")

            # Fragen-Text (Text) einsetzen   -- "mattext_texttype" in xml -- Gibt die eigentliche Fragen-Beschreibung an
            # Wenn Bild enthalten ist, dann in Fragenbeschreibung einbetten
            question_description_mattext.text = XML_Interface.add_picture_to_description_main(
                                                self,
                                                test_data_list[table_index_dict[2]['description_img_path_1']],
                                                test_data_list[table_index_dict[2]['description_img_path_2']],
                                                test_data_list[table_index_dict[2]['description_img_path_3']],
                                                self.img_file_path_output,
                                                self.mc_question_description_main, question_description_mattext, question_description_material, id_nr)

            # "MCMR --> Multiplechoice Identifier für xml datei
            response_lid.set('ident', "MCMR")
            response_lid.set('rcardinality', "Multiple")
            render_choice.set('shuffle', "1")

            # Hier die Question_answer_structure einfügen und Antworten erstellen
            #
            #
            XML_Interface.mc_question_answer_structure(self, test_data_list[table_index_dict[2]['response_1_text']], test_data_list[table_index_dict[2]['response_1_img_path']], test_data_list[table_index_dict[2]['response_1_pts_correct_answer']], test_data_list[table_index_dict[2]['response_1_pts_false_answer']], render_choice, resprocessing, item, "0")
            XML_Interface.mc_question_answer_structure(self, test_data_list[table_index_dict[2]['response_2_text']], test_data_list[table_index_dict[2]['response_2_img_path']], test_data_list[table_index_dict[2]['response_2_pts_correct_answer']], test_data_list[table_index_dict[2]['response_2_pts_false_answer']], render_choice, resprocessing, item, "1")
            XML_Interface.mc_question_answer_structure(self, test_data_list[table_index_dict[2]['response_3_text']], test_data_list[table_index_dict[2]['response_3_img_path']], test_data_list[table_index_dict[2]['response_3_pts_correct_answer']], test_data_list[table_index_dict[2]['response_3_pts_false_answer']], render_choice, resprocessing, item, "2")
            XML_Interface.mc_question_answer_structure(self, test_data_list[table_index_dict[2]['response_4_text']], test_data_list[table_index_dict[2]['response_4_img_path']], test_data_list[table_index_dict[2]['response_4_pts_correct_answer']], test_data_list[table_index_dict[2]['response_4_pts_false_answer']], render_choice, resprocessing, item, "3")
            XML_Interface.mc_question_answer_structure(self, test_data_list[table_index_dict[2]['response_5_text']], test_data_list[table_index_dict[2]['response_5_img_path']], test_data_list[table_index_dict[2]['response_5_pts_correct_answer']], test_data_list[table_index_dict[2]['response_5_pts_false_answer']], render_choice, resprocessing, item, "4")
            XML_Interface.mc_question_answer_structure(self, test_data_list[table_index_dict[2]['response_6_text']], test_data_list[table_index_dict[2]['response_6_img_path']], test_data_list[table_index_dict[2]['response_6_pts_correct_answer']], test_data_list[table_index_dict[2]['response_6_pts_false_answer']], render_choice, resprocessing, item, "5")
            XML_Interface.mc_question_answer_structure(self, test_data_list[table_index_dict[2]['response_7_text']], test_data_list[table_index_dict[2]['response_7_img_path']], test_data_list[table_index_dict[2]['response_7_pts_correct_answer']], test_data_list[table_index_dict[2]['response_7_pts_false_answer']], render_choice, resprocessing, item, "6")
            XML_Interface.mc_question_answer_structure(self, test_data_list[table_index_dict[2]['response_8_text']], test_data_list[table_index_dict[2]['response_8_img_path']], test_data_list[table_index_dict[2]['response_8_pts_correct_answer']], test_data_list[table_index_dict[2]['response_8_pts_false_answer']], render_choice, resprocessing, item, "7")
            XML_Interface.mc_question_answer_structure(self, test_data_list[table_index_dict[2]['response_9_text']], test_data_list[table_index_dict[2]['response_9_img_path']], test_data_list[table_index_dict[2]['response_9_pts_correct_answer']], test_data_list[table_index_dict[2]['response_9_pts_false_answer']], render_choice, resprocessing, item, "8")
            XML_Interface.mc_question_answer_structure(self, test_data_list[table_index_dict[2]['response_10_text']], test_data_list[table_index_dict[2]['response_10_img_path']], test_data_list[table_index_dict[2]['response_10_pts_correct_answer']], test_data_list[table_index_dict[2]['response_10_pts_false_answer']], render_choice, resprocessing, item, "9")

            # Wenn es sich um einen ILIAS-Test handelt, beinhaltet die XML eine Struktur mit mehreren "Zweigen"
            # Der letzte "Zweig" --> "len(self.sc_myroot[0]) - 1" (beschreibt das letze Fach) beinhaltet die eigentlichen Fragen
            if self.create_ilias_test_or_pool == "ilias_test":
                self.ff_myroot[0][len(self.ff_myroot[0]) - 1].append(item)

            # Wenn es sich um einen ILIAS-Pool handelt, beinhaltet die XML keine Struktur
            # Die Frage kann einfach angehangen werden
            else:
                self.ff_myroot.append(item)



            print("MultipleChoice Frage erstellt! --> Titel: " + test_data_list[table_index_dict[1]['question_title']])



        def mc_question_answer_structure(self, mc_response_var_text, mc_response_var_img_path, mc_correct_response_var_pts, mc_false_response_var_pts,
                                         xml_render_choice, xml_resprocessing, xml_item, mc_response_counter):

      
            ### Bild-Daten in base64 speichern. Die XML Datei enthält die Bilder der Antworten in base64 encoded
            # "encoded64_string_raw enthält die Daten als String in der Form b'String'
            # Um die Daten in der richtigen Form zu erhalten (nur den String ohne b''), wird die Funktion .decode('utf-8') verwendet
            # Dieser String kann in der .xml Datei verwendet werden um im Ilias ein Bild zu erzeugen
            if mc_response_var_img_path != "":
                with open(mc_response_var_img_path, "rb") as image_file:
                    self.encoded64_string_raw = base64.b64encode(image_file.read())
                    self.mc_response_var_img_string_base64_encoded = self.encoded64_string_raw.decode('utf-8')


            if mc_response_var_text != "":
                response_label = ET.SubElement(xml_render_choice, 'response_label')
                question_answer_material = ET.SubElement(response_label, 'material')
                question_answer_mattext = ET.SubElement(question_answer_material, 'mattext')
                response_label.set('ident', str(mc_response_counter))
                question_answer_mattext.set('texttype', "text/plain")
                question_answer_mattext.text = mc_response_var_text


                if self.mc_response_var_img_string_base64_encoded != "":
                    question_answer_matimage = ET.SubElement(question_answer_material, 'matimage')

                    if str(mc_response_var_img_path.rpartition('.')[-1]) == "jpg" or str(mc_response_var_img_path.rpartition('.')[-1]) == "jpeg":
                        question_answer_matimage.set('imagtype', "image/jpeg")
                    elif str(mc_response_var_img_path.rpartition('.')[-1]) == "png":
                        question_answer_matimage.set('imagtype', "image/png")
                    elif str(mc_response_var_img_path.rpartition('.')[-1]) == "gif":
                        question_answer_matimage.set('imagtype', "image/gif")
                    else:
                        print("Bildformat ist nicht jpg/jpeg/png/gif und wird von ILIAS nicht unterstützt!")

                    question_answer_matimage.set('label', mc_response_var_img_path.rpartition('/')[-1])
                    question_answer_matimage.set('embedded', "base64")
                    question_answer_matimage.text = str(self.mc_response_var_img_string_base64_encoded)

                # --------------------------------------------------------PUNKTE FÜR ANTWORT 1

                respcondition = ET.SubElement(xml_resprocessing, 'respcondition')
                respcondition.set('continue', "Yes")

                conditionvar = ET.SubElement(respcondition, 'conditionvar')
                varequal = ET.SubElement(conditionvar, 'varequal')
                varequal.set('respident', "MCMR")  # MCMR --> MultipleChoice Ident
                varequal.text = str(mc_response_counter)  # ID der Antwort inkrementiert für jede Antwort

                setvar = ET.SubElement(respcondition, 'setvar')
                setvar.set('action', "Add")
                setvar.text = str(mc_correct_response_var_pts)  # Punktevergabe für die richtige Antwort
                displayfeedback = ET.SubElement(respcondition, 'displayfeedback')
                displayfeedback.set('feedbacktype', "Response")
                displayfeedback.set('linkrefid', "response_" + str(mc_response_counter))

                respcondition = ET.SubElement(xml_resprocessing, 'respcondition')
                respcondition.set('continue', "Yes")
                conditionvar = ET.SubElement(respcondition, 'conditionvar')
                conditionvar_not = ET.SubElement(conditionvar, 'not')
                varequal_not = ET.SubElement(conditionvar_not, 'varequal')
                varequal_not.set('respident', "MCMR")  # MCMR --> MultipleChoice Ident
                varequal_not.text = str(mc_response_counter)  # ID der Antwort inkrementiert für jede Antwort

                setvar_not = ET.SubElement(respcondition, 'setvar')
                setvar_not.set('action', "Add")
                setvar_not.text = str(mc_false_response_var_pts)

                # --------------------------------------------------------ZUSATZ FÜR ANTWORT 1

                itemfeedback = ET.SubElement(xml_item, 'itemfeedback')
                itemfeedback_flow_mat = ET.SubElement(itemfeedback, 'flow_mat')
                itemfeedback_material = ET.SubElement(itemfeedback_flow_mat, 'material')
                itemfeedback_mattext = ET.SubElement(itemfeedback_material, 'mattext')

                itemfeedback.set('ident', "response_" + str(mc_response_counter))
                itemfeedback.set('view', "All")
                itemfeedback_mattext.set('texttype', "text/plain")

        ###### ZUORDNUNGSFRAGE FUNKTIONEN ##############
        
        def mq_question_structure(self, test_data_list, table_index_dict, id_nr, pool_qpl_file_path_template , pool_qpl_file_path_output, img_file_path):
            """Diese Funktion wandelt die SQL-Einträge in die .xml um, welche anschließend in ILIAS eingespielt werden kann"""


            self.assignment_pairs_definitions_terms_to_id_dict = {"Definition 1": 0, "Definition 2": 1, "Definition 3": 2, "Definition 4": 3, "Definition 5": 4,
                                                                  "Definition 6": 5, "Definition 7": 6, "Definition 8": 7, "Definition 9": 8, "Definition 10": 9,

                                                                  "Term 1": 10, "Term 2": 11, "Term 3": 12, "Term 4": 13, "Term 5": 14,
                                                                  "Term 6": 15, "Term 7": 16, "Term 8": 17, "Term 9": 18, "Term 10": 19
                                                            }

            self.pool_qpl_file_path_template = pool_qpl_file_path_template
            self.pool_qpl_file_path_output = pool_qpl_file_path_output
            self.img_file_path_output = img_file_path


            self.mq_question_description_main = XML_Interface.format_description_text_in_xml(self, test_data_list[table_index_dict[3]['question_description_main']])

       

             # Aufbau für  Fragenstruktur "TEST"
            if self.create_ilias_test_or_pool == "ilias_test":
                # XML Struktur aus XML Datei festlegen. Muss nur einmal angelegt werden
                questestinterop = ET.Element('questestinterop')
                assessment = ET.SubElement(questestinterop, 'assessment')
                section = ET.SubElement(assessment, 'section')
                item = ET.SubElement(section, 'item')

            # Aufbau für  Fragenstruktur "POOL"
            else:
                # XML Struktur aus XML Datei festlegen. Muss nur einmal angelegt werden
                questestinterop = ET.Element('questestinterop')
                item = ET.SubElement(questestinterop, 'item')

                # Zusatz für Taxonomie-Einstellungen
                XML_Interface.set_taxonomy_for_question(self,
                                                       id_nr,
                                                       self.number_of_entrys,
                                                       item,
                                                       self.pool_qpl_file_path_template,
                                                       self.pool_qpl_file_path_output)



            # Struktur für den Zuordnungsfrage - Fragen/Antworten Teil  -- HEADER
            # Muss für jede Frage neu angelegt/hinzugefügt werden
            qticomment = ET.SubElement(item, 'qticomment')
            duration = ET.SubElement(item, 'duration')
            itemmetadata = ET.SubElement(item, 'itemmetadata')
            presentation = ET.SubElement(item, 'presentation')
            resprocessing = ET.SubElement(item, 'resprocessing')

            # Struktur für den Zuordnungsfrage - Fragen/Antworten Teil  -- MAIN
            # Muss für jede Frage neu angelegt/hinzugefügt werden
            flow = ET.SubElement(presentation, 'flow')
            question_description_material = ET.SubElement(flow, 'material')
            question_description_mattext = ET.SubElement(question_description_material, 'mattext')
            response_grp = ET.SubElement(flow, 'response_grp')
            render_choice = ET.SubElement(response_grp, 'render_choice')

            qtimetadata = ET.SubElement(itemmetadata, 'qtimetadata')
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')


            ### ------------------------------------------------------- XML Einträge mit Werten füllen

            # Fragen-Titel -- "item title" in xml
            #item_ident_nr = format(id_nr, "06")
            #item.set('ident', "il_0_qst_" + str(item_ident_nr))
            item.set('title', test_data_list[table_index_dict[3]['question_title']])
            item.set('maxattempts', "0")

            # Fragen-Titel Beschreibung
            qticomment.text = test_data_list[table_index_dict[3]['question_description_title']]

            # Testdauer -- "duration" in xml
            # wird keine Testzeit eingetragen, wird 1h vorausgewählt
            duration.text = test_data_list[table_index_dict[3]['test_time']]
            if duration.text == "":
                duration.text = "P0Y0M0DT1H0M0S"

            """ Prüfen ob ILIAS Version ausgelesen werden kann"""
            # -----------------------------------------------------------------------ILIAS VERSION
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "ILIAS_VERSION"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = "5.4.14 2020-07-31"
            # -----------------------------------------------------------------------QUESTIONTYPE
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "QUESTIONTYPE"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = "MATCHING QUESTION"
            # -----------------------------------------------------------------------AUTHOR
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "AUTHOR"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = test_data_list[table_index_dict[3]['question_author']]
            # -----------------------------------------------------------------------ADDITIONAL_CONT_EDIT_MODE
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "additional_cont_edit_mode"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = "default"
            # -----------------------------------------------------------------------EXTERNAL_ID
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "externalId"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = "5f11d3ed9af3e5.53678796"
            # -----------------------------------------------------------------------SHUFFLE
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "shuffle"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = str(test_data_list[table_index_dict[3]['mix_answers']])
            # -----------------------------------------------------------------------THUMB_GEOMETRY
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "thumb_geometry"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = str(test_data_list[table_index_dict[3]['picture_preview_pixel']])
            # -----------------------------------------------------------------------MATCHING MODE
            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
            fieldlabel.text = "matching_mode"
            fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
            fieldentry.text = str(test_data_list[table_index_dict[3]['asignment_mode']])


            # Fragentitel einsetzen -- "presentation label" in xml
            presentation.set('label', test_data_list[table_index_dict[3]['question_title']])

            # Fragen-Text (Format) einsetzen -- "mattext_texttype" in xml -- Gibt das Format des Textes an
            question_description_mattext.set('texttype', "text/html")

            # Fragen-Text (Text) einsetzen   -- "mattext_texttype" in xml -- Gibt die eigentliche Fragen-Beschreibung an
            # Wenn Bild enthalten ist, dann in Fragenbeschreibung einbetten
            # Fragen-Text (Text) einsetzen   -- "mattext_texttype" in xml -- Gibt die eigentliche Fragen-Beschreibung an
            # Wenn Bild enthalten ist, dann in Fragenbeschreibung einbetten
            question_description_mattext.text = XML_Interface.add_picture_to_description_main(
                                                self,
                                                test_data_list[table_index_dict[3]['description_img_path_1']],
                                                test_data_list[table_index_dict[3]['description_img_path_2']],
                                                test_data_list[table_index_dict[3]['description_img_path_3']],
                                                self.img_file_path_output,
                                                self.mq_question_description_main, question_description_mattext, question_description_material, id_nr)

            # "MQ --> Matching Question Identifier für xml datei
            response_grp.set('ident', "MQ")
            response_grp.set('rcardinality', "Multiple")
            render_choice.set('shuffle', "Yes")


            self.mq_number_of_terms_used = []

            if test_data_list[table_index_dict[3]['assignment_pairs_term_1']] != "":
                self.mq_number_of_terms_used.append(self.assignment_pairs_definitions_terms_to_id_dict[test_data_list[table_index_dict[3]['assignment_pairs_term_1']]])
            if test_data_list[table_index_dict[3]['assignment_pairs_term_2']] != "":
                self.mq_number_of_terms_used.append(self.assignment_pairs_definitions_terms_to_id_dict[test_data_list[table_index_dict[3]['assignment_pairs_term_2']]])
            if test_data_list[table_index_dict[3]['assignment_pairs_term_3']] != "":
                self.mq_number_of_terms_used.append(self.assignment_pairs_definitions_terms_to_id_dict[test_data_list[table_index_dict[3]['assignment_pairs_term_3']]])
            if test_data_list[table_index_dict[3]['assignment_pairs_term_4']] != "":
                self.mq_number_of_terms_used.append(self.assignment_pairs_definitions_terms_to_id_dict[test_data_list[table_index_dict[3]['assignment_pairs_term_4']]])
            if test_data_list[table_index_dict[3]['assignment_pairs_term_5']] != "":
                self.mq_number_of_terms_used.append(self.assignment_pairs_definitions_terms_to_id_dict[test_data_list[table_index_dict[3]['assignment_pairs_term_5']]])
            if test_data_list[table_index_dict[3]['assignment_pairs_term_6']] != "":
                self.mq_number_of_terms_used.append(self.assignment_pairs_definitions_terms_to_id_dict[test_data_list[table_index_dict[3]['assignment_pairs_term_6']]])
            if test_data_list[table_index_dict[3]['assignment_pairs_term_7']] != "":
                self.mq_number_of_terms_used.append(self.assignment_pairs_definitions_terms_to_id_dict[test_data_list[table_index_dict[3]['assignment_pairs_term_7']]])
            if test_data_list[table_index_dict[3]['assignment_pairs_term_8']] != "":
                self.mq_number_of_terms_used.append(self.assignment_pairs_definitions_terms_to_id_dict[test_data_list[table_index_dict[3]['assignment_pairs_term_8']]])
            if test_data_list[table_index_dict[3]['assignment_pairs_term_9']] != "":
                self.mq_number_of_terms_used.append(self.assignment_pairs_definitions_terms_to_id_dict[test_data_list[table_index_dict[3]['assignment_pairs_term_9']]])
            if test_data_list[table_index_dict[3]['assignment_pairs_term_10']] != "":
                self.mq_number_of_terms_used.append(self.assignment_pairs_definitions_terms_to_id_dict[test_data_list[table_index_dict[3]['assignment_pairs_term_10']]])

            self.mq_number_of_terms_used_string = str(self.mq_number_of_terms_used)
            self.mq_number_of_terms_used_string = self.mq_number_of_terms_used_string[1:-1]




            #Antworten erstellen
            # Antworten erstellen
            XML_Interface.mq_question_answer_structure_definitions(self, test_data_list[table_index_dict[3]['definitions_response_1_text']], test_data_list[table_index_dict[3]['definitions_response_1_img_path']], render_choice, "0", self.mq_number_of_terms_used_string)
            XML_Interface.mq_question_answer_structure_definitions(self, test_data_list[table_index_dict[3]['definitions_response_2_text']], test_data_list[table_index_dict[3]['definitions_response_2_img_path']], render_choice, "1", self.mq_number_of_terms_used_string)
            XML_Interface.mq_question_answer_structure_definitions(self, test_data_list[table_index_dict[3]['definitions_response_3_text']], test_data_list[table_index_dict[3]['definitions_response_3_img_path']], render_choice, "2", self.mq_number_of_terms_used_string)
            XML_Interface.mq_question_answer_structure_definitions(self, test_data_list[table_index_dict[3]['definitions_response_4_text']], test_data_list[table_index_dict[3]['definitions_response_4_img_path']], render_choice, "3", self.mq_number_of_terms_used_string)
            XML_Interface.mq_question_answer_structure_definitions(self, test_data_list[table_index_dict[3]['definitions_response_5_text']], test_data_list[table_index_dict[3]['definitions_response_5_img_path']], render_choice, "4", self.mq_number_of_terms_used_string)
            XML_Interface.mq_question_answer_structure_definitions(self, test_data_list[table_index_dict[3]['definitions_response_6_text']], test_data_list[table_index_dict[3]['definitions_response_6_img_path']], render_choice, "5", self.mq_number_of_terms_used_string)
            XML_Interface.mq_question_answer_structure_definitions(self, test_data_list[table_index_dict[3]['definitions_response_7_text']], test_data_list[table_index_dict[3]['definitions_response_7_img_path']], render_choice, "6", self.mq_number_of_terms_used_string)
            XML_Interface.mq_question_answer_structure_definitions(self, test_data_list[table_index_dict[3]['definitions_response_8_text']], test_data_list[table_index_dict[3]['definitions_response_8_img_path']], render_choice, "7", self.mq_number_of_terms_used_string)
            XML_Interface.mq_question_answer_structure_definitions(self, test_data_list[table_index_dict[3]['definitions_response_9_text']], test_data_list[table_index_dict[3]['definitions_response_9_img_path']], render_choice, "8", self.mq_number_of_terms_used_string)
            XML_Interface.mq_question_answer_structure_definitions(self, test_data_list[table_index_dict[3]['definitions_response_10_text']], test_data_list[table_index_dict[3]['definitions_response_10_img_path']], render_choice, "9", self.mq_number_of_terms_used_string)

            XML_Interface.mq_question_answer_structure_terms(self, test_data_list[table_index_dict[3]['terms_response_1_text']], test_data_list[table_index_dict[3]['terms_response_1_img_path']], render_choice, "10")
            XML_Interface.mq_question_answer_structure_terms(self, test_data_list[table_index_dict[3]['terms_response_2_text']], test_data_list[table_index_dict[3]['terms_response_2_img_path']], render_choice, "11")
            XML_Interface.mq_question_answer_structure_terms(self, test_data_list[table_index_dict[3]['terms_response_3_text']], test_data_list[table_index_dict[3]['terms_response_3_img_path']], render_choice, "12")
            XML_Interface.mq_question_answer_structure_terms(self, test_data_list[table_index_dict[3]['terms_response_4_text']], test_data_list[table_index_dict[3]['terms_response_4_img_path']], render_choice, "13")
            XML_Interface.mq_question_answer_structure_terms(self, test_data_list[table_index_dict[3]['terms_response_5_text']], test_data_list[table_index_dict[3]['terms_response_5_img_path']], render_choice, "14")
            XML_Interface.mq_question_answer_structure_terms(self, test_data_list[table_index_dict[3]['terms_response_6_text']], test_data_list[table_index_dict[3]['terms_response_6_img_path']], render_choice, "15")
            XML_Interface.mq_question_answer_structure_terms(self, test_data_list[table_index_dict[3]['terms_response_7_text']], test_data_list[table_index_dict[3]['terms_response_7_img_path']], render_choice, "16")
            XML_Interface.mq_question_answer_structure_terms(self, test_data_list[table_index_dict[3]['terms_response_8_text']], test_data_list[table_index_dict[3]['terms_response_8_img_path']], render_choice, "17")
            XML_Interface.mq_question_answer_structure_terms(self, test_data_list[table_index_dict[3]['terms_response_9_text']], test_data_list[table_index_dict[3]['terms_response_9_img_path']], render_choice, "18")
            XML_Interface.mq_question_answer_structure_terms(self, test_data_list[table_index_dict[3]['terms_response_10_text']], test_data_list[table_index_dict[3]['terms_response_10_img_path']], render_choice, "19")

            XML_Interface.mq_question_answer_structure_assignment_pairs(self, test_data_list[table_index_dict[3]['assignment_pairs_definition_1']], test_data_list[table_index_dict[3]['assignment_pairs_term_1']], test_data_list[table_index_dict[3]['assignment_pairs_1_pts']], resprocessing, item)
            XML_Interface.mq_question_answer_structure_assignment_pairs(self, test_data_list[table_index_dict[3]['assignment_pairs_definition_2']], test_data_list[table_index_dict[3]['assignment_pairs_term_2']], test_data_list[table_index_dict[3]['assignment_pairs_2_pts']], resprocessing, item)
            XML_Interface.mq_question_answer_structure_assignment_pairs(self, test_data_list[table_index_dict[3]['assignment_pairs_definition_3']], test_data_list[table_index_dict[3]['assignment_pairs_term_3']], test_data_list[table_index_dict[3]['assignment_pairs_3_pts']], resprocessing, item)
            XML_Interface.mq_question_answer_structure_assignment_pairs(self, test_data_list[table_index_dict[3]['assignment_pairs_definition_4']], test_data_list[table_index_dict[3]['assignment_pairs_term_4']], test_data_list[table_index_dict[3]['assignment_pairs_4_pts']], resprocessing, item)
            XML_Interface.mq_question_answer_structure_assignment_pairs(self, test_data_list[table_index_dict[3]['assignment_pairs_definition_5']], test_data_list[table_index_dict[3]['assignment_pairs_term_5']], test_data_list[table_index_dict[3]['assignment_pairs_5_pts']], resprocessing, item)
            XML_Interface.mq_question_answer_structure_assignment_pairs(self, test_data_list[table_index_dict[3]['assignment_pairs_definition_6']], test_data_list[table_index_dict[3]['assignment_pairs_term_6']], test_data_list[table_index_dict[3]['assignment_pairs_6_pts']], resprocessing, item)
            XML_Interface.mq_question_answer_structure_assignment_pairs(self, test_data_list[table_index_dict[3]['assignment_pairs_definition_7']], test_data_list[table_index_dict[3]['assignment_pairs_term_7']], test_data_list[table_index_dict[3]['assignment_pairs_7_pts']], resprocessing, item)
            XML_Interface.mq_question_answer_structure_assignment_pairs(self, test_data_list[table_index_dict[3]['assignment_pairs_definition_8']], test_data_list[table_index_dict[3]['assignment_pairs_term_8']], test_data_list[table_index_dict[3]['assignment_pairs_8_pts']], resprocessing, item)
            XML_Interface.mq_question_answer_structure_assignment_pairs(self, test_data_list[table_index_dict[3]['assignment_pairs_definition_9']], test_data_list[table_index_dict[3]['assignment_pairs_term_9']], test_data_list[table_index_dict[3]['assignment_pairs_9_pts']], resprocessing, item)
            XML_Interface.mq_question_answer_structure_assignment_pairs(self, test_data_list[table_index_dict[3]['assignment_pairs_definition_10']], test_data_list[table_index_dict[3]['assignment_pairs_term_10']], test_data_list[table_index_dict[3]['assignment_pairs_10_pts']], resprocessing, item)
            


            # Wenn es sich um einen ILIAS-Test handelt, beinhaltet die XML eine Struktur mit mehreren "Zweigen"
            # Der letzte "Zweig" --> "len(self.mq_myroot[0]) - 1" (beschreibt das letze Fach) beinhaltet die eigentlichen Fragen
            if self.create_ilias_test_or_pool == "ilias_test":
                self.ff_myroot[0][len(self.ff_myroot[0]) - 1].append(item)

            # Wenn es sich um einen ILIAS-Pool handelt, beinhaltet die XML keine Struktur
            # Die Frage kann einfach angehangen werden
            else:
                self.ff_myroot.append(item)


            print(str(id_nr) + ".) Zuordnungsfrage Frage erstellt! ---> Titel: " + test_data_list[table_index_dict[3]['question_title']])

        def mq_question_answer_structure_definitions(self, mq_definitions_response_var_text, mq_definitions_response_var_img_path,  xml_render_choice, mq_definition_id, mq_number_of_terms_used):

            self.mq_number_of_terms_used = mq_number_of_terms_used

            ### Bild-Daten in base64 speichern. Die XML Datei enthält die Bilder der Antworten in base64 encoded
            # "encoded64_string_raw enthält die Daten als String in der Form b'String'
            # Um die Daten in der richtigen Form zu erhalten (nur den String ohne b''), wird die Funktion .decode('utf-8') verwendet
            # Dieser String kann in der .xml Datei verwendet werden um im Ilias ein Bild zu erzeugen
            if mq_definitions_response_var_img_path != "":
                with open(mq_definitions_response_var_img_path, "rb") as image_file:
                    self.encoded64_string_raw = base64.b64encode(image_file.read())
                    self.mq_definitions_response_var_img_string_base64_encoded = self.encoded64_string_raw.decode('utf-8')



            # Antworten für Definitionen
            if mq_definitions_response_var_text != "":
                response_label = ET.SubElement(xml_render_choice, 'response_label')
                question_answer_material = ET.SubElement(response_label, 'material')
                question_answer_mattext = ET.SubElement(question_answer_material, 'mattext')

                response_label.set('ident', str(mq_definition_id))
                response_label.set('match_max', "1")
                response_label.set('match_group', str(self.mq_number_of_terms_used))


                question_answer_mattext.set('texttype', "text/plain")
                question_answer_mattext.text = mq_definitions_response_var_text
                if self.mq_definitions_response_var_img_string_base64_encoded != "":
                    question_answer_matimage = ET.SubElement(question_answer_material, 'matimage')

                    if str(mq_definitions_response_var_img_path.rpartition('.')[-1]) == "jpg" or str(mq_definitions_response_var_img_path.rpartition('.')[-1]) == "jpeg":
                        question_answer_matimage.set('imagtype', "image/jpeg")
                    elif str(mq_definitions_response_var_img_path.rpartition('.')[-1]) == "png":
                        question_answer_matimage.set('imagtype', "image/png")
                    elif str(mq_definitions_response_var_img_path.rpartition('.')[-1]) == "gif":
                        question_answer_matimage.set('imagtype', "image/gif")
                    else:
                        print("Bildformat ist nicht jpg/jpeg/png/gif und wird von ILIAS nicht unterstützt!")

                    question_answer_matimage.set('label', mq_definitions_response_var_img_path.rpartition('/')[-1])
                    question_answer_matimage.set('embedded', "base64")
                    question_answer_matimage.text = str(self.mq_definitions_response_var_img_string_base64_encoded)

        def mq_question_answer_structure_terms(self, mq_terms_response_var_text, mq_terms_response_var_img_path, xml_render_choice, mq_response_counter):

            ### Bild-Daten in base64 speichern. Die XML Datei enthält die Bilder der Antworten in base64 encoded
            # "encoded64_string_raw enthält die Daten als String in der Form b'String'
            # Um die Daten in der richtigen Form zu erhalten (nur den String ohne b''), wird die Funktion .decode('utf-8') verwendet
            # Dieser String kann in der .xml Datei verwendet werden um im Ilias ein Bild zu erzeugen
            if mq_terms_response_var_img_path != "":
                with open(mq_terms_response_var_img_path, "rb") as image_file:
                    self.encoded64_string_raw = base64.b64encode(image_file.read())
                    self.mq_terms_response_var_img_string_base64_encoded = self.encoded64_string_raw.decode('utf-8')


            #Antworten für Terme
            if mq_terms_response_var_text != "":


                response_label = ET.SubElement(xml_render_choice, 'response_label')
                question_answer_material = ET.SubElement(response_label, 'material')
                question_answer_mattext = ET.SubElement(question_answer_material, 'mattext')

                response_label.set('ident', str(mq_response_counter))

                question_answer_mattext.set('texttype', "text/plain")
                question_answer_mattext.text = mq_terms_response_var_text
                if self.mq_terms_response_var_img_string_base64_encoded != "":
                    question_answer_matimage = ET.SubElement(question_answer_material, 'matimage')

                    if str(mq_terms_response_var_img_path.rpartition('.')[-1]) == "jpg" or str(mq_terms_response_var_img_path.rpartition('.')[-1]) == "jpeg":
                        question_answer_matimage.set('imagtype', "image/jpeg")
                    elif str(mq_terms_response_var_img_path.rpartition('.')[-1]) == "png":
                        question_answer_matimage.set('imagtype', "image/png")
                    elif str(mq_terms_response_var_img_path.rpartition('.')[-1]) == "gif":
                        question_answer_matimage.set('imagtype', "image/gif")
                    else:
                        print("Bildformat ist nicht jpg/jpeg/png/gif und wird von ILIAS nicht unterstützt!")

                    question_answer_matimage.set('label', mq_terms_response_var_img_path.rpartition('/')[-1])
                    question_answer_matimage.set('embedded', "base64")
                    question_answer_matimage.text = str(self.mq_terms_response_var_img_string_base64_encoded)

        def mq_question_answer_structure_assignment_pairs(self, mq_assignment_pairs_definition_var, mq_assignment_pairs_term_var, mq_assignment_pairs_var_pts, xml_resprocessing, xml_item):

            if mq_assignment_pairs_term_var != "" and mq_assignment_pairs_definition_var != "":
                #Zuordnugspaare definieren
                respcondition = ET.SubElement(xml_resprocessing, 'respcondition')
                respcondition.set('continue', "Yes")
                outcomes = ET.SubElement(xml_resprocessing, 'outcomes')
                decvar = ET.SubElement(outcomes, 'decvar')
                conditionvar = ET.SubElement(respcondition, 'conditionvar')
                varsubset = ET.SubElement(conditionvar, 'varsubset')
                varsubset.set('respident', "MQ")  # MQ --> Matching Question Ident
                varsubset.text = str(self.assignment_pairs_definitions_terms_to_id_dict[mq_assignment_pairs_term_var]) + "," + str(self.assignment_pairs_definitions_terms_to_id_dict[mq_assignment_pairs_definition_var])  # ID der Antwort inkrementiert für jede Antwort

                setvar = ET.SubElement(respcondition, 'setvar')
                setvar.set('action', "Add")
                setvar.text = str(mq_assignment_pairs_var_pts)  # Punktevergabe für die Antwort
                displayfeedback = ET.SubElement(respcondition, 'displayfeedback')
                displayfeedback.set('feedbacktype', "Response")
                displayfeedback.set('linkrefid', "correct_" + str(self.assignment_pairs_definitions_terms_to_id_dict[mq_assignment_pairs_term_var]) + "_")

                # --------------------------------------------------------ZUSATZ FÜR ANTWORT

                itemfeedback = ET.SubElement(xml_item, 'itemfeedback')
                itemfeedback_flow_mat = ET.SubElement(itemfeedback, 'flow_mat')
                itemfeedback_material = ET.SubElement(itemfeedback_flow_mat, 'material')
                itemfeedback_mattext = ET.SubElement(itemfeedback_material, 'mattext')

                itemfeedback.set('ident', "correct_" + str(self.assignment_pairs_definitions_terms_to_id_dict[mq_assignment_pairs_term_var]) + "_" + str(self.assignment_pairs_definitions_terms_to_id_dict[mq_assignment_pairs_definition_var]))
                itemfeedback.set('view', "All")


        ###### FORMELFRAGE PERMUTATION FUNKTIONEN ##############


        
        ###### EXCEL IMPORT FUNKTION ###############
        def excel_import_to_db(self):


            ################################  IMPORT EXCEL FILE TO DB  #################################

            # Pfad zur Datei auswählen
            self.xlsx_path = filedialog.askopenfilename(initialdir=pathlib.Path().absolute(), title="Select a File")

            # Wenn in dem Pfad zur Datei ".ods" enthalten ist, wird eine entsprechende "engine" zum
            # richtigen einlesen der Tabelle verwendet (für OpenOffice und LibreOffice)
            if ".ods" in self.xlsx_path:
                print(self.xlsx_path)
                self.xlsx_path = self.xlsx_path.replace('/', "\\")
                print(self.xlsx_path)
                self.xlsx_data = pd.read_excel(self.xlsx_path, engine="odf")
                # print(self.xlsx_data)
            # Enthält der Pfad kein ".ods" wird davon ausgegangen, dass es sich um eine Excel-Datei handelt
            else:
                self.xlsx_data = pd.read_excel(self.xlsx_path)

            ##### -------------------------------------
            self.xlsx_file_column_labels_list = []
            self.sql_values_question_marks = "("
            self.sql_labels_param = ""

            self.ff_description_img_data = ""
            self.sc_description_img_data = ""
            self.mc_description_img_data = ""

            # Auflistung der Fragentitel in Datenbank
            self.db_entries_list = []
            self.edited_questions_list = []
            entry_string = ""
            # Datentypen die von ILIAS unterstützt werden
            self.ilias_image_types = [".jpg", ".jpeg", ".png", ".gif"]
            ######## -------------------------------


            # Dataframe erstellen
            self.dataframe = pd.DataFrame(self.xlsx_data)

            # Über die Excel Spalten iterieren
            for col in self.dataframe.columns:
                self.xlsx_file_column_labels_list.append(str(col))

            # Dataframe mit neuen Labels belegen
            self.dataframe.columns = self.xlsx_file_column_labels_list

            # Leere Einträge entfernen
            self.dataframe = self.dataframe.fillna("")

            #print("---", self.xlsx_file_column_labels_list)









            #####

            index_list = []
            index_dict = {}
            for excel_row in self.dataframe.itertuples():

                if excel_row.question_type == "formelfrage":

                    # table_index_list gibt den Index für spezifische Fragentypen zurück
                    # Diese Zuordnungs wird getroffen um aus Fragentyp "Formelfrage" das dictionary etc zu beziehen
                    index_list = self.table_index_list[self.table_dict["formelfrage"]]
                    index_dict = self.table_index_dict[self.table_dict["formelfrage"]]
                    for i in range(len(self.xlsx_file_column_labels_list)):
                        index_list[index_dict[self.xlsx_file_column_labels_list[i]]][0].set(str(excel_row[i+1]))

                if excel_row.question_type == "singlechoice":
                    index_list = self.table_index_list[self.table_dict["singlechoice"]]
                    index_dict = self.table_index_dict[self.table_dict["singlechoice"]]
                    for i in range(len(self.xlsx_file_column_labels_list)):
                        index_list[index_dict[self.xlsx_file_column_labels_list[i]]][0].set(str(excel_row[i+1]))

                if excel_row.question_type == "multiplechoice":
                    index_list = self.table_index_list[self.table_dict["multiplechoice"]]
                    index_dict = self.table_index_dict[self.table_dict["multiplechoice"]]
                    for i in range(len(self.xlsx_file_column_labels_list)):
                        index_list[index_dict[self.xlsx_file_column_labels_list[i]]][0].set(str(excel_row[i+1]))

                if excel_row.question_type == "zuordnungsfrage":
                    index_list = self.table_index_list[self.table_dict["zuordnungsfrage"]]
                    index_dict = self.table_index_dict[self.table_dict["zuordnungsfrage"]]
                    for i in range(len(self.xlsx_file_column_labels_list)):
                        index_list[index_dict[self.xlsx_file_column_labels_list[i]]][0].set(str(excel_row[i+1]))


                self.DBI.Add_data_to_DB(index_list, index_list[index_dict["question_title"]][0].get())




            # print("Load File: \"" + self.xlsx_path + "\" in formelfrage_table...done!")

            print("     Datei geladen!")


        ###### ILIAS BESTEHENDER POOL IMPORT IN DB
        def import_illias_pool_oder_test_in_db(self):
            # Pfade für Datenbanken
            #self.project_root_path = project_root_path
            #self.database_formelfrage_path = os.path.normpath(os.path.join(self.project_root_path, "Test_Generator_Datenbanken", "ilias_formelfrage_db.db"))
            #self.database_singlechoice_path = os.path.normpath(os.path.join(self.project_root_path,"Test_Generator_Datenbanken", "ilias_singlechoice_db.db"))
            #self.database_multiplechoice_path = os.path.normpath(os.path.join(self.project_root_path,"Test_Generator_Datenbanken", "ilias_multiplechoice_db.db"))
            #self.database_zuordnungsfrage_path = os.path.normpath(os.path.join(self.project_root_path,"Test_Generator_Datenbanken", "ilias_zuordnungsfrage_db.db"))

            self.ilias_question_type = []

            self.ilias_question_title = []
            self.ilias_question_description_title = []
            self.ilias_question_description_main = []

            # SINGLE CHOICE
            self.ilias_response_text = []
            self.ilias_response_pts = []
            self.ilias_response_img_label = []
            self.ilias_response_img_string_base64_encoded = []
            self.ilias_response_img_path = []
            self.ilias_picture_preview_pixel = []
            ##########

            # MULTIPLE CHOICE
            self.mc_ilias_response_text = []
            self.mc_ilias_response_pts = []
            self.mc_ilias_response_img_label = []
            self.mc_ilias_response_img_string_base64_encoded = []
            self.mc_ilias_response_img_path = []
            self.mc_ilias_picture_preview_pixel = []
            ##########

            # Es werden bis zu drei Bilder im Fragen-Text aufgenommen
            self.ilias_test_question_description_image_name_1 = []
            self.ilias_test_question_description_image_data_1 = []
            self.ilias_test_question_description_image_uri_1 = []
            self.ilias_test_question_description_image_name_2 = []
            self.ilias_test_question_description_image_data_2 = []
            self.ilias_test_question_description_image_uri_2 = []
            self.ilias_test_question_description_image_name_3 = []
            self.ilias_test_question_description_image_data_3 = []
            self.ilias_test_question_description_image_uri_3 = []

            self.ilias_test_duration = []
            self.ilias_question_author = []

            self.description_singlechoice_del_index = []
            self.description_multiplechoice_del_index = []
            self.description_matchedquestion_del_index = []

            self.all_sc_questions_points = []

            self.mattext_text_all_mc_answers = []
            self.all_mc_questions_points = []
            self.mc_questions_correct_points = []
            self.mc_questions_false_points = []


            self.mattext_text_all_mq_answers = []
            self.mattext_text_all_mq_answers_collection = []
            self.mattText_text_all_mq_answers = []

            self.sc_answer_list_nr = ""
            self.mc_answer_list_nr = ""
            self.mq_answer_list_nr = ""

            self.mq_answer_matchings = []
            self.mq_number_of_answers_per_question = []
            self.mq_number_of_answers_per_question_temp = []
            self.mq_answer_matchings_points = []
            self.mq_answer_matching_per_question = []

            self.mq_response_img_label = []
            self.mq_response_img_data = []
            self.mq_response_img_path = []
            self.mq_matching_ids = []
            self.mq_matching_ids_points = []
            self.mq_len_list = []


            self.number_of_answers_per_question_sc = []
            self.number_of_answers_per_question_mc = []
            self.number_of_answers_per_question_mq = []

            self.ilias_question_title_sc = []
            self.ilias_question_author_sc = []
            self.ilias_question_type_ff_question_index = []
            self.ilias_question_type_sc_question_index = []
            self.ilias_question_type_mc_question_index = []
            self.ilias_question_type_mq_question_index = []



            ### Hier wird die ausgewählte XML nach möglichen Fragen-Typen durchsucht und entsprechende flag gesetzt

            self.formelfrage_flag = 0
            self.singlechoice_flag = 0
            self.multiplechoice_flag = 0
            self.matchingquestion_flag = 0

            self.formelfrage_number_of_questions = 0
            self.singlechoice_number_of_questions = 0
            self.multiplechoice_number_of_questions = 0
            self.matchingquestion_number_of_questions = 0



            # Auswahl der Datei die bearbeitet werden soll
            filename = filedialog.askdirectory(initialdir=pathlib.Path().absolute(), title="Select a File")
            self.select_test_import_file = filename

            # Ordner-Name splitten um automatisiert die enthaltene qti.xml Datei einlesen zu können
            self.ilias_folder_name = self.select_test_import_file.rsplit('/', 1)[-1]
            self.ilias_folder_name_split1 = self.ilias_folder_name[:15]
            self.ilias_folder_name_split2 = self.ilias_folder_name.rsplit('_', 1)[-1]
            self.ilias_test_qti_file = os.path.normpath(os.path.join(self.select_test_import_file, self.ilias_folder_name_split1 + "qti_" + self.ilias_folder_name_split2 + ".xml"))



            # XML Datei einlesen -> Root Verzeichnis bestimmen
            self.mytree = ET.parse(self.ilias_test_qti_file)
            self.myroot = self.mytree.getroot()

            # Alle Fragentypen aus der XML Datei aufnehmen
            for qtimetadatafield in self.myroot.iter('qtimetadatafield'):
                if qtimetadatafield.find('fieldlabel').text == "QUESTIONTYPE":
                    self.ilias_question_type.append(qtimetadatafield.find('fieldentry').text)




    #################### ALLE FRAGEN-INDEXE DEN FRAGENTYPEN ZUORDNEN

            for i in range(len(self.ilias_question_type)):
                if self.ilias_question_type[i] == "assFormulaQuestion":
                    self.ilias_question_type_ff_question_index.append(str(i))
                    self.formelfrage_flag = 1
                    self.formelfrage_number_of_questions += 1

                elif self.ilias_question_type[i] == "SINGLE CHOICE QUESTION":
                    self.ilias_question_type_sc_question_index.append(str(i))
                    self.singlechoice_flag = 1
                    self.singlechoice_number_of_questions += 1

                elif self.ilias_question_type[i] == "MULTIPLE CHOICE QUESTION":
                    self.ilias_question_type_mc_question_index.append(str(i))
                    self.multiplechoice_flag = 1
                    self.multiplechoice_number_of_questions += 1

                elif self.ilias_question_type[i] == "MATCHING QUESTION":
                    self.ilias_question_type_mq_question_index.append(str(i))
                    self.matchingquestion_flag = 1
                    self.matchingquestion_number_of_questions += 1

                else:
                    print("Keine Fragen gefunden")



            print("Anzahl Formelfrage: " + str(self.formelfrage_number_of_questions))
            print("Anzahl SingleChoice: " + str(self.singlechoice_number_of_questions))
            print("Anzahl MultipleChoice: " + str(self.multiplechoice_number_of_questions))
            print("Anzahl Zuordnungsfrage: " + str(self.matchingquestion_number_of_questions))


    ################# FRAGEN-BESCHREIBUNG (FRAGEN-TEXT) SAMMELN

            # Fragen-Beschreibung, aller Fragen, sammeln
            for flow in self.myroot.iter('flow'):
                for material in flow.iter('material'):
                    if "" in material.find('mattext').text:


                        # Wenn in dem Fragentext "img" enthalten ist, gibt es immer auch ein Bild zu der Frage
                        if "il_0_mob_" in material.find('mattext').text:
                            self.ilias_question_description_main.append(material.find('mattext').text)

                            #Bildname hinzufügen
                            if material.find('matimage').attrib.get('label'):
                                self.ilias_test_question_description_image_name_1.append(material.find('matimage').attrib.get('label'))


                            # Bild Pfad hinzufügen
                            if material.find('matimage').attrib.get('uri'):
                                self.ilias_test_question_description_image_uri_1.append(material.find('matimage').attrib.get('uri'))

                        else:
                            self.ilias_question_description_main.append(material.find('mattext').text)
                            self.ilias_test_question_description_image_name_1.append("EMPTY")
                            self.ilias_test_question_description_image_uri_1.append("EMPTY")
                            self.ilias_test_question_description_image_name_2.append("EMPTY")
                            self.ilias_test_question_description_image_uri_2.append("EMPTY")
                            self.ilias_test_question_description_image_name_3.append("EMPTY")
                            self.ilias_test_question_description_image_uri_3.append("EMPTY")







    ################# FRAGEN HAUPTATTRIBUTE AUSLESEN
            # Zu den Hauputattributen gehören z.B. "Fragen-Titel", "Fragen-Beschreibung", "Autor" etc.


            # Fragen-Titel auslesen
            for item in self.myroot.iter('item'):
                self.ilias_question_title.append(item.get('title'))

            # Fragen-Einleitungstext auslesen
            # Wenn der Eintrag nicht existiert, dann Eintrag erstellen und "" einfügen
            for qticomment in self.myroot.iter('qticomment'):
                if qticomment.text == None:
                    qticomment.text = ""

            for item in self.myroot.iter('item'):
                if "" in item.find('qticomment').text:
                    self.ilias_question_description_title.append(item.find('qticomment').text)


            # Test-Dauer auslesen (wenn Eintrag existiert
            for item in self.myroot.iter('item'):
                if "" in item.find('duration').text:
                    self.ilias_test_duration.append(item.find('duration').text)

            # Fragen-Autor auslesen
            for qtimetadatafield in self.myroot.iter('qtimetadatafield'):
                if qtimetadatafield.find('fieldlabel').text == "AUTHOR":
                    self.ilias_question_author.append(qtimetadatafield.find('fieldentry').text)


    ########### FRAGEN AUSLESEN JE NACH FRAGEN-TYP

            # Fragen auslesen: Single Choice
            if self.singlechoice_flag == 1:
                XML_Interface.read_singlechoice_questions(self)

            # Fragen auslesen: Formelfrage
            if self.formelfrage_flag == 1:
                XML_Interface.read_formelfrage_questions(self)

            # Fragen auslesen: Multiple Choice
            if self.multiplechoice_flag == 1:
                XML_Interface.read_multiplechoice_questions(self)

            # Fragen auslesen: Matching Question
            if self.matchingquestion_flag == 1:
                XML_Interface.read_matching_questions(self)


    ################ FRAGEN_BESCHREIBUNG (FRAGEN-TEXT) FILTERN
            # Single Choice Antworten entfernen
            for i in range(len(self.ilias_question_description_main)):
                for j in range(len(self.ilias_response_text)):
                    if self.ilias_question_description_main[i] == self.ilias_response_text[j]:
                        self.description_singlechoice_del_index.append(i)


            # Remove any dublicates, dict's können keine Elemente mehrfach besitzen. Daher werden alle doppelten Einträge entfernt
            # Doppelte Einträge entstehen wenn die Antwort bzw. die Beschreibung genau gleich lautet
            # Z.B. Zeigerdiagramm, Zeigerdiagramm
            self.description_singlechoice_del_index = list(dict.fromkeys(self.description_singlechoice_del_index))


            for i in range(len(self.description_singlechoice_del_index)):
                if len(self.description_singlechoice_del_index) > 0:
                    self.ilias_question_description_main.pop(self.description_singlechoice_del_index[i]-i)
                    self.ilias_test_question_description_image_name_1.pop(self.description_singlechoice_del_index[i]-i)
                    self.ilias_test_question_description_image_uri_1.pop(self.description_singlechoice_del_index[i]-i)


            # Multiple Choice Antworten entfernen
            for i in range(len(self.ilias_question_description_main)):
                for j in range(len(self.mattext_text_all_mc_answers)):
                    if self.ilias_question_description_main[i] == self.mattext_text_all_mc_answers[j]:
                        self.description_multiplechoice_del_index.append(i)

            for i in range(len(self.description_multiplechoice_del_index)):
                if len(self.description_multiplechoice_del_index) > 0:
                    self.ilias_question_description_main.pop(self.description_multiplechoice_del_index[i]-i)
                    self.ilias_test_question_description_image_name_1.pop(self.description_multiplechoice_del_index[i]-i)
                    self.ilias_test_question_description_image_uri_1.pop(self.description_multiplechoice_del_index[i]-i)



            # Matched Questions Antworten entfernen
            for i in range(len(self.ilias_question_description_main)):
                for j in range(len(self.mattText_text_all_mq_answers)):
                    if self.ilias_question_description_main[i] == self.mattText_text_all_mq_answers[j]:
                        self.description_matchedquestion_del_index.append(i)



            # Remove any dublicates, dict's können keine Elemente mehrfach besitzen. Daher werden alle doppelten Einträge entfernt
            # Doppelte Einträge entstehen wenn die Antwort bzw. die Beschreibung genau gleich lautet
            # Z.B. Zeigerdiagramm, Zeigerdiagramm
            self.description_matchedquestion_del_index = list(dict.fromkeys(self.description_matchedquestion_del_index))


            for i in range(len(self.description_matchedquestion_del_index)):
                if len(self.description_matchedquestion_del_index) > 0:
                    self.ilias_question_description_main.pop(self.description_matchedquestion_del_index[i]-i)
                    self.ilias_test_question_description_image_name_1.pop(self.description_matchedquestion_del_index[i]-i)
                    self.ilias_test_question_description_image_uri_1.pop(self.description_matchedquestion_del_index[i]-i)




        ########### FRAGEN IN DATENBANK SCHREIBEN
            # Schreiben
            # if self.singlechoice_flag == 1:
            #     XML_Interface.write_data_to_database_sc(self)
            if self.formelfrage_flag == 1:
                 XML_Interface.write_data_to_database_ff(self)
            # if self.multiplechoice_flag == 1:
            #     XML_Interface.write_data_to_database_mc(self)
            # if self.matchingquestion_flag == 1:
            #     XML_Interface.write_data_to_database_mq(self)




        ####### Single Choice Fragen
        def read_singlechoice_questions(self):


            # SINGLE CHOICE Punkte für Antworten
            for respcondition in self.myroot.iter('respcondition'):
                for varequal in respcondition.iter('varequal'):
                    if varequal.attrib.get('respident') == "MCSR":
                        for setvar in respcondition.iter('setvar'):
                            self.ilias_response_pts.append(setvar.text)

            # SINGLE CHOICE Antworten und Bilder
            for response_lid in self.myroot.iter('response_lid'):
                if response_lid.attrib.get('ident') == "MCSR":  # SR -> Single Choice
                    for render_choice in response_lid.iter('render_choice'):
                        for response_label in render_choice.iter('response_label'):
                            for material in response_label.iter('material'):
                                if material.find('matimage') == None:
                                    self.ilias_response_img_label.append("EMPTY")
                                    self.ilias_response_img_string_base64_encoded.append("EMPTY")

                                else:
                                    self.ilias_response_img_label.append(material.find('matimage').attrib.get('label'))
                                    self.ilias_response_img_string_base64_encoded.append(material.find('matimage').text)


                                for mattext in material.iter('mattext'):
                                    self.ilias_response_text.append(mattext.text)



            self.count=[]





    #####################################   Anzahl der Antworten pro SC-Frage
             # Durch diese Iteration und Abfrage nach MCSR (=Single Choice), werden alle Antworten der SC-Fragen aufgelistet
            for response_lid in self.myroot.iter('response_lid'):
                if response_lid.attrib.get('ident') == 'MCSR':
                    for render_choice in response_lid.iter('render_choice'):
                        # Zu Beginn jedes Anwort-Blocks wird ein "$" geschrieben, um hinterher zu splitten
                        self.sc_answer_list_nr += "$"
                        for response_label in render_choice.iter('response_label'):
                            self.sc_answer_list_nr += str(response_label.attrib.get('ident'))

            self.ilias_test_question_type_collection_sc_answers = self.sc_answer_list_nr.split("$")
            self.ilias_test_question_type_collection_sc_answers.pop(0)  # Durch split() enthält erstes Feld keine Daten

            for i in range(len(self.ilias_test_question_type_collection_sc_answers)):
                self.number_of_answers_per_question_sc.append(str( int(max(self.ilias_test_question_type_collection_sc_answers[i]))+1))




    #################################### Punkte für Fragen


    #####################################   Haupt-Fragentext aufzählen


            self.ilias_number_of_response_variables = 10
            self.ilias_response_text_1, self.ilias_response_pts_1, self.ilias_response_img_label_1, self.ilias_response_img_string_base64_encoded_1 = [], [], [], []
            self.ilias_response_text_2, self.ilias_response_pts_2, self.ilias_response_img_label_2, self.ilias_response_img_string_base64_encoded_2 = [], [], [], []
            self.ilias_response_text_3, self.ilias_response_pts_3, self.ilias_response_img_label_3, self.ilias_response_img_string_base64_encoded_3 = [], [], [], []
            self.ilias_response_text_4, self.ilias_response_pts_4, self.ilias_response_img_label_4, self.ilias_response_img_string_base64_encoded_4 = [], [], [], []
            self.ilias_response_text_5, self.ilias_response_pts_5, self.ilias_response_img_label_5, self.ilias_response_img_string_base64_encoded_5 = [], [], [], []
            self.ilias_response_text_6, self.ilias_response_pts_6, self.ilias_response_img_label_6, self.ilias_response_img_string_base64_encoded_6 = [], [], [], []
            self.ilias_response_text_7, self.ilias_response_pts_7, self.ilias_response_img_label_7, self.ilias_response_img_string_base64_encoded_7 = [], [], [], []
            self.ilias_response_text_8, self.ilias_response_pts_8, self.ilias_response_img_label_8, self.ilias_response_img_string_base64_encoded_8 = [], [], [], []
            self.ilias_response_text_9, self.ilias_response_pts_9, self.ilias_response_img_label_9, self.ilias_response_img_string_base64_encoded_9 = [], [], [], []
            self.ilias_response_text_10, self.ilias_response_pts_10, self.ilias_response_img_label_10, self.ilias_response_img_string_base64_encoded_10 = [], [], [], []




            t = 0
            for i in range(len(self.ilias_test_question_type_collection_sc_answers)):
                if i == 1:
                    t = int(max(self.ilias_test_question_type_collection_sc_answers[0])) + 1

                if "0" in self.ilias_test_question_type_collection_sc_answers[i]:
                    self.ilias_response_text_1.append(self.ilias_response_text[t])
                    self.ilias_response_pts_1.append(self.ilias_response_pts[t])
                    self.ilias_response_img_label_1.append(self.ilias_response_img_label[t])
                    self.ilias_response_img_string_base64_encoded_1.append(self.ilias_response_img_string_base64_encoded[t])
                else:
                    self.ilias_response_text_1.append(" ")
                    self.ilias_response_pts_1.append(" ")
                    self.ilias_response_img_label_1.append("EMPTY")
                    self.ilias_response_img_string_base64_encoded_1.append("EMPTY")

                if "1" in self.ilias_test_question_type_collection_sc_answers[i]:
                    self.ilias_response_text_2.append(self.ilias_response_text[t + 1])
                    self.ilias_response_pts_2.append(self.ilias_response_pts[t + 1])
                    self.ilias_response_img_label_2.append(self.ilias_response_img_label[t + 1])
                    self.ilias_response_img_string_base64_encoded_2.append(self.ilias_response_img_string_base64_encoded[t])
                else:
                    self.ilias_response_text_2.append(" ")
                    self.ilias_response_pts_2.append(" ")
                    self.ilias_response_img_label_2.append("EMPTY")
                    self.ilias_response_img_string_base64_encoded_2.append("EMPTY")

                if "2" in self.ilias_test_question_type_collection_sc_answers[i]:
                    self.ilias_response_text_3.append(self.ilias_response_text[t + 2])
                    self.ilias_response_pts_3.append(self.ilias_response_pts[t + 2])
                    self.ilias_response_img_label_3.append(self.ilias_response_img_label[t + 2])
                    self.ilias_response_img_string_base64_encoded_3.append(self.ilias_response_img_string_base64_encoded[t])
                else:
                    self.ilias_response_text_3.append(" ")
                    self.ilias_response_pts_3.append(" ")
                    self.ilias_response_img_label_3.append("EMPTY")
                    self.ilias_response_img_string_base64_encoded_3.append("EMPTY")

                if "3" in self.ilias_test_question_type_collection_sc_answers[i]:
                    self.ilias_response_text_4.append(self.ilias_response_text[t + 3])
                    self.ilias_response_pts_4.append(self.ilias_response_pts[t + 3])
                    self.ilias_response_img_label_4.append(self.ilias_response_img_label[t + 3])
                    self.ilias_response_img_string_base64_encoded_4.append(self.ilias_response_img_string_base64_encoded[t])
                else:
                    self.ilias_response_text_4.append(" ")
                    self.ilias_response_pts_4.append(" ")
                    self.ilias_response_img_label_4.append("EMPTY")
                    self.ilias_response_img_string_base64_encoded_4.append("EMPTY")

                if "4" in self.ilias_test_question_type_collection_sc_answers[i]:
                    self.ilias_response_text_5.append(self.ilias_response_text[t + 4])
                    self.ilias_response_pts_5.append(self.ilias_response_pts[t + 4])
                    self.ilias_response_img_label_5.append(self.ilias_response_img_label[t + 4])
                    self.ilias_response_img_string_base64_encoded_5.append(self.ilias_response_img_string_base64_encoded[t])
                else:
                    self.ilias_response_text_5.append(" ")
                    self.ilias_response_pts_5.append(" ")
                    self.ilias_response_img_label_5.append("EMPTY")
                    self.ilias_response_img_string_base64_encoded_5.append("EMPTY")

                if "5" in self.ilias_test_question_type_collection_sc_answers[i]:
                    self.ilias_response_text_6.append(self.ilias_response_text[t + 5])
                    self.ilias_response_pts_6.append(self.ilias_response_pts[t + 5])
                    self.ilias_response_img_label_6.append(self.ilias_response_img_label[t + 5])
                    self.ilias_response_img_string_base64_encoded_6.append(self.ilias_response_img_string_base64_encoded[t])
                else:
                    self.ilias_response_text_6.append(" ")
                    self.ilias_response_pts_6.append(" ")
                    self.ilias_response_img_label_6.append("EMPTY")
                    self.ilias_response_img_string_base64_encoded_6.append("EMPTY")

                if "6" in self.ilias_test_question_type_collection_sc_answers[i]:
                    self.ilias_response_text_7.append(self.ilias_response_text[t + 6])
                    self.ilias_response_pts_7.append(self.ilias_response_pts[t + 6])
                    self.ilias_response_img_label_7.append(self.ilias_response_img_label[t + 6])
                    self.ilias_response_img_string_base64_encoded_7.append(self.ilias_response_img_string_base64_encoded[t])
                else:
                    self.ilias_response_text_7.append(" ")
                    self.ilias_response_pts_7.append(" ")
                    self.ilias_response_img_label_7.append("EMPTY")
                    self.ilias_response_img_string_base64_encoded_7.append("EMPTY")

                if "7" in self.ilias_test_question_type_collection_sc_answers[i]:
                    self.ilias_response_text_8.append(self.ilias_response_text[t + 7])
                    self.ilias_response_pts_8.append(self.ilias_response_pts[t + 7])
                    self.ilias_response_img_label_8.append(self.ilias_response_img_label[t + 7])
                    self.ilias_response_img_string_base64_encoded_8.append(self.ilias_response_img_string_base64_encoded[t])
                else:
                    self.ilias_response_text_8.append(" ")
                    self.ilias_response_pts_8.append(" ")
                    self.ilias_response_img_label_8.append("EMPTY")
                    self.ilias_response_img_string_base64_encoded_8.append("EMPTY")

                if "8" in self.ilias_test_question_type_collection_sc_answers[i]:
                    self.ilias_response_text_9.append(self.ilias_response_text[t + 8])
                    self.ilias_response_pts_9.append(self.ilias_response_pts[t + 8])
                    self.ilias_response_img_label_9.append(self.ilias_response_img_label[t + 8])
                    self.ilias_response_img_string_base64_encoded_9.append(self.ilias_response_img_string_base64_encoded[t])
                else:
                    self.ilias_response_text_9.append(" ")
                    self.ilias_response_pts_9.append(" ")
                    self.ilias_response_img_label_9.append("EMPTY")
                    self.ilias_response_img_string_base64_encoded_9.append("EMPTY")

                if "9" in self.ilias_test_question_type_collection_sc_answers[i]:
                    self.ilias_response_text_10.append(self.ilias_response_text[t + 9])
                    self.ilias_response_pts_10.append(self.ilias_response_pts[t + 9])
                    self.ilias_response_img_label_10.append(self.ilias_response_img_label[t + 9])
                    self.ilias_response_img_string_base64_encoded_10.append(self.ilias_response_img_string_base64_encoded[t])
                else:
                    self.ilias_response_text_10.append(" ")
                    self.ilias_response_pts_10.append(" ")
                    self.ilias_response_img_label_10.append("EMPTY")
                    self.ilias_response_img_string_base64_encoded_10.append("EMPTY")

                t += int(max(self.ilias_test_question_type_collection_sc_answers[i])) + 1


    ####### Formelfragen
        def read_formelfrage_questions(self):

    ###########################################   INIT VARIABLES ###########################
            self.ilias_test_question_points = []

            ### Variable - Variablen - INIT
            self.ilias_test_variable1, self.ilias_test_variable1_prec, self.ilias_test_variable1_divby, self.ilias_test_variable1_min, self.ilias_test_variable1_max = [], [], [], [], []
            self.ilias_test_variable2, self.ilias_test_variable2_prec, self.ilias_test_variable2_divby, self.ilias_test_variable2_min, self.ilias_test_variable2_max = [], [], [], [], []
            self.ilias_test_variable3, self.ilias_test_variable3_prec, self.ilias_test_variable3_divby, self.ilias_test_variable3_min, self.ilias_test_variable3_max = [], [], [], [], []
            self.ilias_test_variable4, self.ilias_test_variable4_prec, self.ilias_test_variable4_divby, self.ilias_test_variable4_min, self.ilias_test_variable4_max = [], [], [], [], []
            self.ilias_test_variable5, self.ilias_test_variable5_prec, self.ilias_test_variable5_divby, self.ilias_test_variable5_min, self.ilias_test_variable5_max = [], [], [], [], []
            self.ilias_test_variable6, self.ilias_test_variable6_prec, self.ilias_test_variable6_divby, self.ilias_test_variable6_min, self.ilias_test_variable6_max = [], [], [], [], []
            self.ilias_test_variable7, self.ilias_test_variable7_prec, self.ilias_test_variable7_divby, self.ilias_test_variable7_min, self.ilias_test_variable7_max = [], [], [], [], []
            self.ilias_test_variable8, self.ilias_test_variable8_prec, self.ilias_test_variable8_divby, self.ilias_test_variable8_min, self.ilias_test_variable8_max = [], [], [], [], []
            self.ilias_test_variable9, self.ilias_test_variable9_prec, self.ilias_test_variable9_divby, self.ilias_test_variable9_min, self.ilias_test_variable9_max = [], [], [], [], []
            self.ilias_test_variable10, self.ilias_test_variable10_prec, self.ilias_test_variable10_divby, self.ilias_test_variable10_min, self.ilias_test_variable10_max = [], [], [], [], []
            self.ilias_test_variable11, self.ilias_test_variable11_prec, self.ilias_test_variable11_divby, self.ilias_test_variable11_min, self.ilias_test_variable11_max = [], [], [], [], []
            self.ilias_test_variable12, self.ilias_test_variable12_prec, self.ilias_test_variable12_divby, self.ilias_test_variable12_min, self.ilias_test_variable12_max = [], [], [], [], []
            self.ilias_test_variable13, self.ilias_test_variable13_prec, self.ilias_test_variable13_divby, self.ilias_test_variable13_min, self.ilias_test_variable13_max = [], [], [], [], []
            self.ilias_test_variable14, self.ilias_test_variable14_prec, self.ilias_test_variable14_divby, self.ilias_test_variable14_min, self.ilias_test_variable14_max = [], [], [], [], []
            self.ilias_test_variable15, self.ilias_test_variable15_prec, self.ilias_test_variable15_divby, self.ilias_test_variable15_min, self.ilias_test_variable15_max = [], [], [], [], []

            self.ilias_test_variable1_prec_temp, self.ilias_test_variable1_divby_temp, self.ilias_test_variable1_min_temp, self.ilias_test_variable1_max_temp = [], [], [], []
            self.ilias_test_variable2_prec_temp, self.ilias_test_variable2_divby_temp, self.ilias_test_variable2_min_temp, self.ilias_test_variable2_max_temp = [], [], [], []
            self.ilias_test_variable3_prec_temp, self.ilias_test_variable3_divby_temp, self.ilias_test_variable3_min_temp, self.ilias_test_variable3_max_temp = [], [], [], []
            self.ilias_test_variable4_prec_temp, self.ilias_test_variable4_divby_temp, self.ilias_test_variable4_min_temp, self.ilias_test_variable4_max_temp = [], [], [], []
            self.ilias_test_variable5_prec_temp, self.ilias_test_variable5_divby_temp, self.ilias_test_variable5_min_temp, self.ilias_test_variable5_max_temp = [], [], [], []
            self.ilias_test_variable6_prec_temp, self.ilias_test_variable6_divby_temp, self.ilias_test_variable6_min_temp, self.ilias_test_variable6_max_temp = [], [], [], []
            self.ilias_test_variable7_prec_temp, self.ilias_test_variable7_divby_temp, self.ilias_test_variable7_min_temp, self.ilias_test_variable7_max_temp = [], [], [], []
            self.ilias_test_variable8_prec_temp, self.ilias_test_variable8_divby_temp, self.ilias_test_variable8_min_temp, self.ilias_test_variable8_max_temp = [], [], [], []
            self.ilias_test_variable9_prec_temp, self.ilias_test_variable9_divby_temp, self.ilias_test_variable9_min_temp, self.ilias_test_variable9_max_temp = [], [], [], []
            self.ilias_test_variable10_prec_temp, self.ilias_test_variable10_divby_temp, self.ilias_test_variable10_min_temp, self.ilias_test_variable10_max_temp = [], [], [], []
            self.ilias_test_variable11_prec_temp, self.ilias_test_variable11_divby_temp, self.ilias_test_variable11_min_temp, self.ilias_test_variable11_max_temp = [], [], [], []
            self.ilias_test_variable12_prec_temp, self.ilias_test_variable12_divby_temp, self.ilias_test_variable12_min_temp, self.ilias_test_variable12_max_temp = [], [], [], []
            self.ilias_test_variable13_prec_temp, self.ilias_test_variable13_divby_temp, self.ilias_test_variable13_min_temp, self.ilias_test_variable13_max_temp = [], [], [], []
            self.ilias_test_variable14_prec_temp, self.ilias_test_variable14_divby_temp, self.ilias_test_variable14_min_temp, self.ilias_test_variable14_max_temp = [], [], [], []
            self.ilias_test_variable15_prec_temp, self.ilias_test_variable15_divby_temp, self.ilias_test_variable15_min_temp, self.ilias_test_variable15_max_temp = [], [], [], []

            self.ilias_test_variable1_settings, self.ilias_test_variable1_settings_temp = [], []
            self.ilias_test_variable2_settings, self.ilias_test_variable2_settings_temp = [], []
            self.ilias_test_variable3_settings, self.ilias_test_variable3_settings_temp = [], []
            self.ilias_test_variable4_settings, self.ilias_test_variable4_settings_temp = [], []
            self.ilias_test_variable5_settings, self.ilias_test_variable5_settings_temp = [], []
            self.ilias_test_variable6_settings, self.ilias_test_variable6_settings_temp = [], []
            self.ilias_test_variable7_settings, self.ilias_test_variable7_settings_temp = [], []
            self.ilias_test_variable8_settings, self.ilias_test_variable8_settings_temp = [], []
            self.ilias_test_variable9_settings, self.ilias_test_variable9_settings_temp = [], []
            self.ilias_test_variable10_settings, self.ilias_test_variable10_settings_temp = [], []
            self.ilias_test_variable11_settings, self.ilias_test_variable11_settings_temp = [], []
            self.ilias_test_variable12_settings, self.ilias_test_variable12_settings_temp = [], []
            self.ilias_test_variable13_settings, self.ilias_test_variable13_settings_temp = [], []
            self.ilias_test_variable14_settings, self.ilias_test_variable14_settings_temp = [], []
            self.ilias_test_variable15_settings, self.ilias_test_variable15_settings_temp = [], []

            ### Ergebnisse - Variablen - INIT
            self.ilias_test_result1, self.ilias_test_result1_prec, self.ilias_test_result1_tol, self.ilias_test_result1_min, self.ilias_test_result1_max, self.ilias_test_result1_pts, self.ilias_test_result1_formula = [], [], [], [], [], [], []
            self.ilias_test_result2, self.ilias_test_result2_prec, self.ilias_test_result2_tol, self.ilias_test_result2_min, self.ilias_test_result2_max, self.ilias_test_result2_pts, self.ilias_test_result2_formula = [], [], [], [], [], [], []
            self.ilias_test_result3, self.ilias_test_result3_prec, self.ilias_test_result3_tol, self.ilias_test_result3_min, self.ilias_test_result3_max, self.ilias_test_result3_pts, self.ilias_test_result3_formula = [], [], [], [], [], [], []
            self.ilias_test_result4, self.ilias_test_result4_prec, self.ilias_test_result4_tol, self.ilias_test_result4_min, self.ilias_test_result4_max, self.ilias_test_result4_pts, self.ilias_test_result4_formula = [], [], [], [], [], [], []
            self.ilias_test_result5, self.ilias_test_result5_prec, self.ilias_test_result5_tol, self.ilias_test_result5_min, self.ilias_test_result5_max, self.ilias_test_result5_pts, self.ilias_test_result5_formula = [], [], [], [], [], [], []
            self.ilias_test_result6, self.ilias_test_result6_prec, self.ilias_test_result6_tol, self.ilias_test_result6_min, self.ilias_test_result6_max, self.ilias_test_result6_pts, self.ilias_test_result6_formula = [], [], [], [], [], [], []
            self.ilias_test_result7, self.ilias_test_result7_prec, self.ilias_test_result7_tol, self.ilias_test_result7_min, self.ilias_test_result7_max, self.ilias_test_result7_pts, self.ilias_test_result7_formula = [], [], [], [], [], [], []
            self.ilias_test_result8, self.ilias_test_result8_prec, self.ilias_test_result8_tol, self.ilias_test_result8_min, self.ilias_test_result8_max, self.ilias_test_result8_pts, self.ilias_test_result8_formula = [], [], [], [], [], [], []
            self.ilias_test_result9, self.ilias_test_result9_prec, self.ilias_test_result9_tol, self.ilias_test_result9_min, self.ilias_test_result9_max, self.ilias_test_result9_pts, self.ilias_test_result9_formula = [], [], [], [], [], [], []
            self.ilias_test_result10, self.ilias_test_result10_prec, self.ilias_test_result10_tol, self.ilias_test_result10_min, self.ilias_test_result10_max, self.ilias_test_result10_pts, self.ilias_test_result10_formula = [], [], [], [], [], [], []

            self.ilias_test_result1_temp, self.ilias_test_result1_prec_temp, self.ilias_test_result1_tol_temp, self.ilias_test_result1_min_temp, self.ilias_test_result1_max_temp, self.ilias_test_result1_pts_temp, self.ilias_test_result1_formula_temp = [], [], [], [], [], [], []
            self.ilias_test_result2_temp, self.ilias_test_result2_prec_temp, self.ilias_test_result2_tol_temp, self.ilias_test_result2_min_temp, self.ilias_test_result2_max_temp, self.ilias_test_result2_pts_temp, self.ilias_test_result2_formula_temp = [], [], [], [], [], [], []
            self.ilias_test_result3_temp, self.ilias_test_result3_prec_temp, self.ilias_test_result3_tol_temp, self.ilias_test_result3_min_temp, self.ilias_test_result3_max_temp, self.ilias_test_result3_pts_temp, self.ilias_test_result3_formula_temp = [], [], [], [], [], [], []
            self.ilias_test_result4_temp, self.ilias_test_result4_prec_temp, self.ilias_test_result4_tol_temp, self.ilias_test_result4_min_temp, self.ilias_test_result4_max_temp, self.ilias_test_result4_pts_temp, self.ilias_test_result4_formula_temp = [], [], [], [], [], [], []
            self.ilias_test_result5_temp, self.ilias_test_result5_prec_temp, self.ilias_test_result5_tol_temp, self.ilias_test_result5_min_temp, self.ilias_test_result5_max_temp, self.ilias_test_result5_pts_temp, self.ilias_test_result5_formula_temp = [], [], [], [], [], [], []
            self.ilias_test_result6_temp, self.ilias_test_result6_prec_temp, self.ilias_test_result6_tol_temp, self.ilias_test_result6_min_temp, self.ilias_test_result6_max_temp, self.ilias_test_result6_pts_temp, self.ilias_test_result6_formula_temp = [], [], [], [], [], [], []
            self.ilias_test_result7_temp, self.ilias_test_result7_prec_temp, self.ilias_test_result7_tol_temp, self.ilias_test_result7_min_temp, self.ilias_test_result7_max_temp, self.ilias_test_result7_pts_temp, self.ilias_test_result7_formula_temp = [], [], [], [], [], [], []
            self.ilias_test_result8_temp, self.ilias_test_result8_prec_temp, self.ilias_test_result8_tol_temp, self.ilias_test_result8_min_temp, self.ilias_test_result8_max_temp, self.ilias_test_result8_pts_temp, self.ilias_test_result8_formula_temp = [], [], [], [], [], [], []
            self.ilias_test_result9_temp, self.ilias_test_result9_prec_temp, self.ilias_test_result9_tol_temp, self.ilias_test_result9_min_temp, self.ilias_test_result9_max_temp, self.ilias_test_result9_pts_temp, self.ilias_test_result9_formula_temp = [], [], [], [], [], [], []
            self.ilias_test_result10_temp, self.ilias_test_result10_prec_temp, self.ilias_test_result10_tol_temp, self.ilias_test_result10_min_temp, self.ilias_test_result10_max_temp, self.ilias_test_result10_pts_temp, self.ilias_test_result10_formula_temp = [], [], [], [], [], [], []


            self.ilias_test_result1_settings, self.ilias_test_result1_settings_temp = [], []
            self.ilias_test_result2_settings, self.ilias_test_result2_settings_temp = [], []
            self.ilias_test_result3_settings, self.ilias_test_result3_settings_temp = [], []
            self.ilias_test_result4_settings, self.ilias_test_result4_settings_temp = [], []
            self.ilias_test_result5_settings, self.ilias_test_result5_settings_temp = [], []
            self.ilias_test_result6_settings, self.ilias_test_result6_settings_temp = [], []
            self.ilias_test_result7_settings, self.ilias_test_result7_settings_temp = [], []
            self.ilias_test_result8_settings, self.ilias_test_result8_settings_temp = [], []
            self.ilias_test_result9_settings, self.ilias_test_result9_settings_temp = [], []
            self.ilias_test_result10_settings, self.ilias_test_result10_settings_temp = [], []




            self.ilias_question_type_ff_question_index = []

            self.variables_collection_string = ""
            self.result_collection_string = ""
            self.variables_collection_list = []
            self.result_collection_list = []

    ################################ VARIABLEN FÜLLEN AUS XML DATEI #########################
            for qtimetadatafield in self.myroot.iter('qtimetadatafield'):

                # "$" Zeichen werden eingefügt wenn eine neue Frage gefunden wird ("assFormuaQuestion")
                # Später wird der String an den "$" getrennt um die Variablen pro Frage anzuzeigen
                if qtimetadatafield.find('fieldentry').text == "assFormulaQuestion":
                    self.variables_collection_string += '$'
                    self.result_collection_string += '$'

                #if qtimetadatafield.find('fieldlabel').text == "QUESTIONTYPE":
                #    self.ilias_question_type.append(qtimetadatafield.find('fieldentry').text)

                if qtimetadatafield.find('fieldlabel').text == "points":
                    self.ilias_test_question_points.append(qtimetadatafield.find('fieldentry').text)

                if qtimetadatafield.find('fieldlabel').text == "$v1":
                    self.ilias_test_variable1.append(qtimetadatafield.find('fieldentry').text)
                    self.variables_collection_string += 'v1'

                if qtimetadatafield.find('fieldlabel').text == "$v2":
                    self.ilias_test_variable2.append(qtimetadatafield.find('fieldentry').text)
                    self.variables_collection_string += 'v2'

                if qtimetadatafield.find('fieldlabel').text == "$v3":
                    self.ilias_test_variable3.append(qtimetadatafield.find('fieldentry').text)
                    self.variables_collection_string += 'v3'

                if qtimetadatafield.find('fieldlabel').text == "$v4":
                    self.ilias_test_variable4.append(qtimetadatafield.find('fieldentry').text)
                    self.variables_collection_string += 'v4'

                if qtimetadatafield.find('fieldlabel').text == "$v5":
                    self.ilias_test_variable5.append(qtimetadatafield.find('fieldentry').text)
                    self.variables_collection_string += 'v5'

                if qtimetadatafield.find('fieldlabel').text == "$v6":
                    self.ilias_test_variable6.append(qtimetadatafield.find('fieldentry').text)
                    self.variables_collection_string += 'v6'

                if qtimetadatafield.find('fieldlabel').text == "$v7":
                    self.ilias_test_variable7.append(qtimetadatafield.find('fieldentry').text)
                    self.variables_collection_string += 'v7'

                if qtimetadatafield.find('fieldlabel').text == "$v8":
                    self.ilias_test_variable8.append(qtimetadatafield.find('fieldentry').text)
                    self.variables_collection_string += 'v8'

                if qtimetadatafield.find('fieldlabel').text == "$v9":
                    self.ilias_test_variable9.append(qtimetadatafield.find('fieldentry').text)
                    self.variables_collection_string += 'v9'

                if qtimetadatafield.find('fieldlabel').text == "$v10":
                    self.ilias_test_variable10.append(qtimetadatafield.find('fieldentry').text)
                    self.variables_collection_string += 'v10'

                if qtimetadatafield.find('fieldlabel').text == "$v11":
                    self.ilias_test_variable11.append(qtimetadatafield.find('fieldentry').text)
                    self.variables_collection_string += 'v11'

                if qtimetadatafield.find('fieldlabel').text == "$v12":
                    self.ilias_test_variable12.append(qtimetadatafield.find('fieldentry').text)
                    self.variables_collection_string += 'v12'

                if qtimetadatafield.find('fieldlabel').text == "$v13":
                    self.ilias_test_variable13.append(qtimetadatafield.find('fieldentry').text)
                    self.variables_collection_string += 'v13'

                if qtimetadatafield.find('fieldlabel').text == "$v14":
                    self.ilias_test_variable14.append(qtimetadatafield.find('fieldentry').text)
                    self.variables_collection_string += 'v14'

                if qtimetadatafield.find('fieldlabel').text == "$v15":
                    self.ilias_test_variable15.append(qtimetadatafield.find('fieldentry').text)
                    self.variables_collection_string += 'v15'

                if qtimetadatafield.find('fieldlabel').text == "$r1":
                    self.ilias_test_result1.append(qtimetadatafield.find('fieldentry').text)
                    self.result_collection_string += 'r1'

                if qtimetadatafield.find('fieldlabel').text == "$r2":
                    self.ilias_test_result2.append(qtimetadatafield.find('fieldentry').text)
                    self.result_collection_string += 'r2'

                if qtimetadatafield.find('fieldlabel').text == "$r3":
                    self.ilias_test_result3.append(qtimetadatafield.find('fieldentry').text)
                    self.result_collection_string += 'r3'

                if qtimetadatafield.find('fieldlabel').text == "$r4":
                    self.ilias_test_result4.append(qtimetadatafield.find('fieldentry').text)
                    self.result_collection_string += 'r4'

                if qtimetadatafield.find('fieldlabel').text == "$r5":
                    self.ilias_test_result5.append(qtimetadatafield.find('fieldentry').text)
                    self.result_collection_string += 'r5'

                if qtimetadatafield.find('fieldlabel').text == "$r6":
                    self.ilias_test_result6.append(qtimetadatafield.find('fieldentry').text)
                    self.result_collection_string += 'r6'

                if qtimetadatafield.find('fieldlabel').text == "$r7":
                    self.ilias_test_result7.append(qtimetadatafield.find('fieldentry').text)
                    self.result_collection_string += 'r7'

                if qtimetadatafield.find('fieldlabel').text == "$r8":
                    self.ilias_test_result8.append(qtimetadatafield.find('fieldentry').text)
                    self.result_collection_string += 'r8'

                if qtimetadatafield.find('fieldlabel').text == "$r9":
                    self.ilias_test_result9.append(qtimetadatafield.find('fieldentry').text)
                    self.result_collection_string += 'r9'

                if qtimetadatafield.find('fieldlabel').text == "$r10":
                    self.ilias_test_result10.append(qtimetadatafield.find('fieldentry').text)
                    self.result_collection_string += 'r10'

            #### XML durchsuchen und Fragentyp (FF,SC,MC,MQ) nach "Formelfrage" durchsuchen
            #### assFormulaQuestion ist vom ilias codiert für "Formelfrage"
            for i in range(len(self.ilias_question_type)):
                if self.ilias_question_type[i] == "assFormulaQuestion":
                    self.ilias_question_type_ff_question_index.append(str(i))



            # Liste Variable 1 - Werte auftrennen nach ";"
            # Der Eintrag für die "Settings" einer Variablen in der XML Datei sieht wie folgt aus:
            # <fieldentry>a:6:{s:9:"precision";i:1;s:12:"intprecision";  s:1:"1";s:8:"rangemin";  d:1;s:8:"rangemax";  d:10;s:4:"unit";  s:0:"";s:9:"unitvalue";s:0:"";  }</fieldentry>




            for i in range(len(self.ilias_test_variable1)):
                self.ilias_test_variable1_settings += self.ilias_test_variable1[i].split(";")

            for i in range(len(self.ilias_test_variable2)):
                self.ilias_test_variable2_settings += self.ilias_test_variable2[i].split(";")

            for i in range(len(self.ilias_test_variable3)):
                self.ilias_test_variable3_settings += self.ilias_test_variable3[i].split(";")

            for i in range(len(self.ilias_test_variable4)):
                self.ilias_test_variable4_settings += self.ilias_test_variable4[i].split(";")

            for i in range(len(self.ilias_test_variable5)):
                self.ilias_test_variable5_settings += self.ilias_test_variable5[i].split(";")

            for i in range(len(self.ilias_test_variable6)):
                self.ilias_test_variable6_settings += self.ilias_test_variable6[i].split(";")

            for i in range(len(self.ilias_test_variable7)):
                self.ilias_test_variable7_settings += self.ilias_test_variable7[i].split(";")

            for i in range(len(self.ilias_test_variable8)):
                self.ilias_test_variable8_settings += self.ilias_test_variable8[i].split(";")

            for i in range(len(self.ilias_test_variable9)):
                self.ilias_test_variable9_settings += self.ilias_test_variable9[i].split(";")

            for i in range(len(self.ilias_test_variable10)):
                self.ilias_test_variable10_settings += self.ilias_test_variable10[i].split(";")

            for i in range(len(self.ilias_test_variable11)):
                self.ilias_test_variable11_settings += self.ilias_test_variable11[i].split(";")

            for i in range(len(self.ilias_test_variable12)):
                self.ilias_test_variable12_settings += self.ilias_test_variable12[i].split(";")

            for i in range(len(self.ilias_test_variable13)):
                self.ilias_test_variable13_settings += self.ilias_test_variable13[i].split(";")

            for i in range(len(self.ilias_test_variable14)):
                self.ilias_test_variable14_settings += self.ilias_test_variable14[i].split(";")

            for i in range(len(self.ilias_test_variable15)):
                self.ilias_test_variable15_settings += self.ilias_test_variable15[i].split(";")



            for i in range(len(self.ilias_test_result1)):
                self.ilias_test_result1_settings += self.ilias_test_result1[i].split(";")

            for i in range(len(self.ilias_test_result2)):
                self.ilias_test_result2_settings += self.ilias_test_result2[i].split(";")

            for i in range(len(self.ilias_test_result3)):
                self.ilias_test_result3_settings += self.ilias_test_result3[i].split(";")

            for i in range(len(self.ilias_test_result4)):
                self.ilias_test_result4_settings += self.ilias_test_result4[i].split(";")

            for i in range(len(self.ilias_test_result5)):
                self.ilias_test_result5_settings += self.ilias_test_result5[i].split(";")

            for i in range(len(self.ilias_test_result6)):
                self.ilias_test_result6_settings += self.ilias_test_result6[i].split(";")

            for i in range(len(self.ilias_test_result7)):
                self.ilias_test_result7_settings += self.ilias_test_result7[i].split(";")

            for i in range(len(self.ilias_test_result8)):
                self.ilias_test_result8_settings += self.ilias_test_result8[i].split(";")

            for i in range(len(self.ilias_test_result9)):
                self.ilias_test_result9_settings += self.ilias_test_result9[i].split(";")

            for i in range(len(self.ilias_test_result10)):
                self.ilias_test_result10_settings += self.ilias_test_result10[i].split(";")




            # Lösche Fach 12 und danach jedes 13te Feld
            # Diese Felder enthalten keine Informationen. Der String schließt mit "unitvalue";s:0:"";} ab und die gelöschten Felder
            # enthalten den "Wert zwischen ; und } und sind unbrauchbar.
            del self.ilias_test_variable1_settings[12::13]
            del self.ilias_test_variable2_settings[12::13]
            del self.ilias_test_variable3_settings[12::13]
            del self.ilias_test_variable4_settings[12::13]
            del self.ilias_test_variable5_settings[12::13]
            del self.ilias_test_variable6_settings[12::13]
            del self.ilias_test_variable7_settings[12::13]
            del self.ilias_test_variable8_settings[12::13]
            del self.ilias_test_variable9_settings[12::13]
            del self.ilias_test_variable10_settings[12::13]
            del self.ilias_test_variable11_settings[12::13]
            del self.ilias_test_variable12_settings[12::13]
            del self.ilias_test_variable13_settings[12::13]
            del self.ilias_test_variable14_settings[12::13]
            del self.ilias_test_variable15_settings[12::13]


            # Erstes Feld löschen, dann enthält jedes 2. Fach der eigentliche Wert für die jeweilige Einstellung z.B. Präzision
            if len(self.ilias_test_variable1_settings) > 0:
                self.ilias_test_variable1_settings.pop(0)

            if len(self.ilias_test_variable2_settings) > 0:
                self.ilias_test_variable2_settings.pop(0)

            if len(self.ilias_test_variable3_settings) > 0:
                self.ilias_test_variable3_settings.pop(0)

            if len(self.ilias_test_variable4_settings) > 0:
                self.ilias_test_variable4_settings.pop(0)

            if len(self.ilias_test_variable5_settings) > 0:
                self.ilias_test_variable5_settings.pop(0)

            if len(self.ilias_test_variable6_settings) > 0:
                self.ilias_test_variable6_settings.pop(0)

            if len(self.ilias_test_variable7_settings) > 0:
                self.ilias_test_variable7_settings.pop(0)

            if len(self.ilias_test_variable8_settings) > 0:
                self.ilias_test_variable8_settings.pop(0)

            if len(self.ilias_test_variable9_settings) > 0:
                self.ilias_test_variable9_settings.pop(0)

            if len(self.ilias_test_variable10_settings) > 0:
                self.ilias_test_variable10_settings.pop(0)

            if len(self.ilias_test_variable11_settings) > 0:
                self.ilias_test_variable11_settings.pop(0)

            if len(self.ilias_test_variable12_settings) > 0:
                self.ilias_test_variable12_settings.pop(0)

            if len(self.ilias_test_variable13_settings) > 0:
                self.ilias_test_variable13_settings.pop(0)

            if len(self.ilias_test_variable14_settings) > 0:
                self.ilias_test_variable14_settings.pop(0)

            if len(self.ilias_test_variable15_settings) > 0:
                self.ilias_test_variable15_settings.pop(0)

            # jedes 2. Fach enthält den eigentlichen Wert für die jeweilige Einstellung z.B. Präzision
            # die
            self.ilias_test_variable1_settings_temp = self.ilias_test_variable1_settings[::2]
            self.ilias_test_variable2_settings_temp = self.ilias_test_variable2_settings[::2]
            self.ilias_test_variable3_settings_temp = self.ilias_test_variable3_settings[::2]
            self.ilias_test_variable4_settings_temp = self.ilias_test_variable4_settings[::2]
            self.ilias_test_variable5_settings_temp = self.ilias_test_variable5_settings[::2]
            self.ilias_test_variable6_settings_temp = self.ilias_test_variable6_settings[::2]
            self.ilias_test_variable7_settings_temp = self.ilias_test_variable7_settings[::2]
            self.ilias_test_variable8_settings_temp = self.ilias_test_variable8_settings[::2]
            self.ilias_test_variable9_settings_temp = self.ilias_test_variable9_settings[::2]
            self.ilias_test_variable10_settings_temp = self.ilias_test_variable10_settings[::2]
            self.ilias_test_variable11_settings_temp = self.ilias_test_variable11_settings[::2]
            self.ilias_test_variable12_settings_temp = self.ilias_test_variable12_settings[::2]
            self.ilias_test_variable13_settings_temp = self.ilias_test_variable13_settings[::2]
            self.ilias_test_variable14_settings_temp = self.ilias_test_variable14_settings[::2]
            self.ilias_test_variable15_settings_temp = self.ilias_test_variable15_settings[::2]


            self.variables_collection_list = self.variables_collection_string.split('$')
            self.variables_collection_list.pop(0)
            self.result_collection_list = self.result_collection_string.split('$')
            self.result_collection_list.pop(0)

            self.var1_count = 0
            self.var2_count = 0
            self.var3_count = 0
            self.var4_count = 0
            self.var5_count = 0
            self.var6_count = 0
            self.var7_count = 0
            self.var8_count = 0
            self.var9_count = 0
            self.var10_count = 0
            self.var11_count = 0
            self.var12_count = 0
            self.var13_count = 0
            self.var14_count = 0
            self.var15_count = 0

            self.ilias_test_variable1_prec, self.ilias_test_variable1_divby, self.ilias_test_variable1_min,  self.ilias_test_variable1_max, self.var1_count = XML_Interface.append_data_to_var_of_ff_question_type(self, self.var1_count, self.ilias_test_variable1_settings_temp, "v1")
            self.ilias_test_variable2_prec, self.ilias_test_variable2_divby, self.ilias_test_variable2_min,  self.ilias_test_variable2_max, self.var2_count = XML_Interface.append_data_to_var_of_ff_question_type(self, self.var2_count, self.ilias_test_variable2_settings_temp, "v2")
            self.ilias_test_variable3_prec, self.ilias_test_variable3_divby, self.ilias_test_variable3_min,  self.ilias_test_variable3_max, self.var3_count = XML_Interface.append_data_to_var_of_ff_question_type(self, self.var3_count, self.ilias_test_variable3_settings_temp, "v3")
            self.ilias_test_variable4_prec, self.ilias_test_variable4_divby, self.ilias_test_variable4_min,  self.ilias_test_variable4_max, self.var4_count = XML_Interface.append_data_to_var_of_ff_question_type(self, self.var4_count, self.ilias_test_variable4_settings_temp, "v4")
            self.ilias_test_variable5_prec, self.ilias_test_variable5_divby, self.ilias_test_variable5_min,  self.ilias_test_variable5_max, self.var5_count = XML_Interface.append_data_to_var_of_ff_question_type(self, self.var5_count, self.ilias_test_variable5_settings_temp, "v5")
            self.ilias_test_variable6_prec, self.ilias_test_variable6_divby, self.ilias_test_variable6_min,  self.ilias_test_variable6_max, self.var6_count = XML_Interface.append_data_to_var_of_ff_question_type(self, self.var6_count, self.ilias_test_variable6_settings_temp, "v6")
            self.ilias_test_variable7_prec, self.ilias_test_variable7_divby, self.ilias_test_variable7_min,  self.ilias_test_variable7_max, self.var7_count = XML_Interface.append_data_to_var_of_ff_question_type(self, self.var7_count, self.ilias_test_variable7_settings_temp, "v7")
            self.ilias_test_variable8_prec, self.ilias_test_variable8_divby, self.ilias_test_variable8_min,  self.ilias_test_variable8_max, self.var8_count = XML_Interface.append_data_to_var_of_ff_question_type(self, self.var8_count, self.ilias_test_variable8_settings_temp, "v8")
            self.ilias_test_variable9_prec, self.ilias_test_variable9_divby, self.ilias_test_variable9_min,  self.ilias_test_variable9_max, self.var9_count = XML_Interface.append_data_to_var_of_ff_question_type(self, self.var9_count, self.ilias_test_variable9_settings_temp, "v9")
            self.ilias_test_variable10_prec, self.ilias_test_variable10_divby, self.ilias_test_variable10_min,  self.ilias_test_variable10_max, self.var10_count = XML_Interface.append_data_to_var_of_ff_question_type(self, self.var10_count, self.ilias_test_variable10_settings_temp, "v10")
            self.ilias_test_variable11_prec, self.ilias_test_variable11_divby, self.ilias_test_variable11_min,  self.ilias_test_variable11_max, self.var11_count = XML_Interface.append_data_to_var_of_ff_question_type(self, self.var11_count, self.ilias_test_variable11_settings_temp, "v11")
            self.ilias_test_variable12_prec, self.ilias_test_variable12_divby, self.ilias_test_variable12_min,  self.ilias_test_variable12_max, self.var12_count = XML_Interface.append_data_to_var_of_ff_question_type(self, self.var12_count, self.ilias_test_variable12_settings_temp, "v12")
            self.ilias_test_variable13_prec, self.ilias_test_variable13_divby, self.ilias_test_variable13_min,  self.ilias_test_variable13_max, self.var13_count = XML_Interface.append_data_to_var_of_ff_question_type(self, self.var13_count, self.ilias_test_variable13_settings_temp, "v13")
            self.ilias_test_variable14_prec, self.ilias_test_variable14_divby, self.ilias_test_variable14_min,  self.ilias_test_variable14_max, self.var14_count = XML_Interface.append_data_to_var_of_ff_question_type(self, self.var14_count, self.ilias_test_variable14_settings_temp, "v14")
            self.ilias_test_variable15_prec, self.ilias_test_variable15_divby, self.ilias_test_variable15_min,  self.ilias_test_variable15_max, self.var15_count = XML_Interface.append_data_to_var_of_ff_question_type(self, self.var15_count, self.ilias_test_variable15_settings_temp, "v15")



            # Ergebnis String auslesen



            if len(self.ilias_test_result1_settings) > 0:
                self.ilias_test_result1_settings.pop(0)

            if len(self.ilias_test_result2_settings) > 0:
                self.ilias_test_result2_settings.pop(0)

            if len(self.ilias_test_result3_settings) > 0:
                self.ilias_test_result3_settings.pop(0)

            if len(self.ilias_test_result4_settings) > 0:
                self.ilias_test_result4_settings.pop(0)

            if len(self.ilias_test_result5_settings) > 0:
                self.ilias_test_result5_settings.pop(0)

            if len(self.ilias_test_result6_settings) > 0:
                self.ilias_test_result6_settings.pop(0)

            if len(self.ilias_test_result7_settings) > 0:
                self.ilias_test_result7_settings.pop(0)

            if len(self.ilias_test_result8_settings) > 0:
                self.ilias_test_result8_settings.pop(0)

            if len(self.ilias_test_result9_settings) > 0:
                self.ilias_test_result9_settings.pop(0)

            if len(self.ilias_test_result10_settings) > 0:
                self.ilias_test_result10_settings.pop(0)


            self.ilias_test_result1_settings_temp = self.ilias_test_result1_settings[::2]
            self.ilias_test_result2_settings_temp = self.ilias_test_result2_settings[::2]
            self.ilias_test_result3_settings_temp = self.ilias_test_result3_settings[::2]
            self.ilias_test_result4_settings_temp = self.ilias_test_result4_settings[::2]
            self.ilias_test_result5_settings_temp = self.ilias_test_result5_settings[::2]
            self.ilias_test_result6_settings_temp = self.ilias_test_result6_settings[::2]
            self.ilias_test_result7_settings_temp = self.ilias_test_result7_settings[::2]
            self.ilias_test_result8_settings_temp = self.ilias_test_result8_settings[::2]
            self.ilias_test_result9_settings_temp = self.ilias_test_result9_settings[::2]
            self.ilias_test_result10_settings_temp = self.ilias_test_result10_settings[::2]



            for i in range(len(self.ilias_test_result1_settings_temp)):
                self.ilias_test_result1_settings_temp[i] = self.ilias_test_result1_settings_temp[i].replace('"', '')

            for i in range(len(self.ilias_test_result2_settings_temp)):
                self.ilias_test_result2_settings_temp[i] = self.ilias_test_result2_settings_temp[i].replace('"', '')

            for i in range(len(self.ilias_test_result3_settings_temp)):
                self.ilias_test_result3_settings_temp[i] = self.ilias_test_result3_settings_temp[i].replace('"', '')

            for i in range(len(self.ilias_test_result4_settings_temp)):
                self.ilias_test_result4_settings_temp[i] = self.ilias_test_result4_settings_temp[i].replace('"', '')

            for i in range(len(self.ilias_test_result5_settings_temp)):
                self.ilias_test_result5_settings_temp[i] = self.ilias_test_result5_settings_temp[i].replace('"', '')

            for i in range(len(self.ilias_test_result6_settings_temp)):
                self.ilias_test_result6_settings_temp[i] = self.ilias_test_result6_settings_temp[i].replace('"', '')

            for i in range(len(self.ilias_test_result7_settings_temp)):
                self.ilias_test_result7_settings_temp[i] = self.ilias_test_result7_settings_temp[i].replace('"', '')

            for i in range(len(self.ilias_test_result8_settings_temp)):
                self.ilias_test_result8_settings_temp[i] = self.ilias_test_result8_settings_temp[i].replace('"', '')

            for i in range(len(self.ilias_test_result9_settings_temp)):
                self.ilias_test_result9_settings_temp[i] = self.ilias_test_result9_settings_temp[i].replace('"', '')

            for i in range(len(self.ilias_test_result10_settings_temp)):
                self.ilias_test_result10_settings_temp[i] = self.ilias_test_result10_settings_temp[i].replace('"', '')


            self.res1_count = 0
            self.res2_count = 0
            self.res3_count = 0
            self.res4_count = 0
            self.res5_count = 0
            self.res6_count = 0
            self.res7_count = 0
            self.res8_count = 0
            self.res9_count = 0
            self.res10_count = 0

            self.ilias_test_result1_prec, self.ilias_test_result1_tol, self.ilias_test_result1_min,  self.ilias_test_result1_max, self.ilias_test_result1_pts, self.ilias_test_result1_formula, self.res1_count = XML_Interface.append_data_to_res_of_ff_question_type(self, self.res1_count, self.ilias_test_result1_settings_temp, "r1")
            self.ilias_test_result2_prec, self.ilias_test_result2_tol, self.ilias_test_result2_min,  self.ilias_test_result2_max, self.ilias_test_result2_pts, self.ilias_test_result2_formula, self.res2_count = XML_Interface.append_data_to_res_of_ff_question_type(self, self.res2_count, self.ilias_test_result2_settings_temp, "r2")
            self.ilias_test_result3_prec, self.ilias_test_result3_tol, self.ilias_test_result3_min,  self.ilias_test_result3_max, self.ilias_test_result3_pts, self.ilias_test_result3_formula, self.res3_count = XML_Interface.append_data_to_res_of_ff_question_type(self, self.res3_count, self.ilias_test_result3_settings_temp, "r3")
            self.ilias_test_result4_prec, self.ilias_test_result4_tol, self.ilias_test_result4_min,  self.ilias_test_result4_max, self.ilias_test_result4_pts, self.ilias_test_result4_formula, self.res4_count = XML_Interface.append_data_to_res_of_ff_question_type(self, self.res4_count, self.ilias_test_result4_settings_temp, "r4")
            self.ilias_test_result5_prec, self.ilias_test_result5_tol, self.ilias_test_result5_min,  self.ilias_test_result5_max, self.ilias_test_result5_pts, self.ilias_test_result5_formula, self.res5_count = XML_Interface.append_data_to_res_of_ff_question_type(self, self.res5_count, self.ilias_test_result5_settings_temp, "r5")
            self.ilias_test_result6_prec, self.ilias_test_result6_tol, self.ilias_test_result6_min,  self.ilias_test_result6_max, self.ilias_test_result6_pts, self.ilias_test_result6_formula, self.res6_count = XML_Interface.append_data_to_res_of_ff_question_type(self, self.res6_count, self.ilias_test_result6_settings_temp, "r6")
            self.ilias_test_result7_prec, self.ilias_test_result7_tol, self.ilias_test_result7_min,  self.ilias_test_result7_max, self.ilias_test_result7_pts, self.ilias_test_result7_formula, self.res7_count = XML_Interface.append_data_to_res_of_ff_question_type(self, self.res7_count, self.ilias_test_result7_settings_temp, "r7")
            self.ilias_test_result8_prec, self.ilias_test_result8_tol, self.ilias_test_result8_min,  self.ilias_test_result8_max, self.ilias_test_result8_pts, self.ilias_test_result8_formula, self.res8_count = XML_Interface.append_data_to_res_of_ff_question_type(self, self.res8_count, self.ilias_test_result8_settings_temp, "r8")
            self.ilias_test_result9_prec, self.ilias_test_result9_tol, self.ilias_test_result9_min,  self.ilias_test_result9_max, self.ilias_test_result9_pts, self.ilias_test_result9_formula, self.res9_count = XML_Interface.append_data_to_res_of_ff_question_type(self, self.res9_count, self.ilias_test_result9_settings_temp, "r9")
            self.ilias_test_result10_prec, self.ilias_test_result10_tol, self.ilias_test_result10_min,  self.ilias_test_result10_max, self.ilias_test_result10_pts, self.ilias_test_result10_formula, self.res10_count = XML_Interface.append_data_to_res_of_ff_question_type(self, self.res10_count, self.ilias_test_result10_settings_temp, "r10")






            self.ilias_question_description_main = XML_Interface.split_description_main_from_img(self, self.ilias_question_description_main)

        def append_data_to_var_of_ff_question_type(self, var_count, var_settings_temp, var_id ):
            self.var_prec, self.var_prec_temp = [], []
            self.var_min, self.var_min_temp = [], []
            self.var_max, self.var_max_temp = [], []
            self.var_divby, self.var_divby_temp = [], []
            self.var_formula, self.var_formula_temp = [], []

            self.var_settings_temp = var_settings_temp
            self.var_id = var_id
            self.var_count = var_count


            for i in range(0, len(self.var_settings_temp), 6):
                self.var_prec_temp.append(self.var_settings_temp[i].rsplit(':', 1)[-1])
                self.var_divby_temp.append(self.var_settings_temp[i + 1][5:][:-1])
                self.var_min_temp.append(self.var_settings_temp[i + 2].rsplit(':', 1)[-1])
                self.var_max_temp.append(self.var_settings_temp[i + 3].rsplit(':', 1)[-1])

            for i in range(len(self.variables_collection_list)):
                if self.var_id in self.variables_collection_list[i]:
                    self.var_prec.append(self.var_prec_temp[self.var_count])
                    self.var_divby.append(self.var_divby_temp[self.var_count])
                    self.var_min.append(self.var_min_temp[self.var_count])
                    self.var_max.append(self.var_max_temp[self.var_count])
                    self.var_count = self.var_count + 1

                else:
                    self.var_prec.append(" ")
                    self.var_divby.append(" ")
                    self.var_min.append(" ")
                    self.var_max.append(" ")

            return self.var_prec, self.var_divby, self.var_min, self.var_max, self.var_count

        def append_data_to_res_of_ff_question_type(self, res_count, res_settings_temp, res_id):




            self.res_prec, self.res_prec_temp = [], []
            self.res_tol, self.res_tol_temp = [], []
            self.res_min, self.res_min_temp = [], []
            self.res_max, self.res_max_temp = [], []
            self.res_pts, self.res_pts_temp = [], []
            self.res_formula, self.res_formula_temp = [], []

            self.res_settings_temp = res_settings_temp
            self.res_id = res_id
            self.res_count = res_count


            for i in range(0, len(self.res_settings_temp), 10):
                self.res_prec_temp.append(self.res_settings_temp[i].rsplit(':', 1)[-1])
                self.res_tol_temp.append(self.res_settings_temp[i + 1].rsplit(':', 1)[-1])
                self.res_min_temp.append(self.res_settings_temp[i + 2].rsplit(':', 1)[-1])
                self.res_max_temp.append(self.res_settings_temp[i + 3].rsplit(':', 1)[-1])
                self.res_pts_temp.append(self.res_settings_temp[i + 4].rsplit(':', 1)[-1])
                self.res_formula_temp.append(self.res_settings_temp[i + 5].rsplit(':', 1)[-1])

            print("_______________________")

            #print(len(self.res_prec_temp), " ---> ", self.res_prec_temp)
            #print(self.res_count)
            #print("_______________________")


            for i in range(len(self.result_collection_list)):
                if self.res_id in self.result_collection_list[i]:
                    self.res_prec.append(self.res_prec_temp[self.res_count])
                    self.res_tol.append(self.res_tol_temp[self.res_count])
                    self.res_min.append(self.res_min_temp[self.res_count])
                    self.res_max.append(self.res_max_temp[self.res_count])
                    self.res_pts.append(self.res_pts_temp[self.res_count])
                    self.res_formula.append(self.res_formula_temp[self.res_count])
                    self.res_count = self.res_count + 1

                else:
                    self.res_prec.append(" ")
                    self.res_tol.append(" ")
                    self.res_min.append(" ")
                    self.res_max.append(" ")
                    self.res_pts.append(" ")
                    self.res_formula.append(" ")


            return self.res_prec, self.res_tol, self.res_min, self.res_max, self.res_pts, self.res_formula, self.res_count

        def write_data_to_database_ff(self):

            print("WRITE TO DB")

            self.index_list = []
            self.index_dict = {}
            for i in range(len(self.ilias_question_type_ff_question_index)):
                self.index_list = self.table_index_list[self.table_dict["formelfrage"]]
                self.index_dict = self.table_index_dict[self.table_dict["formelfrage"]]



                self.index_list[self.index_dict["question_type"]][0].set("formelfrage")
                self.index_list[self.index_dict["question_title"]][0].set(self.ilias_question_title[int(self.ilias_question_type_ff_question_index[i])])
                self.index_list[self.index_dict["question_description_title"]][0].set(self.ilias_question_description_title[int(self.ilias_question_type_ff_question_index[i])])
                self.index_list[self.index_dict["question_description_main"]][0].set(self.ilias_question_description_main[int(self.ilias_question_type_ff_question_index[i])])

                self.index_list[self.index_dict["res1_formula"]][0].set(self.ilias_test_result1_formula[i])
                self.index_list[self.index_dict["res2_formula"]][0].set(self.ilias_test_result2_formula[i])
                self.index_list[self.index_dict["res3_formula"]][0].set(self.ilias_test_result3_formula[i])
                self.index_list[self.index_dict["res4_formula"]][0].set(self.ilias_test_result4_formula[i])
                self.index_list[self.index_dict["res5_formula"]][0].set(self.ilias_test_result5_formula[i])
                self.index_list[self.index_dict["res6_formula"]][0].set(self.ilias_test_result6_formula[i])
                self.index_list[self.index_dict["res7_formula"]][0].set(self.ilias_test_result7_formula[i])
                self.index_list[self.index_dict["res8_formula"]][0].set(self.ilias_test_result8_formula[i])
                self.index_list[self.index_dict["res9_formula"]][0].set(self.ilias_test_result9_formula[i])
                self.index_list[self.index_dict["res10_formula"]][0].set(self.ilias_test_result10_formula[i])

                self.index_list[self.index_dict["var1_min"]][0].set(self.ilias_test_variable1_min[i])
                self.index_list[self.index_dict["var1_max"]][0].set(self.ilias_test_variable1_max[i])
                self.index_list[self.index_dict["var1_prec"]][0].set(self.ilias_test_variable1_prec[i])
                self.index_list[self.index_dict["var1_divby"]][0].set(self.ilias_test_variable1_divby[i])

                self.index_list[self.index_dict["var2_min"]][0].set(self.ilias_test_variable2_min[i])
                self.index_list[self.index_dict["var2_max"]][0].set(self.ilias_test_variable2_max[i])
                self.index_list[self.index_dict["var2_prec"]][0].set(self.ilias_test_variable2_prec[i])
                self.index_list[self.index_dict["var2_divby"]][0].set(self.ilias_test_variable2_divby[i])

                self.index_list[self.index_dict["var3_min"]][0].set(self.ilias_test_variable3_min[i])
                self.index_list[self.index_dict["var3_max"]][0].set(self.ilias_test_variable3_max[i])
                self.index_list[self.index_dict["var3_prec"]][0].set(self.ilias_test_variable3_prec[i])
                self.index_list[self.index_dict["var3_divby"]][0].set(self.ilias_test_variable3_divby[i])

                self.index_list[self.index_dict["var4_min"]][0].set(self.ilias_test_variable4_min[i])
                self.index_list[self.index_dict["var4_max"]][0].set(self.ilias_test_variable4_max[i])
                self.index_list[self.index_dict["var4_prec"]][0].set(self.ilias_test_variable4_prec[i])
                self.index_list[self.index_dict["var4_divby"]][0].set(self.ilias_test_variable4_divby[i])

                self.index_list[self.index_dict["var5_min"]][0].set(self.ilias_test_variable5_min[i])
                self.index_list[self.index_dict["var5_max"]][0].set(self.ilias_test_variable5_max[i])
                self.index_list[self.index_dict["var5_prec"]][0].set(self.ilias_test_variable5_prec[i])
                self.index_list[self.index_dict["var5_divby"]][0].set(self.ilias_test_variable5_divby[i])

                self.index_list[self.index_dict["var6_min"]][0].set(self.ilias_test_variable6_min[i])
                self.index_list[self.index_dict["var6_max"]][0].set(self.ilias_test_variable6_max[i])
                self.index_list[self.index_dict["var6_prec"]][0].set(self.ilias_test_variable6_prec[i])
                self.index_list[self.index_dict["var6_divby"]][0].set(self.ilias_test_variable6_divby[i])

                self.index_list[self.index_dict["var7_min"]][0].set(self.ilias_test_variable7_min[i])
                self.index_list[self.index_dict["var7_max"]][0].set(self.ilias_test_variable7_max[i])
                self.index_list[self.index_dict["var7_prec"]][0].set(self.ilias_test_variable7_prec[i])
                self.index_list[self.index_dict["var7_divby"]][0].set(self.ilias_test_variable7_divby[i])

                self.index_list[self.index_dict["var8_min"]][0].set(self.ilias_test_variable8_min[i])
                self.index_list[self.index_dict["var8_max"]][0].set(self.ilias_test_variable8_max[i])
                self.index_list[self.index_dict["var8_prec"]][0].set(self.ilias_test_variable8_prec[i])
                self.index_list[self.index_dict["var8_divby"]][0].set(self.ilias_test_variable8_divby[i])

                self.index_list[self.index_dict["var9_min"]][0].set(self.ilias_test_variable9_min[i])
                self.index_list[self.index_dict["var9_max"]][0].set(self.ilias_test_variable9_max[i])
                self.index_list[self.index_dict["var9_prec"]][0].set(self.ilias_test_variable9_prec[i])
                self.index_list[self.index_dict["var9_divby"]][0].set(self.ilias_test_variable9_divby[i])

                self.index_list[self.index_dict["var10_min"]][0].set(self.ilias_test_variable10_min[i])
                self.index_list[self.index_dict["var10_max"]][0].set(self.ilias_test_variable10_max[i])
                self.index_list[self.index_dict["var10_prec"]][0].set(self.ilias_test_variable10_prec[i])
                self.index_list[self.index_dict["var10_divby"]][0].set(self.ilias_test_variable10_divby[i])

                self.index_list[self.index_dict["var11_min"]][0].set(self.ilias_test_variable11_min[i])
                self.index_list[self.index_dict["var11_max"]][0].set(self.ilias_test_variable11_max[i])
                self.index_list[self.index_dict["var11_prec"]][0].set(self.ilias_test_variable11_prec[i])
                self.index_list[self.index_dict["var11_divby"]][0].set(self.ilias_test_variable11_divby[i])

                self.index_list[self.index_dict["var12_min"]][0].set(self.ilias_test_variable12_min[i])
                self.index_list[self.index_dict["var12_max"]][0].set(self.ilias_test_variable12_max[i])
                self.index_list[self.index_dict["var12_prec"]][0].set(self.ilias_test_variable12_prec[i])
                self.index_list[self.index_dict["var12_divby"]][0].set(self.ilias_test_variable12_divby[i])

                self.index_list[self.index_dict["var13_min"]][0].set(self.ilias_test_variable13_min[i])
                self.index_list[self.index_dict["var13_max"]][0].set(self.ilias_test_variable13_max[i])
                self.index_list[self.index_dict["var13_prec"]][0].set(self.ilias_test_variable13_prec[i])
                self.index_list[self.index_dict["var13_divby"]][0].set(self.ilias_test_variable13_divby[i])

                self.index_list[self.index_dict["var14_min"]][0].set(self.ilias_test_variable14_min[i])
                self.index_list[self.index_dict["var14_max"]][0].set(self.ilias_test_variable14_max[i])
                self.index_list[self.index_dict["var14_prec"]][0].set(self.ilias_test_variable14_prec[i])
                self.index_list[self.index_dict["var14_divby"]][0].set(self.ilias_test_variable14_divby[i])

                self.index_list[self.index_dict["var15_min"]][0].set(self.ilias_test_variable15_min[i])
                self.index_list[self.index_dict["var15_max"]][0].set(self.ilias_test_variable15_max[i])
                self.index_list[self.index_dict["var15_prec"]][0].set(self.ilias_test_variable15_prec[i])
                self.index_list[self.index_dict["var15_divby"]][0].set(self.ilias_test_variable15_divby[i])



                self.index_list[self.index_dict["res1_min"]][0].set(self.ilias_test_result1_min[i])
                self.index_list[self.index_dict["res1_max"]][0].set(self.ilias_test_result1_max[i])
                self.index_list[self.index_dict["res1_prec"]][0].set(self.ilias_test_result1_prec[i])
                self.index_list[self.index_dict["res1_tol"]][0].set(self.ilias_test_result1_tol[i])
                self.index_list[self.index_dict["res1_points"]][0].set(self.ilias_test_result1_pts[i])

                self.index_list[self.index_dict["res2_min"]][0].set(self.ilias_test_result2_min[i])
                self.index_list[self.index_dict["res2_max"]][0].set(self.ilias_test_result2_max[i])
                self.index_list[self.index_dict["res2_prec"]][0].set(self.ilias_test_result2_prec[i])
                self.index_list[self.index_dict["res2_tol"]][0].set(self.ilias_test_result2_tol[i])
                self.index_list[self.index_dict["res2_points"]][0].set(self.ilias_test_result2_pts[i])

                self.index_list[self.index_dict["res3_min"]][0].set(self.ilias_test_result3_min[i])
                self.index_list[self.index_dict["res3_max"]][0].set(self.ilias_test_result3_max[i])
                self.index_list[self.index_dict["res3_prec"]][0].set(self.ilias_test_result3_prec[i])
                self.index_list[self.index_dict["res3_tol"]][0].set(self.ilias_test_result3_tol[i])
                self.index_list[self.index_dict["res3_points"]][0].set(self.ilias_test_result3_pts[i])

                self.index_list[self.index_dict["res4_min"]][0].set(self.ilias_test_result4_min[i])
                self.index_list[self.index_dict["res4_max"]][0].set(self.ilias_test_result4_max[i])
                self.index_list[self.index_dict["res4_prec"]][0].set(self.ilias_test_result4_prec[i])
                self.index_list[self.index_dict["res4_tol"]][0].set(self.ilias_test_result4_tol[i])
                self.index_list[self.index_dict["res4_points"]][0].set(self.ilias_test_result4_pts[i])

                self.index_list[self.index_dict["res5_min"]][0].set(self.ilias_test_result5_min[i])
                self.index_list[self.index_dict["res5_max"]][0].set(self.ilias_test_result5_max[i])
                self.index_list[self.index_dict["res5_prec"]][0].set(self.ilias_test_result5_prec[i])
                self.index_list[self.index_dict["res5_tol"]][0].set(self.ilias_test_result5_tol[i])
                self.index_list[self.index_dict["res5_points"]][0].set(self.ilias_test_result5_pts[i])

                self.index_list[self.index_dict["res6_min"]][0].set(self.ilias_test_result6_min[i])
                self.index_list[self.index_dict["res6_max"]][0].set(self.ilias_test_result6_max[i])
                self.index_list[self.index_dict["res6_prec"]][0].set(self.ilias_test_result6_prec[i])
                self.index_list[self.index_dict["res6_tol"]][0].set(self.ilias_test_result6_tol[i])
                self.index_list[self.index_dict["res6_points"]][0].set(self.ilias_test_result6_pts[i])

                self.index_list[self.index_dict["res7_min"]][0].set(self.ilias_test_result7_min[i])
                self.index_list[self.index_dict["res7_max"]][0].set(self.ilias_test_result7_max[i])
                self.index_list[self.index_dict["res7_prec"]][0].set(self.ilias_test_result7_prec[i])
                self.index_list[self.index_dict["res7_tol"]][0].set(self.ilias_test_result7_tol[i])
                self.index_list[self.index_dict["res7_points"]][0].set(self.ilias_test_result7_pts[i])

                self.index_list[self.index_dict["res8_min"]][0].set(self.ilias_test_result8_min[i])
                self.index_list[self.index_dict["res8_max"]][0].set(self.ilias_test_result8_max[i])
                self.index_list[self.index_dict["res8_prec"]][0].set(self.ilias_test_result8_prec[i])
                self.index_list[self.index_dict["res8_tol"]][0].set(self.ilias_test_result8_tol[i])
                self.index_list[self.index_dict["res8_points"]][0].set(self.ilias_test_result8_pts[i])

                self.index_list[self.index_dict["res9_min"]][0].set(self.ilias_test_result9_min[i])
                self.index_list[self.index_dict["res9_max"]][0].set(self.ilias_test_result9_max[i])
                self.index_list[self.index_dict["res9_prec"]][0].set(self.ilias_test_result9_prec[i])
                self.index_list[self.index_dict["res9_tol"]][0].set(self.ilias_test_result9_tol[i])
                self.index_list[self.index_dict["res9_points"]][0].set(self.ilias_test_result9_pts[i])

                self.index_list[self.index_dict["res10_min"]][0].set(self.ilias_test_result10_min[i])
                self.index_list[self.index_dict["res10_max"]][0].set(self.ilias_test_result10_max[i])
                self.index_list[self.index_dict["res10_prec"]][0].set(self.ilias_test_result10_prec[i])
                self.index_list[self.index_dict["res10_tol"]][0].set(self.ilias_test_result10_tol[i])
                self.index_list[self.index_dict["res10_points"]][0].set(self.ilias_test_result10_pts[i])


                self.index_list[self.index_dict["test_time"]][0].set(self.ilias_test_duration[int(self.ilias_question_type_ff_question_index[i])])
                self.index_list[self.index_dict["question_author"]][0].set(self.ilias_question_author[int(self.ilias_question_type_ff_question_index[i])])

                self.DBI.Add_data_to_DB(self.index_list, self.index_list[self.index_dict["question_title"]][0].get())


    ####### Multiple Choice Fragen
        def read_multiplechoice_questions(self):

            # MULTIPLE CHOICE Antworten
            for response_lid in self.myroot.iter('response_lid'):
                if response_lid.attrib.get('ident') == "MCMR":    #MR -> Multiple Choice
                    for render_choice in response_lid.iter('render_choice'):
                        for response_label in render_choice.iter('response_label'):
                            for material in response_label.iter('material'):
                                if material.find('matimage') == None:
                                    self.mc_ilias_response_img_label.append("EMPTY")
                                    self.mc_ilias_response_img_string_base64_encoded.append("EMPTY")

                                else:
                                    self.mc_ilias_response_img_label.append(material.find('matimage').attrib.get('label'))
                                    self.mc_ilias_response_img_string_base64_encoded.append(material.find('matimage').text)



                                for mattext in material.iter('mattext'):
                                    self.mattext_text_all_mc_answers.append(mattext.text)
                                    self.mc_ilias_response_text.append(mattext.text)


    #####################################   Anzahl der Antworten pro MC-Frage
            # Durch diese Iteration und Abfrage nach MCMR (=Multiple Choice), werden alle Antworten der MC-Fragen aufgelistet
            for response_lid in self.myroot.iter('response_lid'):
                if response_lid.attrib.get('ident') == 'MCMR':
                    for render_choice in response_lid.iter('render_choice'):
                        # Zu Beginn jedes Anwort-Blocks wird ein "$" geschrieben, um hinterher zu splitten
                        self.mc_answer_list_nr += "$"
                        for response_label in render_choice.iter('response_label'):
                            self.mc_answer_list_nr += str(response_label.attrib.get('ident'))

            self.ilias_test_question_type_collection_mc_answers = self.mc_answer_list_nr.split("$")
            self.ilias_test_question_type_collection_mc_answers.pop(0)  # Durch split() enthält erstes Feld keine Daten



            for respcondition in self.myroot.iter('respcondition'):
                for varequal in respcondition.iter('varequal'):
                    if varequal.attrib.get('respident') == "MCMR":
                        for setvar in respcondition.iter('setvar'):
                            self.all_mc_questions_points.append(setvar.text)

            # Jedes zweite ELement übernehmen [::2] mit Start beim 1. Fach (nicht das 0. Fach)
            self.mc_questions_false_points = self.all_mc_questions_points[1::2]
            self.mc_questions_correct_points = self.all_mc_questions_points[::2]


            self.mc_ilias_number_of_response_variables = 10
            self.mc_ilias_response_text_1, self.mc_ilias_response_pts_correct_answer_1, self.mc_ilias_response_pts_false_answer_1, self.mc_ilias_response_img_label_1, self.mc_ilias_response_img_string_base64_encoded_1 = [], [], [], [], []
            self.mc_ilias_response_text_2, self.mc_ilias_response_pts_correct_answer_2, self.mc_ilias_response_pts_false_answer_2, self.mc_ilias_response_img_label_2, self.mc_ilias_response_img_string_base64_encoded_2 = [], [], [], [], []
            self.mc_ilias_response_text_3, self.mc_ilias_response_pts_correct_answer_3, self.mc_ilias_response_pts_false_answer_3, self.mc_ilias_response_img_label_3, self.mc_ilias_response_img_string_base64_encoded_3 = [], [], [], [], []
            self.mc_ilias_response_text_4, self.mc_ilias_response_pts_correct_answer_4, self.mc_ilias_response_pts_false_answer_4, self.mc_ilias_response_img_label_4, self.mc_ilias_response_img_string_base64_encoded_4 = [], [], [], [], []
            self.mc_ilias_response_text_5, self.mc_ilias_response_pts_correct_answer_5, self.mc_ilias_response_pts_false_answer_5, self.mc_ilias_response_img_label_5, self.mc_ilias_response_img_string_base64_encoded_5 = [], [], [], [], []
            self.mc_ilias_response_text_6, self.mc_ilias_response_pts_correct_answer_6, self.mc_ilias_response_pts_false_answer_6, self.mc_ilias_response_img_label_6, self.mc_ilias_response_img_string_base64_encoded_6 = [], [], [], [], []
            self.mc_ilias_response_text_7, self.mc_ilias_response_pts_correct_answer_7, self.mc_ilias_response_pts_false_answer_7, self.mc_ilias_response_img_label_7, self.mc_ilias_response_img_string_base64_encoded_7 = [], [], [], [], []
            self.mc_ilias_response_text_8, self.mc_ilias_response_pts_correct_answer_8, self.mc_ilias_response_pts_false_answer_8, self.mc_ilias_response_img_label_8, self.mc_ilias_response_img_string_base64_encoded_8 = [], [], [], [], []
            self.mc_ilias_response_text_9, self.mc_ilias_response_pts_correct_answer_9, self.mc_ilias_response_pts_false_answer_9, self.mc_ilias_response_img_label_9, self.mc_ilias_response_img_string_base64_encoded_9 = [], [], [], [], []
            self.mc_ilias_response_text_10, self.mc_ilias_response_pts_correct_answer_10, self.mc_ilias_response_pts_false_answer_10, self.mc_ilias_response_img_label_10, self.mc_ilias_response_img_string_base64_encoded_10 = [], [], [], [], []


            t = 0
            for i in range(len(self.ilias_test_question_type_collection_mc_answers)):
                if i == 1:
                    t = int(max(self.ilias_test_question_type_collection_mc_answers[0])) + 1

                if "0" in self.ilias_test_question_type_collection_mc_answers[i]:
                    self.mc_ilias_response_text_1.append(self.mc_ilias_response_text[t])
                    self.mc_ilias_response_pts_correct_answer_1.append(self.mc_questions_correct_points[t])
                    self.mc_ilias_response_pts_false_answer_1.append(self.mc_questions_false_points[t])
                    self.mc_ilias_response_img_label_1.append(self.mc_ilias_response_img_label[t])
                    self.mc_ilias_response_img_string_base64_encoded_1.append(self.mc_ilias_response_img_string_base64_encoded[t])
                else:
                    self.mc_ilias_response_text_1.append(" ")
                    self.mc_ilias_response_pts_correct_answer_1.append(" ")
                    self.mc_ilias_response_pts_false_answer_1.append(" ")
                    self.mc_ilias_response_img_label_1.append("EMPTY")
                    self.mc_ilias_response_img_string_base64_encoded_1.append("EMPTY")

                if "1" in self.ilias_test_question_type_collection_mc_answers[i]:
                    self.mc_ilias_response_text_2.append(self.mc_ilias_response_text[t + 1])
                    self.mc_ilias_response_pts_correct_answer_2.append(self.mc_questions_correct_points[t+1])
                    self.mc_ilias_response_pts_false_answer_2.append(self.mc_questions_false_points[t + 1])
                    self.mc_ilias_response_img_label_2.append(self.mc_ilias_response_img_label[t + 1])
                    self.mc_ilias_response_img_string_base64_encoded_2.append(self.mc_ilias_response_img_string_base64_encoded[t])
                else:
                    self.mc_ilias_response_text_2.append(" ")
                    self.mc_ilias_response_pts_correct_answer_2.append(" ")
                    self.mc_ilias_response_pts_false_answer_2.append(" ")
                    self.mc_ilias_response_img_label_2.append("EMPTY")
                    self.mc_ilias_response_img_string_base64_encoded_2.append("EMPTY")

                if "2" in self.ilias_test_question_type_collection_mc_answers[i]:
                    self.mc_ilias_response_text_3.append(self.mc_ilias_response_text[t + 2])
                    self.mc_ilias_response_pts_correct_answer_3.append(self.mc_questions_correct_points[t+2])
                    self.mc_ilias_response_pts_false_answer_3.append(self.mc_questions_false_points[t + 2])
                    self.mc_ilias_response_img_label_3.append(self.mc_ilias_response_img_label[t + 2])
                    self.mc_ilias_response_img_string_base64_encoded_3.append(self.mc_ilias_response_img_string_base64_encoded[t])
                else:
                    self.mc_ilias_response_text_3.append(" ")
                    self.mc_ilias_response_pts_correct_answer_3.append(" ")
                    self.mc_ilias_response_pts_false_answer_3.append(" ")
                    self.mc_ilias_response_img_label_3.append("EMPTY")
                    self.mc_ilias_response_img_string_base64_encoded_3.append("EMPTY")

                if "3" in self.ilias_test_question_type_collection_mc_answers[i]:
                    self.mc_ilias_response_text_4.append(self.mc_ilias_response_text[t + 3])
                    self.mc_ilias_response_pts_correct_answer_4.append(self.mc_questions_correct_points[t+4])
                    self.mc_ilias_response_pts_false_answer_4.append(self.mc_questions_false_points[t + 3])
                    self.mc_ilias_response_img_label_4.append(self.mc_ilias_response_img_label[t + 3])
                    self.mc_ilias_response_img_string_base64_encoded_4.append(self.mc_ilias_response_img_string_base64_encoded[t])
                else:
                    self.mc_ilias_response_text_4.append(" ")
                    self.mc_ilias_response_pts_correct_answer_4.append(" ")
                    self.mc_ilias_response_pts_false_answer_4.append(" ")
                    self.mc_ilias_response_img_label_4.append("EMPTY")
                    self.mc_ilias_response_img_string_base64_encoded_4.append("EMPTY")

                if "4" in self.ilias_test_question_type_collection_mc_answers[i]:
                    self.mc_ilias_response_text_5.append(self.mc_ilias_response_text[t + 4])
                    self.mc_ilias_response_pts_correct_answer_5.append(self.mc_questions_correct_points[t+4])
                    self.mc_ilias_response_pts_false_answer_5.append(self.mc_questions_false_points[t + 4])
                    self.mc_ilias_response_img_label_5.append(self.mc_ilias_response_img_label[t + 4])
                    self.mc_ilias_response_img_string_base64_encoded_5.append(self.mc_ilias_response_img_string_base64_encoded[t])
                else:
                    self.mc_ilias_response_text_5.append(" ")
                    self.mc_ilias_response_pts_correct_answer_5.append(" ")
                    self.mc_ilias_response_pts_false_answer_5.append(" ")
                    self.mc_ilias_response_img_label_5.append("EMPTY")
                    self.mc_ilias_response_img_string_base64_encoded_5.append("EMPTY")

                if "5" in self.ilias_test_question_type_collection_mc_answers[i]:
                    self.mc_ilias_response_text_6.append(self.mc_ilias_response_text[t + 5])
                    self.mc_ilias_response_pts_correct_answer_6.append(self.mc_questions_correct_points[t+5])
                    self.mc_ilias_response_pts_false_answer_6.append(self.mc_questions_false_points[t + 5])
                    self.mc_ilias_response_img_label_6.append(self.mc_ilias_response_img_label[t + 5])
                    self.mc_ilias_response_img_string_base64_encoded_6.append(self.mc_ilias_response_img_string_base64_encoded[t])
                else:
                    self.mc_ilias_response_text_6.append(" ")
                    self.mc_ilias_response_pts_correct_answer_6.append(" ")
                    self.mc_ilias_response_pts_false_answer_6.append(" ")
                    self.mc_ilias_response_img_label_6.append("EMPTY")
                    self.mc_ilias_response_img_string_base64_encoded_6.append("EMPTY")

                if "6" in self.ilias_test_question_type_collection_mc_answers[i]:
                    self.mc_ilias_response_text_7.append(self.mc_ilias_response_text[t + 6])
                    self.mc_ilias_response_pts_correct_answer_7.append(self.mc_questions_correct_points[t+6])
                    self.mc_ilias_response_pts_false_answer_7.append(self.mc_questions_false_points[t + 6])
                    self.mc_ilias_response_img_label_7.append(self.mc_ilias_response_img_label[t + 6])
                    self.mc_ilias_response_img_string_base64_encoded_7.append(self.mc_ilias_response_img_string_base64_encoded[t])
                else:
                    self.mc_ilias_response_text_7.append(" ")
                    self.mc_ilias_response_pts_correct_answer_7.append(" ")
                    self.mc_ilias_response_pts_false_answer_7.append(" ")
                    self.mc_ilias_response_img_label_7.append("EMPTY")
                    self.mc_ilias_response_img_string_base64_encoded_7.append("EMPTY")

                if "7" in self.ilias_test_question_type_collection_mc_answers[i]:
                    self.mc_ilias_response_text_8.append(self.mc_ilias_response_text[t + 7])
                    self.mc_ilias_response_pts_correct_answer_8.append(self.mc_questions_correct_points[t+7])
                    self.mc_ilias_response_pts_false_answer_8.append(self.mc_questions_false_points[t + 7])
                    self.mc_ilias_response_img_label_8.append(self.mc_ilias_response_img_label[t + 7])
                    self.mc_ilias_response_img_string_base64_encoded_8.append(self.mc_ilias_response_img_string_base64_encoded[t])
                else:
                    self.mc_ilias_response_text_8.append(" ")
                    self.mc_ilias_response_pts_correct_answer_8.append(" ")
                    self.mc_ilias_response_pts_false_answer_8.append(" ")
                    self.mc_ilias_response_img_label_8.append("EMPTY")
                    self.mc_ilias_response_img_string_base64_encoded_8.append("EMPTY")

                if "8" in self.ilias_test_question_type_collection_mc_answers[i]:
                    self.mc_ilias_response_text_9.append(self.mc_ilias_response_text[t + 8])
                    self.mc_ilias_response_pts_correct_answer_9.append(self.mc_questions_correct_points[t+8])
                    self.mc_ilias_response_pts_false_answer_9.append(self.mc_questions_false_points[t + 8])
                    self.mc_ilias_response_img_label_9.append(self.mc_ilias_response_img_label[t + 8])
                    self.mc_ilias_response_img_string_base64_encoded_9.append(self.mc_ilias_response_img_string_base64_encoded[t])
                else:
                    self.mc_ilias_response_text_9.append(" ")
                    self.mc_ilias_response_pts_correct_answer_9.append(" ")
                    self.mc_ilias_response_pts_false_answer_9.append(" ")
                    self.mc_ilias_response_img_label_9.append("EMPTY")
                    self.mc_ilias_response_img_string_base64_encoded_9.append("EMPTY")

                if "9" in self.ilias_test_question_type_collection_mc_answers[i]:
                    self.mc_ilias_response_text_10.append(self.mc_ilias_response_text[t + 9])
                    self.mc_ilias_response_pts_correct_answer_10.append(self.mc_questions_correct_points[t+9])
                    self.mc_ilias_response_pts_false_answer_10.append(self.mc_questions_false_points[t + 9])
                    self.mc_ilias_response_img_label_10.append(self.mc_ilias_response_img_label[t + 9])
                    self.mc_ilias_response_img_string_base64_encoded_10.append(self.mc_ilias_response_img_string_base64_encoded[t])
                else:
                    self.mc_ilias_response_text_10.append(" ")
                    self.mc_ilias_response_pts_correct_answer_10.append(" ")
                    self.mc_ilias_response_pts_false_answer_10.append(" ")
                    self.mc_ilias_response_img_label_10.append("EMPTY")
                    self.mc_ilias_response_img_string_base64_encoded_10.append("EMPTY")

                t += int(max(self.ilias_test_question_type_collection_mc_answers[i])) + 1



       

    ####### Matching Question Fragen
        def read_matching_questions(self):

            # MATCHING QUESTIONS Antworten
            # Es werden alle möglichen Antworten (ident_nr) aus der .xml für die MQ-Fragen aufgelistet
            for response_grp in self.myroot.iter('response_grp'):
                if response_grp.attrib.get('ident') == "MQ":      #MQ -> Matching Question
                    self.mattext_text_all_mq_answers.append("$")
                    for render_choice in response_grp.iter('render_choice'):
                        for response_label in render_choice.iter('response_label'):
                            self.mattext_text_all_mq_answers.append(response_label.attrib.get('ident'))
                            self.mattext_text_all_mq_answers_collection.append(response_label.attrib.get('ident'))
                            # Eine Antwort (ident_nr) wird immer einer "match_group" zugewiesen
                            #self.mq_match_group.append(response_label.attrib.get('match_group'))


            for response_grp in self.myroot.iter('response_grp'):
                if response_grp.attrib.get('ident') == "MQ":    #MQ -> Matching Question
                    for render_choice in response_grp.iter('render_choice'):
                        for response_label in render_choice.iter('response_label'):
                            for material in response_label.iter('material'):
                                for mattext in material.iter('mattext'):
                                    self.mattText_text_all_mq_answers.append(mattext.text)



            # MATCHING QUESTIONS Bild-Namen
            for response_grp in self.myroot.iter('response_grp'):
                if response_grp.attrib.get('ident') == "MQ":    #MQ -> Matching Question
                    for render_choice in response_grp.iter('render_choice'):
                        for response_label in render_choice.iter('response_label'):
                            for material in response_label.iter('material'):
                                for matimage in material.iter('matimage'):
                                    self.mq_response_img_label.append(matimage.attrib.get('label'))
                                    self.mq_response_img_data.append(matimage.text)


            for item in self.myroot.iter('item'):
                for resprocessing in item.iter('resprocessing'):
                    for respcondition in resprocessing.iter('respcondition'):
                        for conditionvar in respcondition.iter('conditionvar'):
                            for varsubset in conditionvar.iter('varsubset'):
                                if varsubset.attrib.get('respident') == "MQ":
                                    self.mq_matching_ids.append(varsubset.text)


                self.mq_len_list.append(len(self.mq_matching_ids))

            self.mq_len_list = list(dict.fromkeys(self.mq_len_list))
            for j in range(len(self.mq_len_list)):
                if j > 0:
                    self.mq_len_list[j] = self.mq_len_list[j] - self.mq_len_list[j-1]


            # MATCHING QUESTIONS Punkte für Antworten
            for respcondition in self.myroot.iter('respcondition'):
                for conditionvar in respcondition.iter('conditionvar'):
                    for varsubset in conditionvar.iter('varsubset'):
                        if varsubset.attrib.get('respident') == "MQ":
                            for setvar in respcondition.iter('setvar'):
                                self.mq_matching_ids_points.append(setvar.text)



            # Erstes Fach enthält ein "$" und wird nicht benötigt
            if len(self.mattext_text_all_mq_answers) > 0:
                self.mattext_text_all_mq_answers.pop(0)

            self.index_counter = 0
            for i in range(len(self.mattext_text_all_mq_answers)):
                if self.mattext_text_all_mq_answers[i] == "$":
                    self.mq_number_of_answers_per_question.append(i-self.index_counter)
                    self.index_counter = self.index_counter + 1



            # Die Anzahl der Werte nach dem letzten "$" einfügen. "-1" weil noch ein "$" enhalten ist
            self.mq_number_of_answers_per_question.append(len(self.mattext_text_all_mq_answers)- len(self.mq_number_of_answers_per_question))



            # Letztes Fach der Liste wird, vorletztes Fach abgezogen.
            #self.mq_number_of_answers_per_question[len(self.mq_number_of_answers_per_question)-1] = self.mq_number_of_answers_per_question[len(self.mq_number_of_answers_per_question)-1] - self.mq_number_of_answers_per_question[len(self.mq_number_of_answers_per_question)-2]

            for i in range(len(self.mq_number_of_answers_per_question)):
                if i >= 1:
                    self.mq_number_of_answers_per_question_temp.append(self.mq_number_of_answers_per_question[i] - self.mq_number_of_answers_per_question[i-1])
                else:
                    self.mq_number_of_answers_per_question_temp.append(self.mq_number_of_answers_per_question[i])

            self.mq_number_of_answers_per_question = self.mq_number_of_answers_per_question_temp



            ##

            self.mq_len_list.pop(0)
            len_temp = 0
            for j in range(len(self.mq_number_of_answers_per_question)):
                for k in range(self.mq_number_of_answers_per_question[j]):
                    if k >= self.mq_len_list[j]:
                        self.mq_matching_ids.insert(k+len_temp, " ")
                        self.mq_matching_ids_points.insert(k+len_temp, " ")
                len_temp += self.mq_number_of_answers_per_question[j]





            for varsubset in self.myroot.iter('varsubset'):
                if varsubset.attrib.get('respident') == "MQ":
                    self.mq_answer_matchings.append(varsubset.text)

            # Punkte können nicht spezifisch ausgelesen werden für MQ
            # Jedoch können die einzelnen Lösungen ausgelesen werden und entsprechend für jede Lösung fix "1" Pkt. vergeben
            for i in range(len(self.mq_answer_matchings)):
                self.mq_answer_matchings_points.append("1")

            for i in range(len(self.mq_number_of_answers_per_question)):
                self.mq_answer_matching_per_question.append(int(self.mq_number_of_answers_per_question[i]/2))

            for i in range(len(self.mq_number_of_answers_per_question)):
                self.mq_answer_list_nr += "$"
                for j in range(int(self.mq_number_of_answers_per_question[i])):
                    self.mq_answer_list_nr += str(j)


            self.ilias_test_question_type_collection_mq_answers = self.mq_answer_list_nr.split("$")
            self.ilias_test_question_type_collection_mq_answers.pop(0)  # Durch split() enthält erstes Feld keine Daten


            self.mq_ilias_response_text_1, self.mq_ilias_response_img_label_1, self.mq_ilias_response_img_string_base64_encoded_1 = [],[], []
            self.mq_ilias_response_text_2, self.mq_ilias_response_img_label_2, self.mq_ilias_response_img_string_base64_encoded_2 = [],[], []
            self.mq_ilias_response_text_3, self.mq_ilias_response_img_label_3, self.mq_ilias_response_img_string_base64_encoded_3 = [],[], []
            self.mq_ilias_response_text_4, self.mq_ilias_response_img_label_4, self.mq_ilias_response_img_string_base64_encoded_4 = [],[], []
            self.mq_ilias_response_text_5, self.mq_ilias_response_img_label_5, self.mq_ilias_response_img_string_base64_encoded_5 = [],[], []
            self.mq_ilias_response_text_6, self.mq_ilias_response_img_label_6, self.mq_ilias_response_img_string_base64_encoded_6 = [],[], []
            self.mq_ilias_response_text_7, self.mq_ilias_response_img_label_7, self.mq_ilias_response_img_string_base64_encoded_7 = [],[], []
            self.mq_ilias_response_text_8, self.mq_ilias_response_img_label_8, self.mq_ilias_response_img_string_base64_encoded_8 = [],[], []
            self.mq_ilias_response_text_9, self.mq_ilias_response_img_label_9, self.mq_ilias_response_img_string_base64_encoded_9 = [],[], []
            self.mq_ilias_response_text_10, self.mq_ilias_response_img_label_10, self.mq_ilias_response_img_string_base64_encoded_10 = [],[], []

            self.mq_matching_id_1, self.mq_matching_id_points_1 = [], []
            self.mq_matching_id_2, self.mq_matching_id_points_2 = [], []
            self.mq_matching_id_3, self.mq_matching_id_points_3 = [], []
            self.mq_matching_id_4, self.mq_matching_id_points_4 = [], []
            self.mq_matching_id_5, self.mq_matching_id_points_5 = [], []
            self.mq_matching_id_6, self.mq_matching_id_points_6 = [], []
            self.mq_matching_id_7, self.mq_matching_id_points_7 = [], []
            self.mq_matching_id_8, self.mq_matching_id_points_8 = [], []
            self.mq_matching_id_9, self.mq_matching_id_points_9 = [], []
            self.mq_matching_id_10, self.mq_matching_id_points_10 = [], []

            t = 0
            for i in range(len(self.ilias_test_question_type_collection_mq_answers)):
                if i == 1:
                    t = int(max(self.ilias_test_question_type_collection_mq_answers[0])) + 1

                if "0" in self.ilias_test_question_type_collection_mq_answers[i]:
                    self.mq_ilias_response_text_1.append(self.mattText_text_all_mq_answers[t])
                    self.mq_ilias_response_img_label_1.append(self.mq_response_img_label[t])
                    self.mq_ilias_response_img_string_base64_encoded_1.append(self.mq_response_img_data[t])
                    self.mq_matching_id_1.append(self.mq_matching_ids[t])
                    self.mq_matching_id_points_1.append(self.mq_matching_ids_points[t])
                else:
                    self.mq_ilias_response_text_1.append(" ")
                    self.mq_ilias_response_img_label_1.append(" ")
                    self.mq_ilias_response_img_string_base64_encoded_1.append(" ")
                    self.mq_matching_id_1.append(" ")
                    self.mq_matching_id_points_1.append(" ")

                if "1" in self.ilias_test_question_type_collection_mq_answers[i]:
                    self.mq_ilias_response_text_2.append(self.mattText_text_all_mq_answers[t + 1])
                    self.mq_ilias_response_img_label_2.append(self.mq_response_img_label[t + 1])
                    self.mq_ilias_response_img_string_base64_encoded_2.append(self.mq_response_img_data[t + 1])
                    self.mq_matching_id_2.append(self.mq_matching_ids[t + 1])
                    self.mq_matching_id_points_2.append(self.mq_matching_ids_points[t + 1])
                else:
                    self.mq_ilias_response_text_2.append(" ")
                    self.mq_ilias_response_img_label_2.append(" ")
                    self.mq_ilias_response_img_string_base64_encoded_2.append(" ")
                    self.mq_matching_id_2.append(" ")
                    self.mq_matching_id_points_2.append(" ")

                if "2" in self.ilias_test_question_type_collection_mq_answers[i]:
                    self.mq_ilias_response_text_3.append(self.mattText_text_all_mq_answers[t + 2])
                    self.mq_ilias_response_img_label_3.append(self.mq_response_img_label[t + 2])
                    self.mq_ilias_response_img_string_base64_encoded_3.append(self.mq_response_img_data[t + 2])
                    self.mq_matching_id_3.append(self.mq_matching_ids[t + 2])
                    self.mq_matching_id_points_3.append(self.mq_matching_ids_points[t + 2])
                else:
                    self.mq_ilias_response_text_3.append(" ")
                    self.mq_ilias_response_img_label_3.append(" ")
                    self.mq_ilias_response_img_string_base64_encoded_3.append(" ")
                    self.mq_matching_id_3.append(" ")
                    self.mq_matching_id_points_3.append(" ")

                if "3" in self.ilias_test_question_type_collection_mq_answers[i]:
                    self.mq_ilias_response_text_4.append(self.mattText_text_all_mq_answers[t + 3])
                    self.mq_ilias_response_img_label_4.append(self.mq_response_img_label[t + 3])
                    self.mq_ilias_response_img_string_base64_encoded_4.append(self.mq_response_img_data[t + 3])
                    self.mq_matching_id_4.append(self.mq_matching_ids[t + 3])
                    self.mq_matching_id_points_4.append(self.mq_matching_ids_points[t + 3])
                else:
                    self.mq_ilias_response_text_4.append(" ")
                    self.mq_ilias_response_img_label_4.append(" ")
                    self.mq_ilias_response_img_string_base64_encoded_4.append(" ")
                    self.mq_matching_id_4.append(" ")
                    self.mq_matching_id_points_4.append(" ")

                if "4" in self.ilias_test_question_type_collection_mq_answers[i]:
                    self.mq_ilias_response_text_5.append(self.mattText_text_all_mq_answers[t + 4])
                    self.mq_ilias_response_img_label_5.append(self.mq_response_img_label[t + 4])
                    self.mq_ilias_response_img_string_base64_encoded_5.append(self.mq_response_img_data[t + 4])
                    self.mq_matching_id_5.append(self.mq_matching_ids[t + 4])
                    self.mq_matching_id_points_5.append(self.mq_matching_ids_points[t + 4])
                else:
                    self.mq_ilias_response_text_5.append(" ")
                    self.mq_ilias_response_img_label_5.append(" ")
                    self.mq_ilias_response_img_string_base64_encoded_5.append(" ")
                    self.mq_matching_id_5.append(" ")
                    self.mq_matching_id_points_5.append(" ")

                if "5" in self.ilias_test_question_type_collection_mq_answers[i]:
                    self.mq_ilias_response_text_6.append(self.mattText_text_all_mq_answers[t + 5])
                    self.mq_ilias_response_img_label_6.append(self.mq_response_img_label[t + 5])
                    self.mq_ilias_response_img_string_base64_encoded_6.append(self.mq_response_img_data[t + 5])
                    self.mq_matching_id_6.append(self.mq_matching_ids[t + 5])
                    self.mq_matching_id_points_6.append(self.mq_matching_ids_points[t + 5])
                else:
                    self.mq_ilias_response_text_6.append(" ")
                    self.mq_ilias_response_img_label_6.append(" ")
                    self.mq_ilias_response_img_string_base64_encoded_6.append(" ")
                    self.mq_matching_id_6.append(" ")
                    self.mq_matching_id_points_6.append(" ")

                if "6" in self.ilias_test_question_type_collection_mq_answers[i]:
                    self.mq_ilias_response_text_7.append(self.mattText_text_all_mq_answers[t + 6])
                    self.mq_ilias_response_img_label_7.append(self.mq_response_img_label[t + 6])
                    self.mq_ilias_response_img_string_base64_encoded_7.append(self.mq_response_img_data[t + 6])
                    self.mq_matching_id_7.append(self.mq_matching_ids[t + 6])
                    self.mq_matching_id_points_7.append(self.mq_matching_ids_points[t + 6])
                else:
                    self.mq_ilias_response_text_7.append(" ")
                    self.mq_ilias_response_img_label_7.append(" ")
                    self.mq_ilias_response_img_string_base64_encoded_7.append(" ")
                    self.mq_matching_id_7.append(" ")
                    self.mq_matching_id_points_7.append(" ")

                if "7" in self.ilias_test_question_type_collection_mq_answers[i]:
                    self.mq_ilias_response_text_8.append(self.mattText_text_all_mq_answers[t + 7])
                    self.mq_ilias_response_img_label_8.append(self.mq_response_img_label[t + 7])
                    self.mq_ilias_response_img_string_base64_encoded_8.append(self.mq_response_img_data[t + 7])
                    self.mq_matching_id_8.append(self.mq_matching_ids[t + 7])
                    self.mq_matching_id_points_8.append(self.mq_matching_ids_points[t + 7])
                else:
                    self.mq_ilias_response_text_8.append(" ")
                    self.mq_ilias_response_img_label_8.append(" ")
                    self.mq_ilias_response_img_string_base64_encoded_8.append(" ")
                    self.mq_matching_id_8.append(" ")
                    self.mq_matching_id_points_8.append(" ")

                if "8" in self.ilias_test_question_type_collection_mq_answers[i]:
                    self.mq_ilias_response_text_9.append(self.mattText_text_all_mq_answers[t + 8])
                    self.mq_ilias_response_img_label_9.append(self.mq_response_img_label[t + 8])
                    self.mq_ilias_response_img_string_base64_encoded_9.append(self.mq_response_img_data[t + 8])
                    self.mq_matching_id_9.append(self.mq_matching_ids[t + 8])
                    self.mq_matching_id_points_9.append(self.mq_matching_ids_points[t + 8])
                else:
                    self.mq_ilias_response_text_9.append(" ")
                    self.mq_ilias_response_img_label_9.append(" ")
                    self.mq_ilias_response_img_string_base64_encoded_9.append(" ")
                    self.mq_matching_id_9.append(" ")
                    self.mq_matching_id_points_9.append(" ")

                if "9" in self.ilias_test_question_type_collection_mq_answers[i]:
                    self.mq_ilias_response_text_10.append(self.mattText_text_all_mq_answers[t + 9])
                    self.mq_ilias_response_img_label_10.append(self.mq_response_img_label[t + 9])
                    self.mq_ilias_response_img_string_base64_encoded_10.append(self.mq_response_img_data[t + 9])
                    self.mq_matching_id_10.append(self.mq_matching_ids[t + 9])
                    self.mq_matching_id_points_10.append(self.mq_matching_ids_points[t + 9])
                else:
                    self.mq_ilias_response_text_10.append(" ")
                    self.mq_ilias_response_img_label_10.append(" ")
                    self.mq_ilias_response_img_string_base64_encoded_10.append(" ")
                    self.mq_matching_id_10.append(" ")
                    self.mq_matching_id_points_10.append(" ")

                t += int(max(self.ilias_test_question_type_collection_mq_answers[i])) + 1

       

    ####### Sonstige Funktionen
        def split_description_main_from_img(self, ilias_test_question_description):

            self.ilias_test_question_description = ilias_test_question_description

            self.test_list1 = []
            self.test_list1_l_join = []

            for i in range(len(self.ilias_test_question_description)):


                # Text aus Fach übernehmen
                self.test_neu1 = self.ilias_test_question_description[i]

                #Text auftrennen nach Beschreibung und IMG
                self.test_list1 = self.test_neu1.split('</p>')

                # IMG teil löschen
                for i in range(len(self.test_list1)):
                    if "img" in self.test_list1[i]:
                        self.test_list1.pop(i)
                        break



                self.test_list1_l_join.append('</p>'.join(self.test_list1))


            for i in range(len(self.test_list1_l_join)):
                self.test_list1_l_join[i] = self.test_list1_l_join[i].replace('<p>', "")
                self.test_list1_l_join[i] = self.test_list1_l_join[i].replace('</p>', "")

            return self.test_list1_l_join







        ###### TAXONOMIE FUNKTIONEN ###############
        # Taxonomie aus DB schreiben
        def set_taxonomy_for_question(self, id_nr, number_of_entrys, item, question_type_pool_qpl_file_path_template, question_type_pool_qpl_file_path_output):
            # Zusatz für Taxonomie-Einstellungen
            self.number_of_entrys = number_of_entrys
            self.question_type_pool_qpl_file_path_template = question_type_pool_qpl_file_path_template
            self.question_type_pool_qpl_file_path_output = question_type_pool_qpl_file_path_output

            self.id_int_numbers = 400000 + id_nr

            self.number_of_entrys.append(format(self.id_int_numbers, '06d'))  # Zahlenfolge muss 6-stellig sein.



            item.set('ident', "il_0_qst_" + str(self.id_int_numbers))

            # Hier wird die QPL bearbeitet - Taxonomie
            self.mytree = ET.parse(self.question_type_pool_qpl_file_path_template)
            self.myroot = self.mytree.getroot()


            # Hinzufügen von Question QRef in qpl Datei
            for i in range(id_nr):
                ContentObject = ET.Element('ContentObject')
                MetaData = ET.SubElement(ContentObject, 'MetaData')
                Settings = ET.SubElement(ContentObject, 'Settings')
                PageObject = ET.SubElement(ContentObject, 'PageObject')
                PageContent = ET.SubElement(PageObject, 'PageContent')
                Question = ET.SubElement(PageContent, 'Question')
                Question.set('QRef', "il_0_qst_" + self.number_of_entrys[i])
                print("------->","il_0_qst_" + self.number_of_entrys[i] )
                QuestionSkillAssignments = ET.SubElement(ContentObject, 'QuestionSkillAssignments')
                TriggerQuestion = ET.SubElement(QuestionSkillAssignments, 'TriggerQuestion')
                TriggerQuestion.set('Id', self.number_of_entrys[i])

                self.myroot.append(PageObject)
                # self.myroot.append(QuestionSkillAssignments)

                self.mytree.write(self.question_type_pool_qpl_file_path_output)

            # Hinzufügen von TriggerQuestion ID in qpl Datei
            for i in range(id_nr):
                ContentObject = ET.Element('ContentObject')
                MetaData = ET.SubElement(ContentObject, 'MetaData')
                Settings = ET.SubElement(ContentObject, 'Settings')
                PageObject = ET.SubElement(ContentObject, 'PageObject')
                PageContent = ET.SubElement(PageObject, 'PageContent')
                Question = ET.SubElement(PageContent, 'Question')
                Question.set('QRef', "il_0_qst_" + self.number_of_entrys[i])
                QuestionSkillAssignments = ET.SubElement(ContentObject, 'QuestionSkillAssignments')
                TriggerQuestion = ET.SubElement(QuestionSkillAssignments, 'TriggerQuestion')
                TriggerQuestion.set('Id', self.number_of_entrys[i])

                self.myroot.append(QuestionSkillAssignments)
                self.mytree.write(self.question_type_pool_qpl_file_path_output)

        def taxonomy_file_refresh(self, file_location):
            self.file_location = file_location
            # print("refresh_file_location: " + str(self.file_location))
            with open(self.file_location, 'r') as xml_file:
                xml_str = xml_file.read()
            xml_str = xml_str.replace('ns0:', 'exp:')
            xml_str = xml_str.replace('ns2:', 'ds:')
            xml_str = xml_str.replace('ns3:', '')  # replace "x" with "new value for x"
            xml_str = xml_str.replace(
                '<exp:Export xmlns:ns0="http://www.ilias.de/Services/Export/exp/4_1" xmlns:ns2="http://www.ilias.de/Services/DataSet/ds/4_3" xmlns:ns3="http://www.ilias.de/Services/Taxonomy/tax/4_3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" InstallationId="0" InstallationUrl="https://ilias.th-koeln.de" Entity="tax" SchemaVersion="4.3.0" TargetRelease="5.4.0" xsi:schemaLocation="http://www.ilias.de/Services/Export/exp/4_1 https://ilias.th-koeln.de/xml/ilias_export_4_1.xsd http://www.ilias.de/Services/Taxonomy/tax/4_3 https://ilias.th-koeln.de/xml/ilias_tax_4_3.xsd http://www.ilias.de/Services/DataSet/ds/4_3 https://ilias.th-koeln.de/xml/ilias_ds_4_3.xsd">',
                '<exp:Export InstallationId="0" InstallationUrl="https://ilias.th-koeln.de" Entity="tax" SchemaVersion="4.3.0" TargetRelease="5.4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:exp="http://www.ilias.de/Services/Export/exp/4_1" xsi:schemaLocation="http://www.ilias.de/Services/Export/exp/4_1 https://ilias.th-koeln.de/xml/ilias_export_4_1.xsd http://www.ilias.de/Services/Taxonomy/tax/4_3 https://ilias.th-koeln.de/xml/ilias_tax_4_3.xsd http://www.ilias.de/Services/DataSet/ds/4_3 https://ilias.th-koeln.de/xml/ilias_ds_4_3.xsd" xmlns="http://www.ilias.de/Services/Taxonomy/tax/4_3" xmlns:ds="http://www.ilias.de/Services/DataSet/ds/4_3">')
            xml_str = xml_str.replace(
                '<exp:Export xmlns:ns0="http://www.ilias.de/Services/Export/exp/4_1" xmlns:ns2="http://www.ilias.de/Services/DataSet/ds/4_3" xmlns:ns3="http://www.ilias.de/Services/Taxonomy/tax/4_3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" Entity="tax" InstallationId="0" InstallationUrl="https://ilias.th-koeln.de" SchemaVersion="4.3.0" TargetRelease="5.4.0" xsi:schemaLocation="http://www.ilias.de/Services/Export/exp/4_1 https://ilias.th-koeln.de/xml/ilias_export_4_1.xsd http://www.ilias.de/Services/Taxonomy/tax/4_3 https://ilias.th-koeln.de/xml/ilias_tax_4_3.xsd http://www.ilias.de/Services/DataSet/ds/4_3 https://ilias.th-koeln.de/xml/ilias_ds_4_3.xsd">',
                '<exp:Export InstallationId="0" InstallationUrl="https://ilias.th-koeln.de" Entity="tax" SchemaVersion="4.3.0" TargetRelease="5.4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:exp="http://www.ilias.de/Services/Export/exp/4_1" xsi:schemaLocation="http://www.ilias.de/Services/Export/exp/4_1 https://ilias.th-koeln.de/xml/ilias_export_4_1.xsd http://www.ilias.de/Services/Taxonomy/tax/4_3 https://ilias.th-koeln.de/xml/ilias_tax_4_3.xsd http://www.ilias.de/Services/DataSet/ds/4_3 https://ilias.th-koeln.de/xml/ilias_ds_4_3.xsd" xmlns="http://www.ilias.de/Services/Taxonomy/tax/4_3" xmlns:ds="http://www.ilias.de/Services/DataSet/ds/4_3">')

            with open(self.file_location, 'w') as replaced_xml_file:
                replaced_xml_file.write(xml_str)







        ###### ZUSÄTZLICHE FUNKTIONEN ###############

        # Auflistung der Ordner im Ordner-Pfad: pool_directory_output
        def find_max_id_in_dir(self, directory_path, question_type):

            self.list_of_directories = []
            self.list_of_file_IDs = []
            self.filename_with_zip_index = []


            self.list_of_directories = os.listdir(directory_path)
            self.question_type = question_type



            # Wird in der Liste eine Datei mit der Endung "*.zip" gefunden, dann Index speichern
            for i in range(len(self.list_of_directories)):
                if ".zip" in self.list_of_directories[i]:
                    self.filename_with_zip_index.append(i)



            # Aus der Datei-Liste alle Einträge aus der *.zip Liste entfernen
            # Dadurch enthält die Datei-Liste keine Namen mehr mit ".zip" Endung
            # .pop entfernt einen Eintrag aus der Liste und schiebt die restlichen Einträge wieder zusammen
            # Werden mehrere Einträge entfernt, ändert sich auch immer der Index der verbleibenden Einträge
            # z.B: Liste mit 5 Einträgen: Liste[0,1,2,3,4] -> Liste.pop(0) -> Liste[1,2,3,4]
            # Sollen mehrerer Einträge entfernt werden, veschiebt sich der Index um die Anzahl der bereits gelöschten Einträge
            # Daher ist hier auch ein .pop(x)-j ("j" für Schleifendurchlauf), da sich der Index bei jeden ".pop()" und 1 verschiebt
            for j in range(len(self.filename_with_zip_index)):
                self.list_of_directories.pop(self.filename_with_zip_index[j]-j)


            # Die letzten sieben (7) Zeichen des Orndernamen in eine Liste packen. Die letzten 7 Zeichen geben die ID des Fragenpools an
            # Die Ordnernamen für ILIAS sind immer in dem Format: z.B.: 1604407426__0__tst_2040314
            # Die ID wird im nachhinein um "1" inkrementiert
            for k in range(len(self.list_of_directories)):

                self.list_of_file_IDs.append(self.list_of_directories[k][-7:])

            # Wenn keine Ordner gefunden werden, dann ID aus Vorlage übernehmen
            if len(self.list_of_directories) == 0:

                # Falls sich keine *.zip Ordner in der "ilias_pool_abgabe" befinden, wird die ID über eine Vorlage (fest hinterlegt) bestimmt.
                # Die Zahl muss 7-stellig sein!
                self.pool_id_file_zip_template = ""

                if self.question_type == "formelfrage":
                    self.pool_id_file_zip_template = "1115532"
                elif self.question_type == "singlechoice":
                    self.pool_id_file_zip_template = "2225532"
                elif self.question_type == "multiplechoice":
                    self.pool_id_file_zip_template = "3335532"
                elif self.question_type == "zuordnungsfrage":
                    self.pool_id_file_zip_template = "4445532"
                else:
                    self.pool_id_file_zip_template = "6665532"


                self.list_of_file_IDs.append(self.pool_id_file_zip_template)

            # Alle String Einträge nach "INT" konvertieren um mit der max() funktion die höchste ID herauszufiltern
            self.list_of_file_IDs = list(map(int, self.list_of_file_IDs))
            self.file_max_id = str(max(self.list_of_file_IDs)+1)

            return self.file_max_id

        # Ordner erstellen
        def createFolder(self, directory):
            try:
                if not os.path.exists(directory):
                    os.makedirs(directory)
            except OSError:
                print('Error: Creating directory. ' + directory)

        def create_pool_dir_from_template(self, pool_directory_output):
            # Gibt den Pfad zum Ordner an, indem der Pool erstellt wird
            # --> ILIAS-Formelfrage\ff_ilias_pool_abgabe
            self.pool_directory_output = pool_directory_output

            # Neuen Ordner erstellen
            XML_Interface.createFolder(self, os.path.normpath(os.path.join(self.pool_directory_output, self.ilias_id_pool_qpl_dir)))
            #print("======", os.path.normpath(os.path.join(self.pool_directory_output, self.ilias_id_pool_qpl_dir)))

            # Hier wird das Verzeichnis kopiert, um die Struktur vom Fragenpool-Ordner zu erhalten
            # Die Struktur stammt aus einem Vorlage-Ordner. Die notwendigen XML Dateien werden im Anschluss ersetzt bzw. mit Werten aktualisiert
            XML_Interface.copytree(self, os.path.normpath(os.path.join(self.project_root_path, "Vorlage_für_Fragenpool", 'Vorlage_1596569820__0__qpl_2074808')),
                     os.path.normpath(os.path.join(self.pool_directory_output, self.ilias_id_pool_qpl_dir)))

            # Da durch "copytree" alle Daten kopiert werden, werden hier die qpl.xml und die qti.xml auf die aktuelle Nummer umbenannt und später dadurch überschrieben
            # Anpassung ID für "qti".xml
            os.rename(os.path.normpath(os.path.join(self.pool_directory_output, self.ilias_id_pool_qpl_dir, "1596569820__0__qti_2074808.xml")),
                      os.path.normpath(os.path.join(self.pool_directory_output, self.ilias_id_pool_qpl_dir, self.ilias_id_pool_qti_xml)))

            # Anpassung ID für "qpl".xml
            os.rename(os.path.normpath(os.path.join(self.pool_directory_output, self.ilias_id_pool_qpl_dir, "1596569820__0__qpl_2074808.xml")),
                      os.path.normpath(os.path.join(self.pool_directory_output, self.ilias_id_pool_qpl_dir, self.ilias_id_pool_qpl_xml)))

        # Kopiert komplette Ordnerstruktur und Inhalt. WIrd für Pool Erstellung verwendet
        def copytree(self, src, dst, symlinks=False, ignore=None):
            for item in os.listdir(src):
                s = os.path.join(src, item)
                d = os.path.join(dst, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, symlinks, ignore)
                else:
                    shutil.copy2(s, d)

        def add_dir_for_images(self, orig_img_file_path, dir_path, img_name, img_format, id_nr):

            # Pfad zum Ziel-Ordner. Test oder Pool Ordner , indem das Bild eingefügt werden soll
            self.orig_img_file_path = orig_img_file_path
            self.dir_path = dir_path
            self.img_name = img_name
            self.img_format = img_format

            if self.orig_img_file_path != "":

                # Neuen Ordner in object Ordner ablegen
                self.object_dir = 'il_0_mob_000000' + str(id_nr)
                XML_Interface.createFolder(self, self.dir_path + '/' + self.object_dir + '/')

                self.object_img_dir_output_path = os.path.join(self.dir_path, self.object_dir, self.img_name + "." +self.img_format)



                #Bild Datei kopieren
                print("++++++++++++++++++++++",self.orig_img_file_path, self.object_img_dir_output_path )
                shutil.copyfile(self.orig_img_file_path, self.object_img_dir_output_path)





            # if question_pool_img_path != "ilias_id_pool_img_dir_not_used_for_ilias_test":
            #     if test_or_pool == "ilias_test":
            #
            #         if self.description_img_name_var != "" and self.description_img_name_var != "EMPTY":
            #             XML_Interface.createFolder(self, self.question_test_img_path + '/' + 'il_0_mob_000000' + str(id_nr) + '/')
            #
            #             # img wird immer als PNG Datei abgelegt.
            #             with open(os.path.join(self.question_test_img_path, "il_0_mob_000000" + str(id_nr), self.description_img_name_var + ".png"), 'wb') as image_file:
            #                 image_file.write(self.description_img_data_var)
            #
            #             self.image = Image.open(os.path.join(self.question_test_img_path, "il_0_mob_000000" + str(id_nr), self.description_img_name_var + ".png"))
            #             self.image.save(os.path.join(self.question_test_img_path, "il_0_mob_000000" + str(id_nr), self.description_img_name_var + ".png"))
            #
            #     else:  # image pool
            #         if self.description_img_name_var != "" and self.description_img_name_var != "EMPTY":
            #             XML_Interface.createFolder(self, self.question_pool_img_path + '/' + 'il_0_mob_000000' + str(id_nr) + '/')
            #
            #             # img wird immer als PNG Datei abgelegt.
            #             # with open(self.question_pool_img_path + "\\il_0_mob_000000" + str(id_nr) + "\\" + self.description_img_name_var + ".png", 'wb') as image_file:
            #             with open(os.path.join(self.question_pool_img_path, "il_0_mob_000000" + str(id_nr), self.description_img_name_var + ".png"), 'wb') as image_file:
            #                 image_file.write(self.description_img_data_var)
            #
            #             self.image = Image.open(os.path.join(self.question_pool_img_path, "il_0_mob_000000" + str(id_nr), self.description_img_name_var + ".png"))
            #             self.image.save(os.path.join(self.question_pool_img_path, "il_0_mob_000000" + str(id_nr), self.description_img_name_var + ".png"))

        def get_img_name_and_format_from_path(self, img_path):

            # Im Ordnernamen dürfen keine Umlaute vorhanden sein
            self.char_to_replace_dict = {'A': 'AE',
                                         'Ö': 'OE',
                                         'Ü': 'UE',
                                         'ä': 'ae',
                                         'ö': 'oe',
                                         'ü': 'ue',
                                         'ß': 'ss',
                                         }

            self.img_path = img_path

            self.find_img_name_index = self.img_path.rfind("/")  # Gibt den Index in dem das letzte "/" auftaucht an. "rfind" durchsucht den String von rechts beginnend
            self.find_img_format_index = self.img_path.rfind(".")  # Gibt den Index in dem das letzte "/" auftaucht an. "rfind" durchsucht den String von rechts beginnend

            self.img_name = self.img_path[int(self.find_img_name_index) + 1: int(self.find_img_format_index)]  # letzten char des bildnamens ist das dateiformat: Testbild.jpg
            self.img_format = self.img_path[int(self.find_img_format_index)+1:]

            for key, value in self.char_to_replace_dict.items():
                self.img_name = self.img_name.replace(key, value)


            return self.img_name, self.img_format

        def add_picture_to_description_main(self, description_img_path_1, description_img_path_2, description_img_path_3, img_file_path_output,
                                              question_description_main, question_description_mattext, question_description_material, id_nr):

            self.description_img_path_1 = description_img_path_1
            self.description_img_path_2 = description_img_path_2
            self.description_img_path_3 = description_img_path_3
            self.img_file_path_output = img_file_path_output
            self.question_description_main = question_description_main
            self.question_description_mattext = question_description_mattext



            self.description_img_name_1, self.description_img_format_1  = XML_Interface.get_img_name_and_format_from_path(self, self.description_img_path_1)
            self.description_img_name_2, self.description_img_format_2  = XML_Interface.get_img_name_and_format_from_path(self, self.description_img_path_2)
            self.description_img_name_3, self.description_img_format_3  = XML_Interface.get_img_name_and_format_from_path(self, self.description_img_path_3)


            # Ordner erzeugen und Bild ablegen
            XML_Interface.add_dir_for_images(self, self.description_img_path_1, self.img_file_path_output, self.description_img_name_1, self.description_img_format_1, id_nr)
            XML_Interface.add_dir_for_images(self, self.description_img_path_2, self.img_file_path_output, self.description_img_name_2, self.description_img_format_2, id_nr)
            XML_Interface.add_dir_for_images(self, self.description_img_path_3, self.img_file_path_output, self.description_img_name_3, self.description_img_format_3, id_nr)



            self.picture_string_name_replace_1 = "%Bild1%"
            self.picture_string_name_replace_2 = "%Bild2%"
            self.picture_string_name_replace_3 = "%Bild3%"

            self.check_img_1_exists = False
            self.check_img_2_exists = False
            self.check_img_3_exists = False

            self.question_description_mattext = "<p>" + self.question_description_main + "</p>"
            self.question_description_mattext = XML_Interface.set_picture_in_main(self, self.description_img_path_1, self.description_img_name_1, self.description_img_format_1, "%Bild1%", self.question_description_mattext, question_description_material, id_nr, "0")
            self.question_description_mattext = XML_Interface.set_picture_in_main(self, self.description_img_path_2, self.description_img_name_2, self.description_img_format_2, "%Bild2%", self.question_description_mattext, question_description_material, id_nr, "1")
            self.question_description_mattext = XML_Interface.set_picture_in_main(self, self.description_img_path_3, self.description_img_name_3, self.description_img_format_3, "%Bild3%", self.question_description_mattext, question_description_material, id_nr, "2")

            # prüfen ob alle leer sind?
            #if (self.description_img_data_1 == "" or self.description_img_data_1 == "EMPTY") and (self.description_img_data_2 == "" or self.description_img_data_2 == "EMPTY") and (self.description_img_data_3 == "" or self.description_img_data_3 == "EMPTY"):
            #    self.question_description_mattext = "<p>" + self.question_description_main + "</p>"


            return self.question_description_mattext

        def set_picture_in_main(self, img_path, img_name,img_format, picture_string_name_replace_var, question_description_mattext, question_description_material, id_nr, img_id_nr):

            # img_id: ist notwendig weil die Fragen eigene ID bekommen

            self.img_path = img_path
            self.img_name = img_name
            self.img_format = img_format
            self.picture_string_name_replace_var = picture_string_name_replace_var


            if self.img_path != "":

                self.file_image_raw = Image.open(self.img_path)
                self.file_image_size_width, self.file_image_size_height = self.file_image_raw.size

                self.picture_in_main = "<p><img height=\"" + str(self.file_image_size_height) + "\" src=\"il_0_mob_000000" + str(img_id_nr) + "\" width=\"" + str(self.file_image_size_width) + "\" /></p>"

                # Wird eine Bild Position im Fragen Text eingetragen, wird es hier durch das eigentliche Bild ersetzt
                if self.picture_string_name_replace_var in question_description_mattext.split():
                    question_description_mattext = question_description_mattext.replace(self.picture_string_name_replace_var, self.picture_in_main)

                else:
                    # Wird keine Bild position gewählt, dann wird das Bild am Ende des Textes angehangen
                    question_description_mattext = "<p>" + question_description_mattext + "</p>" + self.picture_in_main

                matimage = ET.SubElement(question_description_material, 'matimage')
                matimage.set('label', "il_0_mob_000000" + str(img_id_nr))  # Object -> Filename
                matimage.set('uri', "objects/il_0_mob_000000" + str(id_nr) + "/" + self.img_name + "." + self.img_format)





            return question_description_mattext




        # Textformatierung
        def replace_amp_in_xml_file(self, file_path_qti_xml):
            # Im Nachgang werden alle "&amp;" wieder gegen "&" getauscht
            # "&" Zeichen kann XML nicht verarbeiten, daher wurde beim schreiben der Texte in die XML "&" gegen "&amp;" getauscht

            # XML Datei zum lesen öffnen 'r' -> "read"
            with open(file_path_qti_xml, 'r') as xml_file:
                xml_str = xml_file.read()
            xml_str = xml_str.replace('&amp;', '&')  # replace 'x' with 'new_x'

            # In XML Datei schreiben 'w" -> "write"
            with open(file_path_qti_xml, 'w') as replaced_xml_file:
                replaced_xml_file.write(xml_str)

            print("...XML_DATEI_QTI --  \"&amp;\"-ZEICHEN ÜBERARBEITUNG ABGESCHLOSSEN!")

        def format_description_text_in_xml(self, description_main_entry):

            #self.var_use_latex_on_text_check = var_use_latex_on_text_check
            self.description_main_entry = description_main_entry

            self.index_list = []


            for i in range(1, len(self.description_main_entry)):
                if self.description_main_entry[i] == '_':
                    self.position_begin = i
                    self.position_end = self.description_main_entry.find(" ", self.position_begin)
                    self.index_list.append(self.position_end)
                    self.description_main_entry = self.description_main_entry[:self.position_end] + ' </sub>' + self.description_main_entry[self.position_end:]

            for i in range(1, len(self.description_main_entry)):
                if self.description_main_entry[i] == '^':
                    self.position_begin = i
                    self.position_end = self.description_main_entry.find(" ", self.position_begin)
                    self.index_list.append(self.position_end)
                    self.description_main_entry = self.description_main_entry[:self.position_end] + ' </sup>' + self.description_main_entry[self.position_end:]

            self.description_main_entry = self.description_main_entry.replace('&', "&amp;")
            self.description_main_entry = self.description_main_entry.replace('\n', "&lt;/p&gt;&#13;&#10;&lt;p&gt;")
            self.description_main_entry = self.description_main_entry.replace('\\)', " </span>")
            self.description_main_entry = self.description_main_entry.replace('\\(', "<span class=\"latex\">")
            self.description_main_entry = self.description_main_entry.replace('^', "<sup>")
            self.description_main_entry = self.description_main_entry.replace('_', "<sub>")
            self.description_main_entry = self.description_main_entry.replace('///', "</i> ")
            self.description_main_entry = self.description_main_entry.replace('//', "<i>")
            self.description_main_entry = self.description_main_entry.replace('$V', "$v")
            self.description_main_entry = self.description_main_entry.replace('$R', "$r")




            return self.description_main_entry

