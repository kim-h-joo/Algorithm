# [Bronze II] 소수 찾기 - 1978 

[문제 링크](https://www.acmicpc.net/problem/1978) 

### 성능 요약

메모리: 34536 KB, 시간: 36 ms

### 분류

소수 판정, 정수론, 수학

### 제출 일자

2025년 1월 3일 22:59:22

### 문제 설명

<p>주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.</p>

### 출력 

 <p>주어진 수들 중 소수의 개수를 출력한다.</p>

***

### 참고 내용
<https://velog.io/@changhee09/알고리즘-소수의-판별-에라토스테네스의-체>

<br>

```python
# 한 줄로 입력받은 숫자를 리스트로 저장
numbers = list(map(int, input().split()))
``` 

* split() : 공백으로 구분된 입력 값을 분리하여 문자열 리스트 생성
    * split(",") : 콤마(,)로 구분
* map() : 문자열 리스트의 각 요소를 int로 변환
    * map(function, iterable, ...)
    * function : 각 요소에 적용할 함수
    * iterable : 반복 가능한 객체  
* list() : 변환된 값을 리스트로 저장
