import random

# 캐릭터 리스트
characters = ["박신빈", "윤정원", "임담희", "김용현"]

def play_game(selected_character):
    # 카드 덱 생성
    deck = random.choices(range(1, 14), k=30)

    # 게임 진행
    rounds = 4
    scores = {character: 0 for character in characters}

    for round_num in range(1, rounds + 1):
        print(f"\n[ Round {round_num} ]")

        # 카드 덱 섞기
        random.shuffle(deck)

        # 카드 뽑기
        round_cards = {character: None for character in characters}

        for i, character in enumerate(characters):
            card = deck.pop()
            round_cards[character] = card
            print(f"{character}가 {card}를 뽑았습니다.")

        # 승리자 결정
        max_card = max(round_cards.values())
        winners = [character for character, card in round_cards.items() if card == max_card]

        # 승리자 점수 계산
        min_card = min(round_cards.values())
        score_diff = max_card - min_card
        for winner in winners:
            scores[winner] += score_diff

        # 업데이트된 플레이어 점수 표시
        print("\n[ Updated Scores ]")
        sorted_scores = sorted(scores.items(), key=lambda x: (-x[1], x[0]))  # 승리한 횟수, 점수에 따라 정렬
        for character, score in sorted_scores:
            if character == selected_character:
                character = "*" + character + "*"
            print(f"{character}: {score}점")

    # 게임 종료 후 결과 출력
    print("\n[ Game Results ]")

    # 승리한 횟수 순서 출력
    print("\n[ Winners by Victories ]")
    sorted_victories = sorted(scores.items(), key=lambda x: (-x[1], x[0]))  # 승리한 횟수, 이름에 따라 정렬
    for character, score in sorted_victories:
        if character == selected_character:
            character = "*" + character + "*"
        print(f"{character}: {score}승")

    # 점수 순서 출력
    print("\n[ Winners by Scores ]")
    sorted_scores = sorted(scores.items(), key=lambda x: (-x[1], x[0]))  # 점수, 이름에 따라 정렬
    for character, score in sorted_scores:
        if character == selected_character:
            character = "*" + character + "*"
        print(f"{character}: {score}점")

while True:
    print("===== 캐릭터 선택 =====")
    for i, character in enumerate(characters):
        print(f"{i + 1}. {character}")

    selection = input("캐릭터를 선택하세요: ")
    if selection.isdigit() and int(selection) in range(1, len(characters) + 1):
        selected_character = characters[int(selection) - 1]
        print(f"선택한 캐릭터: {selected_character}")
        play_game(selected_character)
    else:
        print("유효하지 않은 선택입니다. 다시 선택해주세요.")

    play_again = input("게임을 다시 하시겠습니까? (y/n): ")
    if play_again.lower() != "y":
        break