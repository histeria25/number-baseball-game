import random


COMMENTARY_LINES = [
    "🎙️ 현재 타석에 들어섰습니다... 집중하세요!",
    "🎙️ 투수, 사인을 확인하고 힘차게 던집니다!",
    "🎙️ 관중석이 술렁입니다... 이번 공의 결과는?",
    "🎙️ 긴장감 최고조! 배트를 짧게 잡았습니다.",
    "🎙️ 승부의 한가운데, 침착하게 숫자를 고르세요!",
]


def print_banner():
    print("\n" + "═" * 54)
    print("⚾️  숫자 야구 게임에 오신 것을 환영합니다!  ⚾️")
    print("═" * 54)
    print("📌 규칙: 0~9 사이 서로 다른 숫자 3개를 맞혀보세요.")
    print("📌 결과: ?스트라이크 ?볼 ?아웃 형태로 안내됩니다.\n")


def print_result(strikes, balls, outs, attempts):
    print("─" * 54)
    print(f"📊 {strikes}스트라이크 {balls}볼 {outs}아웃   |   시도 {attempts}회")
    if strikes == 0 and balls == 0:
        print("\n🔥🔥🔥  아웃(Out)!  🔥🔥🔥")
    print("─" * 54)


def generate_answer():
    return random.sample(range(10), 3)


def evaluate_guess(answer, guess):
    strikes = sum(1 for i in range(3) if guess[i] == answer[i])
    balls = sum(1 for num in guess if num in answer) - strikes
    return strikes, balls


def parse_guess(text):
    text = text.strip()
    if len(text) != 3:
        return None, "⚠️ 경고: 반드시 3자리 숫자를 입력하세요."
    if not text.isdigit():
        return None, "⚠️ 경고: 숫자만 입력할 수 있습니다."

    guess = [int(ch) for ch in text]
    if len(set(guess)) != 3:
        return None, "⚠️ 경고: 중복된 숫자는 사용할 수 없습니다."
    return guess, None


def ask_replay():
    while True:
        answer = input("다시 플레이하시겠습니까? (y/n): ").strip().lower()
        if answer in ("y", "n"):
            return answer == "y"
        print("⚠️ 경고: y 또는 n만 입력해주세요.\n")


def play_game():
    answer = generate_answer()
    attempts = 0
    max_attempts = 10

    print_banner()
    print(f"🎯 제한 횟수: {max_attempts}번 안에 맞혀야 합니다!\n")

    while attempts < max_attempts:
        print(random.choice(COMMENTARY_LINES))
        user_input = input("숫자 3개 입력: ")
        guess, warning = parse_guess(user_input)

        if guess is None:
            print(f"{warning} 예) 527\n")
            continue

        attempts += 1
        strikes, balls = evaluate_guess(answer, guess)
        outs = 3 - (strikes + balls)
        print_result(strikes, balls, outs, attempts)

        if strikes == 3:
            print("\n🏆 홈런! 3스트라이크로 경기를 끝냈습니다!")
            print(f"✅ 정답입니다! {attempts}번 만에 맞췄어요.\n")
            return

    answer_text = "".join(str(num) for num in answer)
    print("\n💥 GAME OVER")
    print(f"10번 안에 맞추지 못했습니다. 컴퓨터 숫자는 {answer_text}였습니다.\n")


def main():
    while True:
        play_game()
        if not ask_replay():
            print("👋 게임을 종료합니다. 다음에 또 도전하세요!")
            break
        print("\n🔁 새로운 게임을 시작합니다!\n")


if __name__ == "__main__":
    main()