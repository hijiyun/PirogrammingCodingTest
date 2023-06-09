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
    if round_num == 1:
        # 1라운드에서는 캐릭터 이름을 오름차순으로 정렬하여 순서대로 카드를 뽑음
        player_order = sorted(characters)
    else:
        # 점수가 낮은 순서대로 정렬하기 위해 (캐릭터, 점수) 튜플 리스트를 생성하고, 점수에 따라 정렬
        sorted_scores = sorted(scores.items(), key=lambda x: x[1])
        # 정렬된 캐릭터 리스트를 생성
        player_order = [char for char, _ in sorted_scores]
        
    print(f" \n============================")
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
        for char, _ in sorted_scores:
            print(f" {char} (현재 점수: {scores[char]}) ")
            card = cards.pop()
            print(f"뽑은 카드: {card}")
            lowest_card = min(cards)
            difference = card - lowest_card
            scores[char] += difference

    print(f" \n============================")
    print(f"       Round {round_num} - END ")
    print(f"============================")
    for char, score in scores.items():
        if char == player:
            char = "*" + char + "*"
        print(f"{char}: {score}")
    print()

total_scores = {char: 0 for char in characters}
# 각 캐릭터의 총 점수 계산
total_scores = {char: sum(scores[char] for char in scores) for char in characters}
# 총 점수를 기준으로 내림차순 정렬하여 순위 매기기
sorted_total_scores = sorted(total_scores.items(), key=lambda x: x[1], reverse=True)

print("=============================")
print("      게임순위 - 총 점수 ")
print("=============================")
rank = 1
prev_score = None
for char, score in sorted_total_scores:
    if prev_score is None or score < prev_score:
        rank += 1
    if char == player:
        char = "*" + char + "*"
    print(f"{rank}등: {char} - 총 점수: {score}")
    prev_score = score

print("==================================")
print("      게임순위 - 승리 횟수 ")
print("==================================")
# 각 캐릭터의 승리 횟수 계산
win_counts = {char: 0 for char in characters}
for _ in range(rounds):
    max_score = max(scores.values())
    winners = [char for char, score in scores.items() if score == max_score]
    for winner in winners:
        win_counts[winner] += 1
        scores[winner] = -1  # 승자의 점수를 -1로 설정하여 중복 승리를 방지

# 승리 횟수를 기준으로 내림차순 정렬하여 순위 매기기
sorted_win_counts = sorted(win_counts.items(), key=lambda x: x[1], reverse=True)

rank = 1
prev_count = None
for char, count in sorted_win_counts:
    if prev_count is None or count < prev_count:
        rank += 1
    if char == player:
        char = "*" + char + "*"
    print(f"{rank}등: {char} - 승리 횟수: {count}")
    prev_count = count
print()