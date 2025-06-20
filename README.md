# HomeWork
![Image](https://github.com/user-attachments/assets/ac807e78-3ada-4f3a-88f6-25c20e5fecf0)



본 시퀀스 다이어그램은 회원관리 프로그램을 다루고 있으며 사용자가 회원 등록, 수정, 삭제, 조회 등의 기능을 사용하는 과정을 나타낸다. 주요 모듈로는 사용자, 프로그램, 저장소가 있다.

이러한 시퀀스 다이어그램을 기반으로 'test20230540.py'를 작성하였고 이에 대한 모듈평가는 다음과 같다.

## 1. 응집도 평가

### MemberStore 클래스

- `members` 딕셔너리로 회원 데이터를 관리
- 회원 추가, 중복 검사, 수정, 삭제, 조회 기능이 모두 한 클래스 내에 모여 있음
- 모든 메서드가 “회원 데이터 관리”라는 한 곳에 집중되어 있어 응집도가 매우 높음

### main() 함수

- 사용자 입력 처리, 메뉴 출력, 결과 메시지 출력 등 포함
- 사용자와 MemberStore 간의 상호작용 흐름을 제어하는 역할
- 기능이 조금 섞여 있지만 입력 처리 및 흐름 제어라는 목적이 명확해 응집도는 중간 이상으로 판단 가능

### 종합 :`MemberStore`는 응집도가 뛰어난 모듈이며 `main()`은 적절한 응집도를 가진다


## 2. 결합도 평가

### main() 함수와 MemberStore 클래스

- `main()`에서 `MemberStore` 객체를 생성하고, `add_member()`, `update_member()` 등 메서드를 직접 호출하여 데이터를 조작함
- `main()`이 `MemberStore` 내부 구현에 대해 상세히 알 필요 없이 인터페이스를 통해서만 상호작용 함
- 두 모듈 사이의 결합도는 낮은 편이라고 볼 수 있음

### 내부 결합도

- `MemberStore` 내부 메서드들은 `members` 딕셔너리에 직접 접근하며, 클래스 내부 상태를 공유함
- 이는 자연스러운 내부 결합이며, 객체지향 설계에서 흔히 허용되는 수준임

### 종합 :`main()`과 `MemberStore` 간 결합도는 낮은 편이다.

## 3. 결론

- **응집도 :** `MemberStore`는 회원 관리라는 하나의 역할만을 잘 수행하여 높음. `main()`은 흐름 제어에 집중해 중간 이상임.
- **결합도 :** `main()`과 `MemberStore`가 메서드 인터페이스를 통해 분리되어 낮은 결합도를 유지함.
### 전반적으로 모듈 설계가 잘 되어 있음
