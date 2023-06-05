import random

characters = ["박신빈", "윤정원", "임담희", "김용현"]
player = input("캐릭터를 선택하세요 (박신빈, 윤정원, 임담희, 김용현): ")

while player not in characters:
    print("올바른 캐릭터를 선택해주세요.")
    player = input("캐릭터를 선택하세요 (박신빈, 윤정원, 임담희, 김용현): ")

cards = random.choices(range(1, 14), k=30)

win_counts = {char: 0 for char in characters}
scores = {char: 0 for char in characters}
rounds = 4

for round_num in range(1, rounds + 1):
    random.shuffle(cards)
    if round_num == 1:
        player_order = sorted(characters)
    else:
        sorted_scores = sorted(scores.items(), key=lambda x: x[1])
        player_order = [char for char, _ in sorted_scores]

    print(f"\n============================")
    print(f"       Round {round_num} - START ")
    print(f"============================")
    print(f"게임은 {player_order}으로 진행됩니다.\n")

    print(f"======== Round {round_num} 플레이어가 뽑은 카드 ========")

    if round_num == 1:
        player_index = characters.index(player)
        for i in range(player_index, player_index + 4):
            char = characters[i % 4]
            print(f" {char} (현재 점수: {scores[char]}) ")
            card = cards.pop()
            print(f"뽑은 카드: {card}")
            scores[char] += card
    else:
        sorted_scores = sorted(scores.items(), key=lambda x: x[1])
        highest_score = sorted_scores[-1][1]
        highest_scoring_chars = [char for char, score in sorted_scores if score == highest_score]
        for char, _ in sorted_scores:
            print(f" {char} (현재 점수: {scores[char]}) ")
            card = cards.pop()
            print(f"뽑은 카드: {card}")
            lowest_card = min(cards)
            difference = card - lowest_card
            scores[char] += difference

        round_winners = [char for char in highest_scoring_chars if char in player_order]
        for winner in round_winners:
            win_counts[winner] += 1

    print(f"\n============================")
    print(f"       Round {round_num} - END ")
    print(f"============================")
    for char, score in scores.items():
        if char == player:
            char = "*" + char + "*"
        print(f"{char}: {score}")
    print()


# 총 점수를 기준으로 내림차순 정렬하되, 점수가 같은 경우에는 이름 순으로 정렬
sorted_total_scores = sorted(scores.items(), key=lambda x: (-x[1], x[0]))

print("===============================")
print("      게임순위 - 점수 ")
print("===============================")

grade_rank = 0
prev_score = float('inf')

for char, score in sorted_total_scores:
    if score < prev_score:
        grade_rank += 1
    if char == player:
        char = "*" + char + "*"
    print(f"{grade_rank}등 - {char} : {score}점")
    prev_score = score




print("===============================")
print("      게임순위 - 승리 횟수 ")
print("===============================")
sorted_win_counts = sorted(win_counts.items(), key=lambda x: (-x[1], x[0]))

win_rank = 0
prev_win_count = float('inf')

for char, win_count in sorted_win_counts:
    if win_count < prev_win_count:
        win_rank += 1
    if char == player:
        char = "*" + char + "*"
    print(f"{win_rank}등 - {char} : {win_count}번")
    prev_win_count = win_count