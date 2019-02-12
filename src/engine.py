
from keras.models import Sequential, load_model
from keras.layers import Input, LSTM, Dense, Activation, Flatten

import numpy as np

try:
    model = load_model('khess.h5')
except:

    model = Sequential()
    model.add(Input(69))
    model.add(Dense(552))
    model.add(LSTM(552, return_sequences=True))
    model.add(Dropout(.3))
    model.add(LSTM(552, return_sequences=True))
    model.add(Activation('softmax'))
    model.add(Dense(69))
    model.compile(loss='categorical-cross-entropy', optimizer='rmsprop')


encode_board = { k:i for i,k in enumerate(' PNBRQKpnbrqk') }
encode_turn = {'w':1, 'b':2}
encode_castle = { k:i for i,k in enumerate([ 'KQkq'[i::j] for i in range(4) for k in range(4) ]) }
encode_ep = { k:8*i+j for i,k in enumerate('abcdefgh') for j in range(1,9) }
encode_hm = int
encode_fm = int

decode_board = { i:k for k,i in encode_board.items() }
decode_turn = { i:k for k,i in encode_move.items() }
decode_castle = { i:k for k,i in encode_castle.items() }
decode_ep = { i:k for k,i in encode_ep.items() }
decode_hm = str
decode_fm = str

def prepare(board):
    pass

def postpare(board):
    pass

def encode(board, turn, castle, ep, hm, fm):
    return [ encode_board[k] for k in board ] + [ encode_move[turn], encode_castle[castle], encode_ep[ep], encode_hm(hm), encode_fm(fm) ]

def decode(pred):
    print(pred)
    return decode_board(pred[:64]), decode_turn[pred[64]], decode_castle[pred[65]], decode_ep[pred[66]], decode_hm[pred[67]], decode_fm[pred[68]]

def train(game):
    pass


def query(board):

    return postpare(  model.predict( prepare(board) ) )
