
from tkinter import *
from tkscrolledframe import ScrolledFrame
import os
import pathlib
import xml.etree.ElementTree as ET

class TAX_Interface():
    def __init__(self, bg_color, button_color, label_color, Button_Font, Label_Font):
         self.bg_color = bg_color
         self.button_color = button_color
         self.label_color = label_color
         self.Button_Font = Button_Font
         self.Label_Font = Label_Font




    def open_tax_window(self):

         # Fragenpool auswählen
        self.select_taxonomy_file = filedialog.askdirectory(initialdir=pathlib.Path().absolute(), title="Select a File")


        self.folder_name = self.select_taxonomy_file.rsplit('/', 1)[-1]
        self.folder_name_split1 = self.folder_name[:15]
        self.folder_name_split2 = self.folder_name.rsplit('_', 1)[-1]

        self.taxonomy_exportXML_file = os.path.normpath(os.path.join(self.select_taxonomy_file, 'Services', 'Taxonomy', 'set_1', 'export.xml'))
        self.taxonomy_file_write = self.taxonomy_exportXML_file

        self.taxonomy_qtiXML_file = os.path.normpath(os.path.join(self.select_taxonomy_file, self.folder_name_split1 + "qti_" + self.folder_name_split2 + ".xml"))
        self.taxonomy_file_read = os.path.normpath(os.path.join(self.select_taxonomy_file, 'Services', 'Taxonomy', 'set_1', 'export.xml'))



        # Taxonomy-window
        self.taxonomy_width = 1000
        self.taxonomy_height = 800

        ### Neues Fenster "Taxonomie" erzeugen

        # New Window must be "Toplevel" not "Tk()" in order to get Radiobuttons to work properly
        self.taxonomy_window = Toplevel()
        self.taxonomy_window.title("Taxonomie  --- " + str(self.select_taxonomy_file))

        ### Frame
        # Create a ScrolledFrame widget
        self.sf_taxonomy = ScrolledFrame(self.taxonomy_window, width=self.taxonomy_width, height=self.taxonomy_height)
        self.sf_taxonomy.pack(expand=1, fill="both")

        # Create a frame within the ScrolledFrame
        self.taxonomy = self.sf_taxonomy.display_widget(Frame)

        self.taxonomy_frame_labels_scroll= LabelFrame(self.taxonomy, text="Fragen ID's", padx=5, pady=5)
        self.taxonomy_frame_labels_scroll.grid(row=0, column=0, padx=20, pady=10, sticky=NW)
        self.taxonomy_frame_labels2 = ScrolledFrame(self.taxonomy_frame_labels_scroll, height=700, width=500)
        self.taxonomy_frame_labels2.pack(expand=1, fill="both")
        self.taxonomy_frame_labels = self.taxonomy_frame_labels2.display_widget(Frame)


        self.taxonomy_frame_boxes = LabelFrame(self.taxonomy, text="Fragen ID's", padx=5, pady=5)
        self.taxonomy_frame_boxes.grid(row=0, column=1, padx=20, pady=10, sticky=NW)

        self.taxonomy_frame_tree = LabelFrame(self.taxonomy, text="Taxonomie Baum", padx=5, pady=5)
        self.taxonomy_frame_tree.grid(row=0, column=1, padx=20, pady=200, sticky=NW)


        ### LABELS UND ENTRYIES
        # ---- Starting ID to End ID set to node
        self.label_starting_id = Label(self.taxonomy_frame_boxes, text="von Fragen ID")
        self.label_starting_id.grid(sticky=W, pady=5, row=0, column=0)

        self.starting_id_var = StringVar()
        self.ending_id_var = StringVar()

        self.taxonomy_name = StringVar()
        self.tax_node_name = StringVar()
        self.tax_node_parent = StringVar()

        self.entry_starting_id = Entry(self.taxonomy_frame_boxes, textvariable=self.starting_id_var, width=10)
        self.entry_starting_id.grid(sticky=W, pady=5, row=1, column=0)


        self.label_ending_id = Label(self.taxonomy_frame_boxes, text="bis Fragen ID")
        self.label_ending_id.grid(sticky=W, padx=10, pady=5, row=0, column=1)

        self.entry_ending_id = Entry(self.taxonomy_frame_boxes, textvariable=self.ending_id_var, width=10)
        self.entry_ending_id.grid(sticky=W, padx=10, pady=5, row=1, column=1)



        self.taxonomy_name_label = Label(self.taxonomy_frame_tree, text="Name für Taxonomie")
        self.taxonomy_name_label.grid(sticky=W, padx=10, pady=5, row=0, column=0)
        self.taxonomy_name_entry = Entry(self.taxonomy_frame_tree, textvariable=self.taxonomy_name, width=20)
        self.taxonomy_name_entry.grid(sticky=W, padx=10, pady=5, row=0, column=1)


        self.tax_node_name_label = Label(self.taxonomy_frame_tree, text="Name für Knoten")
        self.tax_node_name_label.grid(sticky=W, padx=10, pady=5, row=1, column=0)
        self.tax_node_name_entry = Entry(self.taxonomy_frame_tree, textvariable=self.tax_node_name, width=20)
        self.tax_node_name_entry.grid(sticky=W, padx=10, pady=5, row=1, column=1)

        self.tax_node_parent_label = Label(self.taxonomy_frame_tree, text="Vaterknoten")
        self.tax_node_parent_label.grid(sticky=W, padx=10, pady=5, row=2, column=0)
        self.tax_node_parent_entry = Entry(self.taxonomy_frame_tree, textvariable=self.tax_node_parent, width=20)
        self.tax_node_parent_entry.grid(sticky=W, padx=10, pady=5, row=2, column=1)


        #### BUTTONS
        # Button to assign questions to node
        self.assign_to_node_btn = Button(self.taxonomy_frame_boxes, text="Fragen dem Knoten\nhinzufügen", command=lambda: TAX_Interface.assign_questions_to_node(self))
        self.assign_to_node_btn.grid(row=4, column=0, sticky=W, pady=(20, 0))

        self.remove_from_node_btn = Button(self.taxonomy_frame_boxes, text="Fragen von Knoten\nentfernen",command=lambda: TAX_Interface.remove_question_from_node(self))
        self.remove_from_node_btn.grid(row=4, column=1, sticky=W, padx=5, pady=(20, 0))

        self.tax_add_node_btn = Button(self.taxonomy_frame_tree, text="Knoten hinzufügen",command=lambda: TAX_Interface.add_node_to_tax(self))
        self.tax_add_node_btn.grid(row=6, column=0, sticky=W, padx=5, pady=(20, 0))

        #self.scan_tax_tree_btn = Button(self.taxonomy_frame_tree, text="scan_tax_tree",command=lambda: Taxonomie.scan_tax_tree(self))
        #self.scan_tax_tree_btn.grid(row=6, column=1, sticky=W, padx=5, pady=(20, 0))

        self.update_taxonomy_name_btn = Button(self.taxonomy_frame_tree, text="Taxonomie-Namen\naktualisieren", command=lambda: TAX_Interface.update_taxonomy_name(self))
        self.update_taxonomy_name_btn.grid(row=0, column=2, sticky=E, padx=5, pady=(5, 0))

        self.tax_remove_node_btn = Button(self.taxonomy_frame_tree, text="Knoten entfernen",command=lambda: TAX_Interface.remove_node_from_tax(self))
        self.tax_remove_node_btn.grid(row=6, column=1, sticky=W, padx=5, pady=(20, 0))

        self.tax_reallocate_btn = Button(self.taxonomy_frame_tree, text="Taxonomie-Datei\nneu anordnen",command=lambda: TAX_Interface.tax_reallocate(self))
        self.tax_reallocate_btn.grid(row=5, column=2, sticky=W, padx=5, pady=(20, 0))


    def edit_tax_of_existing_ilias_pool_file(self):

        TAX_Interface.open_tax_window(self)
        TAX_Interface.tax_file_refresh(self, self.taxonomy_exportXML_file)

        TAX_Interface.read_taxonomy_file(self)
        TAX_Interface.scan_tax_tree(self)


    def read_taxonomy_file(self):

         #self.taxonomy_qtiXML_file = taxonomy_qtiXML_file
         print("read")
         print(self.taxonomy_qtiXML_file)
         self.mytree = ET.parse(self.taxonomy_qtiXML_file)
         self.myroot = self.mytree.getroot()

         self.item_id_list = []
         self.item_title_list = []
         self.item_id_var = 0
         self.item_title_var = 0
         self.item_labels_list = []
         self.combobox_list = []

         for item in self.myroot.iter('item'):
             self.item_id_raw = str(item.get('ident'))
             self.item_id = self.item_id_raw.rsplit('_', 1)[-1]
             self.item_title = str(item.get('title'))
             self.item_id_list.append(self.item_id)
             self.item_title_list.append(self.item_title)

         # print(len(self.ident))

         for id_text in self.item_id_list:
             label_id = Label(self.taxonomy_frame_labels, text=id_text)
             label_id.grid(sticky=W, pady=5, row=self.item_id_var, column=0)
             self.item_labels_list.append(str(label_id.cget("text")))
             print("Label ID: " + str(label_id.cget("text")))

             label_placeholder = Label(self.taxonomy_frame_labels, text=" ---- ")
             label_placeholder.grid(sticky=W, pady=5, row=self.item_id_var, column=1)

             self.item_id_var = self.item_id_var + 1

         for title_text in self.item_title_list:
             label_title = Label(self.taxonomy_frame_labels, text=title_text)
             label_title.grid(sticky=W, pady=5, row=self.item_title_var, column=2)
             self.item_title_var = self.item_title_var + 1

         ##### - Taxonomie Ebenen auslesen - ####
         print("\n")
         print("---- Taxonomie auslesen")
         self.mytree = ET.parse(self.taxonomy_file_read)
         self.myroot = self.mytree.getroot()

         self.tax_title = []
         self.child_tag = []
         self.node_tag = []
         self.item_in_node = []
         self.item_tag = []
         self.root_node = "000000"
         self.id_to_node_dict = {}
         self.item_nr_list = []

         # Auslesen der Root-ID    Diese ID gibt den "Hauptstamm" der Taxonomie an
         # Root-ID wird vorher auf "000000" gesetzt um zu prüfen ob der Wert im nächsten Schritt überschrieben wurde
         for Tax in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Tax'):
             self.root_node = Tax.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Id').text

             if self.root_node != "000000":
                 print("Root Node found: " + str(self.root_node))
             else:
                 print("No Root ID in File!")

         # ---- Alle Ebenen im Dokument suchen ---- #
         for TaxTree in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}TaxTree'):
             if TaxTree.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}TaxId').text == str(self.root_node):
                 self.child_tag.append(TaxTree.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Child').text)
                 self.node_tag.append(TaxTree.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Title').text)

         print("Nodes found: " + str(self.node_tag))
         print("with Child ID: " + str(self.child_tag))

         # convert list "child tag" and list "node_tag" to dictionary
         self.id_to_node_dict = dict(zip(self.child_tag, self.node_tag))
         self.node_to_id_dict = dict(zip(self.node_tag, self.child_tag))
         # print(self.id_to_node_dict)
         print("------------------------------------------------")

         print("\n")
         # print("------- Show Question assignments -------")
         for i in range(len(self.child_tag)):
             for tax_node in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}TaxNodeAssignment'):
                 if tax_node.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}NodeId').text == str(
                         self.child_tag[i]):  # Bsp. für Ebene 1 ID
                     self.item_in_node.append(str(self.child_tag[i]))
                     self.item_tag.append(
                         tax_node.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}ItemId').text)
                     self.item_nr_list.append(self.item_labels_list.index(
                         tax_node.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}ItemId').text))

         for i in range(len(self.item_nr_list)):
             label_taxnode = Label(self.taxonomy_frame_labels,
                                   text=" --- " + str(self.id_to_node_dict.get(self.item_in_node[i])))
             label_taxnode.grid(sticky=W, pady=5, row=self.item_labels_list.index(self.item_tag[i]), column=4)

         # PRüfen ob die Fragen im Fragenpool konsistent sind (fortlaufende ID's
         self.check_question_id_start = str(self.item_labels_list[0])
         self.check_question_id_end = str(self.item_labels_list[len(self.item_labels_list) - 1])
         self.check_question_id_counter = int(self.check_question_id_start)

         # for i in range(len(self.item_labels_list)):
         #    if int(self.item_labels_list[i]) != int(self.check_question_id_counter):
         #        print("Error in Labels list", self.item_labels_list[i], self.check_question_id_counter)

         #    self.check_question_id_counter = self.check_question_id_counter + 1
         # print("Label-check DONE")

         TAX_Interface.tax_combobox_refresh(self)

    def tax_combobox_refresh (self):

        # ---- Alle Ebenen im Dokument suchen ---- #
        self.node_tag_update = []

        for TaxTree in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}TaxTree'):
            if TaxTree.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}TaxId').text == str(self.root_node):
                self.node_tag_update.append(TaxTree.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Title').text)



        self.node_tag_update.sort(key=str.lower)


        self.tax_nodes_myCombo = ttk.Combobox(self.taxonomy_frame_boxes, value=self.node_tag_update, width=30)
        self.tax_nodes_myCombo.current(0)
        # self.tax_nodes_myCombo.bind("<<ComboboxSelected>>", selected_var)
        self.tax_nodes_myCombo.grid(row=1, column=2, sticky=W, padx=10, pady=5)

    def tax_file_refresh(self, file_location):

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

    def scan_tax_tree(self):
        self.mytree = ET.parse(self.taxonomy_file_read)
        self.myroot = self.mytree.getroot()

        self.taxonomy_frame_tree_picture_scroll = LabelFrame(self.taxonomy, text="Taxonomie Bild", padx=5, pady=5)
        self.taxonomy_frame_tree_picture_scroll.grid(row=0, column=1, padx=20, pady=450, sticky=NW)


        self.taxonomy_frame_tree_picture2 = ScrolledFrame(self.taxonomy_frame_tree_picture_scroll, height=250, width=200)
        self.taxonomy_frame_tree_picture2.pack(expand=1, fill="both")

        ### Bind the arrow keys and scroll wheel
        ### Funktion hat keine auswirkungen, erzeugt jedoch (vernachlässigbare) Fehler
        #self.taxonomy_frame_tree_picture2.bind_arrow_keys(app)
        #self.taxonomy_frame_tree_picture2.bind_scroll_wheel(app)
        self.taxonomy_frame_tree_picture = self.taxonomy_frame_tree_picture2.display_widget(Frame)

        self.collect_childs = []
        self.collect_title = []
        self.collect_depth = []
        self.collect_parent = []
        self.collect_order_nr = []
        self.collect_labels_sorted = []

        self.tax_data = []
        self.id_to_depth_dict = {}
        self.parentId_to_title_dict = {}
        self.parentId_from_id_dict = {}
        self.title_to_id_dict = {}


        # Taxonomie Datei nach Hauptebene (ID und Name) suchen
        for TaxId in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Tax'):
            if TaxId.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Id').text == str(self.root_node):
                self.tax_root_id = TaxId.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Id').text
                self.tax_root_label = TaxId.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Title').text

               #print(self.parentId_to_title_dict)


        for child in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Child'):
             self.collect_childs.append(child.text)

        for parent in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Parent'):
             self.collect_parent.append(parent.text)

        for depth in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Depth'):
             self.collect_depth.append(depth.text)

        for title in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Title'):
             self.collect_title.append(title.text)
             #print(title.text)
        for order_nr in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}OrderNr'):
             self.collect_order_nr.append(order_nr.text)








        self.tax_data =  list(zip( self.collect_childs, self.collect_parent, self.collect_depth, self.collect_title, self.collect_order_nr  ))



        # .pop(0) enfternt den 1. Eintrag aus der Liste. In Liste "Title" ist 1 Eintrag mehr enthalten, als in den restlichen Listen. Der Eintrag beschreibt den Taxonomie-Namen
        self.collect_title.pop(0)
        self.id_to_depth_dict = dict(zip(self.collect_childs, self.collect_depth))
        self.id_to_title_dict = dict(zip(self.collect_childs, self.collect_title))
        self.parentId_from_id_dict = dict(zip(self.collect_childs, self.collect_parent))




        # Bild in Labels erstellen
        self.tax_depth_0_label = Label(self.taxonomy_frame_tree_picture, text=str(self.tax_root_label))
        self.tax_depth_0_label.grid(sticky=W)


        # collect_title muss "i+1" da im '0'ten Fach der Hauptitel ist. Title[] ist 1 Fach größer als Child[]
        for i in range(len(self.collect_childs)):
            #print(self.collect_parent[i], self.collect_childs[i],self.id_to_depth_dict.get(self.collect_childs[i]), self.collect_title[i], self.collect_order_nr[i])


            if self.id_to_depth_dict.get(self.collect_childs[i]) == "2":
                self.tax_depth_1_label= Label(self.taxonomy_frame_tree_picture, text="     " + str(self.collect_title[i]))
                #self.tax_depth_1_label.grid(sticky=W)
                self.collect_labels_sorted.append(self.tax_depth_1_label.cget("text"))

            if self.id_to_depth_dict.get(self.collect_childs[i]) == "3":
                self.tax_depth_2_label = Label(self.taxonomy_frame_tree_picture, text="         " + str(self.id_to_title_dict.get(self.collect_parent[i])) + "   ===>   " + str(self.collect_title[i]))
                #self.tax_depth_2_label.grid(sticky=W)
                self.collect_labels_sorted.append(self.tax_depth_2_label.cget("text"))

            if self.id_to_depth_dict.get(self.collect_childs[i]) == "4":
                self.tax_depth_3_label = Label(self.taxonomy_frame_tree_picture, text="            " + str(self.id_to_title_dict.get(self.parentId_from_id_dict.get(self.collect_parent[i])))+ "  ===>    " +str(self.id_to_title_dict.get(self.collect_parent[i]))+ "   ===>   " + str(self.collect_title[i]))
                #self.tax_depth_3_label.grid(sticky=W)
                self.collect_labels_sorted.append(self.tax_depth_3_label.cget("text"))



        for i in range(len(self.collect_labels_sorted)):
            self.collect_labels_sorted[i] = self.collect_labels_sorted[i].strip()

        self.collect_labels_sorted.sort()


        for i in range(len(self.collect_labels_sorted)):

            self.depth_count = "0"
            self.depth_count = self.collect_labels_sorted[i].count("==>")

            if self.depth_count == 0:
                self.sorted_labels = Label(self.taxonomy_frame_tree_picture, text="     " + self.collect_labels_sorted[i])
                self.sorted_labels.grid(sticky=W)

            if self.depth_count == 1:
                self.sorted_labels = Label(self.taxonomy_frame_tree_picture, text="         " + self.collect_labels_sorted[i])
                self.sorted_labels.grid(sticky=W)

            if self.depth_count == 2:
                self.sorted_labels = Label(self.taxonomy_frame_tree_picture, text="            " + self.collect_labels_sorted[i])
                self.sorted_labels.grid(sticky=W)

    def update_taxonomy_name(self):
        self.mytree = ET.parse(self.taxonomy_file_read)
        self.myroot = self.mytree.getroot()

        if self.taxonomy_name_entry.get != "":

            # Auslesen der Root-ID    Diese ID gibt den "Hauptstamm" der Taxonomie an
            # Root-ID wird vorher auf "000000" gesetzt um zu prüfen ob der Wert im nächsten Schritt überschrieben wurde
            for Tax in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Tax'):
                Tax.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Title').text = self.taxonomy_name_entry.get()

                if self.root_node != "000000":
                    print("Root Node found: " + str(self.root_node))
                else:
                    print("No Root ID in File!")

        self.mytree.write(self.taxonomy_file_write)

        # Taxonomie-datei "refreshen"
        TAX_Interface.tax_file_refresh(self, self.taxonomy_exportXML_file)

        self.taxonomy_frame_tree_picture.destroy()
        TAX_Interface.scan_tax_tree(self)


    def add_node_to_tax(self):
        self.mytree = ET.parse(self.taxonomy_file_read)
        self.myroot = self.mytree.getroot()

        self.collect_childs = []
        self.collect_title = []
        self.collect_depth = []
        self.collect_parent = []
        self.collect_order_nr = []


        for child in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Child'):
             self.collect_childs.append(child.text)

        for parent in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Parent'):
             self.collect_parent.append(parent.text)

        for depth in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Depth'):
             self.collect_depth.append(depth.text)

        for title in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Title'):
             self.collect_title.append(title.text)

        for order_nr in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}OrderNr'):
             self.collect_order_nr.append(order_nr.text)

        # Taxonomie Datei nach Hauptebene (ID und Name) suchen
        for TaxId in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Tax'):
            if TaxId.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Id').text == "1970392":
                self.tax_root_id = TaxId.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Id').text



        self.collect_title.pop(0)
        self.title_to_id_dict = {}
        self.title_to_id_dict = dict(zip(self.collect_title, self.collect_childs))

        self.title_to_depth_dict = {}
        self.title_to_depth_dict = dict(zip(self.collect_title, self.collect_depth))



        Export = ET.Element('exp:Export')
        ExportItem = ET.SubElement(Export, 'exp:ExportItem')
        DataSet = ET.SubElement(ExportItem, 'ds:DataSet')
        Rec = ET.SubElement(DataSet, 'ds:Rec')
        TaxTree = ET.SubElement(Rec, 'TaxTree')
        TaxId = ET.SubElement(TaxTree, 'TaxId')
        Child = ET.SubElement(TaxTree, 'Child')
        Parent = ET.SubElement(TaxTree, 'Parent')
        Depth = ET.SubElement(TaxTree, 'Depth')
        Type = ET.SubElement(TaxTree, 'Type')
        Title = ET.SubElement(TaxTree, 'Title')
        OrderNr = ET.SubElement(TaxTree, 'OrderNr')

        Rec.set('Entity', "tax_tree")



        TaxId.text = str(self.tax_root_id)
        Child.text = str(int(max(self.collect_childs))+1)

        if self.tax_node_parent_entry.get() == "":
            Parent.text = str(min(self.collect_childs))
            Depth.text = str(int(min(self.collect_depth)) + 1 )
            if Depth.text == "1":
                Type.text = ""
                OrderNr.text = str(int(max(self.collect_order_nr)) + 1)   #Änderung min() auf max()
            else:
                Type.text = "taxn"  # fix
                Title.text = str(self.tax_node_name_entry.get())
                OrderNr.text = str(int(max(self.collect_order_nr)) + 1)


        else:
            Parent.text = str(self.title_to_id_dict.get(self.tax_node_parent_entry.get()))
            Depth.text = str(int(self.title_to_depth_dict.get(self.tax_node_parent_entry.get())) + 1)
            Type.text = "taxn"  # fix
            Title.text = str(self.tax_node_name_entry.get())
            OrderNr.text = str(int(max(self.collect_order_nr))+1)

        self.myroot.append(ExportItem)
        self.mytree.write(self.taxonomy_file_write)

        # Taxonomie-datei "refreshen"
        TAX_Interface.tax_file_refresh(self, self.taxonomy_exportXML_file)

        self.taxonomy_frame_tree_picture.destroy()
        TAX_Interface.scan_tax_tree(self)


        self.tax_nodes_myCombo.destroy()
        TAX_Interface.tax_combobox_refresh(self)

    def add_node_to_tax_from_excel(self, file_location, new_node_name, parent_node_name):



        self.taxonomy_export_file = file_location
        TAX_Interface.tax_file_refresh(self, self.taxonomy_export_file)

        self.mytree = ET.parse(self.taxonomy_export_file)
        self.myroot = self.mytree.getroot()

        self.collect_childs = []
        self.collect_title = []
        self.collect_depth = []
        self.collect_parent = []
        self.collect_order_nr = []


        for child in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Child'):
             self.collect_childs.append(child.text)

        for parent in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Parent'):
             self.collect_parent.append(parent.text)

        for depth in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Depth'):
             self.collect_depth.append(depth.text)

        for title in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Title'):
             self.collect_title.append(title.text)

        for order_nr in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}OrderNr'):
             self.collect_order_nr.append(order_nr.text)

        #print(self.collect_order_nr)

        # Taxonomie Datei nach Hauptebene (ID und Name) suchen
        for TaxId in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Tax'):
            if TaxId.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Id').text == "1970392":
                self.tax_root_id = TaxId.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Id').text



        self.collect_title.pop(0)
        self.title_to_id_dict = {}
        self.title_to_id_dict = dict(zip(self.collect_title, self.collect_childs))

        self.title_to_depth_dict = {}
        self.title_to_depth_dict = dict(zip(self.collect_title, self.collect_depth))


        #for i in range(len(self.collect_title)):
         #   print(self.collect_childs[i], self.collect_title[i], self.collect_depth[i], self.collect_parent[i], self.collect_order_nr[i])

        Export = ET.Element('exp:Export')
        ExportItem = ET.SubElement(Export, 'exp:ExportItem')
        DataSet = ET.SubElement(ExportItem, 'ds:DataSet')
        Rec = ET.SubElement(DataSet, 'ds:Rec')
        TaxTree = ET.SubElement(Rec, 'TaxTree')
        TaxId = ET.SubElement(TaxTree, 'TaxId')
        Child = ET.SubElement(TaxTree, 'Child')
        Parent = ET.SubElement(TaxTree, 'Parent')
        Depth = ET.SubElement(TaxTree, 'Depth')
        Type = ET.SubElement(TaxTree, 'Type')
        Title = ET.SubElement(TaxTree, 'Title')
        OrderNr = ET.SubElement(TaxTree, 'OrderNr')

        Rec.set('Entity', "tax_tree")



        TaxId.text = str(self.tax_root_id)
        Child.text = str(int(max(self.collect_childs))+1)

        # Wenn kein "Parent"-Node existiert
        if parent_node_name == "EMPTY":
            Parent.text = str(min(self.collect_childs))
            Depth.text = str(int(min(self.collect_depth)) + 1)
            if Depth.text == "1":
                Type.text = ""
                OrderNr.text = str(int(max(self.collect_order_nr)) + 1)   #Änderung min() auf max()
                #print("ORderNr: " + OrderNr.text)
            else:
                Type.text = "taxn"  # fix
                Title.text = str(new_node_name)
                OrderNr.text = str(int(max(self.collect_order_nr)) + 1)
                #print("ORderNr: " + OrderNr.text)

        else:
            Parent.text = str(self.title_to_id_dict.get(parent_node_name))
            Depth.text = str(int(self.title_to_depth_dict.get(parent_node_name)) + 1)
            Type.text = "taxn"  # fix
            Title.text = str(new_node_name)
            OrderNr.text = str(int(max(self.collect_order_nr))+1)

        self.myroot.append(ExportItem)
        self.mytree.write(self.taxonomy_export_file)

        # Taxonomie-datei "refreshen"
        TAX_Interface.tax_file_refresh(self, self.taxonomy_export_file)


    def assign_questions_to_node(self):
        self.mytree = ET.parse(self.taxonomy_file_read)
        self.myroot = self.mytree.getroot()

        self.node_to_id_dict = {}
        self.child_tag_assign = []
        self.node_tag_assign = []

        # ---- Alle Ebenen im Dokument suchen ---- #
        for TaxTree in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}TaxTree'):
            if TaxTree.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}TaxId').text == str(self.root_node):
                self.child_tag_assign.append(TaxTree.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Child').text)
                self.node_tag_assign.append(TaxTree.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Title').text)

        print("Nodes found: " + str(self.node_tag))
        print("with Child ID: " + str(self.child_tag))

        # convert list "child tag" and list "node_tag" to dictionary
        self.node_to_id_dict = dict(zip(self.node_tag_assign, self.child_tag_assign))
        print("------------------------------------------------")

        # Export XML-File
        # xmlns:ns0="http://www.ilias.de/Services/Export/exp/4_1"
        # xmlns:ns2="http://www.ilias.de/Services/DataSet/ds/4_3"
        # xmlns:ns3="http://www.ilias.de/Services/Taxonomy/tax/4_3"
        # xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" InstallationId="0" InstallationUrl="https://ilias.th-koeln.de" Entity="tax" SchemaVersion="4.3.0" TargetRelease="5.4.0" xsi:schemaLocation="http://www.ilias.de/Services/Export/exp/4_1 https://ilias.th-koeln.de/xml/ilias_export_4_1.xsd http://www.ilias.de/Services/Taxonomy/tax/4_3 https://ilias.th-koeln.de/xml/ilias_tax_4_3.xsd http://www.ilias.de/Services/DataSet/ds/4_3 https://ilias.th-koeln.de/xml/ilias_ds_4_3.xsd">
        # Bsp: tax_node.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}ItemId').text)

        # -------- Struktur einer "assignment to node" in der XML
        # < ds: Rec Entity = "tax_node_assignment" >
        #    < TaxNodeAssignment >
        #        < NodeId > 21682 < / NodeId >
        #        < Component > qpl < / Component >
        #        < ItemType > quest < / ItemType >
        #        < ItemId > 470081 < / ItemId >
        #    < / TaxNodeAssignment >
        # < / ds: Rec >


        if self.entry_starting_id.get() != "" and self.entry_ending_id.get() != "":
            self.starting_id = int(self.entry_starting_id.get()[:6])
            self.ending_id = int(self.entry_ending_id.get()[:6])

            for i in range(self.starting_id, self.ending_id+1):
                for tax_node in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}TaxNodeAssignment'):
                    if tax_node.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}ItemId').text == str(i):
                        print("ID found: " + str(i))



        if self.node_to_id_dict.get(self.tax_nodes_myCombo.get()) != self.child_tag[0]:
            if self.entry_starting_id.get() != "" and self.entry_ending_id.get() != "":

                for i in range(self.starting_id, self.ending_id+1):
                    # Die Definition der Haupt- und Sub-Elemente muss in der Schleife für jede Frage neu erstellt werden
                    # Sonst haben die angehängten Fragen alle die gleichen Werte, da es sich auf das Gleiche "Attribut" handelt
                    Export = ET.Element('exp:Export')
                    ExportItem = ET.SubElement(Export, 'exp:ExportItem')
                    DataSet = ET.SubElement(ExportItem, 'ds:DataSet')
                    Rec = ET.SubElement(DataSet, 'ds:Rec')
                    TaxNodeAssignment = ET.SubElement(Rec, 'TaxNodeAssignment')
                    NodeId = ET.SubElement(TaxNodeAssignment, 'NodeId')
                    Component = ET.SubElement(TaxNodeAssignment, 'Component')
                    ItemType = ET.SubElement(TaxNodeAssignment, 'ItemType')
                    ItemId = ET.SubElement(TaxNodeAssignment, 'ItemId')


                    #Rec = ET.SubElement(DataSet, 'ds:Rec')
                    Rec.set('Entity', "tax_node_assignment")
                    #ItemId = ET.SubElement(TaxNodeAssignment, 'ItemId')

                    NodeId.text = self.node_to_id_dict.get(self.tax_nodes_myCombo.get())

                    Component.text = "qpl"  # fix
                    ItemType.text = "quest" # fix
                    ItemId.text = str(i)     # Fragen ID üblicherweise > 100000, wenn Fragen ID z.B. 000001 dann ist der itemValue "nur" 1 und es fehlen nullen
                    self.myroot[0][len(self.myroot[0]) - 1].append(Rec)

                    #print("NodeId: " + NodeId.text)
                    #print("ItemId: " + ItemId.text)

                    self.mytree.write(self.taxonomy_file_write)

            else:
                print("Need starting/ending ID")
        else:
            print("Node for Questions not selected")


        # Taxonomie-datei "refreshen"
        TAX_Interface.tax_file_refresh(self, self.taxonomy_exportXML_file)


         # Taxonomie Fesnter wird "refreshed" um Text der Labels zu aktualisieren
        self.taxonomy_frame_labels.destroy()

        self.taxonomy_frame_labels_scroll= LabelFrame(self.taxonomy, text="Question ID's", padx=5, pady=5)
        self.taxonomy_frame_labels_scroll.grid(row=0, column=0, padx=20, pady=10, sticky=NW)
        self.taxonomy_frame_labels2 = ScrolledFrame(self.taxonomy_frame_labels_scroll, height=700, width=500)
        self.taxonomy_frame_labels2.pack(expand=1, fill="both")
        #self.taxonomy_frame_labels2.bind_arrow_keys(app)
        #self.taxonomy_frame_labels2.bind_scroll_wheel(app)
        self.taxonomy_frame_labels = self.taxonomy_frame_labels2.display_widget(Frame)

        #self.taxonomy_frame_labels = LabelFrame(self.taxonomy, text="Question ID's", padx=5, pady=5)
        #self.taxonomy_frame_labels.grid(row=0, column=0, padx=20, pady=10, sticky=NW)

        TAX_Interface.read_taxonomy_file(self)

    def assign_questions_to_node_from_excel(self, file_location, item_id, item_pool):

        self.taxonomy_export_file = file_location



        # Fragen einem Knoten hinzufügen
        self.mytree = ET.parse(self.taxonomy_export_file)
        self.myroot = self.mytree.getroot()

        self.node_to_id_dict = {}
        self.child_tag_assign = []
        self.node_tag_assign = []
        self.child_tag = []
        self.node_tag = []


        # Auslesen der Root-ID    Diese ID gibt den "Hauptstamm" der Taxonomie an
        # Root-ID wird vorher auf "000000" gesetzt um zu prüfen ob der Wert im nächsten Schritt überschrieben wurde
        self.root_node = "000000"
        for Tax in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Tax'):
                self.root_node = Tax.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Id').text

                #if self.root_node != "000000":
                #    print("Root Node found: " + str(self.root_node))
                #else:
                #    print("No Root ID in File!")


        # ---- Alle Ebenen im Dokument suchen ---- #
        for TaxTree in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}TaxTree'):
            if TaxTree.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}TaxId').text == str(self.root_node):
                self.child_tag.append(TaxTree.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Child').text)
                self.node_tag.append(TaxTree.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Title').text)


        # ---- Alle Ebenen im Dokument suchen ---- #
        for TaxTree in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}TaxTree'):
            if TaxTree.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}TaxId').text == str(self.root_node):
                self.child_tag_assign.append(TaxTree.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Child').text)
                self.node_tag_assign.append(TaxTree.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Title').text)

        #print("Nodes found: " + str(self.node_tag))
        #print("with Child ID: " + str(self.child_tag))

        # convert list "child tag" and list "node_tag" to dictionary
        self.node_to_id_dict = dict(zip(self.node_tag_assign, self.child_tag_assign))
        #print("------------------------------------------------")

        # Export XML-File
        # xmlns:ns0="http://www.ilias.de/Services/Export/exp/4_1"
        # xmlns:ns2="http://www.ilias.de/Services/DataSet/ds/4_3"
        # xmlns:ns3="http://www.ilias.de/Services/Taxonomy/tax/4_3"
        # xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" InstallationId="0" InstallationUrl="https://ilias.th-koeln.de" Entity="tax" SchemaVersion="4.3.0" TargetRelease="5.4.0" xsi:schemaLocation="http://www.ilias.de/Services/Export/exp/4_1 https://ilias.th-koeln.de/xml/ilias_export_4_1.xsd http://www.ilias.de/Services/Taxonomy/tax/4_3 https://ilias.th-koeln.de/xml/ilias_tax_4_3.xsd http://www.ilias.de/Services/DataSet/ds/4_3 https://ilias.th-koeln.de/xml/ilias_ds_4_3.xsd">
        # Bsp: tax_node.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}ItemId').text)

        # -------- Struktur einer "assignment to node" in der XML
        # < ds: Rec Entity = "tax_node_assignment" >
        #    < TaxNodeAssignment >
        #        < NodeId > 21682 < / NodeId >
        #        < Component > qpl < / Component >
        #        < ItemType > quest < / ItemType >
        #        < ItemId > 470081 < / ItemId >
        #    < / TaxNodeAssignment >
        # < / ds: Rec >



        # Die Definition der Haupt- und Sub-Elemente muss in der Schleife für jede Frage neu erstellt werden
        # Sonst haben die angehängten Fragen alle die gleichen Werte, da es sich auf das Gleiche "Attribut" handelt
        Export = ET.Element('exp:Export')
        ExportItem = ET.SubElement(Export, 'exp:ExportItem')
        DataSet = ET.SubElement(ExportItem, 'ds:DataSet')
        Rec = ET.SubElement(DataSet, 'ds:Rec')
        TaxNodeAssignment = ET.SubElement(Rec, 'TaxNodeAssignment')
        NodeId = ET.SubElement(TaxNodeAssignment, 'NodeId')
        Component = ET.SubElement(TaxNodeAssignment, 'Component')
        ItemType = ET.SubElement(TaxNodeAssignment, 'ItemType')
        ItemId = ET.SubElement(TaxNodeAssignment, 'ItemId')


        #Rec = ET.SubElement(DataSet, 'ds:Rec')
        Rec.set('Entity', "tax_node_assignment")
        #ItemId = ET.SubElement(TaxNodeAssignment, 'ItemId')

        NodeId.text = self.node_to_id_dict.get(item_pool)

        Component.text = "qpl"  # fix
        ItemType.text = "quest" # fix
        ItemId.text = item_id     # Fragen ID üblicherweise > 100000, wenn Fragen ID z.B. 000001 dann ist der itemValue "nur" 1 und es fehlen nullen
        self.myroot[0][len(self.myroot[0]) - 1].append(Rec)



        self.mytree.write(file_location)



        # Taxonomie-datei "refreshen"
        TAX_Interface.tax_file_refresh(self, file_location)


    def remove_node_from_tax(self):
        self.mytree = ET.parse(self.taxonomy_file_read)
        self.myroot = self.mytree.getroot()

        self.node_to_remove = self.tax_node_name_entry.get()

        self.taxTree_taxIds = []
        self.taxTree_childs = []
        self.taxTree_parents = []
        self.taxTree_depths = []
        self.taxTree_types = []
        self.taxTree_titles = []
        self.taxTree_orderNrs = []





        self.remove_node = self.tax_node_name_entry.get()
        for tax_node in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}TaxTree'):
            if tax_node.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Title').text == self.remove_node:
                print("found node: " + str(self.remove_node))
                tax_node.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Title').text = "delete"
                self.mytree.write(self.taxonomy_file_write)
                print("Node auf \"delete\"")


        # Alle Daten der Knoten speichern

        for taxId in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}TaxId'):
            self.taxTree_taxIds.append(taxId.text)
            # wert ist fix

        for child in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Child'):
            self.taxTree_childs.append(child.text)

        for parent in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Parent'):
            self.taxTree_parents.append(parent.text)

        for depth in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Depth'):
            self.taxTree_depths.append(depth.text)

        for typ in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Type'):
            self.taxTree_types.append(typ.text)

        for title in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Title'):
            self.taxTree_titles.append(title.text)

        for orderNr in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}OrderNr'):
            self.taxTree_orderNrs.append(orderNr.text)

        # 1. Eintrag entfernen, da dieser Eintrag dem Taxonomie-Namen entspricht und nicht vom Knoten
        self.taxTree_titles.pop(0)


        # Alle TaxTree löschen
        for rec in self.myroot.iter('{http://www.ilias.de/Services/DataSet/ds/4_3}DataSet'):
            for child in list(rec):
                if child.attrib['Entity'] == "tax_tree":
                    rec.remove(child)
        self.mytree.write(self.taxonomy_file_write)
        print("Deleted!")


        for i in range(len(self.taxTree_titles)):
            if self.taxTree_titles[i] != "delete":
                Export = ET.Element('exp:Export')
                ExportItem = ET.SubElement(Export, 'exp:ExportItem')
                DataSet = ET.SubElement(ExportItem, 'ds:DataSet')
                Rec = ET.SubElement(DataSet, 'ds:Rec')
                TaxTree = ET.SubElement(Rec, 'TaxTree')
                TaxId = ET.SubElement(TaxTree, 'TaxId')
                Child = ET.SubElement(TaxTree, 'Child')
                Parent = ET.SubElement(TaxTree, 'Parent')
                Depth = ET.SubElement(TaxTree, 'Depth')
                Type = ET.SubElement(TaxTree, 'Type')
                Title = ET.SubElement(TaxTree, 'Title')
                OrderNr = ET.SubElement(TaxTree, 'OrderNr')


                Rec.set('Entity', "tax_tree")

                TaxId.text = str(self.tax_root_id)
                Child.text = str(self.taxTree_childs[i])
                Parent.text = str(self.taxTree_parents[i])
                Depth.text = str(self.taxTree_depths[i])
                if Depth.text == "1":
                    Type.text = ""
                    Title.text = str(self.taxTree_titles[i])
                    OrderNr.text = str(self.taxTree_orderNrs[i])
                else:
                    Type.text = "taxn"  # fix
                    Title.text = str(self.taxTree_titles[i])
                    OrderNr.text = str(self.taxTree_orderNrs[i])

                self.myroot.append(ExportItem)
                self.mytree.write(self.taxonomy_file_write)

        # Taxonomie-datei "refreshen"
        TAX_Interface.tax_file_refresh(self, self.taxonomy_exportXML_file)


        # Taxonomie Baum und Combobox aktualisieren
        self.taxonomy_frame_tree_picture.destroy()
        TAX_Interface.scan_tax_tree(self)

        self.tax_nodes_myCombo.destroy()
        TAX_Interface.tax_combobox_refresh(self)


    def tax_reallocate(self):
        print("Taxonomie wird neu sortiert ")
        self.mytree = ET.parse(self.taxonomy_file_read)
        self.myroot = self.mytree.getroot()

        for TaxId in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Tax'):
            if TaxId.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Id').text == "1970392":
                self.tax_root_id = TaxId.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Id').text

        self.reallocate_taxIds = []
        self.reallocate_childs = []
        self.reallocate_parents = []
        self.reallocate_depths = []
        self.reallocate_types = []
        self.reallocate_titles = []
        self.reallocate_orderNrs = []


        ##################################### Taxonomie Knoten löschen #####################################

        for taxId in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}TaxId'):
            self.reallocate_taxIds.append(taxId.text)
            # wert ist fix

        for child in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Child'):
            self.reallocate_childs.append(child.text)

        for parent in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Parent'):
            self.reallocate_parents.append(parent.text)

        for depth in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Depth'):
            self.reallocate_depths.append(depth.text)

        for typ in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Type'):
            self.reallocate_types.append(typ.text)

        for title in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Title'):
            self.reallocate_titles.append(title.text)

        for orderNr in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}OrderNr'):
            self.reallocate_orderNrs.append(orderNr.text)

        # 1. Eintrag entfernen, da dieser Eintrag dem Taxonomie-Namen entspricht und nicht vom Knoten
        self.reallocate_titles.pop(0)



        # Alle TaxTree löschen
        for rec in self.myroot.iter('{http://www.ilias.de/Services/DataSet/ds/4_3}DataSet'):
            for child in list(rec):
                if child.attrib['Entity'] == "tax_tree":
                    rec.remove(child)
        self.mytree.write(self.taxonomy_file_write)


        ##############################
        # Beim schreiben in die XML Datei müssen konvertierungen vorgenommen werden
        # Es wird automatisch "ns0" etc. durch Python geschrieben und muss in das ilias Format abgeändert werden
        # Taxonomie-datei "refreshen"
        TAX_Interface.tax_file_refresh(self, self.taxonomy_exportXML_file)

        ############################



         # Alle Fragen im Array speichern bevor die XML gelöscht wird
        self.reallocate_child_id = []
        self.reallocate_node_id = []
        self.reallocate_item_id = []
        self.reallocate_item_list = []

        for tax_node in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}TaxNodeAssignment'):
            self.reallocate_child_id.append(tax_node.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}ItemId').text)

        for node_id in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}NodeId'):
            self.reallocate_node_id.append(node_id.text)

        for item_id in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}ItemId'):
            self.reallocate_item_id.append(item_id.text)

        self.reallocate_item_list =  list(zip(self.reallocate_item_id, self.reallocate_node_id))


        # Alle TaxNodeAssignments löschen
        for rec in self.myroot.iter('{http://www.ilias.de/Services/DataSet/ds/4_3}DataSet'):
            for child in list(rec):
                if child.attrib['Entity'] == "tax_node_assignment":
                    rec.remove(child)
        self.mytree.write(self.taxonomy_file_write)



        # TaxTree in Datei schreiben / aktualisieren
        for i in range(len(self.reallocate_titles)):

            if self.reallocate_titles[i] != "delete":
                Export = ET.Element('exp:Export')
                ExportItem = ET.SubElement(Export, 'exp:ExportItem')
                DataSet = ET.SubElement(ExportItem, 'ds:DataSet')
                Rec = ET.SubElement(DataSet, 'ds:Rec')
                TaxTree = ET.SubElement(Rec, 'TaxTree')
                TaxId = ET.SubElement(TaxTree, 'TaxId')
                Child = ET.SubElement(TaxTree, 'Child')
                Parent = ET.SubElement(TaxTree, 'Parent')
                Depth = ET.SubElement(TaxTree, 'Depth')
                Type = ET.SubElement(TaxTree, 'Type')
                Title = ET.SubElement(TaxTree, 'Title')
                OrderNr = ET.SubElement(TaxTree, 'OrderNr')


                Rec.set('Entity', "tax_tree")

                TaxId.text = str(self.tax_root_id)
                Child.text = str(self.reallocate_childs[i])
                Parent.text = str(self.reallocate_parents[i])
                Depth.text = str(self.reallocate_depths[i])
                if Depth.text == "1":
                    Type.text = ""
                    Title.text = str(self.reallocate_titles[i])
                    OrderNr.text = str(self.reallocate_orderNrs[i])
                else:
                    Type.text = "taxn"  # fix
                    Title.text = str(self.reallocate_titles[i])
                    OrderNr.text = str(self.reallocate_orderNrs[i])

                self.myroot.append(ExportItem)
                self.mytree.write(self.taxonomy_file_write)


         # Wiederherstellen der Fragen die nicht auf "00000" gesetzt sind
        for i in range(len(self.reallocate_item_id)):
            if self.reallocate_node_id[i] != "00000":
                Export = ET.Element('exp:Export')
                ExportItem = ET.SubElement(Export, 'exp:ExportItem')
                DataSet = ET.SubElement(ExportItem, 'ds:DataSet')
                Rec = ET.SubElement(DataSet, 'ds:Rec')
                TaxNodeAssignment = ET.SubElement(Rec, 'TaxNodeAssignment')
                NodeId = ET.SubElement(TaxNodeAssignment, 'NodeId')
                Component = ET.SubElement(TaxNodeAssignment, 'Component')
                ItemType = ET.SubElement(TaxNodeAssignment, 'ItemType')
                ItemId = ET.SubElement(TaxNodeAssignment, 'ItemId')

                # Rec = ET.SubElement(DataSet, 'ds:Rec')
                Rec.set('Entity', "tax_node_assignment")
                # ItemId = ET.SubElement(TaxNodeAssignment, 'ItemId')

                NodeId.text = self.reallocate_node_id[i]
                Component.text = "qpl"  # fix
                ItemType.text = "quest"  # fix
                ItemId.text = self.reallocate_item_id[i]

                self.myroot.append(ExportItem)
                self.mytree.write(self.taxonomy_file_write)


        # Beim schreiben in die XML Datei müssen konvertierungen vorgenommen werden
        # Es wird automatisch "ns0" etc. durch Python geschrieben und muss in das ilias Format abgeändert werden
        # Taxonomie-datei "refreshen"
        TAX_Interface.tax_file_refresh(self, self.taxonomy_exportXML_file)

        print("...abgeschlossen")

    def tax_reallocate_from_excel(self, file_location, actual_pool_number, max_number_of_pools):
        print("Taxonomie wird überarbeitet...          ", end="", flush=True)
        self.mytree = ET.parse(file_location)
        self.myroot = self.mytree.getroot()

        for TaxId in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Tax'):
            if TaxId.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Id').text == "1970392":
                self.tax_root_id = TaxId.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Id').text

        self.reallocate_taxIds = []
        self.reallocate_childs = []
        self.reallocate_parents = []
        self.reallocate_depths = []
        self.reallocate_types = []
        self.reallocate_titles = []
        self.reallocate_orderNrs = []


        ##################################### Taxonomie Knoten löschen #####################################

        for taxId in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}TaxId'):
            self.reallocate_taxIds.append(taxId.text)
            # wert ist fix

        for child in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Child'):
            self.reallocate_childs.append(child.text)

        for parent in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Parent'):
            self.reallocate_parents.append(parent.text)

        for depth in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Depth'):
            self.reallocate_depths.append(depth.text)

        for typ in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Type'):
            self.reallocate_types.append(typ.text)

        for title in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}Title'):
            self.reallocate_titles.append(title.text)

        for orderNr in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}OrderNr'):
            self.reallocate_orderNrs.append(orderNr.text)

        # 1. Eintrag entfernen, da dieser Eintrag dem Taxonomie-Namen entspricht und nicht vom Knoten
        self.reallocate_titles.pop(0)



        # Alle TaxTree löschen
        for rec in self.myroot.iter('{http://www.ilias.de/Services/DataSet/ds/4_3}DataSet'):
            for child in list(rec):
                if child.attrib['Entity'] == "tax_tree":
                    rec.remove(child)
        self.mytree.write(file_location)


        ##############################
        # Beim schreiben in die XML Datei müssen konvertierungen vorgenommen werden
        # Es wird automatisch "ns0" etc. durch Python geschrieben und muss in das ilias Format abgeändert werden
        # Taxonomie-datei "refreshen"
        TAX_Interface.tax_file_refresh(self, file_location)

        ############################



         # Alle Fragen im Array speichern bevor die XML gelöscht wird
        self.reallocate_child_id = []
        self.reallocate_node_id = []
        self.reallocate_item_id = []
        self.reallocate_item_list = []

        for tax_node in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}TaxNodeAssignment'):
            self.reallocate_child_id.append(tax_node.find('{http://www.ilias.de/Services/Taxonomy/tax/4_3}ItemId').text)

        for node_id in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}NodeId'):
            self.reallocate_node_id.append(node_id.text)

        for item_id in self.myroot.iter('{http://www.ilias.de/Services/Taxonomy/tax/4_3}ItemId'):
            self.reallocate_item_id.append(item_id.text)

        self.reallocate_item_list =  list(zip(self.reallocate_item_id, self.reallocate_node_id))


        # Alle TaxNodeAssignments löschen
        for rec in self.myroot.iter('{http://www.ilias.de/Services/DataSet/ds/4_3}DataSet'):
            for child in list(rec):
                if child.attrib['Entity'] == "tax_node_assignment":
                    rec.remove(child)
        self.mytree.write(file_location)



        # TaxTree in Datei schreiben
        for i in range(len(self.reallocate_titles)):

            if self.reallocate_titles[i] != "delete":
                Export = ET.Element('exp:Export')
                ExportItem = ET.SubElement(Export, 'exp:ExportItem')
                DataSet = ET.SubElement(ExportItem, 'ds:DataSet')
                Rec = ET.SubElement(DataSet, 'ds:Rec')
                TaxTree = ET.SubElement(Rec, 'TaxTree')
                TaxId = ET.SubElement(TaxTree, 'TaxId')
                Child = ET.SubElement(TaxTree, 'Child')
                Parent = ET.SubElement(TaxTree, 'Parent')
                Depth = ET.SubElement(TaxTree, 'Depth')
                Type = ET.SubElement(TaxTree, 'Type')
                Title = ET.SubElement(TaxTree, 'Title')
                OrderNr = ET.SubElement(TaxTree, 'OrderNr')


                Rec.set('Entity', "tax_tree")

                TaxId.text = str(self.tax_root_id)
                Child.text = str(self.reallocate_childs[i])
                Parent.text = str(self.reallocate_parents[i])
                Depth.text = str(self.reallocate_depths[i])
                if Depth.text == "1":
                    Type.text = ""
                    Title.text = str(self.reallocate_titles[i])
                    OrderNr.text = str(self.reallocate_orderNrs[i])
                else:
                    Type.text = "taxn"  # fix
                    Title.text = str(self.reallocate_titles[i])
                    OrderNr.text = str(self.reallocate_orderNrs[i])

                self.myroot.append(ExportItem)
                self.mytree.write(file_location)


         # Wiederherstellen der Fragen die nicht auf "00000" gesetzt sind
        for i in range(len(self.reallocate_item_id)):
            if self.reallocate_node_id[i] != "00000":
                Export = ET.Element('exp:Export')
                ExportItem = ET.SubElement(Export, 'exp:ExportItem')
                DataSet = ET.SubElement(ExportItem, 'ds:DataSet')
                Rec = ET.SubElement(DataSet, 'ds:Rec')
                TaxNodeAssignment = ET.SubElement(Rec, 'TaxNodeAssignment')
                NodeId = ET.SubElement(TaxNodeAssignment, 'NodeId')
                Component = ET.SubElement(TaxNodeAssignment, 'Component')
                ItemType = ET.SubElement(TaxNodeAssignment, 'ItemType')
                ItemId = ET.SubElement(TaxNodeAssignment, 'ItemId')

                # Rec = ET.SubElement(DataSet, 'ds:Rec')
                Rec.set('Entity', "tax_node_assignment")
                # ItemId = ET.SubElement(TaxNodeAssignment, 'ItemId')

                NodeId.text = self.reallocate_node_id[i]
                Component.text = "qpl"  # fix
                ItemType.text = "quest"  # fix
                ItemId.text = self.reallocate_item_id[i]

                self.myroot.append(ExportItem)
                self.mytree.write(file_location)


        # Beim schreiben in die XML Datei müssen konvertierungen vorgenommen werden
        # Es wird automatisch "ns0" etc. durch Python geschrieben und muss in das ilias Format abgeändert werden
        # Taxonomie-datei "refreshen"
        TAX_Interface.tax_file_refresh(self, file_location)
        print("abgeschlossen!")







        #
        #messagebox.showinfo("Fragenpool erstellen", "Fragenpool wurde erstellt! ---> Fragenpool-Nr.: " + str(actual_pool_number+1) + "/" + str(max_number_of_pools) + "\n\n"
        #                     "Abgelegt im Ordner: " + str(data_folder) + "\n"
        #                     "Anzahl der Fragen: " + str(len(self.reallocate_item_id)) + "\n\n")