`collections` 모듈의 `Counter` 클래스는 주어진 시퀀스(리스트, 문자열 등)의 각 요소의 개수를 세는 데 사용됩니다. 아래는 `Counter` 클래스를 사용하여 할 수 있는 몇 가지 일반적인 작업입니다.

1. **요소 개수 세기:**
    ```python
    counts = Counter(['a', 'b', 'a', 'c', 'a', 'b'])
    print(counts)
    # 출력: Counter({'a': 3, 'b': 2, 'c': 1})
    ```

2. **가장 많이 등장하는 요소 찾기:**
    ```python
    counts = Counter(['a', 'b', 'a', 'c', 'a', 'b'])
    most_common = counts.most_common(1)
    print(most_common)
    # 출력: [('a', 3)]
    ```

3. **n개의 가장 많이 등장하는 요소 찾기:**
    ```python
    counts = Counter(['a', 'b', 'a', 'c', 'a', 'b'])
    most_common = counts.most_common(2)
    print(most_common)
    # 출력: [('a', 3), ('b', 2)]
    ```

4. **요소 추가하기:**
    ```python
    counts = Counter(['a', 'b', 'a', 'c', 'a', 'b'])
    counts['d'] += 1
    print(counts)
    # 출력: Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
    ```

5. **요소 제거하기:**
    ```python
    counts = Counter(['a', 'b', 'a', 'c', 'a', 'b'])
    del counts['a']
    print(counts)
    # 출력: Counter({'b': 2, 'c': 1})
    ```

6. **Counter 객체 병합하기:**
    ```python
    counts1 = Counter(['a', 'b', 'a', 'c', 'a', 'b'])
    counts2 = Counter(['a', 'b', 'd'])
    merged_counts = counts1 + counts2
    print(merged_counts)
    # 출력: Counter({'a': 4, 'b': 3, 'c': 1, 'd': 1})
    ```

7. **Counter 객체의 요소들 합치기:**
    ```python
    counts1 = Counter(['a', 'b', 'a', 'c', 'a', 'b'])
    counts2 = Counter(['a', 'b', 'd'])
    counts1.update(counts2)
    print(counts1)
    # 출력: Counter({'a': 4, 'b': 3, 'c': 1, 'd': 1})
    ```

`Counter` 클래스는 주어진 시퀀스에서 각 요소의 개수를 효율적으로 계산하고 다양한 유용한 작업을 수행하는 데 사용됩니다.
