## Python 타입 힌트(Type Hints) 사용 예

### 변수에 타입 힌트 추가하기

```python
age: int = 25  # age 변수가 정수임을 명시
name: str = "Alice"  # name 변수가 문자열임을 명시
scores: list = [90, 80, 70]  # scores 변수가 리스트임을 명시
```

### 함수 매개변수와 반환 값에 타입 힌트 추가하기

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
# 이 함수는 문자열 매개변수를 받아 문자열을 반환한다는 것을 명시
```

### 리스트와 같은 컨테이너 타입에 타입 힌트 사용하기

```python
from typing import List

def get_top_scores(scores: List[int], top: int) -> List[int]:
    return sorted(scores, reverse=True)[:top]
# 이 함수는 정수 리스트를 매개변수로 받고, 정렬된 정수 리스트의 상위 N개를 반환
```

### 선택적(Optional) 값에 대한 타입 힌트

```python
from typing import Optional

def find_employee(id: int) -> Optional[str]:
    if id in employee_database:
        return employee_database[id]
    else:
        return None
# 이 함수는 직원 ID를 기반으로 직원 이름을 찾아 반환하거나, 찾지 못했을 때는 None을 반환
```

### 함수가 아무것도 반환하지 않을 때(None을 반환할 때)

```python
def log_message(message: str) -> None:
    print(f"Log: {message}")
# 이 함수는 로그 메시지를 출력만 하고, 명시적으로 아무것도 반환하지 않음(None).
```
