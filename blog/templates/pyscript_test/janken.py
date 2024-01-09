import random

HANDS = ("グー", "チョキ", "パー")


def janken(hand):
    my_hand = random.randrange(3)
    result = ("あいこ", "わたしの勝ち", "あなたの勝ち")[(hand - my_hand) % 3]
    display(f"あなた：{HANDS[hand]}、わたし：{HANDS[my_hand]}、{result}", target="result")