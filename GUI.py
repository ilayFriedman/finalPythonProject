#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.19
#  in conjunction with Tcl version 8.6
#    Jan 06, 2020 03:50:29 PM +0200  platform: Windows NT

import sys
from collections import Counter
import main
import matplotlib.figure
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

from functools import partial
from tkinter import messagebox
from tkinter.filedialog import askdirectory, askopenfile
from tkinter import filedialog as fd

from pandas._libs import json

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True



def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        font11 = "-family {Segoe UI} -size 40 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 9 -weight bold -slant roman" \
        " -underline 0 -overstrike 0"

        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("939x634+376+101")
        top.title("Yelper")
        top.configure(background="#d9d9d9")

        #COMMANDS!
        enable_ReviewsView_Frame_TRUE = partial(self.show_ReviewsView_Frame, True)
        enable_ReviewsView_Frame_FALSE = partial(self.show_ReviewsView_Frame, False)
        importCSVClick = partial(self.switchImportRadioButton, "CSV")
        importDATAClick = partial(self.switchImportRadioButton, "DATA")

        self.radioButtonVar_CSV = tk.IntVar()
        self.radioButtonVar_Dataset = tk.IntVar()
        self.radioButtonVar_CSV.set(0)
        self.radioButtonVar_Dataset.set(0)
        self.canvas =None

        print("......CREATING ALL THE LABELS......")
        self.queryFrame = ttk.Frame(top)
        self.queryFrame.place(relx=0.202, rely=0.047, relheight=0.087, relwidth=0.634)
        self.queryFrame.configure(relief='groove')
        self.queryFrame.configure(borderwidth="2")
        self.queryFrame.configure(relief='groove')
        self.queryFrame.configure(width=595)


        self.query_textEntry = ttk.Entry(self.queryFrame)
        self.query_textEntry.place(relx=0.05, rely=0.364, relheight=0.382, relwidth=0.548)
        self.query_textEntry.configure(width=326)
        self.query_textEntry.configure(takefocus="")
        self.query_textEntry.configure(cursor="ibeam")

        self.enterResturant_Label = ttk.Label(self.queryFrame)
        self.enterResturant_Label.place(relx=0.0, rely=-0.091, height=19, width=122)
        self.enterResturant_Label.configure(background="#d9d9d9")
        self.enterResturant_Label.configure(foreground="#000000")
        self.enterResturant_Label.configure(font="TkDefaultFont")
        self.enterResturant_Label.configure(relief='flat')
        self.enterResturant_Label.configure(text='''Enter Resturant Name:''')


        self.Search_Button = ttk.Button(self.queryFrame)
        self.Search_Button.place(relx=0.605, rely=0.364, height=25, width=106)
        self.Search_Button.configure(takefocus="")
        self.Search_Button.configure(text='''Search''')
        self.Search_Button.configure(width=106)
        self.Search_Button.configure(command=self.onClick_Search)


        self.ResetAll_Button = ttk.Button(self.queryFrame)
        self.ResetAll_Button.place(relx=0.807, rely=0.364, height=25, width=96)
        self.ResetAll_Button.configure(takefocus="")
        self.ResetAll_Button.configure(text='''Reset All''')
        self.ResetAll_Button.configure(width=96)
        self.ResetAll_Button.configure(command=self.resetAll)

        self.YELPER = ttk.Label(top)
        self.YELPER.place(relx=0.011, rely=0.018, height=84, width=175)
        self.YELPER.configure(background="#d9d9d9")
        self.YELPER.configure(foreground="#000000")
        self.YELPER.configure(font=font11)
        self.YELPER.configure(relief='flat')
        self.YELPER.configure(text='''Yelper''')
        self.YELPER.configure(width=175)

        self.details_Frame = ttk.Frame(top)
        self.details_Frame.place(relx=0.021, rely=0.158, relheight=0.197
                                 , relwidth=0.953)
        self.details_Frame.configure(relief='groove')
        self.details_Frame.configure(borderwidth="2")
        self.details_Frame.configure(relief='groove')
        self.details_Frame.configure(width=895)

        self.ResturantDetails_Label = ttk.Label(self.details_Frame)
        self.ResturantDetails_Label.place(relx=0.0, rely=0.0, height=19, width=95)
        self.ResturantDetails_Label.configure(background="#d9d9d9")
        self.ResturantDetails_Label.configure(foreground="#000000")
        self.ResturantDetails_Label.configure(font="TkDefaultFont")
        self.ResturantDetails_Label.configure(relief='flat')
        self.ResturantDetails_Label.configure(text='''Resturant Details:''')


        self.details_Label = ttk.Label(self.details_Frame)
        self.details_Label.place(relx=0.022, rely=0.16, height=19, width=137)
        self.details_Label.configure(background="#d9d9d9")
        self.details_Label.configure(foreground="#000000")
        self.details_Label.configure(font=font12)
        self.details_Label.configure(relief='flat')
        self.details_Label.configure(text='''details on the resturant''')


        self.info_addr_Label = ttk.Label(self.details_Frame)
        self.info_addr_Label.place(relx=0.022, rely=0.32, height=19, width=205)
        self.info_addr_Label.configure(background="#d9d9d9")
        self.info_addr_Label.configure(foreground="#000000")
        self.info_addr_Label.configure(font="TkDefaultFont")
        self.info_addr_Label.configure(relief='flat')
        self.info_addr_Label.configure(text='''address''')
        self.info_addr_Label.configure(width=205)

        self.info_city_Label = ttk.Label(self.details_Frame)
        self.info_city_Label.place(relx=0.022, rely=0.48, height=19, width=195)
        self.info_city_Label.configure(background="#d9d9d9")
        self.info_city_Label.configure(foreground="#000000")
        self.info_city_Label.configure(font="TkDefaultFont")
        self.info_city_Label.configure(relief='flat')
        self.info_city_Label.configure(text='''city''')
        self.info_city_Label.configure(width=195)

        self.info_postal_Label = ttk.Label(self.details_Frame)
        self.info_postal_Label.place(relx=0.022, rely=0.64, height=19, width=195)

        self.info_postal_Label.configure(background="#d9d9d9")
        self.info_postal_Label.configure(foreground="#000000")
        self.info_postal_Label.configure(font="TkDefaultFont")
        self.info_postal_Label.configure(relief='flat')
        self.info_postal_Label.configure(text='''postal code''')
        self.info_postal_Label.configure(width=195)

        self.info_stars_Label = ttk.Label(self.details_Frame)
        self.info_stars_Label.place(relx=0.022, rely=0.80, height=19, width=188)
        self.info_stars_Label.configure(background="#d9d9d9")
        self.info_stars_Label.configure(foreground="#000000")
        self.info_stars_Label.configure(font="TkDefaultFont")
        self.info_stars_Label.configure(relief='flat')
        self.info_stars_Label.configure(text='''stars''')
        self.info_stars_Label.configure(width=188)

        self.info_catrgoriesT_Label = ttk.Label(self.details_Frame)
        self.info_catrgoriesT_Label.place(relx=0.335, rely=0.16, height=19
                                          , width=66)
        self.info_catrgoriesT_Label.configure(background="#d9d9d9")
        self.info_catrgoriesT_Label.configure(foreground="#000000")
        self.info_catrgoriesT_Label.configure(font=font12)
        self.info_catrgoriesT_Label.configure(relief='flat')
        self.info_catrgoriesT_Label.configure(text='''Categories:''')

        self.info_catrgories = ttk.Label(self.details_Frame)
        self.info_catrgories.place(relx=0.335, rely=0.32, height=69, width=125)
        self.info_catrgories.configure(background="#d9d9d9")
        self.info_catrgories.configure(foreground="#000000")
        self.info_catrgories.configure(font="TkDefaultFont")
        self.info_catrgories.configure(relief='flat')
        self.info_catrgories.configure(text='''Unknown categories''')
        self.info_catrgories.configure(width=125)

        self.info_openHours_Label = ttk.Label(self.details_Frame)
        self.info_openHours_Label.place(relx=0.615, rely=0.08, height=19, width = 73)
        self.info_openHours_Label.configure(background="#d9d9d9")
        self.info_openHours_Label.configure(foreground="#000000")
        self.info_openHours_Label.configure(font=font12)
        self.info_openHours_Label.configure(relief='flat')
        self.info_openHours_Label.configure(text='''Open Hours:''')

        self.info_hours_Label = ttk.Label(self.details_Frame)
        self.info_hours_Label.place(relx=0.626, rely=0.24, height=79, width=254)
        self.info_hours_Label.configure(background="#d9d9d9")
        self.info_hours_Label.configure(foreground="#000000")
        self.info_hours_Label.configure(font="TkDefaultFont")
        self.info_hours_Label.configure(relief='flat')
        self.info_hours_Label.configure(text='''Unkwon hours''')
        self.info_hours_Label.configure(width=254)

        self.Reviewsview_Frame = ttk.Frame(top)
        self.Reviewsview_Frame.place(relx=0.021, rely=0.379, relheight=0.544
                                     , relwidth=0.495)
        self.Reviewsview_Frame.configure(relief='groove')
        self.Reviewsview_Frame.configure(borderwidth="2")
        self.Reviewsview_Frame.configure(relief='groove')
        self.Reviewsview_Frame.configure(width=465)

        self.Reviewsview_Label = ttk.Label(self.Reviewsview_Frame)
        self.Reviewsview_Label.place(relx=0.0, rely=-0.014, height=19, width=73)
        self.Reviewsview_Label.configure(background="#d9d9d9")
        self.Reviewsview_Label.configure(foreground="#000000")
        self.Reviewsview_Label.configure(font="TkDefaultFont")
        self.Reviewsview_Label.configure(relief='flat')
        self.Reviewsview_Label.configure(text='''Reviews view''')

        self.LoadReview_Button = ttk.Button(self.Reviewsview_Frame)
        self.LoadReview_Button.place(relx=0.409, rely=0.14, height=25, width=115)
        self.LoadReview_Button.configure(takefocus="")
        self.LoadReview_Button.configure(text='''Load Review file''')
        self.LoadReview_Button.configure(width=115)
        self.LoadReview_Button.configure(state='disabled')
        self.LoadReview_Button.configure(command=self.onClick_import)

        self.reviewPath_textEntry = ttk.Entry(self.Reviewsview_Frame)
        self.reviewPath_textEntry.place(relx=0.043, rely=0.145, relheight=0.061, relwidth=0.357)
        self.reviewPath_textEntry.configure(width=166)
        self.reviewPath_textEntry.configure(takefocus="")
        self.reviewPath_textEntry.configure(cursor="ibeam")
        self.reviewPath_textEntry.configure(state='disabled')

        self.AnalysisReviews_Button = ttk.Button(self.Reviewsview_Frame)
        self.AnalysisReviews_Button.place(relx=0.043, rely=0.232, height=35, width=285)
        self.AnalysisReviews_Button.configure(takefocus="")
        self.AnalysisReviews_Button.configure(text='''Analysis reviews''')
        self.AnalysisReviews_Button.configure(width=285)
        self.AnalysisReviews_Button.configure(state='disabled')
        self.AnalysisReviews_Button.configure(command=self.onClick_AnalysisReviews)

        self.style.map('TRadiobutton',background=
            [('selected', _bgcolor), ('active', _ana2color)])
        self.importCSV_RadioB = ttk.Radiobutton(self.Reviewsview_Frame)
        self.importCSV_RadioB.place(relx=0.032, rely=0.048, relwidth=0.314, relheight=0.0, height=31)
        self.importCSV_RadioB.configure(takefocus="")
        self.importCSV_RadioB.configure(text='''Import review file (.csv)''')
        self.importCSV_RadioB.configure(state='disabled')
        self.importCSV_RadioB.configure(variable=self.radioButtonVar_CSV)
        self.importCSV_RadioB.configure(command=importCSVClick)

        self.fromDataSet_RadioB = ttk.Radiobutton(self.Reviewsview_Frame)
        self.fromDataSet_RadioB.place(relx=0.398, rely=0.048, relwidth=0.258, relheight=0.0, height=31)
        self.fromDataSet_RadioB.configure(takefocus="")
        self.fromDataSet_RadioB.configure(text='''Load from Dataset''')
        self.fromDataSet_RadioB.configure(state='disabled')
        self.fromDataSet_RadioB.configure(variable=self.radioButtonVar_Dataset)
        self.fromDataSet_RadioB.configure(command=importDATAClick)


        self.totalReviews_Label = ttk.Label(self.Reviewsview_Frame)
        self.totalReviews_Label.place(relx=0.043, rely=0.348, height=19, width=78)
        self.totalReviews_Label.configure(background="#d9d9d9")
        self.totalReviews_Label.configure(foreground="#000000")
        self.totalReviews_Label.configure(font="TkDefaultFont")
        self.totalReviews_Label.configure(relief='flat')
        self.totalReviews_Label.configure(text='''Total reviews:''')

        self.numberReviews_Label = ttk.Label(self.Reviewsview_Frame)
        self.numberReviews_Label.place(relx=0.237, rely=0.348, height=19
                , width=16)
        self.numberReviews_Label.configure(background="#d9d9d9")
        self.numberReviews_Label.configure(foreground="#d9d9d9")
        self.numberReviews_Label.configure(font="TkDefaultFont")
        self.numberReviews_Label.configure(relief='flat')
        self.numberReviews_Label.configure(text='''20''')

        # self.style.configure('Treeview.Heading',  font="TkDefaultFont")
        # self.resultTreeTopic_ScrollTree = ScrolledTreeView(self.Reviewsview_Frame)
        # self.resultTreeTopic_ScrollTree.place(relx=0.022, rely=0.493, relheight=0.368, relwidth=0.581)
        # self.resultTreeTopic_ScrollTree.configure(columns=('Col1', 'Col2'))
        # self.resultTreeTopic_ScrollTree.heading("#0",text="")
        # self.resultTreeTopic_ScrollTree.heading("#0",anchor="center")
        # self.resultTreeTopic_ScrollTree.column("#0",width="25")
        # self.resultTreeTopic_ScrollTree.column("#0",minwidth="20")
        # self.resultTreeTopic_ScrollTree.column("#0",stretch="1")
        # self.resultTreeTopic_ScrollTree.column("#0",anchor="w")
        # self.resultTreeTopic_ScrollTree.heading("Col1",text="Review")
        # self.resultTreeTopic_ScrollTree.heading("Col1",anchor="center")
        # self.resultTreeTopic_ScrollTree.column("Col2",width="126")
        # self.resultTreeTopic_ScrollTree.heading("Col2",text="Positive/Negative")
        # self.resultTreeTopic_ScrollTree.heading("Col2",anchor="center")
        # self.resultTreeTopic_ScrollTree.column("Col2",width="126")
        # # self.resultTreeTopic_ScrollTree.column("Col1",minwidth="20")
        # # self.resultTreeTopic_ScrollTree.column("Col1",stretch="1")
        # # self.resultTreeTopic_ScrollTree.column("Col1",anchor="w")
        # self.resultTreeTopic_ScrollTree['show'] = 'headings'

        self.chartFrame = ttk.Frame(self.Reviewsview_Frame)
        self.chartFrame.place(relx=0.470, rely=0.379, relheight=0.544, relwidth = 0.495)

        self.pieChart_Label = ttk.Label(self.Reviewsview_Frame)
        self.pieChart_Label.place(relx=0.824, rely=0.300, height=19, width=55)
        self.pieChart_Label.configure(background="#d9d9d9")
        self.pieChart_Label.configure(foreground="#000000")
        self.pieChart_Label.configure(font="TkDefaultFont")
        self.pieChart_Label.configure(relief='flat')
        self.pieChart_Label.configure(text='''Pie Chart:''')

        self.mainTopics_Label = ttk.Label(self.Reviewsview_Frame)
        self.mainTopics_Label.place(relx=0.022, rely=0.435, height=19, width=69)
        self.mainTopics_Label.configure(background="#d9d9d9")
        self.mainTopics_Label.configure(foreground="#000000")
        self.mainTopics_Label.configure(font="TkDefaultFont")
        self.mainTopics_Label.configure(relief='flat')
        self.mainTopics_Label.configure(text='''Main topics:''')

        self.SimilarityRestaurants_Frame = ttk.Frame(top)
        self.SimilarityRestaurants_Frame.place(relx=0.532, rely=0.379
                , relheight=0.544, relwidth=0.453)
        self.SimilarityRestaurants_Frame.configure(relief='groove')
        self.SimilarityRestaurants_Frame.configure(borderwidth="2")
        self.SimilarityRestaurants_Frame.configure(relief='groove')
        self.SimilarityRestaurants_Frame.configure(width=425)
        self.SimilarityRestaurants_Frame.configure(cursor="fleur")

        self.SimilarityRestaurants_Label = ttk.Label(self.SimilarityRestaurants_Frame)
        self.SimilarityRestaurants_Label.place(relx=0.0, rely=-0.014, height=19
                , width=117)
        self.SimilarityRestaurants_Label.configure(background="#d9d9d9")
        self.SimilarityRestaurants_Label.configure(foreground="#000000")
        self.SimilarityRestaurants_Label.configure(font="TkDefaultFont")
        self.SimilarityRestaurants_Label.configure(relief='flat')
        self.SimilarityRestaurants_Label.configure(text='''Similarity Restaurants''')

        self.CategorySim_RadioB = ttk.Radiobutton(self.SimilarityRestaurants_Frame)
        self.CategorySim_RadioB.place(relx=0.047, rely=0.087, relwidth=0.287
                , relheight=0.0, height=21)
        self.CategorySim_RadioB.configure(takefocus="")
        self.CategorySim_RadioB.configure(text='''Category similarity''')

        self.locationSim_RadioB = ttk.Radiobutton(self.SimilarityRestaurants_Frame)
        self.locationSim_RadioB.place(relx=0.047, rely=0.174, relwidth=0.282
                , relheight=0.0, height=21)
        self.locationSim_RadioB.configure(takefocus="")
        self.locationSim_RadioB.configure(text='''Location similarity''')

        self.categoriesInput_textEntry = ttk.Entry(self.SimilarityRestaurants_Frame)
        self.categoriesInput_textEntry.place(relx=0.353, rely=0.087
                , relheight=0.061, relwidth=0.132)
        self.categoriesInput_textEntry.configure(width=56)
        self.categoriesInput_textEntry.configure(takefocus="")
        self.categoriesInput_textEntry.configure(cursor="ibeam")

        self.minPercent_Label = ttk.Label(self.SimilarityRestaurants_Frame)
        self.minPercent_Label.place(relx=0.506, rely=0.087, height=19, width=140)

        self.minPercent_Label.configure(background="#d9d9d9")
        self.minPercent_Label.configure(foreground="#000000")
        self.minPercent_Label.configure(font="TkDefaultFont")
        self.minPercent_Label.configure(relief='flat')
        self.minPercent_Label.configure(text='''Min similarity percent (%)''')

        self.locationInput_textEntry = ttk.Entry(self.SimilarityRestaurants_Frame)
        self.locationInput_textEntry.place(relx=0.353, rely=0.174
                , relheight=0.061, relwidth=0.132)
        self.locationInput_textEntry.configure(width=56)
        self.locationInput_textEntry.configure(takefocus="")
        self.locationInput_textEntry.configure(cursor="ibeam")

        self.maxRadius_Label = ttk.Label(self.SimilarityRestaurants_Frame)
        self.maxRadius_Label.place(relx=0.506, rely=0.174, height=19, width=93)
        self.maxRadius_Label.configure(background="#d9d9d9")
        self.maxRadius_Label.configure(foreground="#000000")
        self.maxRadius_Label.configure(font="TkDefaultFont")
        self.maxRadius_Label.configure(relief='flat')
        self.maxRadius_Label.configure(text='''Max Radius (km)''')

        self.showMe_Label = ttk.Label(self.SimilarityRestaurants_Frame)
        self.showMe_Label.place(relx=0.047, rely=0.261, height=19, width=55)
        self.showMe_Label.configure(background="#d9d9d9")
        self.showMe_Label.configure(foreground="#000000")
        self.showMe_Label.configure(font="TkDefaultFont")
        self.showMe_Label.configure(relief='flat')
        self.showMe_Label.configure(text='''Show me''')
        self.showMe_Label.configure(width=55)

        self.numResult_textInput = ttk.Entry(self.SimilarityRestaurants_Frame)
        self.numResult_textInput.place(relx=0.188, rely=0.261, relheight=0.061
                , relwidth=0.108)
        self.numResult_textInput.configure(width=46)
        self.numResult_textInput.configure(takefocus="")
        self.numResult_textInput.configure(cursor="ibeam")

        self.Results_Label = ttk.Label(self.SimilarityRestaurants_Frame)
        self.Results_Label.place(relx=0.318, rely=0.275, height=19, width=41)
        self.Results_Label.configure(background="#d9d9d9")
        self.Results_Label.configure(foreground="#000000")
        self.Results_Label.configure(font="TkDefaultFont")
        self.Results_Label.configure(relief='flat')
        self.Results_Label.configure(text='''Results''')

        self.Go_Button = ttk.Button(self.SimilarityRestaurants_Frame)
        self.Go_Button.place(relx=0.518, rely=0.261, height=25, width=176)
        self.Go_Button.configure(takefocus="")
        self.Go_Button.configure(text='''Go!''')
        self.Go_Button.configure(width=176)

        self.results_click_Label = ttk.Label(self.SimilarityRestaurants_Frame)
        self.results_click_Label.place(relx=0.024, rely=0.435, height=19
                , width=251)
        self.results_click_Label.configure(background="#d9d9d9")
        self.results_click_Label.configure(foreground="#000000")
        self.results_click_Label.configure(font="TkDefaultFont")
        self.results_click_Label.configure(relief='flat')
        self.results_click_Label.configure(text='''Results: (click on each name to see recomend!)''')

        self.resultsTreeSim_ScrollTree = ScrolledTreeView(self.SimilarityRestaurants_Frame)
        self.resultsTreeSim_ScrollTree.place(relx=0.024, rely=0.493, relheight=0.397, relwidth=0.941)
        self.resultsTreeSim_ScrollTree.configure(columns="Col1")
        self.resultsTreeSim_ScrollTree.heading("#0",text="Tree")
        self.resultsTreeSim_ScrollTree.heading("#0",anchor="center")
        self.resultsTreeSim_ScrollTree.column("#0",width="190")
        self.resultsTreeSim_ScrollTree.column("#0",minwidth="20")
        self.resultsTreeSim_ScrollTree.column("#0",stretch="1")
        self.resultsTreeSim_ScrollTree.column("#0",anchor="w")
        self.resultsTreeSim_ScrollTree.heading("Col1",text="Col1")
        self.resultsTreeSim_ScrollTree.heading("Col1",anchor="center")
        self.resultsTreeSim_ScrollTree.column("Col1",width="191")
        self.resultsTreeSim_ScrollTree.column("Col1",minwidth="20")
        self.resultsTreeSim_ScrollTree.column("Col1",stretch="1")
        self.resultsTreeSim_ScrollTree.column("Col1",anchor="w")

        self.SaveRes_Button = ttk.Button(self.SimilarityRestaurants_Frame)
        self.SaveRes_Button.place(relx=0.024, rely=0.899, height=25, width=86)
        self.SaveRes_Button.configure(takefocus="")
        self.SaveRes_Button.configure(text='''Save results''')
        self.SaveRes_Button.configure(width=86)

        print("......COMPILING DATA, ALMOST......")
        try:
            self.db = main.DataBase("C:\\Users\\User\\Desktop\\DATA_SET")
            print("......AFTER CREATION......")
            self.show_DetailsInfo_Frame(False)
        except:
            raise ("CANT CREATE DATABASE!")


    def onClick_Search(self):
        if(len(self.query_textEntry.get()) == 0):
            messagebox.showerror('oops!','You have to insert some bussiness name to start!')

        else:
            if (self.db.business_Json[self.db.business_Json['name'] == self.query_textEntry.get()].size.compute() == 0):
                messagebox.showinfo('oops!', 'The Bussiness name doesnt exist.\nSearch another one.')

            else: ## bussines exist : fill and enable everything
                self.show_Search_Frame(False)
                self.show_ReviewsView_Frame_RadioB(True)
                self.fillInfo(self.query_textEntry.get())
                self.show_DetailsInfo_Frame(True)


    def onClick_import(self):
        dirWind = tk.Tk()
        dirWind.withdraw()
        self.path = fd.askopenfilename(title = "Select CSV file",filetypes = (("CSV Files","*.csv"),))
        self.AnalysisReviews_Button.configure(state='normal')
        if (len(str(self.reviewPath_textEntry.get())) != 0):
            self.reviewPath_textEntry.delete(0, 'end')
        self.reviewPath_textEntry.insert(0, str(self.path))
        dirWind.destroy()

    def onClick_AnalysisReviews(self):
        if(self.radioButtonVar_CSV.get() == 1):
            self.db.businessSentimentAnalysis_FromCSV(self.path)
        else:
            self.reviewsAnsList = self.db.businessSentimentAnalysis_FromDATASET(self.query_textEntry.get())
            self.numberReviews_Label.configure(text=len(self.reviewsAnsList[2]))
            self.show_ReviewsView_Frame(True)
            if(len(self.reviewsAnsList[2]) > 0):
                self.putPieChart(self.reviewsAnsList[0])

    def show_Search_Frame(self, enable):
        if enable == True:
            self.query_textEntry.configure(state='normal')
            self.Search_Button.configure(state='normal')
        else:
            self.query_textEntry.configure(state='disable')
            self.Search_Button.configure(state='disable')

    def show_DetailsInfo_Frame(self,enable):
        if enable==True:
            self.details_Label.configure(foreground="#000000")
            self.info_addr_Label.configure(foreground="#000000")
            self.info_city_Label.configure(foreground="#000000")
            self.info_postal_Label.configure(foreground="#000000")
            self.info_stars_Label.configure(foreground="#000000")
            self.info_catrgories.configure(foreground="#000000")
            self.info_hours_Label.configure(foreground="#000000")
            self.info_catrgoriesT_Label.configure(foreground="#000000")
            self.info_openHours_Label.configure(foreground="#000000")

        else:
            self.details_Label.configure(foreground="#d9d9d9")
            self.info_addr_Label.configure(foreground="#d9d9d9")
            self.info_city_Label.configure(foreground="#d9d9d9")
            self.info_postal_Label.configure(foreground="#d9d9d9")
            self.info_stars_Label.configure(foreground="#d9d9d9")
            self.info_catrgories.configure(foreground="#d9d9d9")
            self.info_hours_Label.configure(foreground="#d9d9d9")
            self.info_catrgoriesT_Label.configure(foreground="#d9d9d9")
            self.info_openHours_Label.configure(foreground="#d9d9d9")

    def show_ReviewsView_Frame_RadioB(self, enable):
        if enable == True:
            self.fromDataSet_RadioB.configure(state='normal')
            self.importCSV_RadioB.configure(state='normal')
        else:
            self.fromDataSet_RadioB.configure(state='disable')
            self.importCSV_RadioB.configure(state='disable')

    def show_ReviewsView_Frame(self, enable):
        if enable == True:
            self.AnalysisReviews_Button.configure(state='normal')
            self.reviewPath_textEntry.configure(state='normal')
            self.LoadReview_Button.configure(state='normal')
            self.numberReviews_Label.configure(foreground="#000000")
        else:
            self.AnalysisReviews_Button.configure(state='disable')
            self.reviewPath_textEntry.configure(state='disable')
            self.LoadReview_Button.configure(state='disable')
            if (self.canvas is not None):
                 self.canvas.get_tk_widget().pack_forget()
            self.numberReviews_Label.configure(foreground="#d9d9d9")


    def fillInfo(self,bussinessName):
        if (self.db.business_Json[self.db.business_Json['name'] == bussinessName]['address'] is not None):
            self.info_addr_Label.configure(text='Address: '+str(self.db.business_Json[self.db.business_Json['name'] == bussinessName]['address'].compute().tolist()[0]))
        if (self.db.business_Json[self.db.business_Json['name'] == bussinessName]['city'].compute() is not None):
            self.info_city_Label.configure(text='City: '+str(self.db.business_Json[self.db.business_Json['name'] == bussinessName]['city'].compute().tolist()[0]))
        if (self.db.business_Json[self.db.business_Json['name'] == bussinessName]['postal_code'].compute() is not None):
            self.info_postal_Label.configure(text='Postal Code: '+str(self.db.business_Json[self.db.business_Json['name'] == bussinessName]['postal_code'].compute().tolist()[0]))
        if (self.db.business_Json[self.db.business_Json['name'] == bussinessName]['stars'].compute() is not None):
            self.info_stars_Label.configure(text='Stars: '+str(self.db.business_Json[self.db.business_Json['name'] == bussinessName]['stars'].compute().tolist()[0]))
        if (self.db.business_Json[self.db.business_Json['name'] == bussinessName]['categories'].compute().tolist()[0] is not None):
            self.info_catrgories.configure(text='\n'.join(self.db.business_Json[self.db.business_Json['name'] == bussinessName]['categories'].compute().tolist()[0].replace(', ',',').split(",")[:4]))
        if (self.db.business_Json[self.db.business_Json['name'] == bussinessName]['hours'].compute().tolist()[0] is not None):
            self.info_hours_Label.configure(text='\n'.join([str([key, value]) for key, value in self.db.business_Json[self.db.business_Json['name'] == bussinessName]['hours'].compute().tolist()[0].items()]))

    def putPieChart(self,listPrecentage):
        fig = matplotlib.figure.Figure(figsize=(5, 5))
        ax = fig.add_subplot(111)
        counter = Counter(listPrecentage)
        sizes = [counter[1], counter[-1]]
        ax.pie(sizes,autopct='%1.1f%%',shadow=True, startangle=140)
        # circle = matplotlib.patches.Circle((0, 0), 0.7, color='white')
        # ax.add_artist(circle)
        self.canvas = FigureCanvasTkAgg(fig, master=self.chartFrame)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()

    def switchImportRadioButton(self,whoIsClicked):
        if(whoIsClicked == "CSV"):
            if(self.radioButtonVar_Dataset.get() == 1):
                self.radioButtonVar_Dataset.set(0)
            self.radioButtonVar_CSV.set(1)
            self.show_ReviewsView_Frame(False)
            self.LoadReview_Button.configure(state='normal')
            self.reviewPath_textEntry.configure(state='normal')

            if (len(str(self.reviewPath_textEntry.get())) == 0):
                self.AnalysisReviews_Button.configure(state='disable')
        else:
            if(self.radioButtonVar_CSV.get() == 1):
                self.radioButtonVar_CSV.set(0)
            self.reviewPath_textEntry.delete(0, 'end')
            self.radioButtonVar_Dataset.set(1)
            self.show_ReviewsView_Frame(False)
            self.AnalysisReviews_Button.configure(state='normal')



    def resetAll(self):
        self.show_ReviewsView_Frame(False)
        self.show_ReviewsView_Frame_RadioB(False)
        self.show_DetailsInfo_Frame(False)
        self.show_Search_Frame(True)
        self.radioButtonVar_CSV.set(0)
        self.radioButtonVar_Dataset.set(0)


    # def searchClick(self):

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





