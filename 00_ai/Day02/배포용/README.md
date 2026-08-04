# AI Python Day02 - 데이터 시각화, 전처리와 EDA

SSAFY 16기 AI Python 2일차 교육생 배포 자료입니다. Matplotlib과 Seaborn으로 데이터의 특징을 시각화하고, 결측치, 이상치 처리와 값 변환을 거쳐 Titanic 데이터의 탐색적 데이터 분석을 완성합니다.

2일차 자료는 다음 역할로 구성됩니다.

- **배포용** - 환경 확인 문서, 실습 명세서, 진행 가이드, 빈칸 노트북, Titanic 데이터

---

## 폴더 구조

```text
배포용/
├─ README.md
├─ 실습_3_EDA와_시각화_전처리_환경_설정.pdf
├─ 2일차_실습_명세서.pdf
├─ 2일차_실습_가이드.pdf
├─ requirements.txt
├─ 라이브실습/
│  └─ 라이브3_실습_빈칸.ipynb
├─ 실습3_EDA와시각화/
│  └─ 실습3_EDA와시각화_빈칸.ipynb
└─ data/
   ├─ titanic.csv
   ├─ SCHEMA.md
   └─ SOURCE.md
```

교육생은 파일명에 `_빈칸`이 붙은 노트북을 사용합니다.

---

## 시작 순서

1. [실습*3_EDA와*시각화*전처리*환경\_설정.pdf](실습_3_EDA와_시각화_전처리_환경_설정.pdf) - 공통 가상환경, 패키지, 한글 폰트, 데이터 확인
2. [2일차*실습*명세서.pdf](2일차_실습_명세서.pdf) - TODO와 완료 기준 확인
3. [2일차*실습*가이드.pdf](2일차_실습_가이드.pdf) - 권장 진행 순서와 문제 해결 확인
4. `라이브 3 → 실습 3` 순서로 노트북 실행

---

## 공통 실습 환경

2일차에는 새 가상환경을 만들지 않습니다. Windows PowerShell에서 `ai-python` 저장소 루트를 열고 1일차에 만든 `ai-python/.venv`를 다시 활성화합니다. `requirements.txt`는 1일차와 내용이 같으므로, 이미 설치를 마쳤다면 `pip check`로 확인만 하고 넘어가도 됩니다.

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r .\Day02\배포용\requirements.txt
python -m pip check
Set-Location .\Day02\배포용
python -m jupyter lab
```

`Day02/배포용` 폴더에서 PowerShell을 열었다면 공통 환경은 다음 경로로 활성화합니다.

```powershell
..\..\.venv\Scripts\Activate.ps1
```

---

## Titanic 데이터

노트북은 `seaborn.load_dataset("titanic")` → 원격 CSV → 배포된 `data/titanic.csv` 순서로 데이터를 불러옵니다. 사내망이나 오프라인 환경에서도 `data` 폴더를 함께 두면 실습을 이어갈 수 있습니다.

- 891행 15컬럼, 결측치는 `age` 177건, `deck` 688건, `embarked` 2건
- 컬럼 설명은 [SCHEMA.md](data/SCHEMA.md), 출처는 [SOURCE.md](data/SOURCE.md)를 확인합니다.
- 로컬 CSV로 불러오면 `deck`이 문자열 타입이므로, `.cat` 접근자를 쓰기 전에 `df["deck"] = df["deck"].astype("category")`가 필요합니다.

---

## 라이브 3 - 데이터 시각화와 전처리

**배포용**

- [라이브3*실습*빈칸.ipynb](라이브실습/라이브3_실습_빈칸.ipynb) - Matplotlib, Seaborn 차트, 결측치, 이상치 처리, 정규화, 인코딩, 구간화

---

## 실습 3 - EDA와 시각화

**배포용**

- [실습3*EDA와시각화*빈칸.ipynb](실습3_EDA와시각화/실습3_EDA와시각화_빈칸.ipynb) - Titanic 데이터 구조 확인, 시각화, 집계, 결측치 처리, 특성 공학
- [titanic.csv](data/titanic.csv), [SCHEMA.md](data/SCHEMA.md), [SOURCE.md](data/SOURCE.md) - 로컬 데이터, 구조와 출처

---
