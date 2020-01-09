# import csv
#
# import nltk
#
# from dask.bag import read_text
#
# import json
#
#
#
# import gensim.models.doc2vec
# import re
# assert gensim.models.doc2vec.FAST_VERSION > -1, "This will be painfully slow otherwise"
#
# if __name__ == '__main__':
#     review_Json = read_text("C:\\Users\\User\\Desktop\\DATA_SET\\selected_entries_reviews_30k.json").map(json.loads).to_dataframe()
#     business_Json = read_text("C:\\Users\\User\\Desktop\\DATA_SET\\business_MinCorpus.json").map(json.loads).to_dataframe()
#
#     print(list(set(business_Json['business_id'].compute().tolist()) & set(review_Json['business_id'].compute().tolist())))
#
#
# # from tkinter import *
# # #!/usr/bin/env python3
# # # -*-coding: utf8-*-
# # import tkinter as Tk
# #
# #
# # ########################################################################
# # class OtherFrame(Tk.Toplevel):
# #     """"""
# #
# #     # ----------------------------------------------------------------------
# #     def __init__(self):
# #         """Constructor"""
# #         Tk.Toplevel.__init__(self)
# #         self.geometry("400x300")
# #         self.title("otherFrame")
# #
# #
# # ########################################################################
# # class MyApp(object):
# #     """"""
# #
# #     # ----------------------------------------------------------------------
# #     def __init__(self, parent):
# #         """Constructor"""
# #         self.root = parent
# #         self.root.title("Main frame")
# #         self.frame = Tk.Frame(parent)
# #         self.frame.pack()
# #
# #         btn = Tk.Button(self.frame, text="Open Frame", command=self.openFrame)
# #         btn.pack()
# #
# #     # ----------------------------------------------------------------------
# #     def hide(self):
# #         """"""
# #         self.root.withdraw()
# #
# #     # ----------------------------------------------------------------------
# #     def openFrame(self):
# #         """"""
# #         self.hide()
# #         subFrame = OtherFrame()
# #         handler = lambda: self.onCloseOtherFrame(subFrame)
# #         btn = Tk.Button(subFrame, text="Close", command=handler)
# #         btn.pack()
# #
# #     # ----------------------------------------------------------------------
# #     def onCloseOtherFrame(self, otherFrame):
# #         """"""
# #         otherFrame.destroy()
# #         self.show()
# #
# #     # ----------------------------------------------------------------------
# #     def show(self):
# #         """"""
# #         self.root.update()
# #         self.root.deiconify()
# #
# #
# # # ----------------------------------------------------------------------
# # if __name__ == "__main__":
# #     root = Tk.Tk()
# #     root.geometry("800x600")
# #     app = MyApp(root)
# #     root.mainloop()
#
# # from tkinter import *
# #
# # from PIL import Image, ImageTk
# #
# # root = Tk()
# # root.title("Title")
# # root.geometry("600x600")
# # root.configure(background="black")
# #
# #
# #
# # class Example(Frame):
# #     def __init__(self, master, *pargs):
# #         Frame.__init__(self, master, *pargs)
# #
# #
# #
# #         self.image = Image.open("background5.png")
# #         self.img_copy= self.image.copy()
# #
# #
# #         self.background_image = ImageTk.PhotoImage(self.image)
# #
# #         self.background = Label(self, image=self.background_image)
# #         self.background.pack(fill=BOTH, expand=YES)
# #         self.background.bind('<Configure>', self._resize_image)
# #
# #     def _resize_image(self,event):
# #
# #         new_width = event.width
# #         new_height = event.height
# #
# #         self.image = self.img_copy.resize((new_width, new_height))
# #
# #         self.background_image = ImageTk.PhotoImage(self.image)
# #         self.background.configure(image =  self.background_image)
# #
# #
# #
# # e = Example(root)
# # e.pack(fill=BOTH, expand=YES)
# #
# #
# # root.mainloop()


a= [2,3,2,1]
indices = [i for i, x in enumerate(a) if x == 2]
print(indices)