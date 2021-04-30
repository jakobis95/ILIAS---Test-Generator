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
                    XML_Interface.ff_question_structure(self, self.test_data[i], self.table_index_dict, self.id_nr, self.pool_qpl_file_path_template, self.pool_qpl_file_path_output, self.img_file_path_output)

                if self.test_data[i][2].lower() == "singlechoice":
                   XML_Interface.sc_question_structure(self, self.test_data[i], self.table_index_dict, self.id_nr, self.pool_qpl_file_path_template, self.pool_qpl_file_path_output,  self.img_file_path_output)

                if self.test_data[i][2].lower() == "multiplechoice":
                   XML_Interface.mc_question_structure(self, self.test_data[i], self.table_index_dict, self.id_nr, self.pool_qpl_file_path_template, self.pool_qpl_file_path_output,  self.img_file_path_output)
                
                if self.test_data[i][2].lower() == "zuordnungsfrage":
                   XML_Interface.mq_question_structure(self, self.test_data[i], self.table_index_dict, self.id_nr, self.pool_qpl_file_path_template, self.pool_qpl_file_path_output,  self.img_file_path_output)


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
        def ff_question_structure(self, test_data_list, table_index_dict, id_nr, pool_qpl_file_path_template , pool_qpl_file_path_output, img_file_path):
                """Diese Funktion wandelt die SQL-Einträge in die .xml um, welche anschließend in ILIAS eingespielt werden kann"""


                self.pool_qpl_file_path_template = pool_qpl_file_path_template
                self.pool_qpl_file_path_output = pool_qpl_file_path_output

                self.img_file_path_output = img_file_path

                #self.ff_question_description_main = test_generator_modul_taxonomie_und_textformatierung.Textformatierung.format_description_text_in_xml(self, self.ff_var_use_latex_on_text_check.get(), test_data_list[table_index_dict[0]['question_description_main']])
                # Abfrage LATEX fehlt
                self.ff_question_description_main = XML_Interface.format_description_text_in_xml(self, test_data_list[table_index_dict[0]['question_description_main']])




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
                item.set('title', test_data_list[table_index_dict[0]['question_title']])

                # Fragen-Titel Beschreibung
                qticomment.text = test_data_list[table_index_dict[0]['question_description_title']]

                # Testdauer -- "duration" in xml
                # wird keine Testzeit eingetragen, wird 1h vorausgewählt
                duration.text = test_data_list[table_index_dict[0]['test_time']]
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
                fieldentry.text = test_data_list[table_index_dict[0]['question_author']]
                # -----------------------------------------------------------------------POINTS
                qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
                fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
                fieldlabel.text = "points"
                fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
                fieldentry.text = str(test_data_list[table_index_dict[0]['res1_points']])

                # Fragentitel einsetzen -- "presentation label" in xml
                presentation.set('label', test_data_list[table_index_dict[0]['question_title']])

                # Fragen-Text (Format) einsetzen -- "mattext_texttype" in xml -- Gibt das Format des Textes an
                question_description_mattext.set('texttype', "text/html")

                # Fragen-Text (Text) einsetzen   -- "mattext_texttype" in xml -- Gibt die eigentliche Fragen-Beschreibung an
                # Wenn Bild enthalten ist, dann in Fragenbeschreibung einbetten
                question_description_mattext.text = XML_Interface.add_picture_to_description_main(
                                                    self,
                                                    test_data_list[table_index_dict[0]['description_img_path_1']],
                                                    test_data_list[table_index_dict[0]['description_img_path_2']],
                                                    test_data_list[table_index_dict[0]['description_img_path_3']],
                                                    self.img_file_path_output,
                                                    self.ff_question_description_main, question_description_mattext, question_description_material, id_nr)




                # ----------------------------------------------------------------------- Variable
                XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v1", test_data_list[table_index_dict[0]['var1_min']], test_data_list[table_index_dict[0]['var1_max']], test_data_list[table_index_dict[0]['var1_prec']], test_data_list[table_index_dict[0]['var1_divby']], test_data_list[table_index_dict[0]['var1_unit']])
                XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v2", test_data_list[table_index_dict[0]['var2_min']], test_data_list[table_index_dict[0]['var2_max']], test_data_list[table_index_dict[0]['var2_prec']], test_data_list[table_index_dict[0]['var2_divby']], test_data_list[table_index_dict[0]['var2_unit']])
                XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v3", test_data_list[table_index_dict[0]['var3_min']], test_data_list[table_index_dict[0]['var3_max']], test_data_list[table_index_dict[0]['var3_prec']], test_data_list[table_index_dict[0]['var3_divby']], test_data_list[table_index_dict[0]['var3_unit']])
                XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v4", test_data_list[table_index_dict[0]['var4_min']], test_data_list[table_index_dict[0]['var4_max']], test_data_list[table_index_dict[0]['var4_prec']], test_data_list[table_index_dict[0]['var4_divby']], test_data_list[table_index_dict[0]['var4_unit']])
                XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v5", test_data_list[table_index_dict[0]['var5_min']], test_data_list[table_index_dict[0]['var5_max']], test_data_list[table_index_dict[0]['var5_prec']], test_data_list[table_index_dict[0]['var5_divby']], test_data_list[table_index_dict[0]['var6_unit']])
                XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v6", test_data_list[table_index_dict[0]['var6_min']], test_data_list[table_index_dict[0]['var6_max']], test_data_list[table_index_dict[0]['var6_prec']], test_data_list[table_index_dict[0]['var6_divby']], test_data_list[table_index_dict[0]['var1_unit']])
                XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v7", test_data_list[table_index_dict[0]['var7_min']], test_data_list[table_index_dict[0]['var7_max']], test_data_list[table_index_dict[0]['var7_prec']], test_data_list[table_index_dict[0]['var7_divby']], test_data_list[table_index_dict[0]['var7_unit']])
                XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v8", test_data_list[table_index_dict[0]['var8_min']], test_data_list[table_index_dict[0]['var8_max']], test_data_list[table_index_dict[0]['var8_prec']], test_data_list[table_index_dict[0]['var8_divby']], test_data_list[table_index_dict[0]['var8_unit']])
                XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v9", test_data_list[table_index_dict[0]['var9_min']], test_data_list[table_index_dict[0]['var9_max']], test_data_list[table_index_dict[0]['var9_prec']], test_data_list[table_index_dict[0]['var9_divby']], test_data_list[table_index_dict[0]['var9_unit']])
                XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v10", test_data_list[table_index_dict[0]['var10_min']], test_data_list[table_index_dict[0]['var10_max']], test_data_list[table_index_dict[0]['var10_prec']], test_data_list[table_index_dict[0]['var10_divby']], test_data_list[table_index_dict[0]['var10_unit']])
                XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v11", test_data_list[table_index_dict[0]['var11_min']], test_data_list[table_index_dict[0]['var11_max']], test_data_list[table_index_dict[0]['var11_prec']], test_data_list[table_index_dict[0]['var11_divby']], test_data_list[table_index_dict[0]['var11_unit']])
                XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v12", test_data_list[table_index_dict[0]['var12_min']], test_data_list[table_index_dict[0]['var12_max']], test_data_list[table_index_dict[0]['var12_prec']], test_data_list[table_index_dict[0]['var12_divby']], test_data_list[table_index_dict[0]['var12_unit']])
                XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v13", test_data_list[table_index_dict[0]['var13_min']], test_data_list[table_index_dict[0]['var13_max']], test_data_list[table_index_dict[0]['var13_prec']], test_data_list[table_index_dict[0]['var13_divby']], test_data_list[table_index_dict[0]['var13_unit']])
                XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v14", test_data_list[table_index_dict[0]['var14_min']], test_data_list[table_index_dict[0]['var14_max']], test_data_list[table_index_dict[0]['var14_prec']], test_data_list[table_index_dict[0]['var14_divby']], test_data_list[table_index_dict[0]['var14_unit']])
                XML_Interface.ff_question_variables_structure(self, qtimetadata, "$v15", test_data_list[table_index_dict[0]['var15_min']], test_data_list[table_index_dict[0]['var15_max']], test_data_list[table_index_dict[0]['var15_prec']], test_data_list[table_index_dict[0]['var15_divby']], test_data_list[table_index_dict[0]['var15_unit']])



                # ----------------------------------------------------------------------- Solution
                XML_Interface.ff_question_results_structure(self, qtimetadata, "$r1", test_data_list[table_index_dict[0]['res1_formula']], test_data_list[table_index_dict[0]['res1_min']], test_data_list[table_index_dict[0]['res1_max']], test_data_list[table_index_dict[0]['res1_prec']], test_data_list[table_index_dict[0]['res1_tol']], test_data_list[table_index_dict[0]['res1_points']], test_data_list[table_index_dict[0]['res1_unit']])
                XML_Interface.ff_question_results_structure(self, qtimetadata, "$r2", test_data_list[table_index_dict[0]['res2_formula']], test_data_list[table_index_dict[0]['res2_min']], test_data_list[table_index_dict[0]['res2_max']], test_data_list[table_index_dict[0]['res2_prec']], test_data_list[table_index_dict[0]['res2_tol']], test_data_list[table_index_dict[0]['res2_points']], test_data_list[table_index_dict[0]['res2_unit']])
                XML_Interface.ff_question_results_structure(self, qtimetadata, "$r3", test_data_list[table_index_dict[0]['res3_formula']], test_data_list[table_index_dict[0]['res3_min']], test_data_list[table_index_dict[0]['res3_max']], test_data_list[table_index_dict[0]['res3_prec']], test_data_list[table_index_dict[0]['res3_tol']], test_data_list[table_index_dict[0]['res3_points']], test_data_list[table_index_dict[0]['res3_unit']])
                XML_Interface.ff_question_results_structure(self, qtimetadata, "$r4", test_data_list[table_index_dict[0]['res4_formula']], test_data_list[table_index_dict[0]['res4_min']], test_data_list[table_index_dict[0]['res4_max']], test_data_list[table_index_dict[0]['res4_prec']], test_data_list[table_index_dict[0]['res4_tol']], test_data_list[table_index_dict[0]['res4_points']], test_data_list[table_index_dict[0]['res4_unit']])
                XML_Interface.ff_question_results_structure(self, qtimetadata, "$r5", test_data_list[table_index_dict[0]['res5_formula']], test_data_list[table_index_dict[0]['res5_min']], test_data_list[table_index_dict[0]['res5_max']], test_data_list[table_index_dict[0]['res5_prec']], test_data_list[table_index_dict[0]['res5_tol']], test_data_list[table_index_dict[0]['res5_points']], test_data_list[table_index_dict[0]['res5_unit']])
                XML_Interface.ff_question_results_structure(self, qtimetadata, "$r6", test_data_list[table_index_dict[0]['res6_formula']], test_data_list[table_index_dict[0]['res6_min']], test_data_list[table_index_dict[0]['res6_max']], test_data_list[table_index_dict[0]['res6_prec']], test_data_list[table_index_dict[0]['res6_tol']], test_data_list[table_index_dict[0]['res6_points']], test_data_list[table_index_dict[0]['res6_unit']])
                XML_Interface.ff_question_results_structure(self, qtimetadata, "$r7", test_data_list[table_index_dict[0]['res7_formula']], test_data_list[table_index_dict[0]['res7_min']], test_data_list[table_index_dict[0]['res7_max']], test_data_list[table_index_dict[0]['res7_prec']], test_data_list[table_index_dict[0]['res7_tol']], test_data_list[table_index_dict[0]['res7_points']], test_data_list[table_index_dict[0]['res7_unit']])
                XML_Interface.ff_question_results_structure(self, qtimetadata, "$r8", test_data_list[table_index_dict[0]['res8_formula']], test_data_list[table_index_dict[0]['res8_min']], test_data_list[table_index_dict[0]['res8_max']], test_data_list[table_index_dict[0]['res8_prec']], test_data_list[table_index_dict[0]['res8_tol']], test_data_list[table_index_dict[0]['res8_points']], test_data_list[table_index_dict[0]['res8_unit']])
                XML_Interface.ff_question_results_structure(self, qtimetadata, "$r9", test_data_list[table_index_dict[0]['res9_formula']], test_data_list[table_index_dict[0]['res9_min']], test_data_list[table_index_dict[0]['res9_max']], test_data_list[table_index_dict[0]['res9_prec']], test_data_list[table_index_dict[0]['res9_tol']], test_data_list[table_index_dict[0]['res9_points']], test_data_list[table_index_dict[0]['res9_unit']])
                XML_Interface.ff_question_results_structure(self, qtimetadata, "$r10", test_data_list[table_index_dict[0]['res10_formula']], test_data_list[table_index_dict[0]['res10_min']], test_data_list[table_index_dict[0]['res10_max']], test_data_list[table_index_dict[0]['res10_prec']], test_data_list[table_index_dict[0]['res10_tol']], test_data_list[table_index_dict[0]['res10_points']], test_data_list[table_index_dict[0]['res10_unit']])








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

        def ff_question_results_structure(self, xml_qtimetadata, ff_res_name, ff_res_formula, ff_res_min, ff_res_max, ff_res_prec, ff_res_tol, ff_res_points, ff_res_unit):

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
                self.ff_res_formula = replace_words_in_formula(self.ff_res_formula)




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





    ####################### QUESTION_ANSWER STRUCTURE #############################
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
            for ff_row in self.dataframe.itertuples():

                if ff_row.question_type == "formelfrage":

                    index_list = self.table_index_list[self.table_dict[ff_row.question_type]]
                    index_dict = self.table_index_dict[self.table_dict[ff_row.question_type]]
                    for i in range(len(self.xlsx_file_column_labels_list)):
                        index_list[index_dict[self.xlsx_file_column_labels_list[i]]][0].set(str(ff_row[i+1]))

                if ff_row.question_type == "singlechoice":
                    index_list = self.table_index_list[self.table_dict[ff_row.question_type]]
                    index_dict = self.table_index_dict[self.table_dict[ff_row.question_type]]
                    for i in range(len(self.xlsx_file_column_labels_list)):
                        index_list[index_dict[self.xlsx_file_column_labels_list[i]]][0].set(str(ff_row[i+1]))

                if ff_row.question_type == "multiplechoice":
                    index_list = self.table_index_list[self.table_dict[ff_row.question_type]]
                    index_dict = self.table_index_dict[self.table_dict[ff_row.question_type]]
                    for i in range(len(self.xlsx_file_column_labels_list)):
                        index_list[index_dict[self.xlsx_file_column_labels_list[i]]][0].set(str(ff_row[i+1]))

                if ff_row.question_type == "zuordnungsfrage":
                    index_list = self.table_index_list[self.table_dict[ff_row.question_type]]
                    index_dict = self.table_index_dict[self.table_dict[ff_row.question_type]]
                    for i in range(len(self.xlsx_file_column_labels_list)):
                        index_list[index_dict[self.xlsx_file_column_labels_list[i]]][0].set(str(ff_row[i+1]))

                self.DBI.Add_data_to_DB(index_list, index_list[index_dict["question_title"]][0].get())




            # print("Load File: \"" + self.xlsx_path + "\" in formelfrage_table...done!")

            print("     Datei geladen!")


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

