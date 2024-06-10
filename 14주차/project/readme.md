# 로또 번호 생성기 GUI 애플리케이션    
이 문서는 tkinter를 사용하여 로또 번호를 생성하고 이를 GUI 창에 표시하는 애플리케이션의 코드를 설명합니다. 이 애플리케이션은 1부터 45 사이의 무작위 숫자 6개를 생성하여 사용자에게 보여줍니다.

## 제작 동기
수업시간에 배운 내용들 중에 어떤 부분을 활용하여 프로젝트를 진행할지 많이 고민하였다. 수업시간에 배운 내용중에 random모듈이 가장 흥미로웠고 가장 최근에 배운 내용이 함수였다. 그래서 두 파트를 합쳐보고 전에 독학해보았던 GUI영역을 합쳐보니 로또 번호 생성기 GUI 애플리케이션이 가장 먼저 생각에 들어왔다. 프로젝트를 진행하며 전공인 인공지능과도 예측에 있어서 연계성이 살짝 있는 것 같다고 느꼈다. 실제 AI모델에서는 대용량의 데이터를 활용하고 random.randint 보다 더 고급진 알고리즘을 사용하여서 만들겠지만 살짝이나마 비슷한 점이 있었던 것 같았다.

## 코드 설명
### 모듈 임포트
필요한 모듈들을 임포트 합니다
```py
import random
import tkinter as tk
```
- random: 난수 생성을 위한 모듈입니다.
- tkinter: GUI 애플리케이션을 만들기 위한 모듈입니다.

### 로또 번호 생성 함수(make_rand_num)
로또 번호를 생성하는 함수입니다
```py
def make_rand_num():
    return [random.randint(1, 45) for _ in range(6)]
```
- make_rand_num 함수는 1부터 45 사이의 무작위 정수 6개를 생성하여 리스트로 반환합니다.

### 번호 생성 버튼 클릭 이벤트 핸들러
버튼을 클릭했을 때 실행될 함수를 정의합니다.
```py
def generate_numbers():
    numbers = make_rand_num()
    result_label.config(text=f'이번주 로또 당첨번호는 {numbers} 입니다.')
```
- generate_numbers 함수는 make_rand_num 함수를 호출하여 로또 번호를 생성하고, 결과 레이블에 이를 표시합니다.

### 메인 애플리케이션 창 생성
tkinter를 사용하여 GUI 요소들을 설정합니다.
```py
root = tk.Tk()
root.title("로또 번호 생성기")
```
- root: 메인 애플리케이션 창을 생성하고, 창의 제목을 "로또 번호 생성기"로 설정합니다.

### 안내 레이블 생성 및 배치
사용자에게 안내 메시지를 표지하는 레이블을 생성합니다.
```py
instruction_label = tk.Label(root, text="버튼을 눌러 로또 번호를 생성하세요:")
instruction_label.pack(pady=10)
```
- instruction_label: 사용자에게 안내 메시지를 표시하는 레이블을 생성하고, 여백을 추가하여 창에 배치합니다.

### 결과 레이블 생성 및 배치
로또 번호를 표시할 레이블을 생성합니다.
```py
result_label = tk.Label(root, text="")
result_label.pack(pady=10)
```
- result_label: 생성된 로또 번호를 표시할 레이블을 생성하고, 여백을 추가하여 창에 배치합니다.

### 번호 생성 버튼 생성 및 배치
번호를 생성하는 버튼을 생성합니다.
```py
generate_button = tk.Button(root, text="번호 생성", command=generate_numbers)
generate_button.pack(pady=10)
```
- generate_button: "번호 생성" 버튼을 생성하고, 클릭 시 generate_numbers 함수를 호출하도록 설정합니다. 버튼은 창에 배치됩니다.

### 메인 루프 시작
GUI 애플리케이션의 메인 루프를 시작합니다.
```py
root.mainloop()
```
- root.mainloop(): 애플리케이션이 종료될 때까지 GUI 이벤트 루프를 실행합니다.

## 실행방법

- 터미널을 이용할 경우
```
python3 main.py
```

- vscode / pycharm을 이용할 경우    
실행 버튼을 클릭

## 실행결과
![alt text](<images/버튼클릭전 상태.png>)

![alt text](<images/버튼1회클릭 후 상태.png>)

![alt text](<images/버튼2회클릭 후 상태.png>)

![alt text](<images/창을 닫고 난 뒤 터미널 화면.png>)