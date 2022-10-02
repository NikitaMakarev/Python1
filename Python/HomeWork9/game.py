
from telegram.ext import ConversationHandler

from utils import keyboard

board = list(range(1, 10))

def draw_board(update, context):
    global board
    for i in range(3):
        update.messege.replay_text(f"| {board[0 + i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |",reply_markup=keyboard())

def start_game(update, context):
    global board
    text = 'Отсюда начнется игра:'
    update.messege.replay_text(text)
    board = list(range(1, 10))
    draw_board(update, context)
    update.messege.replay_text(f"Куда поставим X?")
    return "choosing_X"

def check_win():
    global board
    win_coord = ((0, 1, 2),(3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    counter = 0
    for i in board:
        if type(i) == int:
            continue
        else:
            counter +=1
    if counter == 9:
        return counter
    else:
        return False

def tic(update, context):
    global board
    player_answer = int(update.message.text)
    if str(board[player_answer - 1]) not in "XO":
        board[player_answer - 1] = "X"
        draw_board(update, context)
    else:
        update.message.reply_text("Эта клетка уже занята, выберите другую")
        return f"choosing_X"
    tmp = check_win()
    if type(tmp) == str:
        update.message.reply_text(f"{tmp} выиграл!")
        return ConversationHandler.END
    elif type(tmp) == int:
        update.message.reply_text("Ничья!")
        return ConversationHandler.END
    else:
         update.message.reply_text(f"Куда поставим O?")
         return "choosing_O"

def tac(update, context):
    global board
    player_answer = int(update.message.text)
    if str(board[player_answer - 1]) not in "XO":
        board[player_answer - 1] = "O"
        draw_board(update, context)
    else:
        update.message.reply_text("Эта клетка уже занята, выберите другую")
        return f"choosing_O"
    tmp = check_win()
    if type(tmp) == str:
         update.message.reply_text(f"{tmp} выиграл!")
         board = list(range(1, 10))
         return ConversationHandler.END
    else:
        update.message.reply_text(f"Куда поставим X?")
    return f"choosing_X"