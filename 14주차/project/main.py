import random
import tkinter as tk

def make_rand_num():
    """
    1부터 45 사이의 랜덤한 숫자 6개를 생성하여 리스트로 반환하는 함수.

    이 함수는 로또 번호와 같은 랜덤한 숫자들을 생성하는 데 사용됩니다. 
    1부터 45 사이의 정수 중에서 중복되지 않은 6개의 숫자를 랜덤으로 선택합니다.f

    반환값:
        List[int]: 1부터 45 사이의 랜덤한 정수 6개를 담고 있는 리스트.
    """
    # 리스트 컴프리헨션을 사용하여 1부터 45 사이의 난수 6개를 생성합니다.
    return [random.randint(1, 45) for _ in range(6)]

def generate_numbers():
    # 로또 번호 생성
    numbers = make_rand_num()
    # 레이블에 로또 번호 표시
    result_label.config(text=f'이번주 로또 당첨번호는 {numbers} 입니다.')

# 메인 애플리케이션 창 생성
root = tk.Tk()
root.title("로또 번호 생성기")

# 안내 레이블
instruction_label = tk.Label(root, text="버튼을 눌러 로또 번호를 생성하세요:")
instruction_label.pack(pady=10)

# 결과 레이블
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# 번호 생성 버튼
generate_button = tk.Button(root, text="번호 생성", command=generate_numbers)
generate_button.pack(pady=10)

# 메인 루프 시작
root.mainloop()
