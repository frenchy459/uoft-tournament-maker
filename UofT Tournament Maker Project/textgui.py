from player import *
from trees import *
from generatefiles import *
from shimpan import *
import datetime
import os

exit = False

################# THIS THE MAIN FILE, run program from here ############

CLUB_LIST = {}
PLAYER_LIST = []
PATH = 'C:/Users/franc/Documents/Kendo/{} UofT Tournament/'.format(datetime.datetime.now().year)

def get_workbook_info (player_list: List[Player], div: str):

    group_sizes = []
    size = int(input('How many groups in division {}: '.format(div)))

    for i in range(size):
        group_sizes.append(int(input('Size of group {}: '.format(str(i + 1)))))


    create_workbook('A', player_list, group_sizes)

"""
createFolder(PATH)
createFolder(PATH + 'Shimpan/')
createFolder(PATH + 'Shimpan/Print/')
createFolder(PATH + 'Shimpan/Email/')
createFolder(PATH + 'Club files')
"""
"""
while not exit:
    file_name = input("Enter name of club's file: ")

    temp = convert_to_Player(file_name)
    PLAYER_LIST.extend(temp)
    CLUB_LIST[file_name] = Dojo(file_name, read_club_file_info(file_name), temp)

    #extension = print("Is there an extension file (yes/no): ")

    leave = input("Exit program (yes/no): ")
    if leave.lower() == 'yes':
        exit = True
"""
if __name__ == '__main__':
        
    for file_name in os.listdir(PATH + 'Club files'):    

        temp = convert_to_Player(file_name)
        PLAYER_LIST.extend(temp)
        CLUB_LIST[file_name.strip('.csv')] = Dojo(file_name.strip('.csv'), read_club_file_info(file_name), temp)


    d = div_totals(PLAYER_LIST)
    print ('========================')
    for div in d:
        print ('{} players in division {}'.format(d[div], div))
        #recommend_div_size(div)
    print ('========================\n\n')

    get_workbook_info(PLAYER_LIST, 'A')
    #get_workbook_info(player_list, 'B')
    #get_workbook_info(player_list, 'C')
    #10sget_workbook_info(player_list, 'W')
        