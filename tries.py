from tkinter import *
import multiprocessing
import threading
import time
import logging


class Application(Frame):
    def create_widgets(self):
        self.quit_button = Button(self)
        self.quit_button['text'] = 'QUIT'
        self.quit_button['fg'] = 'red'
        self.quit_button['command'] = self.quit
        self.quit_button.pack({'side': 'left'})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.quit_button = None
        self.pack()
        self.create_widgets()
        self.poll()

    def poll(self):
        """
        This method is required to allow the mainloop to receive keyboard
        interrupts when the frame does not have the focus
        """
        self.master.after(250, self.poll)


def worker_function(quit_flag):
    counter = 0
    while not quit_flag.value:
        counter += 1
        logging.info("Work # %d" % counter)
        time.sleep(1.0)


format = '%(levelname)s: %(filename)s: %(lineno)d: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=format)
root = Tk()
app = Application(master=root)
quit_flag = multiprocessing.Value('i', int(False))
worker_thread = threading.Thread(target=worker_function, args=(quit_flag,))
worker_thread.start()
logging.info("quit_flag.value = %s" % bool(quit_flag.value))
try:
    app.mainloop()
except KeyboardInterrupt:
    logging.info("Keyboard interrupt")
quit_flag.value = True
logging.info("quit_flag.value = %s" % bool(quit_flag.value))
worker_thread.join()