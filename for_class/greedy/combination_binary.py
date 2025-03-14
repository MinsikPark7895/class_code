arr = ['A', 'B', 'C']
n = len(arr)

def get_sub(tar):
    print(f'target = {tar}', end='/')
    for i in range(n):
        # 각각 원소가 포함되어 있나요?
        # 1도 되고, 0b1도 되고, 0x1도 되는데 왜 0x1이냐?
        # -> 비트 연산임을 명시하고 권장하는 방법
        if tar & 0x1:    #
            print(arr[i], end='')
        tar >>= 1        # 맨 우측 비트를 삭제한다
                         # == 다음 원소를 확인하겠다

for target in range(1 << n):
    get_sub(target)
    print()


