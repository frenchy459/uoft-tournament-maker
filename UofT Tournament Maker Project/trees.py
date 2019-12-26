import openpyxl as op
from player import *
import random


class Div:

    groups: List[Player]
    trees: dict


def get_player_list_by_div (all_player_list: List[Player], div: str) -> List[Player]:
    
    player_list = []

    for player in all_player_list:
        if player.division == div:
            player_list.append(player)

    return player_list


def sort_players_into_groups (all_player_list: List[Player], group_sizes: List[int], div: str) -> List[List[Player]]:
    #figure out some next level sorting algorithm
    
    player_list = get_player_list_by_div(all_player_list, div)

    random.shuffle(player_list)
    players_in_group = {}
    obj = list(enumerate(group_sizes))
    k = 0

    for i, size in obj:
        players_in_group[i + 1] = []

        for j in range(size):
            players_in_group[i + 1].append(player_list[k])
            k += 1

    return players_in_group


def create_workbook (div: str, player_list: List[Player], group_sizes: List[int]):

    tree = op.load_workbook('Div {}.xlsx'.format(div))

    obj = list(enumerate(tree.worksheets))
    players_in_group = sort_players_into_groups(player_list, group_sizes, div)

    for i, sheet in obj:
        sheet.title = 'Group {}'.format(str(i + 1))
        sheet['A1'] = 'Group {} - {} | X'.format(div, str(i + 1))

        insert_player_into_tree(players_in_group[i + 1], sheet, group_sizes[i])


    tree.save('Div {}.xlsx'.format(div))


def insert_player_into_tree (player_list: List[Player], sheet, size):
    
    i = 0

    obj = list(enumerate(range(3, size * 4 + 1, 4)))

    for i, row in obj:
        sheet['A' + str(row)] = player_list[i].tarenum
        sheet['A' + str(row + 2)] = '{} ({})'.format(player_list[i].name, player_list[i].club)


if __name__ == '__main__':
    create_workbook('A', players, [8])


def div_totals (player_list: List[Player]) -> dict:
    divs = {'A': 0, 'B': 0, 'C': 0, 'W': 0}

    player_list.sort(key = lambda player: player.club)

    for player in player_list:
        divs[player.division] += 1
        player.tarenum = '{}{:02d}'.format(player.division, divs[player.division])

    return divs

"""
def recommend_div_size(size: int) -> None:
    if size <= 26:  #2 groups
        pass:
    elif size <= 52:  #4 groups
        pass
    elif size <= 104:  #8 groups
        pass
"""