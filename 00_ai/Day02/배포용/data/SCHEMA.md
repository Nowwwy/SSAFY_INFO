# 타이타닉 실습 데이터 스키마

Seaborn 예제 데이터 저장소에서 배포하는 `titanic.csv`의 컬럼을 설명합니다.

---

## 파일 구조

| 항목 | 내용 |
| --- | --- |
| 형식 | CSV, 쉼표 구분 |
| 데이터 크기 | 891행 × 15열 |
| 결측치가 있는 컬럼 | `age`, `embarked`, `deck`, `embark_town` |

## 컬럼

| 컬럼 | 자료형 | 설명 |
| --- | --- | --- |
| `survived` | integer | 생존 여부, 1은 생존, 0은 사망 |
| `pclass` | integer | 객실 등급, 1, 2, 3등급 |
| `sex` | string | 성별 |
| `age` | float | 나이 |
| `sibsp` | integer | 함께 탄 형제, 자매와 배우자 수 |
| `parch` | integer | 함께 탄 부모와 자녀 수 |
| `fare` | float | 운임 |
| `embarked` | string | 탑승 항구 코드, C, Q, S |
| `class` | category | 객실 등급 이름 |
| `who` | string | man, woman, child 구분 |
| `adult_male` | boolean | 성인 남성 여부 |
| `deck` | category | 객실 데크 |
| `embark_town` | string | 탑승 항구 이름 |
| `alive` | string | 생존 여부, yes, no |
| `alone` | boolean | 혼자 탑승했는지 여부 |

## 주의사항

- `survived`의 평균은 그룹별 생존율로 해석할 수 있습니다.
- `class`, `deck`은 CSV로 읽은 뒤 `category` 자료형으로 변환합니다.
- 결측치를 채우기 전에는 원본을 복사해 사본에서 전처리하세요.
