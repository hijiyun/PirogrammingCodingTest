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
    print(f"--- Round {round_num} ---")

    for char in characters:
        if round_num == 1:
            print(f"{char} 플레이어의 차례입니다.")
        else:
            print(f"{char} 플레이어의 차례입니다. (점수: {scores[char]})")

        card = cards.pop()
        print(f"{char} 플레이어가 {card}를 뽑았습니다.")

        if round_num == 1:
            scores[char] += card
        else:
            lowest_card = min(cards)
            difference = card - lowest_card
            scores[char] += difference

    round_winner = max(characters, key=lambda x: scores[x])
    round_winners = [char for char in characters if scores[char] == scores[round_winner]]

    print("라운드 종료")
    print(f"이번 라운드 승리자: {', '.join(round_winners)}")
    print("===============================")
    print(f"Round {round_num} - END")
    print("===============================")
    print(f"점수: {scores}")

sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
sorted_winners = sorted(scores.items(), key=lambda x: (x[1], x[0]))

print("--- 게임 종료 ---")
print("승리 횟수 순서:")
for char, score in sorted_winners:
    if char == player:
        char = "*" + char + "*"
    print(f"{char}: {score}승")

print("\n점수 순서:")
for char, score in sorted_scores:
    if char == player:
        char = "*" + char + "*"
    print(f"{char}: {score}점")
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