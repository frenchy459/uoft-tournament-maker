from tkinter import *
from textgui import *
from tkinter import filedialog

DIRECTORY = ''

class Window1():
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        master.title("Tournament Maker")
        master.geometry('200x200')

        self.label = Label(master, text="Please select directory to save files to")
        self.label.pack()

        self.get_path_button = Button(master, text='Open directory', command=lambda:[self.get_path(), self.new_window()])
        self.get_path_button.pack()


        #self.read_club_files_button = Button(master, text='Read club files in \'Club files\' folder', command=self.read_files_in_folder())
        #self.read_club_files_button.pack()

        self.close_button = Button(master, text="Close", command=master.destroy)
        self.close_button.pack()

        #self.new_window_button = Button(master, text='New window', command=self.new_window)
        #self.new_window_button.pack()


    def read_files_in_folder(self):

        for file_name in os.listdir(PATH + 'Club files'):    
            temp = convert_to_Player(file_name)
            PLAYER_LIST.extend(temp)
            CLUB_LIST[file_name.strip('.csv')] = Dojo(file_name.strip('.csv'), read_club_file_info(file_name), temp)


    def new_window(self):
        self.app = Window2(Toplevel(self.master))


    def get_path(self):
        self.master.withdraw()
        DIRECTORY = filedialog.askdirectory(parent=self.master,initialdir="/",title='Please select a directory')
        #DIRECTORY = 'aaaa'
        self.master.deiconify()


class Window2():

    def __init__ (self, master):
        self.master = master
        self.frame = Frame(self.master)
        master.title("Tournament Maker")
        master.geometry('500x500')

        print (DIRECTORY + 'aaa')

        self.create_all_folders_button = Button(master, text=
            #"Create all folders for {}".format(datetime.datetime.now().year), 
            'Create all folders for xyear',
            command=lambda:[
            createFolder(DIRECTORY),
            createFolder(DIRECTORY + 'Shimpan/'),
            createFolder(DIRECTORY + 'Shimpan/Print/'),
            createFolder(DIRECTORY + 'Shimpan/Email/'),
            createFolder(DIRECTORY + 'Club files/')])
        self.create_all_folders_button.pack()

        self.close_button = Button(master, text="Close", command=master.destroy())
        self.close_button.pack()



def main():
    root = Tk()
    app = Window1(root)
    
    root.mainloop()


if __name__ == '__main__':
    main()