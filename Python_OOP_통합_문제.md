# Python OOP & Exception 확인 문제 (통합)

> 대상: 비전공자 Python 학습자
> 범위 ①  OOP 1 — 절차/객체지향 · 클래스 · 인스턴스 · 클래스변수/인스턴스변수 · 생성자 · 인스턴스/클래스/스태틱 메서드 · 이름공간 · 매직 메서드 · 데코레이터
> 범위 ②  OOP 2 & Exception — 상속 · 오버라이딩 · super() · 다중 상속 · MRO · 에러/예외 · try-except-else-finally · EAFP/LBYL
> 구성: 객관식 15문항 · 주관식 5문항 · 서술형 2문항 (총 22문항)

---

## Ⅰ. 객관식 (15문항)

**1.** 다음 중 클래스(class)를 정의하는 올바른 방법은?

- a) `define Student:`
- b) `def class Student():`
- c) `class = Student`
- d) `class Student:`

<br>

**2.** 객체 지향 프로그래밍(OOP)에 대한 설명으로 옳은 것은?

- a) 데이터와 함수를 철저히 분리하여 순서대로만 실행하는 방식이다
- b) 데이터(속성)와 기능(메서드)을 하나의 객체로 묶어 관리하는 방식이다
- c) 전역 변수만 사용해 작성하는 방식이다
- d) 반복문을 전혀 사용하지 않는 프로그래밍 방식이다

<br>

**3.** 다음 중 클래스와 인스턴스에 대한 설명으로 **옳지 않은 것**은?

- a) 클래스는 객체를 만들기 위한 설계도이다
- b) 인스턴스는 클래스를 통해 만들어진 실제 객체이다
- c) 하나의 클래스로는 오직 하나의 인스턴스만 만들 수 있다
- d) 클래스는 변수와 메서드를 포함할 수 있다

<br>

**4.** 다음 중 인스턴스 메서드를 정의하는 방법으로 올바른 것은?

- a) `def method():`
- b) `def method(self):`
- c) `def method(cls):`
- d) `@staticmethod` 를 붙인 `def method():`

<br>

**5.** 다음 중 클래스 변수에 대한 설명으로 **옳지 않은 것**은?

- a) 모든 인스턴스가 공유한다
- b) 클래스 내부에서 직접 정의된다
- c) `클래스명.변수명` 형태로 접근할 수 있다
- d) 인스턴스마다 서로 다른 개별 값을 가진다

<br>

**6.** 다음 중 스태틱 메서드(static method)의 특징으로 옳은 것은?

- a) 객체(인스턴스) 없이도 호출할 수 있다
- b) 첫 번째 인자로 반드시 `self`를 받는다
- c) 반드시 인스턴스를 통해서만 호출할 수 있다
- d) 인스턴스 속성을 자동으로 수정한다

<br>

**7.** 인스턴스 메서드, 클래스 메서드, 스태틱 메서드가 **첫 번째 인자로 자동으로 받는 것**을 순서대로 옳게 짝지은 것은?

- a) self - cls - (없음)
- b) cls - self - (없음)
- c) (없음) - self - cls
- d) self - (없음) - cls

<br>

**8.** 다음 코드의 실행 결과는?

```python
class Person:
    name = 'unknown'   # 클래스 변수

    def talk(self):
        print(self.name)

p1 = Person()
p2 = Person()
p2.name = 'Kim'        # p2에만 인스턴스 변수 생성

p1.talk()
p2.talk()
```

- a) unknown / unknown
- b) unknown / Kim
- c) Kim / Kim
- d) 에러 발생

<br>

**9.** 상속(Inheritance)에 대한 설명으로 옳은 것은?

- a) 한 클래스(부모)의 속성과 메서드를 다른 클래스(자식)가 물려받는 것
- b) 같은 이름의 메서드를 매개변수만 다르게 여러 개 정의하는 것
- c) 예외가 발생했을 때 프로그램을 강제 종료시키는 것
- d) 프로그램 실행 중 버그를 찾아 수정하는 과정

<br>

**10.** `Animal` 클래스를 상속받는 `Dog` 클래스를 올바르게 정의한 것은?

- a) `class Dog: Animal`
- b) `class Dog(Animal):`
- c) `class Dog -> Animal:`
- d) `class Dog inherits Animal:`

<br>

**11.** 메서드 오버라이딩(Overriding)에 대한 설명으로 옳은 것은?

- a) 같은 이름의 메서드를 매개변수만 다르게 여러 개 정의하는 것
- b) 부모 클래스의 메서드를 자식 클래스에서 같은 이름·같은 파라미터 구조로 재정의하는 것
- c) 부모 클래스의 속성을 완전히 삭제하는 것
- d) 두 개 이상의 클래스를 동시에 상속받는 것

<br>

**12.** 다음 코드의 실행 결과는?

```python
class Animal:
    def sound(self):
        print('동물 소리')

class Cat(Animal):
    def sound(self):
        print('야옹')

c = Cat()
c.sound()
```

- a) 동물 소리
- b) 야옹
- c) 동물 소리 / 야옹 (두 줄 모두 출력)
- d) 에러 발생

<br>

**13.** `super()`를 사용하는 주된 이유로 옳은 것은?

- a) 예외를 처리하기 위해
- b) 명시적으로 부모 클래스 이름을 적지 않고도 부모 클래스의 메서드를 호출하기 위해
- c) 반복문을 더 빠르게 실행하기 위해
- d) 딕셔너리에 키가 존재하는지 확인하기 위해

<br>

**14.** 다음 코드의 실행 결과는?

```python
class Person:
    def __init__(self, name):
        self.name = name

class Mom(Person):
    gene = 'XX'

class Dad(Person):
    gene = 'XY'

class Child(Dad, Mom):
    pass

baby = Child('아가')
print(baby.gene)
```

- a) XX
- b) XY
- c) None
- d) 에러 발생

<br>

**15.** 다음 코드 실행 시 발생하는 예외는?

```python
my_dict = {'name': 'Alice'}
print(my_dict['age'])
```

- a) IndexError
- b) ValueError
- c) KeyError
- d) TypeError

---

## Ⅱ. 주관식 (5문항)

**16.** 인스턴스가 생성될 때 자동으로 호출되어 인스턴스 변수의 초기값을 설정하는 특별한 메서드(생성자 메서드)의 **이름**을 쓰시오.

<br>

**17.** 다음 코드의 출력 결과를 쓰시오.

```python
class Calc:
    @staticmethod
    def double(n):
        return n * 2

print(Calc.double(7))
```

<br>

**18.** 다음 빈칸에 들어갈 내장 함수를 쓰시오.

```python
class Student(Person):
    def __init__(self, name, age, student_id):
        ________.__init__(name, age)
        self.student_id = student_id
```

<br>

**19.** 다음 코드 실행 시 발생하는 예외의 이름을 정확히 쓰시오.

```python
nums = [10, 20, 30]
print(nums[5])
```

<br>

**20.** 다음 두 예외 처리 접근 방식의 약어(영문 대문자)를 각각 쓰시오.

- (1) "일단 실행해 보고, 예외가 발생하면 그때 처리한다" (try-except 중심) → ________
- (2) "실행하기 전에 조건문 등으로 미리 검사한다" (if-else 중심) → ________

---

## Ⅲ. 서술형 (2문항)

**21.** 인스턴스 메서드 · 클래스 메서드 · 스태틱 메서드의 차이를, **각 메서드가 첫 번째 인자로 받는 것(self / cls / 없음)** 과 **주된 용도**를 포함하여 서술하시오.

<br>

**22.** 여러 개의 `except` 절을 사용할 때, **구체적인 예외(예: `ZeroDivisionError`)를 먼저 쓰고 범용 예외(`Exception`)를 마지막에 써야 하는 이유**를 서술하시오.
