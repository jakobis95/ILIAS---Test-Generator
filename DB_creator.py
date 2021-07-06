import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk

#Bevor diese Datei ausgeführt wird muss generaldb.db und generaldb2.db im projekt gelöscht werden
#Diese Datei ausgeführt werden und erstellt zwei neue leere Datenbanken
#Hier können auch anpassungen an den Datenstruckturen vorgenommen werden

class generate_db():
    def __init__(self, dbname):

        mydb = sqlite3.connect(dbname)
        cursor = mydb.cursor()


        cursor.execute("""CREATE TABLE IF NOT EXISTS formelfrage (
                            question_difficulty text,
                            question_category text,
                            question_type text,
                            question_title text,
                            question_description_title text,
                            question_description_main text,
                            res1_formula text,
                            res2_formula text,
                            res3_formula text,
                            res4_formula text,
                            res5_formula text,
                            res6_formula text,
                            res7_formula text,
                            res8_formula text,
                            res9_formula text,
                            res10_formula text,
                            var1_name text,
                            var1_min int,
                            var1_max int,
                            var1_prec int,
                            var1_divby int,
                            var1_unit text,
                            var2_name text,
                            var2_min int,
                            var2_max int,
                            var2_prec int,
                            var2_divby int,
                            var2_unit text,
                            var3_name text,
                            var3_min int,
                            var3_max int,
                            var3_prec int,
                            var3_divby int,
                            var3_unit text,
                            var4_name text,
                            var4_min int,
                            var4_max int,
                            var4_prec int,
                            var4_divby int,
                            var4_unit text,
                            var5_name text,
                            var5_min int,
                            var5_max int,
                            var5_prec int,
                            var5_divby int,
                            var5_unit text,
                            var6_name text,
                            var6_min int,
                            var6_max int,
                            var6_prec int,
                            var6_divby int,
                            var6_unit text,
                            var7_name text,
                            var7_min int,
                            var7_max int,
                            var7_prec int,
                            var7_divby int,
                            var7_unit text,
                            var8_name text,
                            var8_min int,
                            var8_max int,
                            var8_prec int,
                            var8_divby int,
                            var8_unit text,
                            var9_name text,
                            var9_min int,
                            var9_max int,
                            var9_prec int,
                            var9_divby int,
                            var9_unit text,
                            var10_name text,
                            var10_min int,
                            var10_max int,
                            var10_prec int,
                            var10_divby int,
                            var10_unit text,
                            var11_name text,
                            var11_min int,
                            var11_max int,
                            var11_prec int,
                            var11_divby int,
                            var11_unit text,
                            var12_name text,
                            var12_min int,
                            var12_max int,
                            var12_prec int,
                            var12_divby int,
                            var12_unit text,
                            var13_name text,
                            var13_min int,
                            var13_max int,
                            var13_prec int,
                            var13_divby int,
                            var13_unit text,
                            var14_name text,
                            var14_min int,
                            var14_max int,
                            var14_prec int,
                            var14_divby int,
                            var14_unit text,
                            var15_name text,
                            var15_min int,
                            var15_max int,
                            var15_prec int,
                            var15_divby int,
                            var15_unit text,
                            res1_name text,
                            res1_min int,
                            res1_max int,
                            res1_prec int,
                            res1_tol int,
                            res1_points int,
                            res1_unit text,
                            res2_name text,
                            res2_min int,
                            res2_max int,
                            res2_prec int,
                            res2_tol int,
                            res2_points int,
                            res2_unit text,
                            res3_name text,
                            res3_min int,
                            res3_max int,
                            res3_prec int,
                            res3_tol int,
                            res3_points int,
                            res3_unit text,
                            res4_name text,
                            res4_min int,
                            res4_max int,
                            res4_prec int,
                            res4_tol int,
                            res4_points int,
                            res4_unit text,
                            res5_name text,
                            res5_min int,
                            res5_max int,
                            res5_prec int,
                            res5_tol int,
                            res5_points int,
                            res5_unit text,
                            res6_name text,
                            res6_min int,
                            res6_max int,
                            res6_prec int,
                            res6_tol int,
                            res6_points int,
                            res6_unit text,
                            res7_name text,
                            res7_min int,
                            res7_max int,
                            res7_prec int,
                            res7_tol int,
                            res7_points int,
                            res7_unit text,
                            res8_name text,
                            res8_min int,
                            res8_max int,
                            res8_prec int,
                            res8_tol int,
                            res8_points int,
                            res8_unit text,
                            res9_name text,
                            res9_min int,
                            res9_max int,
                            res9_prec int,
                            res9_tol int,
                            res9_points int,
                            res9_unit text,
                            res10_name text,
                            res10_min int,
                            res10_max int,
                            res10_prec int,
                            res10_tol int,
                            res10_points int,
                            res10_unit text,
        
                            description_img_name_1 text,
                            description_img_data_1 blop,
                            description_img_path_1 text,
        
                            description_img_name_2 text,
                            description_img_data_2 blop,
                            description_img_path_2 text,
        
                            description_img_name_3 text,
                            description_img_data_3 blop,
                            description_img_path_3 text,
        
                            test_time text,
                            var_number int,
                            res_number int,
                            question_pool_tag text,
                            question_author text,
                            date text
                            )""")



        mydb.commit()

        cursor.execute("""CREATE TABLE IF NOT EXISTS formelfrage_permutation_table (
                            question_difficulty text,
                            question_category text,
                            question_type text,
                            question_title text,
                            question_description_title text,
                            question_description_main text,
                            res1_formula text,
                            res2_formula text,
                            res3_formula text,
                            res4_formula text,
                            res5_formula text,
                            res6_formula text,
                            res7_formula text,
                            res8_formula text,
                            res9_formula text,
                            res10_formula text,
                            var1_name text,
                            var1_min int,
                            var1_max int,
                            var1_prec int,
                            var1_divby int,
                            var1_unit text,
                            var2_name text,
                            var2_min int,
                            var2_max int,
                            var2_prec int,
                            var2_divby int,
                            var2_unit text,
                            var3_name text,
                            var3_min int,
                            var3_max int,
                            var3_prec int,
                            var3_divby int,
                            var3_unit text,
                            var4_name text,
                            var4_min int,
                            var4_max int,
                            var4_prec int,
                            var4_divby int,
                            var4_unit text,
                            var5_name text,
                            var5_min int,
                            var5_max int,
                            var5_prec int,
                            var5_divby int,
                            var5_unit text,
                            var6_name text,
                            var6_min int,
                            var6_max int,
                            var6_prec int,
                            var6_divby int,
                            var6_unit text,
                            var7_name text,
                            var7_min int,
                            var7_max int,
                            var7_prec int,
                            var7_divby int,
                            var7_unit text,
                            var8_name text,
                            var8_min int,
                            var8_max int,
                            var8_prec int,
                            var8_divby int,
                            var8_unit text,
                            var9_name text,
                            var9_min int,
                            var9_max int,
                            var9_prec int,
                            var9_divby int,
                            var9_unit text,
                            var10_name text,
                            var10_min int,
                            var10_max int,
                            var10_prec int,
                            var10_divby int,
                            var10_unit text,
                            res1_name text,
                            res1_min int,
                            res1_max int,
                            res1_prec int,
                            res1_tol int,
                            res1_points int,
                            res1_unit text,
                            res2_name text,
                            res2_min int,
                            res2_max int,
                            res2_prec int,
                            res2_tol int,
                            res2_points int,
                            res2_unit text,
                            res3_name text,
                            res3_min int,
                            res3_max int,
                            res3_prec int,
                            res3_tol int,
                            res3_points int,
                            res3_unit text,
                            res4_name text,
                            res4_min int,
                            res4_max int,
                            res4_prec int,
                            res4_tol int,
                            res4_points int,
                            res4_unit text,
                            res5_name text,
                            res5_min int,
                            res5_max int,
                            res5_prec int,
                            res5_tol int,
                            res5_points int,
                            res5_unit text,
                            res6_name text,
                            res6_min int,
                            res6_max int,
                            res6_prec int,
                            res6_tol int,
                            res6_points int,
                            res6_unit text,
                            res7_name text,
                            res7_min int,
                            res7_max int,
                            res7_prec int,
                            res7_tol int,
                            res7_points int,
                            res7_unit text,
                            res8_name text,
                            res8_min int,
                            res8_max int,
                            res8_prec int,
                            res8_tol int,
                            res8_points int,
                            res8_unit text,
                            res9_name text,
                            res9_min int,
                            res9_max int,
                            res9_prec int,
                            res9_tol int,
                            res9_points int,
                            res9_unit text,
                            res10_name text,
                            res10_min int,
                            res10_max int,
                            res10_prec int,
                            res10_tol int,
                            res10_points int,
                            res10_unit text,
                            
                            
                            perm_var_symbol_1 text,
                            perm_var_value_1 text,
                            perm_var_symbol_2 text,
                            perm_var_value_2 text,
                            perm_var_symbol_3 text,
                            perm_var_value_3 text,
                            perm_var_symbol_4 text,
                            perm_var_value_4 text,
                            perm_var_symbol_5 text,
                            perm_var_value_5 text,
                            perm_var_symbol_6 text,
                            perm_var_value_6 text,
                            perm_var_symbol_7 text,
                            perm_var_value_7 text,
                            perm_var_symbol_8 text,
                            perm_var_value_8 text,
                            perm_var_symbol_9 text,
                            perm_var_value_9 text,
                            perm_var_symbol_10 text,
                            perm_var_value_10 text,
                            
                            
                            description_img_name_1 text,
                            description_img_data_1 blop,
                            description_img_path_1 text,
                            
                            description_img_name_2 text,
                            description_img_data_2 blop,
                            description_img_path_2 text,
                            
                            description_img_name_3 text,
                            description_img_data_3 blop,
                            description_img_path_3 text,
                            
                            test_time text,
                            var_number int,
                            res_number int,
                            question_pool_tag text,
                            question_author text,
                            date text
                            )""")
        mydb.commit()

        cursor.execute("""CREATE TABLE IF NOT EXISTS singlechoice (
                            question_difficulty text,
                            question_category text,
                            question_type text,
                            question_title text,
                            question_description_title text,
                            question_description_main text,
        
                            response_1_text text,
                            response_1_img_path text,
                            response_1_pts int,
                            
        
                            response_2_text text,
                            response_2_img_path text,
                            response_2_pts int,
                           
        
                            response_3_text text,
                            response_3_img_path text,
                            response_3_pts int,
                            
        
                            response_4_text text,
                            response_4_img_path text,
                            response_4_pts int,
                            
        
                            response_5_text text,
                            response_5_img_path text,
                            response_5_pts int,
                            
        
                            response_6_text text,
                            response_6_img_path text,
                            response_6_pts int,
                            
        
                            response_7_text text,
                            response_7_img_path text,
                            response_7_pts int,
                            
        
                            response_8_text text,
                            response_8_img_path text,
                            response_8_pts int,
                            
        
                            response_9_text text,
                            response_9_img_path text,
                            response_9_pts int,
                        
        
                            response_10_text text,
                            response_10_img_path text,
                            response_10_pts int,
                            
        
                            picture_preview_pixel int,
        
                            description_img_name_1 text,
                            description_img_data_1 blop,
                            description_img_path_1 text,
        
                            description_img_name_2 text,
                            description_img_data_2 blop,
                            description_img_path_2 text,
        
                            description_img_name_3 text,
                            description_img_data_3 blop,
                            description_img_path_3 text,
                            
                            
                            test_time text,
                            var_number int,
                            question_pool_tag text,
                            question_author text,
                            shuffle_answers,
                            date text
                            )""")
        mydb.commit()
        cursor.execute("""CREATE TABLE IF NOT EXISTS multiplechoice (
                                question_difficulty text,
                                question_category text,
                                question_type text,
                                question_title text,
                                question_description_title text,
                                question_description_main text,
        
                                response_1_text text,
                                response_1_img_path text,
                                response_1_pts_correct_answer int,
                                response_1_pts_false_answer int,
                                
        
                                response_2_text text,
                                response_2_img_path text,
                                response_2_pts_correct_answer int,
                                response_2_pts_false_answer int,
                                
        
                                response_3_text text,
                                response_3_img_path text,
                                response_3_pts_correct_answer int,
                                response_3_pts_false_answer int,
                                
        
                                response_4_text text,
                                response_4_img_path text,
                                response_4_pts_correct_answer int,
                                response_4_pts_false_answer int,
                                
        
                                response_5_text text,
                                response_5_img_path text,
                                response_5_pts_correct_answer int,
                                response_5_pts_false_answer int,
                                
        
                                response_6_text text,
                                response_6_img_path text,
                                response_6_pts_correct_answer int,
                                response_6_pts_false_answer int,
                                
        
                                response_7_text text,
                                response_7_img_path text,
                                response_7_pts_correct_answer int,
                                response_7_pts_false_answer int,
                                
        
                                response_8_text text,
                                response_8_img_path text,
                                response_8_pts_correct_answer int,
                                response_8_pts_false_answer int,
                                
                                
        
                                response_9_text text,
                                response_9_img_path text,
                                response_9_pts_correct_answer int,
                                response_9_pts_false_answer int,
                                
        
                                response_10_text text,
                                response_10_img_path text,
                                response_10_pts_correct_answer int,
                                response_10_pts_false_answer int,
                                
        
        
                                picture_preview_pixel int,
        
        
                                description_img_name_1 text,
                                description_img_data_1 blop,
                                description_img_path_1 text,
        
                                description_img_name_2 text,
                                description_img_data_2 blop,
                                description_img_path_2 text,
        
                                description_img_name_3 text,
                                description_img_data_3 blop,
                                description_img_path_3 text,
        
                                test_time text,
        
                                var_number int,
                                question_pool_tag text,
                                question_author text,
                                shuffle_answers,
                                multiple_row_answ,
                                date text
                                )""")
        mydb.commit()
        cursor.execute("""CREATE TABLE IF NOT EXISTS zuordnungsfrage (
                            question_difficulty text,
                            question_category text,
                            question_type text,
                            question_title text,
                            question_description_title text,
                            question_description_main text,
                            mix_answers text,
                            asignment_mode int,
        
                            definitions_response_1_text text,
                            definitions_response_1_img_path text,
                            
        
                            definitions_response_2_text text,
                            
                            definitions_response_2_img_path text,
                            
        
                            definitions_response_3_text text,
                            
                            definitions_response_3_img_path text,
                            
        
                            definitions_response_4_text text,
                            
                            definitions_response_4_img_path text,
                            
        
                            definitions_response_5_text text,
                            
                            definitions_response_5_img_path text,
                            
        
                            definitions_response_6_text text,
                           
                            definitions_response_6_img_path text,
                            
        
                            definitions_response_7_text text,
                            
                            definitions_response_7_img_path text,
                            
        
                            definitions_response_8_text text,
                            
                            definitions_response_8_img_path text,
                            
        
                            definitions_response_9_text text,
                            
                            definitions_response_9_img_path text,
                            
        
                            definitions_response_10_text text,
                            
                            definitions_response_10_img_path text,
                            
        
        
        
                            terms_response_1_text text,
                            
                            terms_response_1_img_path text,
                            
        
                            terms_response_2_text text,
                            
                            terms_response_2_img_path text,
                            
        
                            terms_response_3_text text,
                            
                            terms_response_3_img_path text,
                            
        
                            terms_response_4_text text,
                            
                            terms_response_4_img_path text,
                            
        
                            terms_response_5_text text,
                            
                            terms_response_5_img_path text,
                            
        
                            terms_response_6_text text,
                            
                            terms_response_6_img_path text,
                            
        
                            terms_response_7_text text,
                            
                            terms_response_7_img_path text,
                            
        
                            terms_response_8_text text,
                            
                            terms_response_8_img_path text,
                            
        
                            terms_response_9_text text,
                            
                            terms_response_9_img_path text,
                            
        
                            terms_response_10_text text,
                            terms_response_10_img_path text,
                            
        
        
        
                            assignment_pairs_definition_1 text,
                            assignment_pairs_term_1 text,
                            assignment_pairs_1_pts int,
        
                            assignment_pairs_definition_2 text,
                            assignment_pairs_term_2 text,
                            assignment_pairs_2_pts int,
        
                            assignment_pairs_definition_3 text,
                            assignment_pairs_term_3 text,
                            assignment_pairs_3_pts int,
        
                            assignment_pairs_definition_4 text,
                            assignment_pairs_term_4 text,
                            assignment_pairs_4_pts int,
        
                            assignment_pairs_definition_5 text,
                            assignment_pairs_term_5 text,
                            assignment_pairs_5_pts int,
        
                            assignment_pairs_definition_6 text,
                            assignment_pairs_term_6 text,
                            assignment_pairs_6_pts int,
        
                            assignment_pairs_definition_7 text,
                            assignment_pairs_term_7 text,
                            assignment_pairs_7_pts int,
        
                            assignment_pairs_definition_8 text,
                            assignment_pairs_term_8 text,
                            assignment_pairs_8_pts int,
        
                            assignment_pairs_definition_9 text,
                            assignment_pairs_term_9 text,
                            assignment_pairs_9_pts int,
        
                            assignment_pairs_definition_10 text,
                            assignment_pairs_term_10 text,
                            assignment_pairs_10_pts int,
        
        
        
        
                            picture_preview_pixel int,
        
                            description_img_name_1 text,
                            description_img_data_1 blop,
                            description_img_path_1 text,
        
                            description_img_name_2 text,
                            description_img_data_2 blop,
                            description_img_path_2 text,
        
                            description_img_name_3 text,
                            description_img_data_3 blop,
                            description_img_path_3 text,
        
                            test_time text,
                            var_number int,
                            res_number int,
                            question_pool_tag text,
                            question_author text,
                            date text
                            )""")


        cursor.execute("""CREATE TABLE IF NOT EXISTS formelfrage_permutation (
                            question_difficulty text,
                            question_category text,
                            question_type text,
                            question_title text,
                            question_description_title text,
                            question_description_main text,
                            res1_formula text,
                            res2_formula text,
                            res3_formula text,
                            res4_formula text,
                            res5_formula text,
                            res6_formula text,
                            res7_formula text,
                            res8_formula text,
                            res9_formula text,
                            res10_formula text,
                            var1_name text,
                            var1_min int,
                            var1_max int,
                            var1_prec int,
                            var1_divby int,
                            var1_unit text,
                            var2_name text,
                            var2_min int,
                            var2_max int,
                            var2_prec int,
                            var2_divby int,
                            var2_unit text,
                            var3_name text,
                            var3_min int,
                            var3_max int,
                            var3_prec int,
                            var3_divby int,
                            var3_unit text,
                            var4_name text,
                            var4_min int,
                            var4_max int,
                            var4_prec int,
                            var4_divby int,
                            var4_unit text,
                            var5_name text,
                            var5_min int,
                            var5_max int,
                            var5_prec int,
                            var5_divby int,
                            var5_unit text,
                            var6_name text,
                            var6_min int,
                            var6_max int,
                            var6_prec int,
                            var6_divby int,
                            var6_unit text,
                            var7_name text,
                            var7_min int,
                            var7_max int,
                            var7_prec int,
                            var7_divby int,
                            var7_unit text,
                            var8_name text,
                            var8_min int,
                            var8_max int,
                            var8_prec int,
                            var8_divby int,
                            var8_unit text,
                            var9_name text,
                            var9_min int,
                            var9_max int,
                            var9_prec int,
                            var9_divby int,
                            var9_unit text,
                            var10_name text,
                            var10_min int,
                            var10_max int,
                            var10_prec int,
                            var10_divby int,
                            var10_unit text,
                            res1_name text,
                            res1_min int,
                            res1_max int,
                            res1_prec int,
                            res1_tol int,
                            res1_points int,
                            res1_unit text,
                            res2_name text,
                            res2_min int,
                            res2_max int,
                            res2_prec int,
                            res2_tol int,
                            res2_points int,
                            res2_unit text,
                            res3_name text,
                            res3_min int,
                            res3_max int,
                            res3_prec int,
                            res3_tol int,
                            res3_points int,
                            res3_unit text,
                            res4_name text,
                            res4_min int,
                            res4_max int,
                            res4_prec int,
                            res4_tol int,
                            res4_points int,
                            res4_unit text,
                            res5_name text,
                            res5_min int,
                            res5_max int,
                            res5_prec int,
                            res5_tol int,
                            res5_points int,
                            res5_unit text,
                            res6_name text,
                            res6_min int,
                            res6_max int,
                            res6_prec int,
                            res6_tol int,
                            res6_points int,
                            res6_unit text,
                            res7_name text,
                            res7_min int,
                            res7_max int,
                            res7_prec int,
                            res7_tol int,
                            res7_points int,
                            res7_unit text,
                            res8_name text,
                            res8_min int,
                            res8_max int,
                            res8_prec int,
                            res8_tol int,
                            res8_points int,
                            res8_unit text,
                            res9_name text,
                            res9_min int,
                            res9_max int,
                            res9_prec int,
                            res9_tol int,
                            res9_points int,
                            res9_unit text,
                            res10_name text,
                            res10_min int,
                            res10_max int,
                            res10_prec int,
                            res10_tol int,
                            res10_points int,
                            res10_unit text,
                            
                            
                            perm_var_symbol_1 text,
                            perm_var_value_1 text,
                            perm_var_symbol_2 text,
                            perm_var_value_2 text,
                            perm_var_symbol_3 text,
                            perm_var_value_3 text,
                            perm_var_symbol_4 text,
                            perm_var_value_4 text,
                            perm_var_symbol_5 text,
                            perm_var_value_5 text,
                            perm_var_symbol_6 text,
                            perm_var_value_6 text,
                            perm_var_symbol_7 text,
                            perm_var_value_7 text,
                            perm_var_symbol_8 text,
                            perm_var_value_8 text,
                            perm_var_symbol_9 text,
                            perm_var_value_9 text,
                            perm_var_symbol_10 text,
                            perm_var_value_10 text,
                            
                            
                            description_img_name_1 text,
                            description_img_data_1 blop,
                            description_img_path_1 text,
                            
                            description_img_name_2 text,
                            description_img_data_2 blop,
                            description_img_path_2 text,
                            
                            description_img_name_3 text,
                            description_img_data_3 blop,
                            description_img_path_3 text,
                            
                            test_time text,
                            var_number int,
                            res_number int,
                            question_pool_tag text,
                            question_author text,
                            date text
                            )""")


        mydb.commit()

        cursor.execute("""CREATE TABLE IF NOT EXISTS testeinstellungen (
                            entry_description text,
                            radio_select_question text,
                            type text,
                            profile_name text,
                            radio_select_anonymous text,
                            check_online int,
                            check_time_limited int,
                            check_introduction int,
                            entry_introduction text,
                            check_test_properties int,
                            entry_test_start_year text,
                            entry_test_start_month text,
                            entry_test_start_day text,
                            entry_test_start_hour text,
                            entry_test_start_minute text,
                            entry_test_end_year text,
                            entry_test_end_month text,
                            entry_test_end_day text,
                            entry_test_end_hour text,
                            entry_test_end_minute text,
                            entry_test_password text,
                            check_specific_users int,
                            entry_limit_unsers text,
                            entry_unser_inactivity text,
                            entry_limit_test_runs text,
                            entry_limit_time_betw_test_run_month text,
                            entry_limit_time_betw_test_run_day text,
                            entry_limit_time_betw_test_run_hour text,
                            entry_limit_time_betw_test_run_minute text,
                            check_processing_time int,
                            entry_processing_time_in_minutes text,
                            check_processing_time_reset int,
                            check_examview int,
                            check_examview_title int,
                            check_examview_username int,
                            check_show_ilias_nr int,
                            radio_select_show_question_title text,
                            check_autosave int,
                            entry_autosave text,
                            entry_autosave_interval text,
                            check_mix_questions int,
                            check_show_solutions_notes int,
                            check_direct_response int,
                            radio_select_user_response text,
                            check_mandatory_questions int,
                            check_use_previous_solution int,
                            check_show_test_cancel int,
                            radio_select_not_answered_questions text,
                            check_show_question_list_process_status int,
                            check_question_mark int,
                            check_overview_answers int,
                            check_show_end_comment int,
                            entry_end_comment text,
                            check_forwarding text,
                            check_notification text,
                            title_entry
                            )""")
        mydb.commit()

if __name__ == "__main__":
    #Wenn diese Datei ausgeführt wird werden zwei leere Datenbanken erstellt
    db = generate_db('generaldb.db')
    db = generate_db('Zwischenspeicher_Datenbank.db')