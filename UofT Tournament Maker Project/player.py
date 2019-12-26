from typing import List, TextIO
import os
from generatefiles import *


TROPHIES = 694.33
BENTOR = 13
BENTOS = 15
FEES = 40
LUNCH_FEES = 10


class Dojo:

    fullname: str
    shortname: str
    nplayers: int
    lunch: dict  #R, V, RS, VS
    money: float
    team: int

    def __init__ (self, shortname, info_list, player_list):
        self.fullname = info_list['Fullname']
        self.shortname = shortname
        self.nplayers = len(player_list)
        self.lunch = self.calculate_lunch(player_list)
        self.money = self.calculate_fees(player_list, self.lunch)
        self.team = info_list['Team']


    def __str__(self):
        return '{} {} {} {} ${} {}'.format(self.fullname, self.shortname, self.nplayers,
            self.lunch, self.money, self.team)


    def calculate_fees (self, player_list: list, lunch: list) -> float:
        return FEES * len(player_list) + (lunch['R'] + lunch['V']) * LUNCH_FEES


    def calculate_lunch (self, player_list: list) -> dict:
        lunch = {'R': 0, 'V': 0, 'RS': 0, 'VS': 0}

        for player in player_list:
            if player.shimpan:
                if player.lunch[0] == 'R':
                    lunch['RS'] += player.lunch[1]
                elif player.lunch[0] == 'V':  
                    lunch['VS'] += player.lunch[1]
            else:
                if player.lunch[0] == 'R':
                    lunch['R'] += player.lunch[1]
                elif player.lunch[0] == 'V':
                    lunch['V'] += player.lunch[1]

        return lunch


class Player:
    """
    === Attributes ===
    name: player's full name
    rank: rank of player 
    lunch: lunch choice (r, v, 2 x r, 2 x v)
    division: choice of division
    shimpan: if they are shimpaning (T or F)
    tarenum: division+num

    === Representation Invariants ===
    0 <= rank <= 7 (0=kyu, 1=shodan, etc)
    """

    #Attribute types
    club: str
    name: str
    rank: int 
    division: str
    lunch: str
    shimpan: bool
    tarenum: str

    def __init__(self, info):
        self.name = info[0]
        self.rank = info[1]
        self.division = info[2]
        self.lunch = info[3]
        self.shimpan = info[4]
        self.tarenum = ''
        self.club = info[5]
        

    def __str__ (self):
        return '{} {} {} {} {} {} {}'.format(self.name, self.rank, self.division, self.lunch, self.shimpan, self.tarenum, self.club)


def convert_to_Player (file_name: str) -> List[Player]:
    players = []
    temp = read_club_file_players(file_name)

    for i in temp:

        i[1] = rank_converter(i[1])  #rank
        
        temp = ['', 0]

        if 'Regular' in i[3]:  #lunch is a list ['r/v', num]
            temp[0] = 'R'
            if i[3] == '2 x Regular':    
                temp[1] = 2
            else:
                temp[1] = 1
        elif 'Vegetarian' in i[3]:
            temp[0] = 'V'
            if i[3] == '2 x Vegetarian':
                temp[1] = 2
            else:
                temp[1] = 1
        else:
            temp[0] = 'N'

        i[3] = temp
        
        if i[4] in 'Yesyes':  #shimpan
            i[4] = True
        else:
            i[4] = False

        i.append(file_name.strip('.csv'))

        players.append(Player(i))

    return players


def rank_converter (rank: str) -> int:
    return {'Kyu': 0, '1D': 1, '2D': 2, '3D': 3, '4D': 4, '5D': 5, '6D': 6, '7D': 7}[rank]


def read_club_file_info (file_name: str) -> dict:
    #Return fullname, representative, email and number of team

    info = {'Fullname': '', 'Represntative': '', 'Email': '', 'Team': 0}

    file = open(file_name, 'r')
    doc = file.readlines()
        
    info['Fullname'] = doc[3][16:-4]
    info['Represntative'] = doc[4][16:-4]
    info['Email'] = doc[5][15:-4]
    info['Team'] = int(doc[33][-2])

    file.close()

    return info


def read_club_file_players(file_name: str) -> list:
    #Return list of players' info as nested list

    player_list = []

    file = open(file_name, 'r')
    doc = file.readlines()

    for line in doc[11:31]:
        if line[2].isalpha():
            player_list.append(line[2:].strip('\n').split(','))

    file.close()

    return player_list






if __name__ == '__main__':    
    club_list = {}
    players = []

    a = convert_to_Player('UOT.csv')
    b = convert_to_Player('JCC.csv')
    players.extend(a)
    players.extend(b)

    club_list['UOT'] = Dojo('UOT', read_club_file_info('UOT.csv'), a)
    club_list['JCC'] = Dojo('JCC', read_club_file_info('JCC.csv'), b)