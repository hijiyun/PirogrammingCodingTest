import random

characters = ["박신빈", "윤정원", "임담희", "김용현"]
player = input("캐릭터를 선택하세요 (박신빈, 윤정원, 임담희, 김용현): ")

while player not in characters:
    print("올바른 캐릭터를 선택해주세요.")
    player = input("캐릭터를 선택하세요 (박신빈, 윤정원, 임담희, 김용현): ")

cards = random.choices(range(1, 14), k=30)

scores = {char: 0 for char in characters}
rounds = 4

for round_num in range(1, rounds + 1):
    random.shuffle(cards)
    print(f"====== Round {round_num} ======")

    if round_num == 1:
        player_index = characters.index(player)
        for i in range(player_index, player_index + 4):
            char = characters[i % 4]
            print(f"{char} 플레이어의 차례입니다.")
            card = cards.pop()
            print(f"{char} 플레이어가 {card}를 뽑았습니다.")
            scores[char] += card
    else:
        sorted_scores = sorted(scores.items(), key=lambda x: x[1])
        for char, _ in sorted_scores:
            print(f"{char} 플레이어의 차례입니다. (점수: {scores[char]})")
            card = cards.pop()
            print(f"{char} 플레이어가 {card}를 뽑았습니다.")
            lowest_card = min(cards)
            difference = card - lowest_card
            scores[char] += difference

    print("라운드 종료")
    print("=================================")
    print(f"      Round {round_num} - END              ")
    print("=================================")
    print(f"현재 점수: {scores}")

round_win_count = {char: 0 for char in characters}

for char in characters:
    round_win_count[char] = sum(1 for _, score in sorted_scores if score == scores[char])

sorted_win_counts = sorted(round_win_count.items(), key=lambda x: (x[1], x[0]), reverse=True)

print("--- 게임 종료 ---")
print("승리 횟수 순서:")
for char, count in sorted_win_counts:
    if char == player:
        char = "*" + char + "*"
    print(f"{char}: {count}승")

print("\n점수 순서:")
for char, score in sorted_scores:
    if char == player:
        char = "*" + char + "*"
    print(f"{char}: {score}점")