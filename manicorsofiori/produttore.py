from redeal import *
import itertools
from redeal import dds
from redeal.global_defs import Seat, Suit, Card, Rank, Strain

Deal.set_str_style("long")

mani = [
    "AK52 Q6 QJ AK862",
    "QT6 AT832 76 QT3",
    "J4 974 AKT92 754",
    "9873 KJ5 8543 J9",
    "JT32 9654 T32 K9",
    "Q975 J KQ985 A64",
    "86 AKQ83 76 Q752",
    "AK4 T72 AJ4 JT83",
    "87 AK75 AJ2 7643",
    "JT5 QJT4 T95 982",
    "AK3 932 KQ6 QJT5",
    "Q9642 86 8743 AK",
    "K8762 9832 A4 53",
    "94 K65 KQJT 8764",
    "QJ3 JT7 932 JT92",
    "AT5 AQ4 8765 AKQ",
    "AK5 AJ KQ987 KQ8",
    "JT984 KQ6 54 A74",
    "Q62 T92 AJ6 JT92",
    "73 87543 T32 653",
    "A43 A932 T652 98",
    "K Q764 AKQ87 AKT",
    "QJT92 KT8 93 532",
    "8765 J5 J4 QJ764",
    "642 A9 JT963 AK4",
    "K8 QJT732 52 987",
    "A75 K654 KQ7 QJ3",
    "QJT93 8 A84 T652",
    "AK T3 AJT93 J854",
    "98 A96 654 QT732",
    "T7654 QJ85 K87 9",
    "QJ32 K742 Q2 AK6",
]

mani = [H(x.upper()) for x in mani]

posizioni = (Seat["N"], Seat["E"], Seat["S"], Seat["W"])
predeal = dict()
counter = 0
while mani:
    for seat in posizioni:
        predeal[seat] = mani.pop(0)
    deal = Deal.prepare(predeal)()
    counter += 1
    print(f'[Board "{counter}"]')
    print(deal._pbn_str())
