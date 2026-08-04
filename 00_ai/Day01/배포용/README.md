# AI Python Day01 - Python 기초와 데이터 다루기

SSAFY 16기 AI Python 1일차 교육생 배포 자료입니다. Python 핵심 문법과 API, JSON 흐름을 익힌 뒤 NumPy와 Pandas로 데이터를 계산, 조회, 필터, 집계합니다.

1일차 자료는 다음 역할로 구성됩니다.

- **배포용** - 환경 설정 문서, 실습 명세서, 진행 가이드, 빈칸 노트북, 실습 데이터

---

## 폴더 구조

```text
배포용/
├─ README.md
├─ 실습_1_Python_기초와_API_연결_환경_설정.pdf
├─ 실습_2_NumPy와_Pandas_환경_설정.pdf
├─ 1일차_실습_명세서.pdf
├─ 1일차_실습_가이드.pdf
├─ requirements.txt
├─ 라이브실습/
│  ├─ 라이브1_실습_빈칸.ipynb
│  └─ 라이브2_실습_빈칸.ipynb
├─ 실습1_Python기초와API연결/
│  └─ 실습1_Python기초와API연결_빈칸.ipynb
└─ 실습2_NumPy와Pandas/
   ├─ cafe_sales.csv
   └─ 실습2_NumPy와Pandas_빈칸.ipynb
```

교육생은 파일명에 `_빈칸`이 붙은 노트북을 사용합니다.

---

## 시작 순서

1. [실습*1_Python*기초와*API*연결*환경*설정.pdf](실습_1_Python_기초와_API_연결_환경_설정.pdf) - 공통 가상환경과 JupyterLab 설정
2. [실습*2_NumPy와\_Pandas*환경\_설정.pdf](실습_2_NumPy와_Pandas_환경_설정.pdf) - 라이브러리와 카페 판매 데이터 확인
3. [1일차*실습*명세서.pdf](1일차_실습_명세서.pdf) - TODO와 완료 기준 확인
4. [1일차*실습*가이드.pdf](1일차_실습_가이드.pdf) - 권장 진행 순서와 문제 해결 확인
5. `라이브 1 → 실습 1 → 라이브 2 → 실습 2` 순서로 노트북 실행

---

## 공통 실습 환경

기준 환경은 **Python 3.12.x**입니다. `requirements.txt`의 `numpy>=2.5.0`은 Python 3.12 이상에서만 설치되므로, 3.11 이하에서는 설치가 실패합니다. `python -V`로 버전을 먼저 확인해 주세요.

가상환경은 `Day01/배포용` 안에 만들지 않습니다. Windows PowerShell에서 `ai-python` 저장소 루트를 열고 `ai-python/.venv`를 생성합니다.

```powershell
python -V                      # Python 3.12.x 확인
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r .\Day01\배포용\requirements.txt
Set-Location .\Day01\배포용
python -m jupyter lab
```

`Day01/배포용` 폴더에서 PowerShell을 열었다면 공통 환경은 다음 경로로 활성화합니다.

```powershell
..\..\.venv\Scripts\Activate.ps1
```

---

## 라이브 1 - Python 핵심 문법

**배포용**

- [라이브1*실습*빈칸.ipynb](라이브실습/라이브1_실습_빈칸.ipynb) - 변수, 자료형, 조건문, 반복문, 함수, API 요청, 응답, JSON 흐름

---

## 실습 1 - Python 기초와 API 연결

**배포용**

- [실습1*Python기초와API연결*빈칸.ipynb](실습1_Python기초와API연결/실습1_Python기초와API연결_빈칸.ipynb) - Python 기초, API, JSON 데이터 추출, 모의 LLM 응답, 사용자 데이터 리포트

---

## 라이브 2 - NumPy와 Pandas

**배포용**

- [라이브2*실습*빈칸.ipynb](라이브실습/라이브2_실습_빈칸.ipynb) - NumPy 배열 연산과 통계, Pandas 조회, 필터, 집계

---

## 실습 2 - NumPy와 Pandas

**배포용**

- [실습2*NumPy와Pandas*빈칸.ipynb](실습2_NumPy와Pandas/실습2_NumPy와Pandas_빈칸.ipynb) - 카페 판매 데이터의 계산, 필터링, `groupby`, `pivot_table` 분석
- [cafe_sales.csv](실습2_NumPy와Pandas/cafe_sales.csv) - 실습 데이터

---
