from DB_interface import DB_Interface

class xml_interface(DBI, self, db_entry_to_index_dict, ids_in_entry_box, question_type, pool_img_dir,
                 ilias_id_pool_qpl_dir, xml_read_qti_template_path, xml_qti_output_file_path,
                 xml_qpl_output_file_path, max_id_pool_qti_xml, max_id, taxonomy_file_question_pool):
#DBI = DB_Interface
#DBI.get_dbtemp_data gibt die daten aus formelfrage zurück
    self.DBI = DBI
    # INIT
    # ff_question_structure
    # ff_question_variable_structure
    # ff_question_results_structure

    def create_test(self, db_entry_to_index_dict, ids_in_entry_box, question_type, pool_img_dir,
                 ilias_id_pool_qpl_dir, xml_read_qti_template_path, xml_qti_output_file_path,
                 xml_qpl_output_file_path, max_id_pool_qti_xml, max_id, taxonomy_file_question_pool):

        # Gibt die ANzahl der Pools an
        # Üblicherweise wird nur 1 Pool erzeugt. Nur bei "Taxonomie getrennt" Erstellung, werden mehrere Pools erzeugt
        # self.number_of_pools = 1

        self.ff_db_entry_to_index_dict = db_entry_to_index_dict
        self.ff_test_entry_splitted = ids_in_entry_box.split(
            ",")  # todo das sind die eingegebenen ids welche zu den gewünschten Testfragen gehören
        self.qti_file_path_output = xml_qti_output_file_path
        self.formelfrage_pool_qpl_file_path_output = xml_qpl_output_file_path
        self.ff_mytree = ET.parse(xml_read_qti_template_path)
        self.ff_myroot = self.ff_mytree.getroot()
        self.ff_question_type_test_or_pool = question_type
        self.formelfrage_pool_img_file_path = pool_img_dir  # Wird nur bei Erstellung eines Fragen-Pool verwendet. Ordnername wird erst bei Laufzeit erstellt)

        self.all_entries_from_db_list = []
        self.number_of_entrys = []

        self.question_pool_id_list = []
        self.question_title_list = []

        self.ff_number_of_questions_generated = 1

        self.ilias_id_pool_qpl_dir = ilias_id_pool_qpl_dir
        self.ff_file_max_id = max_id
        self.taxonomy_file_question_pool = taxonomy_file_question_pool
        self.ilias_id_pool_qti_xml = max_id_pool_qti_xml

        print("\n")

        if self.ff_question_type_test_or_pool == "question_test":
            print("FORMELFRAGE: ILIAS-TEST WIRD ERSTELLT...  ID: " + str(
                ids_in_entry_box))  # todo die ID ist für eine Frage?

        else:
            print("FORMELFRAGE: ILIAS-POOL WIRD ERSTELLT...  ID: " + str(ids_in_entry_box))

        # Mit FF_Datenbank verknüpfen
        connect_ff_db = sqlite3.connect(self.database_formelfrage_path)
        cursor = connect_ff_db.cursor()

        # Prüfen ob alle Einträge generiert werden sollen (checkbox gesetzt)
        if self.ff_var_create_question_pool_all_check.get() == 1 and self.ff_var_create_multiple_question_pools_from_tax_check.get() == 0:
            conn = sqlite3.connect(self.database_formelfrage_path)
            c = conn.cursor()
            c.execute("SELECT *, oid FROM %s" % self.ff_database_table)

            ff_db_records = c.fetchall()

            for ff_db_record in ff_db_records:
                self.all_entries_from_db_list.append(int(ff_db_record[len(ff_db_record) - 1]))

            self.string_temp = ','.join(map(str, self.all_entries_from_db_list))
            self.ff_test_entry_splitted = self.string_temp.split(",")

            # Eintrag mit ID "1" entspricht der Vorlage und soll nicht mit erstellt werden
            self.ff_test_entry_splitted.pop(0)

            print(self.ff_test_entry_splitted)

            # print("Number of Pools: " + str(len(self.list_of_lists)))
            # self.number_of_pools = len(self.list_of_lists)

        # Sämtliche Datenbank Einträge auslesen mit der entsprechenden "oid" (Datenbank ID)
        # Datenbank ID wird automatisch bei einem neuen Eintrag erstellt (fortlaufend) und kann nicht beeinflusst werden
        cursor.execute(
            "SELECT *, oid FROM %s" % self.ff_database_table)  # todo Wo kommt das Database_table her?
        ff_db_records = cursor.fetchall()
        """
        for pool_number in range(self.number_of_pools):

            self.string2_temp = ','.join(map(str, self.list_of_lists[pool_number]))
            self.ff_test_entry_splitted = self.string2_temp.split(",")
            print("%%%%%%")
            print(self.ff_test_entry_splitted)

        """
        # todo die einzelnen Inhalte werden aus DB records(zwischenspeicher) in einen weiteren zwischenspeicher der bereits den zutreffenden namen hat zugeordnet um damit eine Frage zu erstellen
        for i in range(
                len(self.ff_test_entry_splitted)):  # todo ein durchlauf für jede Frage in die zum test gehört
            for ff_db_record in ff_db_records:  # todo Inhalt aller Fragen  oder nur einer Frage aus der Datenbank die in die Test sollen
                if str(ff_db_record[len(ff_db_record) - 1]) == self.ff_test_entry_splitted[
                    i]:  # todo da bin ich mir nicht sicher was es unterscheiden soll?
                    for t in range(len(ff_db_record)):
                        if ff_db_record[self.ff_db_entry_to_index_dict[
                            'question_type']].lower() == self.ff_question_type_name.lower():
                            self.ff_question_difficulty = ff_db_record[
                                self.ff_db_entry_to_index_dict['question_difficulty']]
                            self.ff_question_category = ff_db_record[
                                self.ff_db_entry_to_index_dict['question_category']]
                            self.ff_question_type = ff_db_record[
                                self.ff_db_entry_to_index_dict['question_type']]
                            self.ff_question_title = ff_db_record[
                                self.ff_db_entry_to_index_dict['question_title']].replace('&', "&amp;")
                            self.ff_question_description_title = ff_db_record[
                                self.ff_db_entry_to_index_dict['question_description_title']].replace('&',
                                                                                                      "&amp;")
                            self.ff_question_description_main = ff_db_record[
                                self.ff_db_entry_to_index_dict['question_description_main']]
                            self.ff_res1_formula = ff_db_record[self.ff_db_entry_to_index_dict['res1_formula']]
                            self.ff_res2_formula = ff_db_record[self.ff_db_entry_to_index_dict['res2_formula']]
                            self.ff_res3_formula = ff_db_record[self.ff_db_entry_to_index_dict['res3_formula']]
                            self.ff_res4_formula = ff_db_record[self.ff_db_entry_to_index_dict['res4_formula']]
                            self.ff_res5_formula = ff_db_record[self.ff_db_entry_to_index_dict['res5_formula']]
                            self.ff_res6_formula = ff_db_record[self.ff_db_entry_to_index_dict['res6_formula']]
                            self.ff_res7_formula = ff_db_record[self.ff_db_entry_to_index_dict['res7_formula']]
                            self.ff_res8_formula = ff_db_record[self.ff_db_entry_to_index_dict['res8_formula']]
                            self.ff_res9_formula = ff_db_record[self.ff_db_entry_to_index_dict['res9_formula']]
                            self.ff_res10_formula = ff_db_record[
                                self.ff_db_entry_to_index_dict['res10_formula']]

                            self.ff_var1_name = ff_db_record[self.ff_db_entry_to_index_dict['var1_name']]
                            self.ff_var1_min = ff_db_record[self.ff_db_entry_to_index_dict['var1_min']]
                            self.ff_var1_max = ff_db_record[self.ff_db_entry_to_index_dict['var1_max']]
                            self.ff_var1_prec = ff_db_record[self.ff_db_entry_to_index_dict['var1_prec']]
                            self.ff_var1_divby = ff_db_record[self.ff_db_entry_to_index_dict['var1_divby']]
                            self.ff_var1_unit = ff_db_record[self.ff_db_entry_to_index_dict['var1_unit']]

                            self.ff_var2_name = ff_db_record[self.ff_db_entry_to_index_dict['var2_name']]
                            self.ff_var2_min = ff_db_record[self.ff_db_entry_to_index_dict['var2_min']]
                            self.ff_var2_max = ff_db_record[self.ff_db_entry_to_index_dict['var2_max']]
                            self.ff_var2_prec = ff_db_record[self.ff_db_entry_to_index_dict['var2_prec']]
                            self.ff_var2_divby = ff_db_record[self.ff_db_entry_to_index_dict['var2_divby']]
                            self.ff_var2_unit = ff_db_record[self.ff_db_entry_to_index_dict['var2_unit']]

                            self.ff_var3_name = ff_db_record[self.ff_db_entry_to_index_dict['var3_name']]
                            self.ff_var3_min = ff_db_record[self.ff_db_entry_to_index_dict['var3_min']]
                            self.ff_var3_max = ff_db_record[self.ff_db_entry_to_index_dict['var3_max']]
                            self.ff_var3_prec = ff_db_record[self.ff_db_entry_to_index_dict['var3_prec']]
                            self.ff_var3_divby = ff_db_record[self.ff_db_entry_to_index_dict['var3_divby']]
                            self.ff_var3_unit = ff_db_record[self.ff_db_entry_to_index_dict['var3_unit']]

                            self.ff_var4_name = ff_db_record[self.ff_db_entry_to_index_dict['var4_name']]
                            self.ff_var4_min = ff_db_record[self.ff_db_entry_to_index_dict['var4_min']]
                            self.ff_var4_max = ff_db_record[self.ff_db_entry_to_index_dict['var4_max']]
                            self.ff_var4_prec = ff_db_record[self.ff_db_entry_to_index_dict['var4_prec']]
                            self.ff_var4_divby = ff_db_record[self.ff_db_entry_to_index_dict['var4_divby']]
                            self.ff_var4_unit = ff_db_record[self.ff_db_entry_to_index_dict['var4_unit']]

                            self.ff_var5_name = ff_db_record[self.ff_db_entry_to_index_dict['var5_name']]
                            self.ff_var5_min = ff_db_record[self.ff_db_entry_to_index_dict['var5_min']]
                            self.ff_var5_max = ff_db_record[self.ff_db_entry_to_index_dict['var5_max']]
                            self.ff_var5_prec = ff_db_record[self.ff_db_entry_to_index_dict['var5_prec']]
                            self.ff_var5_divby = ff_db_record[self.ff_db_entry_to_index_dict['var5_divby']]
                            self.ff_var5_unit = ff_db_record[self.ff_db_entry_to_index_dict['var5_unit']]

                            self.ff_var6_name = ff_db_record[self.ff_db_entry_to_index_dict['var6_name']]
                            self.ff_var6_min = ff_db_record[self.ff_db_entry_to_index_dict['var6_min']]
                            self.ff_var6_max = ff_db_record[self.ff_db_entry_to_index_dict['var6_max']]
                            self.ff_var6_prec = ff_db_record[self.ff_db_entry_to_index_dict['var6_prec']]
                            self.ff_var6_divby = ff_db_record[self.ff_db_entry_to_index_dict['var6_divby']]
                            self.ff_var6_unit = ff_db_record[self.ff_db_entry_to_index_dict['var6_unit']]

                            self.ff_var7_name = ff_db_record[self.ff_db_entry_to_index_dict['var7_name']]
                            self.ff_var7_min = ff_db_record[self.ff_db_entry_to_index_dict['var7_min']]
                            self.ff_var7_max = ff_db_record[self.ff_db_entry_to_index_dict['var7_max']]
                            self.ff_var7_prec = ff_db_record[self.ff_db_entry_to_index_dict['var7_prec']]
                            self.ff_var7_divby = ff_db_record[self.ff_db_entry_to_index_dict['var7_divby']]
                            self.ff_var7_unit = ff_db_record[self.ff_db_entry_to_index_dict['var7_unit']]

                            self.ff_var8_name = ff_db_record[self.ff_db_entry_to_index_dict['var8_name']]
                            self.ff_var8_min = ff_db_record[self.ff_db_entry_to_index_dict['var8_min']]
                            self.ff_var8_max = ff_db_record[self.ff_db_entry_to_index_dict['var8_max']]
                            self.ff_var8_prec = ff_db_record[self.ff_db_entry_to_index_dict['var8_prec']]
                            self.ff_var8_divby = ff_db_record[self.ff_db_entry_to_index_dict['var8_divby']]
                            self.ff_var8_unit = ff_db_record[self.ff_db_entry_to_index_dict['var8_unit']]

                            self.ff_var9_name = ff_db_record[self.ff_db_entry_to_index_dict['var9_name']]
                            self.ff_var9_min = ff_db_record[self.ff_db_entry_to_index_dict['var9_min']]
                            self.ff_var9_max = ff_db_record[self.ff_db_entry_to_index_dict['var9_max']]
                            self.ff_var9_prec = ff_db_record[self.ff_db_entry_to_index_dict['var9_prec']]
                            self.ff_var9_divby = ff_db_record[self.ff_db_entry_to_index_dict['var9_divby']]
                            self.ff_var9_unit = ff_db_record[self.ff_db_entry_to_index_dict['var9_unit']]

                            self.ff_var10_name = ff_db_record[self.ff_db_entry_to_index_dict['var10_name']]
                            self.ff_var10_min = ff_db_record[self.ff_db_entry_to_index_dict['var10_min']]
                            self.ff_var10_max = ff_db_record[self.ff_db_entry_to_index_dict['var10_max']]
                            self.ff_var10_prec = ff_db_record[self.ff_db_entry_to_index_dict['var10_prec']]
                            self.ff_var10_divby = ff_db_record[self.ff_db_entry_to_index_dict['var10_divby']]
                            self.ff_var10_unit = ff_db_record[self.ff_db_entry_to_index_dict['var10_unit']]

                            self.ff_var11_name = ff_db_record[self.ff_db_entry_to_index_dict['var11_name']]
                            self.ff_var11_min = ff_db_record[self.ff_db_entry_to_index_dict['var11_min']]
                            self.ff_var11_max = ff_db_record[self.ff_db_entry_to_index_dict['var11_max']]
                            self.ff_var11_prec = ff_db_record[self.ff_db_entry_to_index_dict['var11_prec']]
                            self.ff_var11_divby = ff_db_record[self.ff_db_entry_to_index_dict['var11_divby']]
                            self.ff_var11_unit = ff_db_record[self.ff_db_entry_to_index_dict['var11_unit']]

                            self.ff_var12_name = ff_db_record[self.ff_db_entry_to_index_dict['var12_name']]
                            self.ff_var12_min = ff_db_record[self.ff_db_entry_to_index_dict['var12_min']]
                            self.ff_var12_max = ff_db_record[self.ff_db_entry_to_index_dict['var12_max']]
                            self.ff_var12_prec = ff_db_record[self.ff_db_entry_to_index_dict['var12_prec']]
                            self.ff_var12_divby = ff_db_record[self.ff_db_entry_to_index_dict['var12_divby']]
                            self.ff_var12_unit = ff_db_record[self.ff_db_entry_to_index_dict['var12_unit']]

                            self.ff_var13_name = ff_db_record[self.ff_db_entry_to_index_dict['var13_name']]
                            self.ff_var13_min = ff_db_record[self.ff_db_entry_to_index_dict['var13_min']]
                            self.ff_var13_max = ff_db_record[self.ff_db_entry_to_index_dict['var13_max']]
                            self.ff_var13_prec = ff_db_record[self.ff_db_entry_to_index_dict['var13_prec']]
                            self.ff_var13_divby = ff_db_record[self.ff_db_entry_to_index_dict['var13_divby']]
                            self.ff_var13_unit = ff_db_record[self.ff_db_entry_to_index_dict['var13_unit']]

                            self.ff_var14_name = ff_db_record[self.ff_db_entry_to_index_dict['var14_name']]
                            self.ff_var14_min = ff_db_record[self.ff_db_entry_to_index_dict['var14_min']]
                            self.ff_var14_max = ff_db_record[self.ff_db_entry_to_index_dict['var14_max']]
                            self.ff_var14_prec = ff_db_record[self.ff_db_entry_to_index_dict['var14_prec']]
                            self.ff_var14_divby = ff_db_record[self.ff_db_entry_to_index_dict['var14_divby']]
                            self.ff_var14_unit = ff_db_record[self.ff_db_entry_to_index_dict['var14_unit']]

                            self.ff_var15_name = ff_db_record[self.ff_db_entry_to_index_dict['var15_name']]
                            self.ff_var15_min = ff_db_record[self.ff_db_entry_to_index_dict['var15_min']]
                            self.ff_var15_max = ff_db_record[self.ff_db_entry_to_index_dict['var15_max']]
                            self.ff_var15_prec = ff_db_record[self.ff_db_entry_to_index_dict['var15_prec']]
                            self.ff_var15_divby = ff_db_record[self.ff_db_entry_to_index_dict['var15_divby']]
                            self.ff_var15_unit = ff_db_record[self.ff_db_entry_to_index_dict['var15_unit']]

                            self.ff_res1_name = ff_db_record[self.ff_db_entry_to_index_dict['res1_name']]
                            self.ff_res1_min = ff_db_record[self.ff_db_entry_to_index_dict['res1_min']]
                            self.ff_res1_max = ff_db_record[self.ff_db_entry_to_index_dict['res1_max']]
                            self.ff_res1_prec = ff_db_record[self.ff_db_entry_to_index_dict['res1_prec']]
                            self.ff_res1_tol = ff_db_record[self.ff_db_entry_to_index_dict['res1_tol']]
                            self.ff_res1_points = ff_db_record[self.ff_db_entry_to_index_dict['res1_points']]
                            self.ff_res1_unit = ff_db_record[self.ff_db_entry_to_index_dict['res1_unit']]

                            self.ff_res2_name = ff_db_record[self.ff_db_entry_to_index_dict['res2_name']]
                            self.ff_res2_min = ff_db_record[self.ff_db_entry_to_index_dict['res2_min']]
                            self.ff_res2_max = ff_db_record[self.ff_db_entry_to_index_dict['res2_max']]
                            self.ff_res2_prec = ff_db_record[self.ff_db_entry_to_index_dict['res2_prec']]
                            self.ff_res2_tol = ff_db_record[self.ff_db_entry_to_index_dict['res2_tol']]
                            self.ff_res2_points = ff_db_record[self.ff_db_entry_to_index_dict['res2_points']]
                            self.ff_res2_unit = ff_db_record[self.ff_db_entry_to_index_dict['res2_unit']]

                            self.ff_res3_name = ff_db_record[self.ff_db_entry_to_index_dict['res3_name']]
                            self.ff_res3_min = ff_db_record[self.ff_db_entry_to_index_dict['res3_min']]
                            self.ff_res3_max = ff_db_record[self.ff_db_entry_to_index_dict['res3_max']]
                            self.ff_res3_prec = ff_db_record[self.ff_db_entry_to_index_dict['res3_prec']]
                            self.ff_res3_tol = ff_db_record[self.ff_db_entry_to_index_dict['res3_tol']]
                            self.ff_res3_points = ff_db_record[self.ff_db_entry_to_index_dict['res3_points']]
                            self.ff_res3_unit = ff_db_record[self.ff_db_entry_to_index_dict['res3_unit']]

                            self.ff_res4_name = ff_db_record[self.ff_db_entry_to_index_dict['res4_name']]
                            self.ff_res4_min = ff_db_record[self.ff_db_entry_to_index_dict['res4_min']]
                            self.ff_res4_max = ff_db_record[self.ff_db_entry_to_index_dict['res4_max']]
                            self.ff_res4_prec = ff_db_record[self.ff_db_entry_to_index_dict['res4_prec']]
                            self.ff_res4_tol = ff_db_record[self.ff_db_entry_to_index_dict['res4_tol']]
                            self.ff_res4_points = ff_db_record[self.ff_db_entry_to_index_dict['res4_points']]
                            self.ff_res4_unit = ff_db_record[self.ff_db_entry_to_index_dict['res4_unit']]

                            self.ff_res5_name = ff_db_record[self.ff_db_entry_to_index_dict['res5_name']]
                            self.ff_res5_min = ff_db_record[self.ff_db_entry_to_index_dict['res5_min']]
                            self.ff_res5_max = ff_db_record[self.ff_db_entry_to_index_dict['res5_max']]
                            self.ff_res5_prec = ff_db_record[self.ff_db_entry_to_index_dict['res5_prec']]
                            self.ff_res5_tol = ff_db_record[self.ff_db_entry_to_index_dict['res5_tol']]
                            self.ff_res5_points = ff_db_record[self.ff_db_entry_to_index_dict['res5_points']]
                            self.ff_res5_unit = ff_db_record[self.ff_db_entry_to_index_dict['res5_unit']]

                            self.ff_res6_name = ff_db_record[self.ff_db_entry_to_index_dict['res6_name']]
                            self.ff_res6_min = ff_db_record[self.ff_db_entry_to_index_dict['res6_min']]
                            self.ff_res6_max = ff_db_record[self.ff_db_entry_to_index_dict['res6_max']]
                            self.ff_res6_prec = ff_db_record[self.ff_db_entry_to_index_dict['res6_prec']]
                            self.ff_res6_tol = ff_db_record[self.ff_db_entry_to_index_dict['res6_tol']]
                            self.ff_res6_points = ff_db_record[self.ff_db_entry_to_index_dict['res6_points']]
                            self.ff_res6_unit = ff_db_record[self.ff_db_entry_to_index_dict['res6_unit']]

                            self.ff_res7_name = ff_db_record[self.ff_db_entry_to_index_dict['res7_name']]
                            self.ff_res7_min = ff_db_record[self.ff_db_entry_to_index_dict['res7_min']]
                            self.ff_res7_max = ff_db_record[self.ff_db_entry_to_index_dict['res7_max']]
                            self.ff_res7_prec = ff_db_record[self.ff_db_entry_to_index_dict['res7_prec']]
                            self.ff_res7_tol = ff_db_record[self.ff_db_entry_to_index_dict['res7_tol']]
                            self.ff_res7_points = ff_db_record[self.ff_db_entry_to_index_dict['res7_points']]
                            self.ff_res7_unit = ff_db_record[self.ff_db_entry_to_index_dict['res7_unit']]

                            self.ff_es8_name = ff_db_record[self.ff_db_entry_to_index_dict['res8_name']]
                            self.ff_res8_min = ff_db_record[self.ff_db_entry_to_index_dict['res8_min']]
                            self.ff_res8_max = ff_db_record[self.ff_db_entry_to_index_dict['res8_max']]
                            self.ff_res8_prec = ff_db_record[self.ff_db_entry_to_index_dict['res8_prec']]
                            self.ff_res8_tol = ff_db_record[self.ff_db_entry_to_index_dict['res8_tol']]
                            self.ff_res8_points = ff_db_record[self.ff_db_entry_to_index_dict['res8_points']]
                            self.ff_res8_unit = ff_db_record[self.ff_db_entry_to_index_dict['res8_unit']]

                            self.ff_res9_name = ff_db_record[self.ff_db_entry_to_index_dict['res9_name']]
                            self.ff_res9_min = ff_db_record[self.ff_db_entry_to_index_dict['res9_min']]
                            self.ff_res9_max = ff_db_record[self.ff_db_entry_to_index_dict['res9_max']]
                            self.ff_res9_prec = ff_db_record[self.ff_db_entry_to_index_dict['res9_prec']]
                            self.ff_res9_tol = ff_db_record[self.ff_db_entry_to_index_dict['res9_tol']]
                            self.ff_res9_points = ff_db_record[self.ff_db_entry_to_index_dict['res9_points']]
                            self.ff_res9_unit = ff_db_record[self.ff_db_entry_to_index_dict['res9_unit']]

                            self.ff_res10_name = ff_db_record[self.ff_db_entry_to_index_dict['res10_name']]
                            self.ff_res10_min = ff_db_record[self.ff_db_entry_to_index_dict['res10_min']]
                            self.ff_res10_max = ff_db_record[self.ff_db_entry_to_index_dict['res10_max']]
                            self.ff_res10_prec = ff_db_record[self.ff_db_entry_to_index_dict['res10_prec']]
                            self.ff_res10_tol = ff_db_record[self.ff_db_entry_to_index_dict['res10_tol']]
                            self.ff_res10_points = ff_db_record[self.ff_db_entry_to_index_dict['res10_points']]
                            self.ff_res10_unit = ff_db_record[self.ff_db_entry_to_index_dict['res10_unit']]

                            self.ff_description_img_name_1 = ff_db_record[
                                self.ff_db_entry_to_index_dict['description_img_name_1']]
                            self.ff_description_img_data_1 = ff_db_record[
                                self.ff_db_entry_to_index_dict['description_img_data_1']]
                            self.ff_description_img_path_1 = ff_db_record[
                                self.ff_db_entry_to_index_dict['description_img_path_1']]
                            self.ff_description_img_name_2 = ff_db_record[
                                self.ff_db_entry_to_index_dict['description_img_name_2']]
                            self.ff_description_img_data_2 = ff_db_record[
                                self.ff_db_entry_to_index_dict['description_img_data_2']]
                            self.ff_description_img_path_2 = ff_db_record[
                                self.ff_db_entry_to_index_dict['description_img_path_2']]
                            self.ff_description_img_name_3 = ff_db_record[
                                self.ff_db_entry_to_index_dict['description_img_name_3']]
                            self.ff_description_img_data_3 = ff_db_record[
                                self.ff_db_entry_to_index_dict['description_img_data_3']]
                            self.ff_description_img_path_3 = ff_db_record[
                                self.ff_db_entry_to_index_dict['description_img_path_3']]

                            self.ff_test_time = ff_db_record[self.ff_db_entry_to_index_dict['test_time']]
                            self.ff_var_number = ff_db_record[self.ff_db_entry_to_index_dict['var_number']]
                            self.ff_res_number = ff_db_record[self.ff_db_entry_to_index_dict['res_number']]
                            self.ff_question_pool_tag = ff_db_record[
                                self.ff_db_entry_to_index_dict['question_pool_tag']]
                            self.ff_question_author = ff_db_record[
                                self.ff_db_entry_to_index_dict['question_author']].replace('&', "&amp;")

            Create_Formelfrage_Questions.ff_question_structure(self, i)

    def ff_question_structure(self, id_nr):  # todo wird von der Funktion oben drüber aufgerufen
        """Diese Funktion wandelt die SQL-Einträge in die .xml um, welche anschließend in ILIAS eingespielt werden kann"""

        # VARIABLEN
        self.ff_response_counter = 0  # wird verwendet zu zählen, wieviele Anworten pro Frage verwendet werden. Bei einer neuer Antwort -> +1

        self.ff_question_description_main = test_generator_modul_taxonomie_und_textformatierung.Textformatierung.format_description_text_in_xml(
            self, self.ff_var_use_latex_on_text_check.get(), self.ff_question_description_main)

        # todo es wurden doch bereits alle daten zugeordnet warum wird die Datenbank nochmal verwendet?
        # Verbindung zur FF-Datenank
        ff_connect = sqlite3.connect(self.database_formelfrage_path)
        ff_cursor = ff_connect.cursor()

        # Alle Einträge auslesen
        ff_cursor.execute("SELECT *, oid FROM %s" % self.ff_database_table)
        ff_db_records = ff_cursor.fetchall()

        for ff_db_record in ff_db_records:

            # Hier werden die Fragen anhand der ID's erstellt
            if str(ff_db_record[len(ff_db_record) - 1]) == self.ff_test_entry_splitted[id_nr]:

                # Bilder für die Beschreibung speichern
                test_generator_modul_ilias_test_struktur.Additional_Funtions.add_dir_for_images(self,
                                                                                                self.ff_description_img_name_1,
                                                                                                self.ff_description_img_data_1,
                                                                                                id_nr,
                                                                                                self.ff_question_type_test_or_pool,
                                                                                                self.formelfrage_test_img_file_path,
                                                                                                self.formelfrage_pool_img_file_path)
                test_generator_modul_ilias_test_struktur.Additional_Funtions.add_dir_for_images(self,
                                                                                                self.ff_description_img_name_2,
                                                                                                self.ff_description_img_data_2,
                                                                                                id_nr,
                                                                                                self.ff_question_type_test_or_pool,
                                                                                                self.formelfrage_test_img_file_path,
                                                                                                self.formelfrage_pool_img_file_path)
                test_generator_modul_ilias_test_struktur.Additional_Funtions.add_dir_for_images(self,
                                                                                                self.ff_description_img_name_3,
                                                                                                self.ff_description_img_data_3,
                                                                                                id_nr,
                                                                                                self.ff_question_type_test_or_pool,
                                                                                                self.formelfrage_test_img_file_path,
                                                                                                self.formelfrage_pool_img_file_path)

                # Aufbau für  Fragenstruktur "TEST"
                if self.ff_question_type_test_or_pool == "question_test":
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

                    test_generator_modul_ilias_test_struktur.Additional_Funtions.set_taxonomy_for_question(self,
                                                                                                           id_nr,
                                                                                                           self.number_of_entrys,
                                                                                                           item,
                                                                                                           self.formelfrage_pool_qpl_file_path_template,
                                                                                                           self.formelfrage_pool_qpl_file_path_output
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
                item.set('title', self.ff_question_title)

                # Fragen-Titel Beschreibung
                qticomment.text = self.ff_question_description_title

                # Testdauer -- "duration" in xml
                # wird keine Testzeit eingetragen, wird 1h vorausgewählt
                duration.text = self.ff_test_time  # todo ist das die Testzeit oder die Zeit für die eine Frage?
                if duration.text == "":
                    duration.text = "P0Y0M0DT1H0M0S"

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
                fieldentry.text = self.ff_question_author
                # -----------------------------------------------------------------------POINTS
                qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
                fieldlabel = ET.SubElement(qtimetadatafield, 'fieldlabel')
                fieldlabel.text = "points"
                fieldentry = ET.SubElement(qtimetadatafield, 'fieldentry')
                fieldentry.text = str(self.ff_res1_points)

                # Fragentitel einsetzen -- "presentation label" in xml
                presentation.set('label', self.ff_question_title)

                # Fragen-Text (Format) einsetzen -- "mattext_texttype" in xml -- Gibt das Format des Textes an
                question_description_mattext.set('texttype', "text/html")

                # Fragen-Text (Text) einsetzen   -- "mattext_texttype" in xml -- Gibt die eigentliche Fragen-Beschreibung an
                # Wenn Bild enthalten ist, dann in Fragenbeschreibung einbetten
                question_description_mattext.text = test_generator_modul_ilias_test_struktur.Additional_Funtions.add_picture_to_description_main(
                    self, self.ff_description_img_name_1, self.ff_description_img_data_1,
                    self.ff_description_img_name_2, self.ff_description_img_data_2,
                    self.ff_description_img_name_3, self.ff_description_img_data_3,
                    self.ff_question_description_main, question_description_mattext,
                    question_description_material, id_nr)

                # ----------------------------------------------------------------------- Variable
                Create_Formelfrage_Questions.ff_question_variables_structure(self, qtimetadata, "$v1",
                                                                             self.ff_var1_min, self.ff_var1_max,
                                                                             self.ff_var1_prec,
                                                                             self.ff_var1_divby,
                                                                             self.ff_var1_unit)
                Create_Formelfrage_Questions.ff_question_variables_structure(self, qtimetadata, "$v2",
                                                                             self.ff_var2_min, self.ff_var2_max,
                                                                             self.ff_var2_prec,
                                                                             self.ff_var2_divby,
                                                                             self.ff_var2_unit)
                Create_Formelfrage_Questions.ff_question_variables_structure(self, qtimetadata, "$v3",
                                                                             self.ff_var3_min, self.ff_var3_max,
                                                                             self.ff_var3_prec,
                                                                             self.ff_var3_divby,
                                                                             self.ff_var3_unit)
                Create_Formelfrage_Questions.ff_question_variables_structure(self, qtimetadata, "$v4",
                                                                             self.ff_var4_min, self.ff_var4_max,
                                                                             self.ff_var4_prec,
                                                                             self.ff_var4_divby,
                                                                             self.ff_var4_unit)
                Create_Formelfrage_Questions.ff_question_variables_structure(self, qtimetadata, "$v5",
                                                                             self.ff_var5_min, self.ff_var5_max,
                                                                             self.ff_var5_prec,
                                                                             self.ff_var5_divby,
                                                                             self.ff_var5_unit)
                Create_Formelfrage_Questions.ff_question_variables_structure(self, qtimetadata, "$v6",
                                                                             self.ff_var6_min, self.ff_var6_max,
                                                                             self.ff_var6_prec,
                                                                             self.ff_var6_divby,
                                                                             self.ff_var6_unit)
                Create_Formelfrage_Questions.ff_question_variables_structure(self, qtimetadata, "$v7",
                                                                             self.ff_var7_min, self.ff_var7_max,
                                                                             self.ff_var7_prec,
                                                                             self.ff_var7_divby,
                                                                             self.ff_var7_unit)
                Create_Formelfrage_Questions.ff_question_variables_structure(self, qtimetadata, "$v8",
                                                                             self.ff_var8_min, self.ff_var8_max,
                                                                             self.ff_var8_prec,
                                                                             self.ff_var8_divby,
                                                                             self.ff_var8_unit)
                Create_Formelfrage_Questions.ff_question_variables_structure(self, qtimetadata, "$v9",
                                                                             self.ff_var9_min, self.ff_var9_max,
                                                                             self.ff_var9_prec,
                                                                             self.ff_var9_divby,
                                                                             self.ff_var9_unit)
                Create_Formelfrage_Questions.ff_question_variables_structure(self, qtimetadata, "$v10",
                                                                             self.ff_var10_min,
                                                                             self.ff_var10_max,
                                                                             self.ff_var10_prec,
                                                                             self.ff_var10_divby,
                                                                             self.ff_var10_unit)
                Create_Formelfrage_Questions.ff_question_variables_structure(self, qtimetadata, "$v11",
                                                                             self.ff_var11_min,
                                                                             self.ff_var11_max,
                                                                             self.ff_var11_prec,
                                                                             self.ff_var11_divby,
                                                                             self.ff_var11_unit)
                Create_Formelfrage_Questions.ff_question_variables_structure(self, qtimetadata, "$v12",
                                                                             self.ff_var12_min,
                                                                             self.ff_var12_max,
                                                                             self.ff_var12_prec,
                                                                             self.ff_var12_divby,
                                                                             self.ff_var12_unit)
                Create_Formelfrage_Questions.ff_question_variables_structure(self, qtimetadata, "$v13",
                                                                             self.ff_var13_min,
                                                                             self.ff_var13_max,
                                                                             self.ff_var13_prec,
                                                                             self.ff_var13_divby,
                                                                             self.ff_var13_unit)
                Create_Formelfrage_Questions.ff_question_variables_structure(self, qtimetadata, "$v14",
                                                                             self.ff_var14_min,
                                                                             self.ff_var14_max,
                                                                             self.ff_var14_prec,
                                                                             self.ff_var14_divby,
                                                                             self.ff_var14_unit)
                Create_Formelfrage_Questions.ff_question_variables_structure(self, qtimetadata, "$v15",
                                                                             self.ff_var15_min,
                                                                             self.ff_var15_max,
                                                                             self.ff_var15_prec,
                                                                             self.ff_var15_divby,
                                                                             self.ff_var15_unit)

                # ----------------------------------------------------------------------- Solution
                Create_Formelfrage_Questions.ff_question_results_structure(self, qtimetadata, "$r1",
                                                                           self.ff_res1_formula,
                                                                           self.ff_res1_min, self.ff_res1_max,
                                                                           self.ff_res1_prec, self.ff_res1_tol,
                                                                           self.ff_res1_points,
                                                                           self.ff_res1_unit)
                Create_Formelfrage_Questions.ff_question_results_structure(self, qtimetadata, "$r2",
                                                                           self.ff_res2_formula,
                                                                           self.ff_res2_min, self.ff_res2_max,
                                                                           self.ff_res2_prec, self.ff_res2_tol,
                                                                           self.ff_res2_points,
                                                                           self.ff_res2_unit)
                Create_Formelfrage_Questions.ff_question_results_structure(self, qtimetadata, "$r3",
                                                                           self.ff_res3_formula,
                                                                           self.ff_res3_min, self.ff_res3_max,
                                                                           self.ff_res3_prec, self.ff_res3_tol,
                                                                           self.ff_res3_points,
                                                                           self.ff_res3_unit)
                Create_Formelfrage_Questions.ff_question_results_structure(self, qtimetadata, "$r4",
                                                                           self.ff_res4_formula,
                                                                           self.ff_res4_min, self.ff_res4_max,
                                                                           self.ff_res4_prec, self.ff_res4_tol,
                                                                           self.ff_res4_points,
                                                                           self.ff_res4_unit)
                Create_Formelfrage_Questions.ff_question_results_structure(self, qtimetadata, "$r5",
                                                                           self.ff_res5_formula,
                                                                           self.ff_res5_min, self.ff_res5_max,
                                                                           self.ff_res5_prec, self.ff_res5_tol,
                                                                           self.ff_res5_points,
                                                                           self.ff_res5_unit)
                Create_Formelfrage_Questions.ff_question_results_structure(self, qtimetadata, "$r6",
                                                                           self.ff_res6_formula,
                                                                           self.ff_res6_min, self.ff_res6_max,
                                                                           self.ff_res6_prec, self.ff_res6_tol,
                                                                           self.ff_res6_points,
                                                                           self.ff_res6_unit)
                Create_Formelfrage_Questions.ff_question_results_structure(self, qtimetadata, "$r7",
                                                                           self.ff_res7_formula,
                                                                           self.ff_res7_min, self.ff_res7_max,
                                                                           self.ff_res7_prec, self.ff_res7_tol,
                                                                           self.ff_res7_points,
                                                                           self.ff_res7_unit)
                Create_Formelfrage_Questions.ff_question_results_structure(self, qtimetadata, "$r8",
                                                                           self.ff_res8_formula,
                                                                           self.ff_res8_min, self.ff_res8_max,
                                                                           self.ff_res8_prec, self.ff_res8_tol,
                                                                           self.ff_res8_points,
                                                                           self.ff_res8_unit)
                Create_Formelfrage_Questions.ff_question_results_structure(self, qtimetadata, "$r9",
                                                                           self.ff_res9_formula,
                                                                           self.ff_res9_min, self.ff_res9_max,
                                                                           self.ff_res9_prec, self.ff_res9_tol,
                                                                           self.ff_res9_points,
                                                                           self.ff_res9_unit)
                Create_Formelfrage_Questions.ff_question_results_structure(self, qtimetadata, "$r10",
                                                                           self.ff_res10_formula,
                                                                           self.ff_res10_min, self.ff_res10_max,
                                                                           self.ff_res10_prec,
                                                                           self.ff_res10_tol,
                                                                           self.ff_res10_points,
                                                                           self.ff_res10_unit)

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
                if self.ff_question_type_test_or_pool == "question_test":
                    self.ff_myroot[0][len(self.ff_myroot[0]) - 1].append(item)

                # Wenn es sich um einen ILIAS-Pool handelt, beinhaltet die XML keine Struktur
                # Die Frage kann einfach angehangen werden
                else:
                    self.ff_myroot.append(item)

                self.ff_mytree.write(self.qti_file_path_output)

                print(str(
                    self.ff_number_of_questions_generated) + ".) Formelfrage Frage erstellt! ---> Titel: " + str(
                    self.ff_question_title))
                self.ff_number_of_questions_generated += 1
                self.ff_collection_of_question_titles.append(self.ff_question_title)

        ff_connect.commit()
        ff_connect.close()

        if self.ff_question_type_test_or_pool == "question_pool":
            ######  Anpassung der Datei "qpl". Akualisierung des Dateinamens
            self.qpl_file = os.path.normpath(
                os.path.join(self.formelfrage_files_path, "ff_ilias_pool_abgabe", self.ilias_id_pool_qpl_dir,
                             self.ilias_id_pool_qti_xml))

            self.mytree = ET.parse(self.qpl_file)
            self.myroot = self.mytree.getroot()

            for ident_id in self.myroot.iter('Identifier'):
                ident_id.set('Entry', "il_0_qpl_" + str(self.ff_file_max_id + 1))
            self.mytree.write(self.qpl_file)

    def ff_question_variables_structure(self, xml_qtimetadata, ff_var_name, ff_var_min, ff_var_max, ff_var_prec,
                                        ff_var_divby, ff_var_unit):

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

        # Mit Einheiten:
        if self.ff_var_unit != "":
            fieldentry.text = "a:6:{" \
                              "s:9:\"precision\";i:" + self.ff_var_prec + ";" \
                                                                          "s:12:\"intprecision\";s:" + str(
                self.ff_var_divby_length) + ":\"" + self.ff_var_divby + "\";" \
                                                                        "s:8:\"rangemin\";d:" + self.ff_var_min + ";" \
                                                                                                                  "s:8:\"rangemax\";d:" + self.ff_var_max + ";" \
                                                                                                                                                            "s:4:\"unit\";s:" + str(
                self.ff_var_unit_length) + ":\"" + self.ff_var_unit + "\";" \
                                                                      "s:9:\"unitvalue\";s:" + str(
                len(Formelfrage.unit_table(self, self.ff_var_unit))) + ":\"" + Formelfrage.unit_table(self,
                                                                                                      self.ff_var_unit) + "\";" \
                                                                                                                          "}"
        # Ohne Einheiten:
        else:
            fieldentry.text = "a:6:{" \
                              "s:9:\"precision\";i:" + self.ff_var_prec + ";" \
                                                                          "s:12:\"intprecision\";s:" + str(
                self.ff_var_divby_length) + ":\"" + self.ff_var_divby + "\";" \
                                                                        "s:8:\"rangemin\";d:" + self.ff_var_min + ";" \
                                                                                                                  "s:8:\"rangemax\";d:" + self.ff_var_max + ";" \
                                                                                                                                                            "s:4:\"unit\";s:0:\"\";" \
                                                                                                                                                            "s:9:\"unitvalue\";s:0:\"\";" \
                                                                                                                                                            "}"

    def ff_question_results_structure(self, xml_qtimetadata, ff_res_name, ff_res_formula, ff_res_min,
                                      ff_res_max, ff_res_prec, ff_res_tol, ff_res_points, ff_res_unit):

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

            formula = ' '.join([self.replace_words_dict.get(i, i) for i in formula.split()])

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

        # Mit Einheiten:
        if self.ff_res_unit != "":
            fieldentry.text = "a:10:{" \
                              "s:9:\"precision\";i:" + self.ff_res_prec + ";" \
                                                                          "s:9:\"tolerance\";s:" + self.ff_res_tol_length + ":\"" + self.ff_res_tol + "\";" \
                                                                                                                                                      "s:8:\"rangemin\";s:" + self.ff_res_min_length + ":\"" + self.ff_res_min + "\";" \
                                                                                                                                                                                                                                 "s:8:\"rangemax\";s:" + self.ff_res_max_length + ":\"" + self.ff_res_max + "\";" \
                                                                                                                                                                                                                                                                                                            "s:6:\"points\";s:1:\"" + self.ff_res_points + "\";" \
                                                                                                                                                                                                                                                                                                                                                           "s:7:\"formula\";s:" + self.ff_res_formula_length + ":\"" + self.ff_res_formula + "\";" \
                                                                                                                                                                                                                                                                                                                                                                                                                                             "s:6:\"rating\";s:0:\"\";" \
                                                                                                                                                                                                                                                                                                                                                                                                                                             "s:4:\"unit\";s:" + str(
                self.ff_res_unit_length) + ":\"" + self.ff_res_unit + "\";" \
                                                                      "s:9:\"unitvalue\";s:" + str(
                len(Formelfrage.unit_table(self, self.ff_res_unit))) + ":\"" + Formelfrage.unit_table(self,
                                                                                                      self.ff_res_unit) + "\";" \
                                                                                                                          "s:11:\"resultunits\";a:27:{i:0;a:2:{s:4:\"unit\";s:1:\"H\";s:9:\"unitvalue\";s:3:\"125\";}" \
                                                                                                                          "i:1;a:2:{s:4:\"unit\";s:2:\"mH\";s:9:\"unitvalue\";s:3:\"126\";}" \
                                                                                                                          "i:2;a:2:{s:4:\"unit\";s:3:\"µH\";s:9:\"unitvalue\";s:3:\"127\";}" \
                                                                                                                          "i:3;a:2:{s:4:\"unit\";s:2:\"nH\";s:9:\"unitvalue\";s:3:\"128\";}" \
                                                                                                                          "i:4;a:2:{s:4:\"unit\";s:2:\"kH\";s:9:\"unitvalue\";s:3:\"129\";}" \
                                                                                                                          "i:5;a:2:{s:4:\"unit\";s:2:\"pH\";s:9:\"unitvalue\";s:3:\"130\";}" \
                                                                                                                          "i:6;a:2:{s:4:\"unit\";s:1:\"F\";s:9:\"unitvalue\";s:3:\"131\";}" \
                                                                                                                          "i:7;a:2:{s:4:\"unit\";s:2:\"mF\";s:9:\"unitvalue\";s:3:\"132\";}" \
                                                                                                                          "i:8;a:2:{s:4:\"unit\";s:3:\"µF\";s:9:\"unitvalue\";s:3:\"133\";}" \
                                                                                                                          "i:9;a:2:{s:4:\"unit\";s:2:\"nF\";s:9:\"unitvalue\";s:3:\"134\";}" \
                                                                                                                          "i:10;a:2:{s:4:\"unit\";s:2:\"pF\";s:9:\"unitvalue\";s:3:\"135\";}" \
                                                                                                                          "i:11;a:2:{s:4:\"unit\";s:1:\"W\";s:9:\"unitvalue\";s:3:\"136\";}" \
                                                                                                                          "i:12;a:2:{s:4:\"unit\";s:2:\"kW\";s:9:\"unitvalue\";s:3:\"137\";}" \
                                                                                                                          "i:13;a:2:{s:4:\"unit\";s:2:\"MW\";s:9:\"unitvalue\";s:3:\"138\";}" \
                                                                                                                          "i:14;a:2:{s:4:\"unit\";s:1:\"V\";s:9:\"unitvalue\";s:3:\"139\";}" \
                                                                                                                          "i:15;a:2:{s:4:\"unit\";s:2:\"kV\";s:9:\"unitvalue\";s:3:\"140\";}" \
                                                                                                                          "i:16;a:2:{s:4:\"unit\";s:2:\"mV\";s:9:\"unitvalue\";s:3:\"141\";}" \
                                                                                                                          "i:17;a:2:{s:4:\"unit\";s:3:\"µV\";s:9:\"unitvalue\";s:3:\"142\";}" \
                                                                                                                          "i:18;a:2:{s:4:\"unit\";s:2:\"MV\";s:9:\"unitvalue\";s:3:\"143\";}" \
                                                                                                                          "i:19;a:2:{s:4:\"unit\";s:1:\"A\";s:9:\"unitvalue\";s:3:\"144\";}" \
                                                                                                                          "i:20;a:2:{s:4:\"unit\";s:2:\"mA\";s:9:\"unitvalue\";s:3:\"145\";}" \
                                                                                                                          "i:21;a:2:{s:4:\"unit\";s:3:\"µA\";s:9:\"unitvalue\";s:3:\"146\";}" \
                                                                                                                          "i:22;a:2:{s:4:\"unit\";s:2:\"kA\";s:9:\"unitvalue\";s:3:\"147\";}" \
                                                                                                                          "i:23;a:2:{s:4:\"unit\";s:3:\"Ohm\";s:9:\"unitvalue\";s:3:\"148\";}" \
                                                                                                                          "i:24;a:2:{s:4:\"unit\";s:2:\"mW\";s:9:\"unitvalue\";s:3:\"149\";}" \
                                                                                                                          "i:25;a:2:{s:4:\"unit\";s:4:\"kOhm\";s:9:\"unitvalue\";s:3:\"150\";}" \
                                                                                                                          "i:26;a:2:{s:4:\"unit\";s:4:\"mOhm\";s:9:\"unitvalue\";s:3:\"151\";}}" \
                                                                                                                          "}"

        # Ohne Einheiten:
        else:
            fieldentry.text = "a:10:{" \
                              "s:9:\"precision\";i:" + self.ff_res_prec + ";" \
                                                                          "s:9:\"tolerance\";s:" + str(
                self.ff_res_tol_length) + ":\"" + self.ff_res_tol + "\";" \
                                                                    "s:8:\"rangemin\";s:" + str(
                self.ff_res_min_length) + ":\"" + self.ff_res_min + "\";" \
                                                                    "s:8:\"rangemax\";s:" + str(
                self.ff_res_max_length) + ":\"" + self.ff_res_max + "\";" \
                                                                    "s:6:\"points\";s:1:\"" + self.ff_res_points + "\";" \
                                                                                                                   "s:7:\"formula\";s:" + str(
                self.ff_res_formula_length) + ":\"" + self.ff_res_formula + "\";" \
                                                                            "s:6:\"rating\";s:0:\"\";" \
                                                                            "s:4:\"unit\";s:0:\"\";" \
                                                                            "s:9:\"unitvalue\";s:0:\"\";" \
                                                                            "s:11:\"resultunits\";a:0:{}" \
                                                                            "}"

    def create_formelfrage_test(self, entry_to_index_dict):
        self.ff_db_entry_to_index_dict = entry_to_index_dict

        test_generator_modul_ilias_test_struktur.Create_ILIAS_Test.__init__(self,
                                                                            self.ff_db_entry_to_index_dict,
                                                                            self.formelfrage_test_tst_file_path_template,
                                                                            self.formelfrage_test_tst_file_path_output,
                                                                            self.formelfrage_test_qti_file_path_template,
                                                                            self.formelfrage_test_qti_file_path_output,
                                                                            self.ff_ilias_test_title_entry.get(),
                                                                            self.create_formelfrage_test_entry.get(),
                                                                            self.ff_question_type_entry.get(),
                                                                            )

