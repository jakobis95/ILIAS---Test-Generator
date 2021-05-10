from tkinter import *
import tkinter as tk
import tkinter.font as font
#from Main import Main
from DB_interface import DB_Interface
from tkinter import ttk
from Fragen_GUI import formelfrage, singlechoice, multiplechoice, zuordnungsfrage
from ScrolledText_Functionality import Textformatierung


class Testeinstellungen():
    def __init__(self, DBI, index_list, index_dict, table_dict, Width, Label_Font, Entry_Font, Button_Font, bg_color, entry_color, label_color, button_color, fg_color):
        self.work_window = Toplevel(bg=bg_color)

        self.table_dict = table_dict
        self.DBI = DBI
        self.index_list = index_list
        self.index_dict = index_dict
        for i in self.index_list:
            i[0].set('')
        self.work_window.geometry("%dx%d+%d+%d" % (Width/1.5, Width/2.7, Width/5, Width/8))
        self.DBI.subscribe(self.Fill_Entrys_From_DB)



        self.frame1 = LabelFrame(self.work_window, text="Test Einstellungen", padx=5, pady=5)
        self.frame1.grid(row=0, column=0, padx=20, pady=10, sticky=NW)

        self.frame2 = LabelFrame(self.work_window, text="Test Einstellungen", padx=5, pady=5)
        self.frame2.grid(row=0, column=1, padx=20, pady=10, sticky=NW)

        self.Labels()
        self.Checkboxes_Entrys()
        self.Radiobuttons()
        self.index_list[self.index_dict['type']][0].set('testeinstellungen')


    def Labels(self):
        self.res12_min_listbox_label = Label(self.frame1, text="EINSTELLUNGEN DES TESTS",
                                             font=('Helvetica', 10, 'bold'))
        self.res12_min_listbox_label.grid(row=0, column=0, sticky=W, padx=10, pady=(20, 0))

        self.res90_min_listbox_label = Label(self.frame1, text="Test-Titel")
        self.res90_min_listbox_label.grid(row=1, column=0, sticky=W, padx=10)
        self.res91_max_listbox_label = Label(self.frame1, text="Beschreibung")
        self.res91_max_listbox_label.grid(row=2, column=0, sticky=W, padx=10)

        self.res1_max_listbox_label = Label(self.frame1, text="Auswahl der Testfragen")
        self.res1_max_listbox_label.grid(row=4, column=0, sticky=W, padx=10)
        self.res1_prec_listbox_label = Label(self.frame1, text="Datenschutz")
        self.res1_prec_listbox_label.grid(row=7, column=0, sticky=W, padx=10)

        self.res1_tol_listbox_label = Label(self.frame1, text="VERFÜGBARKEIT", font=('Helvetica', 10, 'bold'))
        self.res1_tol_listbox_label.grid(row=9, column=0, sticky=W, padx=10, pady=(20, 0))
        self.res1_points_listbox_label = Label(self.frame1, text="Online   ---   not working")
        self.res1_points_listbox_label.grid(row=10, column=0, sticky=W, padx=10)
        self.res13_points_listbox_label = Label(self.frame1,
                                                text="Zeitlich begrenzte Verfügbarkeit   ---   not working")
        self.res13_points_listbox_label.grid(row=11, column=0, sticky=W, padx=10)

        self.res22_tol_listbox_label = Label(self.frame1, text="INFORMATIONEN ZUM EINSTIEG",
                                             font=('Helvetica', 10, 'bold'))
        self.res22_tol_listbox_label.grid(row=14, column=0, sticky=W, padx=10, pady=(20, 0))

        self.res23_points_listbox_label = Label(self.frame1, text="Einleitung")
        self.res23_points_listbox_label.grid(row=15, column=0, sticky=W, padx=10)
        self.res24_points_listbox_label = Label(self.frame1, text="Testeigenschaften anzeigen")
        self.res24_points_listbox_label.grid(row=16, column=0, sticky=W, padx=10)

        self.res31_tol_listbox_label = Label(self.frame1, text="DURCHFÜHRUNG: ZUGANG", font=('Helvetica', 10, 'bold'))
        self.res31_tol_listbox_label.grid(row=17, column=0, sticky=W, padx=10, pady=(20, 0))

        self.test_time_year_label = Label(self.frame1, text="Jahr")
        self.test_time_year_label.grid(row=17, column=1, sticky=W)
        self.test_time_month_label = Label(self.frame1, text="Mon.")
        self.test_time_month_label.grid(row=17, column=1, sticky=W, padx=35)
        self.test_time_day_label = Label(self.frame1, text="Tag")
        self.test_time_day_label.grid(row=17, column=1, sticky=W, padx=70)
        self.test_time_hour_label = Label(self.frame1, text="Std.")
        self.test_time_hour_label.grid(row=17, column=1, sticky=W, padx=105)
        self.test_time_minute_label = Label(self.frame1, text="Min.")
        self.test_time_minute_label.grid(row=17, column=1, sticky=W, padx=140)

        self.res32_points_listbox_label = Label(self.frame1, text="Test-Start")
        self.res32_points_listbox_label.grid(row=18, column=0, sticky=W, padx=10)
        self.res33_points_listbox_label = Label(self.frame1, text="Test-Ende")
        self.res33_points_listbox_label.grid(row=19, column=0, sticky=W, padx=10)
        self.res34_tol_listbox_label = Label(self.frame1, text="Test-Passwort")
        self.res34_tol_listbox_label.grid(row=20, column=0, sticky=W, padx=10)
        self.res35_points_listbox_label = Label(self.frame1, text="Nur ausgewählte Teilnehmer")
        self.res35_points_listbox_label.grid(row=21, column=0, sticky=W, padx=10)
        self.res36_points_listbox_label = Label(self.frame1, text="Anzahl gleichzeitiger Teilnehmer begrenzen")
        self.res36_points_listbox_label.grid(row=22, column=0, sticky=W, padx=10)
        self.res37_points_listbox_label = Label(self.frame1, text="Inaktivitätszeit der Teilnehmner (in Sek.)")
        self.res37_points_listbox_label.grid(row=23, column=0, sticky=W, padx=30)

        self.res41_tol_listbox_label = Label(self.frame1, text="DURCHFÜHRUNG: STEUERUNG TESTDURCHLAUF",
                                             font=('Helvetica', 10, 'bold'))
        self.res41_tol_listbox_label.grid(row=24, column=0, sticky=W, padx=10, pady=(20, 0))
        self.res42_points_listbox_label = Label(self.frame1, text="Anzahl von Testdurchläufen begrenzen")
        self.res42_points_listbox_label.grid(row=25, column=0, sticky=W, padx=10)
        self.res43_points_listbox_label = Label(self.frame1, text="Wartezeit zwischen Durchläufen erzwingen")
        self.res43_points_listbox_label.grid(row=26, column=0, sticky=W, padx=10)
        self.res44_tol_listbox_label = Label(self.frame1, text="Bearbeitungsdauer begrenzen")
        self.res44_tol_listbox_label.grid(row=27, column=0, sticky=W, padx=10)
        self.res44_tol_listbox_label = Label(self.frame1, text="Bearbeitungsdauer (in Min).")
        self.res44_tol_listbox_label.grid(row=28, column=0, sticky=W, padx=30)
        self.res44_tol_listbox_label = Label(self.frame1, text="Max. Bearbeitungsdauer für jeden Testlauf zurücksetzen")
        self.res44_tol_listbox_label.grid(row=29, column=0, sticky=W, padx=30)
        self.res45_points_listbox_label = Label(self.frame1, text="Prüfungsansicht")
        self.res45_points_listbox_label.grid(row=30, column=0, sticky=W, padx=10)
        self.res45_1_points_listbox_label = Label(self.frame1, text="Titel des Tests")
        self.res45_1_points_listbox_label.grid(row=31, column=0, sticky=W, padx=30)
        self.res45_2_points_listbox_label = Label(self.frame1, text="Name des Teilnehmers")
        self.res45_2_points_listbox_label.grid(row=32, column=0, sticky=W, padx=30)
        self.res46_points_listbox_label = Label(self.frame1, text="ILIAS-Prüfungsnummer anzeigen")
        self.res46_points_listbox_label.grid(row=33, column=0, sticky=W, padx=10)

        self.res51_tol_listbox_label = Label(self.frame2, text="DURCHFÜHRUNG: VERHALTEN DER FRAGE",
                                             font=('Helvetica', 10, 'bold'))
        self.res51_tol_listbox_label.grid(row=0, column=2, sticky=W, padx=10, pady=(20, 0))
        self.res52_points_listbox_label = Label(self.frame2, text="Anzeige der Fragentitel")
        self.res52_points_listbox_label.grid(row=1, column=2, sticky=W, padx=10)
        self.res53_points_listbox_label = Label(self.frame2, text="Automatisches speichern")
        self.res53_points_listbox_label.grid(row=4, column=2, sticky=W, padx=10)
        self.res54_tol_listbox_label = Label(self.frame2, text="Fragen mischen")
        self.res54_tol_listbox_label.grid(row=5, column=2, sticky=W, padx=10)
        self.res55_points_listbox_label = Label(self.frame2, text="Lösungshinweise")
        self.res55_points_listbox_label.grid(row=6, column=2, sticky=W, padx=10)
        self.res56_points_listbox_label = Label(self.frame2, text="Direkte Rückmeldung   ---   not working")
        self.res56_points_listbox_label.grid(row=7, column=2, sticky=W, padx=10)
        self.res57_tol_listbox_label = Label(self.frame2, text="Teilnehmerantworten")
        self.res57_tol_listbox_label.grid(row=8, column=2, sticky=W, padx=10)
        self.res58_points_listbox_label = Label(self.frame2, text="Verpflichtende Fragen")
        self.res58_points_listbox_label.grid(row=12, column=2, sticky=W, padx=10)

        self.res61_tol_listbox_label = Label(self.frame2, text="DURCHFÜHRUNG: FUNKTIONEN FÜR TEILNEHMER",
                                             font=('Helvetica', 10, 'bold'))
        self.res61_tol_listbox_label.grid(row=13, column=2, sticky=W, padx=10, pady=(20, 0))
        self.res62_points_listbox_label = Label(self.frame2, text="Verwendung vorheriger Lösungen")
        self.res62_points_listbox_label.grid(row=14, column=2, sticky=W, padx=10)
        self.res63_points_listbox_label = Label(self.frame2, text="\"Test unterbrechen\" anzeigen")
        self.res63_points_listbox_label.grid(row=15, column=2, sticky=W, padx=10)
        self.res64_tol_listbox_label = Label(self.frame2, text="Nicht beantwortete Fragen")
        self.res64_tol_listbox_label.grid(row=16, column=2, sticky=W, padx=10)
        self.res65_points_listbox_label = Label(self.frame2, text="Fragenliste und Bearbeitungsstand anzeigen")
        self.res65_points_listbox_label.grid(row=18, column=2, sticky=W, padx=10)
        self.res66_points_listbox_label = Label(self.frame2, text="Fragen markieren")
        self.res66_points_listbox_label.grid(row=19, column=2, sticky=W, padx=10)

        self.res71_tol_listbox_label = Label(self.frame2, text="TEST ABSCHLIESSEN", font=('Helvetica', 10, 'bold'))
        self.res71_tol_listbox_label.grid(row=20, column=2, sticky=W, padx=10, pady=(20, 0))
        self.res72_points_listbox_label = Label(self.frame2, text="Übersicht gegebener Antworten")
        self.res72_points_listbox_label.grid(row=21, column=2, sticky=W, padx=10)
        self.res73_points_listbox_label = Label(self.frame2, text="Abschließende Bemerkung")
        self.res73_points_listbox_label.grid(row=22, column=2, sticky=W, padx=10)
        self.res74_tol_listbox_label = Label(self.frame2, text="Weiterleitung")
        self.res74_tol_listbox_label.grid(row=23, column=2, sticky=W, padx=10)
        self.res75_points_listbox_label = Label(self.frame2, text="Benachrichtigung")
        self.res75_points_listbox_label.grid(row=24, column=2, sticky=W, padx=10)

        # --------------------------- DEFINE CHECKBOXES WITH ENTRYS ---------------------------------------

        # --------------------------- CHECKBOXES ---------------------------------------
    def Checkboxes_Entrys(self):
        self.var_online = IntVar()
        self.check_online = Checkbutton(self.frame1, text="", variable=self.var_online, onvalue=1, offvalue=0)
        self.check_online.deselect()
        self.check_online.grid(row=10, column=1, sticky=W)

        self.var_time_limited = IntVar()
        self.time_limited_start_label = Label(self.frame1, text="Start")
        self.time_limited_start_day_label = Label(self.frame1, text="Tag")
        self.time_limited_start_day_entry = Entry(self.frame1, width=3, textvariable=self.index_list[self.index_dict['entry_test_start_day']][0])
        self.time_limited_start_month_label = Label(self.frame1, text="Mo")
        self.time_limited_start_month_entry = Entry(self.frame1, width=3, textvariable=self.index_list[self.index_dict['entry_test_start_month']][0])
        self.time_limited_start_year_label = Label(self.frame1, text="Jahr")
        self.time_limited_start_year_entry = Entry(self.frame1, width=4, textvariable=self.index_list[self.index_dict['entry_test_start_year']][0])
        self.time_limited_start_hour_label = Label(self.frame1, text="Std")
        self.time_limited_start_hour_entry = Entry(self.frame1, width=3, textvariable=self.index_list[self.index_dict['entry_test_start_hour']][0])
        self.time_limited_start_minute_label = Label(self.frame1, text="Min")
        self.time_limited_start_minute_entry = Entry(self.frame1, width=3, textvariable=self.index_list[self.index_dict['entry_test_start_minute']][0])

        self.time_limited_end_label = Label(self.frame1, text="Ende")
        self.time_limited_end_day_label = Label(self.frame1, text="Tag")
        self.time_limited_end_day_entry = Entry(self.frame1, width=3, textvariable=self.index_list[self.index_dict['entry_test_end_day']][0])
        self.time_limited_end_month_label = Label(self.frame1, text="Mo")
        self.time_limited_end_month_entry = Entry(self.frame1, width=3, textvariable=self.index_list[self.index_dict['entry_test_end_month']][0])
        self.time_limited_end_year_label = Label(self.frame1, text="Jahr")
        self.time_limited_end_year_entry = Entry(self.frame1, width=4, textvariable=self.index_list[self.index_dict['entry_test_end_year']][0])
        self.time_limited_end_hour_label = Label(self.frame1, text="Std")
        self.time_limited_end_hour_entry = Entry(self.frame1, width=3, textvariable=self.index_list[self.index_dict['entry_test_end_hour']][0])
        self.time_limited_end_minute_label = Label(self.frame1, text="Min")
        self.time_limited_end_minute_entry = Entry(self.frame1, width=3, textvariable=self.index_list[self.index_dict['entry_test_end_minute']][0])


        self.check_time_limited = Checkbutton(self.frame1, text="", variable=self.index_list[self.index_dict['check_time_limited']][0], onvalue=1,
                                              offvalue=0,
                                              command=lambda
                                                  v=self.index_list[self.index_dict['check_time_limited']][0]: self.show_entry_time_limited_start(
                                                  self, v))
        self.check_time_limited.deselect()
        self.check_time_limited.grid(row=11, column=1, sticky=W)


        self.check_introduction = Checkbutton(self.frame1, text="", variable=self.index_list[self.index_dict['check_introduction']][0], onvalue=1,
                                              offvalue=0,
                                              command=lambda
                                                  v=self.index_list[self.index_dict['check_introduction']][0]: self.show_introduction_textfield(
                                                  self, v))
        self.check_introduction.deselect()
        self.check_introduction.grid(row=15, column=1, sticky=W)


        self.check_test_prop = Checkbutton(self.frame1, text="", variable=self.index_list[self.index_dict['check_test_properties']][0], onvalue=1, offvalue=0)
        self.check_test_prop.deselect()
        self.check_test_prop.grid(row=16, column=1, sticky=W)


        self.check_specific_users = Checkbutton(self.frame1, text="", variable=self.index_list[self.index_dict['check_specific_users']][0], onvalue=1,
                                                offvalue=0)
        self.check_specific_users.deselect()
        self.check_specific_users.grid(row=21, column=1, sticky=W)



        self.check_processing_time = Checkbutton(self.frame1, text="", variable=self.index_list[self.index_dict['check_processing_time']][0], onvalue=1,
                                                 offvalue=0)
        self.check_processing_time.deselect()
        self.check_processing_time.grid(row=27, column=1, sticky=W)


        self.check_processing_time_reset = Checkbutton(self.frame1, text="", variable=self.index_list[self.index_dict['check_processing_time_reset']][0],
                                                       onvalue=1, offvalue=0)
        self.check_processing_time_reset.deselect()
        self.check_processing_time_reset.grid(row=29, column=1, sticky=W)


        self.check_examview = Checkbutton(self.frame1, text="", variable=self.index_list[self.index_dict['check_examview']][0], onvalue=1, offvalue=0)
        self.check_examview.deselect()
        self.check_examview.grid(row=30, column=1, sticky=W)

        self.check_examview_test_title = Checkbutton(self.frame1, text="", variable=self.index_list[self.index_dict['check_examview_title']][0],
                                                     onvalue=1, offvalue=0)
        self.check_examview_test_title.deselect()
        self.check_examview_test_title.grid(row=31, column=1, sticky=W)


        self.check_examview_username = Checkbutton(self.frame1, text="", variable=self.index_list[self.index_dict['check_examview_username']][0],
                                                    onvalue=1, offvalue=0)
        self.check_examview_username.deselect()
        self.check_examview_username.grid(row=32, column=1, sticky=W)


        self.check_show_ilias_nr = Checkbutton(self.frame1, text="", variable=self.index_list[self.index_dict['check_show_ilias_nr']][0], onvalue=1,
                                               offvalue=0)
        self.check_show_ilias_nr.deselect()
        self.check_show_ilias_nr.grid(row=33, column=1, sticky=W)


        self.check_autosave = Checkbutton(self.frame2, text="", variable=self.index_list[self.index_dict['check_autosave']][0], onvalue=1, offvalue=0,
                                          command=lambda v=self.index_list[self.index_dict['check_autosave']][0].get(): self.enable_autosave(
                                              self,
                                              v))

        # self.check_autosave_interval_label = Label(self.frame2, text="Speicherintervall (in Sek.):")
        # self.check_autosave_interval_entry = Entry(self.frame2, variable=self.index_list[self.index_dict['entry_autosave_interval']][0], width=10)
        # self.check_autosave.deselect()
        # self.check_autosave.grid(row=4, column=3, sticky=W)

        self.check_mix_questions = Checkbutton(self.frame2, text="", variable=self.index_list[self.index_dict['check_mix_questions']][0], onvalue=1,
                                               offvalue=0)
        self.check_mix_questions.deselect()
        print("Ckeck question hat die werigkeit:",self.index_list[self.index_dict['check_mix_questions']][0].get())
        self.check_mix_questions.grid(row=5, column=3, sticky=W)


        self.check_show_solution_notes = Checkbutton(self.frame2, text="", variable=self.index_list[self.index_dict['check_show_solutions_notes']][0],
                                                     onvalue=1, offvalue=0)
        self.check_show_solution_notes.deselect()
        self.check_show_solution_notes.grid(row=6, column=3, sticky=W)

        self.check_direct_response = Checkbutton(self.frame2, text="", variable=self.index_list[self.index_dict['check_direct_response']][0], onvalue=1,
                                                 offvalue=0)
        self.check_direct_response.deselect()
        self.check_direct_response.grid(row=7, column=3, sticky=W)
        self.index_list[self.index_dict['check_direct_response']][0].set(0)


        self.check_mandatory_questions = Checkbutton(self.frame2, text="", variable=self.index_list[self.index_dict['check_mandatory_questions']][0],
                                                     onvalue=1, offvalue=0)
        self.check_mandatory_questions.deselect()
        self.check_mandatory_questions.grid(row=12, column=3, sticky=W)


        self.check_use_previous_solution = Checkbutton(self.frame2, text="", variable=self.index_list[self.index_dict['check_use_previous_solution']][0],
                                                       onvalue=1, offvalue=0)
        self.check_use_previous_solution.deselect()
        self.check_use_previous_solution.grid(row=14, column=3, sticky=W)


        self.check_show_test_cancel = Checkbutton(self.frame2, text="", variable=self.index_list[self.index_dict['check_show_test_cancel']][0], onvalue=1,
                                                  offvalue=0)
        self.check_show_test_cancel.deselect()
        self.check_show_test_cancel.grid(row=15, column=3, sticky=W)


        self.check_show_question_list_process_status = Checkbutton(self.frame2, text="",
                                                                   variable=self.index_list[self.index_dict['check_show_question_list_process_status']][0],
                                                                   onvalue=1, offvalue=0)
        self.check_show_question_list_process_status.deselect()
        self.check_show_question_list_process_status.grid(row=18, column=3, sticky=W)

        self.check_question_mark = Checkbutton(self.frame2, text="", variable=self.index_list[self.index_dict['check_question_mark']][0], onvalue=1,
                                               offvalue=0)
        self.check_question_mark.deselect()
        self.check_question_mark.grid(row=19, column=3, sticky=W)


        self.check_overview_answers = Checkbutton(self.frame2, text="", variable=self.index_list[self.index_dict['check_overview_answers']][0], onvalue=1,
                                                  offvalue=0)
        self.check_overview_answers.grid(row=21, column=3, sticky=W)

        self.check_show_end_comment = Checkbutton(self.frame2, text="", variable=self.index_list[self.index_dict['check_overview_answers']][0], onvalue=1,
                                                  offvalue=0,
                                                  command=lambda
                                                      v=self.index_list[self.index_dict['check_overview_answers']][0].get(): self.show_concluding_remarks(
                                                      self, v))
        self.check_show_end_comment.deselect()
        self.check_show_end_comment.grid(row=22, column=3, sticky=W)


        self.check_forwarding = Checkbutton(self.frame2, text="", variable=self.index_list[self.index_dict['check_forwarding']][0], onvalue=1, offvalue=0)
        self.check_forwarding.deselect()
        self.check_forwarding.grid(row=23, column=3, sticky=W)


        self.check_notification = Checkbutton(self.frame2, text="", variable=self.index_list[self.index_dict['check_notification']][0], onvalue=1,
                                              offvalue=0)
        self.check_notification.deselect()
        self.check_notification.grid(row=24, column=3, sticky=W)

        # --------------------------- RADIO BUTTONS ---------------------------------------
    def Radiobuttons(self):
        self.select_question = self.index_list[self.index_dict['radio_select_question']][0]
        self.select_question.set(0)
        self.select_question_radiobtn1 = Radiobutton(self.frame1, text="Fest definierte Fragenauswahl",
                                                     variable=self.select_question, value=0)
        self.select_question_radiobtn1.grid(row=4, column=1, pady=0, sticky=W)  # FIXED_QUEST_SET
        self.select_question_radiobtn2 = Radiobutton(self.frame1, text="Zufällige Fragenauswahl",
                                                     variable=self.select_question, value=1)
        self.select_question_radiobtn2.grid(row=5, column=1, pady=0, sticky=W)  # RANDOM_QUEST_SET
        self.select_question_radiobtn3 = Radiobutton(self.frame1,
                                                     text="Wiedervorlagemodus - alle Fragen eines Fragenpools",
                                                     variable=self.select_question, value=2)
        self.select_question_radiobtn3.grid(row=6, column=1, pady=0, sticky=W)  # DYNAMIC_QUEST_SET

        self.select_anonym = IntVar()
        self.select_anonym.set(0)
        self.select_anonym_radiobtn1 = Radiobutton(self.frame1, text="Testergebnisse ohne Namen",
                                                   variable=self.select_anonym, value=0, borderwidth=0,
                                                   command=self.select_anonym.get())
        self.select_anonym_radiobtn1.grid(row=7, column=1, pady=0, sticky=W)
        self.select_anonym_radiobtn2 = Radiobutton(self.frame1, text="Testergebnisse mit Namen",
                                                   variable=self.select_anonym, value=1, borderwidth=0,
                                                   command=self.select_anonym.get())
        self.select_anonym_radiobtn2.grid(row=8, column=1, pady=0, sticky=W)

        self.select_show_question_title = IntVar()
        self.select_show_question_title.set(0)
        self.select_show_question_title_radiobtn1 = Radiobutton(self.frame2, text="Fragentitel und erreichbare Punkte",
                                                                variable=self.select_show_question_title, value=0,
                                                                borderwidth=0,
                                                                command=self.select_show_question_title.get())
        self.select_show_question_title_radiobtn1.grid(row=1, column=3, pady=0, sticky=W)
        self.select_show_question_title_radiobtn2 = Radiobutton(self.frame2, text="Nur Fragentitel",
                                                                variable=self.select_show_question_title, value=1,
                                                                borderwidth=0,
                                                                command=self.select_show_question_title.get())
        self.select_show_question_title_radiobtn2.grid(row=2, column=3, pady=0, sticky=W)
        self.select_show_question_title_radiobtn3 = Radiobutton(self.frame2,
                                                                text="Weder Fragentitel noch erreichbare Punkte",
                                                                variable=self.select_show_question_title, value=2,
                                                                borderwidth=0,
                                                                command=self.select_show_question_title.get())
        self.select_show_question_title_radiobtn3.grid(row=3, column=3, pady=0, sticky=W)

        self.select_user_response = IntVar()
        self.select_user_response.set(0)
        self.select_user_response_radiobtn1 = Radiobutton(self.frame2,
                                                          text="Antworten während des Testdurchlaufs nicht festschreiben",
                                                          variable=self.select_user_response, value=0, borderwidth=0,
                                                          command=self.select_user_response.get())
        self.select_user_response_radiobtn1.grid(row=8, column=3, pady=0, sticky=W)
        self.select_user_response_radiobtn2 = Radiobutton(self.frame2,
                                                          text="Antworten bei Anzeige der Rückmeldung festschreiben",
                                                          variable=self.select_user_response, value=1, borderwidth=0,
                                                          command=self.select_user_response.get())
        self.select_user_response_radiobtn2.grid(row=9, column=3, pady=0, sticky=W)
        self.select_user_response_radiobtn3 = Radiobutton(self.frame2,
                                                          text="Antworten bei Anzeige der Folgefrage festschreiben",
                                                          variable=self.select_user_response, value=2, borderwidth=0,
                                                          command=self.select_user_response.get())
        self.select_user_response_radiobtn3.grid(row=10, column=3, pady=0, sticky=W)
        self.select_user_response_radiobtn4 = Radiobutton(self.frame2,
                                                          text="Antworten mit der Anzeige von Rückmeldungen oder der Folgefrage festschreiben",
                                                          variable=self.select_user_response, value=3, borderwidth=0,
                                                          command=self.select_user_response.get())
        self.select_user_response_radiobtn4.grid(row=11, column=3, pady=0, sticky=W)

        self.select_not_answered_questions = IntVar()
        self.select_not_answered_questions.set(0)
        self.select_not_answered_questions_radiobtn1 = Radiobutton(self.frame2,
                                                                   text="Nicht beantwortete Fragen bleiben an ihrem Platz",
                                                                   variable=self.select_not_answered_questions, value=0,
                                                                   borderwidth=0,
                                                                   command=self.select_not_answered_questions.get())
        self.select_not_answered_questions_radiobtn1.grid(row=16, column=3, pady=0, sticky=W)
        self.select_not_answered_questions_radiobtn2 = Radiobutton(self.frame2,
                                                                   text="Nicht beantwortete Fragen werden ans Testende gesschoben",
                                                                   variable=self.select_not_answered_questions, value=1,
                                                                   borderwidth=0,
                                                                   command=self.select_not_answered_questions.get())
        self.select_not_answered_questions_radiobtn2.grid(row=17, column=3, pady=0, sticky=W)

        # --------------------------- ENTRY BOXES ---------------------------------------

        self.titel_entry = Entry(self.frame1, width=47)
        self.titel_entry.grid(row=1, column=1)
        self.introduction_bar = Scrollbar(self.frame1)
        self.introduction_infobox = Text(self.frame1, height=4, width=40, font=('Helvetica', 9))

        self.test_start_year_entry = Entry(self.frame1, width=5)
        self.test_start_year_entry.grid(row=18, column=1, sticky=W)
        self.test_start_year_entry.insert(0, "YYYY")
        self.test_start_month_entry = Entry(self.frame1, width=5)
        self.test_start_month_entry.grid(row=18, column=1, sticky=W, padx=35)
        self.test_start_month_entry.insert(0, "MM")
        self.test_start_day_entry = Entry(self.frame1, width=5)
        self.test_start_day_entry.grid(row=18, column=1, sticky=W, padx=70)
        self.test_start_day_entry.insert(0, "DD")
        self.test_start_hour_entry = Entry(self.frame1, width=5)
        self.test_start_hour_entry.grid(row=18, column=1, sticky=W, padx=105)
        self.test_start_hour_entry.insert(0, "HH")
        self.test_start_minute_entry = Entry(self.frame1, width=5)
        self.test_start_minute_entry.grid(row=18, column=1, sticky=W, padx=140)
        self.test_start_minute_entry.insert(0, "mm")

        self.test_end_year_entry = Entry(self.frame1, width=5)
        self.test_end_year_entry.grid(row=19, column=1, sticky=W, pady=5)
        self.test_end_year_entry.insert(0, "YYYY")
        self.test_end_month_entry = Entry(self.frame1, width=5)
        self.test_end_month_entry.grid(row=19, column=1, sticky=W, padx=35)
        self.test_end_month_entry.insert(0, "MM")
        self.test_end_day_entry = Entry(self.frame1, width=5)
        self.test_end_day_entry.grid(row=19, column=1, sticky=W, padx=70)
        self.test_end_day_entry.insert(0, "DD")
        self.test_end_hour_entry = Entry(self.frame1, width=5)
        self.test_end_hour_entry.grid(row=19, column=1, sticky=W, padx=105)
        self.test_end_hour_entry.insert(0, "HH")
        self.test_end_minute_entry = Entry(self.frame1, width=5)
        self.test_end_minute_entry.grid(row=19, column=1, sticky=W, padx=140)
        self.test_end_minute_entry.insert(0, "mm")

        self.test_password_entry = Entry(self.frame1, width=20)
        self.test_password_entry.grid(row=20, column=1, sticky=W, pady=3)

        self.description_bar = Scrollbar(self.frame1)
        self.description_infobox = Text(self.frame1, height=4, width=40, font=('Helvetica', 9))
        self.description_bar.grid(row=2, column=2)
        self.description_infobox.grid(row=2, column=1, pady=10)
        self.description_bar.config(command=self.description_infobox.yview)
        self.description_infobox.config(yscrollcommand=self.description_bar.set)

        self.limit_users_max_amount_entry = Entry(self.frame1, width=5)
        self.limit_users_max_amount_entry.grid(row=22, column=1, sticky=W)
        self.inactivity_time_for_users_entry = Entry(self.frame1, width=5)
        self.inactivity_time_for_users_entry.grid(row=23, column=1, sticky=W)
        self.inactivity_time_for_users_entry.insert(0, "300")

        self.limit_test_runs_entry = Entry(self.frame1, width=10)
        self.limit_test_runs_entry.grid(row=25, column=1, sticky=W)
        self.limit_test_runs_entry.insert(0, "3")

        self.limit_time_betw_test_runs_month_entry = Entry(self.frame1, width=5)
        self.limit_time_betw_test_runs_month_entry.grid(row=26, column=1, sticky=W, pady=5)
        self.limit_time_betw_test_runs_month_entry.insert(0, "MM")
        self.limit_time_betw_test_runs_day_entry = Entry(self.frame1, width=5)
        self.limit_time_betw_test_runs_day_entry.grid(row=26, column=1, sticky=W, padx=35)
        self.limit_time_betw_test_runs_day_entry.insert(0, "DD")
        self.limit_time_betw_test_runs_hour_entry = Entry(self.frame1, width=5)
        self.limit_time_betw_test_runs_hour_entry.grid(row=26, column=1, sticky=W, padx=70)
        self.limit_time_betw_test_runs_hour_entry.insert(0, "HH")
        self.limit_time_betw_test_runs_minute_entry = Entry(self.frame1, width=5)
        self.limit_time_betw_test_runs_minute_entry.grid(row=26, column=1, sticky=W, padx=105)
        self.limit_time_betw_test_runs_minute_entry.insert(0, "mm")

        self.limit_processing_time_minutes_entry = Entry(self.frame1, width=5)
        self.limit_processing_time_minutes_entry.grid(row=28, column=1, sticky=W)
        self.limit_processing_time_minutes_entry.insert(0, "90")

        self.concluding_remarks_bar = Scrollbar(self.frame2)
        self.concluding_remarks_infobox = Text(self.frame2, height=4, width=40, font=('Helvetica', 9))

        self.profile_name_label = Label(self.frame2, text="Speichern unter...")
        self.profile_name_label.grid(row=29, column=0)

        self.profile_name_entry = Entry(self.frame2, width=15, textvariable=self.index_list[self.index_dict['profile_name']][0])
        self.profile_name_entry.grid(row=29, column=1)

        self.Save_btn = Button(self.frame2, text="Save Profile", width=15, command=self.save_testeinstellungen_in_db)
        self.Save_btn.grid(row=29, column=3)





    def show_entry_time_limited_start(self, e, var):
        if var.get() == 0:
            self.time_limited_start_label.grid_forget()
            self.time_limited_start_year_label.grid_forget()
            self.time_limited_start_year_entry.grid_forget()
            self.time_limited_start_month_label.grid_forget()
            self.time_limited_start_month_entry.grid_forget()
            self.time_limited_start_day_label.grid_forget()
            self.time_limited_start_day_entry.grid_forget()
            self.time_limited_start_hour_label.grid_forget()
            self.time_limited_start_hour_entry.grid_forget()
            self.time_limited_start_minute_label.grid_forget()
            self.time_limited_start_minute_entry.grid_forget()

            self.time_limited_end_label.grid_forget()
            self.time_limited_end_year_label.grid_forget()
            self.time_limited_end_year_entry.grid_forget()
            self.time_limited_end_month_label.grid_forget()
            self.time_limited_end_month_entry.grid_forget()
            self.time_limited_end_day_label.grid_forget()
            self.time_limited_end_day_entry.grid_forget()
            self.time_limited_end_hour_label.grid_forget()
            self.time_limited_end_hour_entry.grid_forget()
            self.time_limited_end_minute_label.grid_forget()
            self.time_limited_end_minute_entry.grid_forget()

        else:
            self.time_limited_start_label.grid(row=10, column=1, sticky=W, padx=50)
            self.time_limited_start_day_label.grid(row=11, column=1, sticky=W, padx=30)
            self.time_limited_start_month_label.grid(row=11, column=1, sticky=W, padx=55)
            self.time_limited_start_year_label.grid(row=11, column=1, sticky=W, padx=80)
            self.time_limited_start_hour_label.grid(row=11, column=1, sticky=W, padx=110)
            self.time_limited_start_minute_label.grid(row=11, column=1, sticky=W, padx=135)

            self.time_limited_end_label.grid(row=10, column=1, sticky=E, padx=50)
            self.time_limited_end_day_label.grid(row=11, column=1, sticky=E, padx=110)
            self.time_limited_end_month_label.grid(row=11, column=1, sticky=E, padx=85)
            self.time_limited_end_year_label.grid(row=11, column=1, sticky=E, padx=55)
            self.time_limited_end_hour_label.grid(row=11, column=1, sticky=E, padx=30)
            self.time_limited_end_minute_label.grid(row=11, column=1, sticky=E, padx=5)

            self.time_limited_start_day_entry.grid(row=12, column=1, sticky=W, padx=30)
            self.time_limited_start_month_entry.grid(row=12, column=1, sticky=W, padx=55)
            self.time_limited_start_year_entry.grid(row=12, column=1, sticky=W, padx=80)
            self.time_limited_start_hour_entry.grid(row=12, column=1, sticky=W, padx=110)
            self.time_limited_start_minute_entry.grid(row=12, column=1, sticky=W, padx=135)

            self.time_limited_end_day_entry.grid(row=12, column=1, sticky=E, padx=110)
            self.time_limited_end_month_entry.grid(row=12, column=1, sticky=E, padx=85)
            self.time_limited_end_year_entry.grid(row=12, column=1, sticky=E, padx=55)
            self.time_limited_end_hour_entry.grid(row=12, column=1, sticky=E, padx=30)
            self.time_limited_end_minute_entry.grid(row=12, column=1, sticky=E, padx=5)

    def show_introduction_textfield(self, e, introduction_var):
        print(introduction_var.get())
        if introduction_var.get() == 0:

            self.introduction_bar.grid_forget()
            self.introduction_infobox.grid_forget()

        else:
            self.introduction_bar.grid(row=15, column=1, sticky=E)
            self.introduction_infobox.grid(row=15, column=1, padx=30)
            self.introduction_bar.config(command=self.introduction_infobox.yview)
            self.introduction_infobox.config(yscrollcommand=self.introduction_bar.set)

    def enable_autosave(self, e, var):
        if var.get() == 0:
            self.check_autosave_interval_entry.grid_forget()
            self.check_autosave_interval_label.grid_forget()

        else:
            self.check_autosave_interval_entry.grid(row=4, column=3, padx=10)
            self.check_autosave_interval_label.grid(row=4, column=3, padx=50, sticky=W)

    def show_concluding_remarks(self, e, var):
        if var.get() == 0:
            self.concluding_remarks_bar.grid_forget()
            self.concluding_remarks_infobox.grid_forget()

        else:
            self.concluding_remarks_bar.grid(row=22, column=3, sticky=E)
            self.concluding_remarks_infobox.grid(row=22, column=3, padx=30)
            self.concluding_remarks_bar.config(command=self.concluding_remarks_infobox.yview)
            self.concluding_remarks_infobox.config(yscrollcommand=self.concluding_remarks_bar.set)

    def Fill_Entrys_From_DB(self, db_data):
        j = 0
        print("Fill entry mit", db_data[1][4])
        for i in db_data[1][4]:  # todo diese exception ist so nicht ok aber funktioniert erstmal um den Textbox Ihren Textzuzuweisen.

            self.index_list[j][0].set(i)
            j = j + 1
        print(self.index_list[self.index_dict['profile_name']][0].get())

    def save_testeinstellungen_in_db(self):
        print("das soll gespeichert werden:", self.index_list)
        DBI.Add_data_to_DB(self.index_list, self.index_list[3][0].get())

    def on_closing(self):
        self.DBI.unsubscribe(self.Fill_Entrys_From_DB)

        self.work_window.destroy()

class Testeinstellungen_TRV():
    def __init__(self, DBI, index_list, index_dict, table_dict, Width, Label_Font, Entry_Font, Button_Font, bg_color, entry_color, label_color, button_color, fg_color):
        self.work_window = Toplevel(bg=bg_color)
        self.table_dict = table_dict
        self.Width = Width
        self.DBI = DBI
        self.ID =4
        self.rel_Top_Abstand = .1
        self.index_list = index_list
        self.index_dict = index_dict
        self.work_window.geometry("%dx%d+%d+%d" % (Width / 4, Width / 8, Width / 5, Width / 8))
        self.DBI.subscribe(self.Update_TRV)
        self.Frame = Frame(self.work_window)
        self.Frame.place(relwidth=1, relheight=1, relx=0, rely=0)
        self.create_trv()
        self.testeinstellungen_menu()
        self.clear()
        self.trv.bind('<Double-Button-1>', self.Select_from_DB)

    def testeinstellungen_menu(self):
        self.neue_einstellungen = Button(self.Frame, text="Neue einstellung erstellen", command=self.neue_einstellungen_fenster)
        self.neue_einstellungen.place(relx=.05, rely=.9)

    def neue_einstellungen_fenster(self):
        test_conf = Testeinstellungen(DBI, table_index_list[4], table_index_dict[4], table_dict['testeinstellungen'],
                                      WIDTH, Label_Font, Entry_Font, Button_Font, bg_color, entry_color, label_color,
                                      button_color, fg_color)

    def Update_TRV(self, db_data):
        self.trv.delete(*self.trv.get_children())
        print("fill trv from db", db_data[0][4])
        data = db_data[0][4]
        for input in data:
                self.trv.insert('', 'end', values=input)


    def create_trv(self):
        self.trv_label = Label(self.Frame, text="Testeinstellungs Profile")
        self.trv_label.place(relx=0.05, rely=0, relwidth=.5)
        # Create Treview Frame
        self.DB_frame = tk.Frame(self.Frame)
        self.DB_frame.place(relx=0.05, rely=self.rel_Top_Abstand)
        # create Scrollbar
        self.vsb = ttk.Scrollbar(self.DB_frame)
        self.vsb.pack(side=RIGHT, fill=Y)
        # create Treeview
        self.trv = ttk.Treeview(self.DB_frame, columns=(1), show="headings", height=9,
                                style="mystyle.Treeview")
        self.trv.configure(yscrollcommand=self.vsb.set)
        self.trv.tag_configure('odd', background='#ff5733')
        self.trv.pack(fill=BOTH)
        # Create Treeview Headings
        self.trv.heading(1, text="Name")
        #self.trv.heading(8, text="Zuletzt verändert")
        # Format Columns
        self.trv.column(1, width=int(self.Width / 9), anchor=CENTER,
                        minwidth=int(self.Width / 30))

        print('trv created')

    def clear(self):
        #self.DBI.get_complete_DB(0)
        self.DBI.get_complete_DB(0)

    def on_closing(self):
        self.DBI.unsubscribe(self.Update_TRV())
        self.work_window.destroy()

    def Select_from_DB(self, a):

        gesucht = self.trv.item(self.trv.focus())
        print("gesucht:", gesucht)
        self.neue_einstellungen_fenster()
        self.DBI.get_question(gesucht['values'][0], 1)

if __name__ == "__main__":


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
    table_list = ['formelfrage', 'singlechoice', 'multiplechoice', 'zuordnungsfrage', 'testeinstellungen']  # hier sind die Namen der Table drinne die verwendet werden können
    bg_color = '#4cc9f0'  # general Background color
    efg_color = '#3a0ca3'  # Entry foreground color
    entry_color = 'white'  # Entry Background color
    label_color = '#3a0ca3'
    button_color = '#3f37c9'
    fg_color = '#4cc9f0'  # general foregroundcolor
    table_dict = {'formelfrage': 0, 'singlechoice': 1, 'multiplechoice': 2, 'zuordnungsfrage': 3, 'testeinstellungen': 4}

    mydb_name = 'generaldb.db'  # Datenbank mit allen Fragentypen
    mytempdb_name = 'generaldb2.db'  # Kopie der originalen Datenbank
    WIDTH = int(root.winfo_screenwidth())

    DBI = DB_Interface(mydb_name, mytempdb_name, table_dict, table_list)
    index_info = DBI.get_index_info()
    table_index_list = index_info[0]
    table_index_dict = index_info[1]
    Test_TRV = Testeinstellungen_TRV(DBI, table_index_list[4], table_index_dict[4], table_dict['testeinstellungen'], WIDTH, Label_Font, Entry_Font, Button_Font, bg_color, entry_color, label_color, button_color, fg_color)

    #test_conf = Testeinstellungen(DBI, table_index_list[4], table_index_dict[4], table_dict['testeinstellungen'], WIDTH, Label_Font, Entry_Font, Button_Font, bg_color, entry_color, label_color, button_color, fg_color)
    root.mainloop()

