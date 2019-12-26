#this is getting shit from files to go into sql table called players
#should also make a file for making a shimpan table or atleast generate an excel file for shimpan
#or maybe export a whole woorkbook where page 1 is players and page 2 is shimpan
#actually first page is for dojo info

from typing import List, TextIO
import os
import mysql.connector as mysql

DIVA = 0
DIVB = 0
DIVC = 0
DIVW = 0

def read_club_file_players(file_name: str) -> list:
    #Return list of players' info as [(name, dan, division, club, tarenum, shimpan, lunchtype, lunchnum] from an open file

    file = open(file_name, 'r')
    doc = file.readlines()

    #player_list = [tuple(line[2:].strip('\n').split(',')) for line in doc[11:31] if line[2].isalpha()]

    player_list = []
    for line in doc[11:31]:
        if line[2].isalpha():
            temp = line[2:].strip('\n').split(',')
            player_list.append(tuple(temp[0], temp[1], temp[2], file_name[:-4], get_tarenum(temp[1]), get_shimpan(temp[4])))

    file.close()

    return player_list

def get_shimpan(x: str) -> bool:
    return x == 'Yes'


def get_tarenum(division: str) -> str:
    if division == 'A':
        DIVA += 1
        return 'A' + str(DIVA)
    elif division == 'B':
        DIVB += 1
        return 'B' + str(DIVB)
    elif division == 'C':
        DIVC += 1
        return 'C' + str(DIVC)
    elif division == 'W':
        DIVW += 1
        return 'W' + str(DIVW)


def insert_player_list_into_sql(player_list: List[list]) -> None:

    uot19 = mysql.connect(
        host='localhost',
        user='root',
        passwd='m0therfuc',
        database='uot19')

    mycursor = uot19.cursor()

    sql = 'INSERT INTO players (name, dan, division, shimpan) VALUES (%s, %s, %s, %s)'

    val = player_list

    mycursor.executemany(sql, val)

    uot19.commit()

    print(mycursor.rowcount, 'was inserted.')


if __name__ == '__main__':    
    club_list = {}
    players = []

    players.extend(read_club_file_players('UOT.csv'))
    insert_player_list_into_sql(players)



