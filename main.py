def binary_addition(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

# Test qilish
a = 5  # 101
b = 3  # 011
print(binary_addition(a, b))  # 110 (8)
```

```python
def binary_addition(a, b):
    max_len = max(len(bin(a)[2:]), len(bin(b)[2:]))
    a = bin(a)[2:].zfill(max_len)
    b = bin(b)[2:].zfill(max_len)
    result = ''
    carry = 0
    for i in range(max_len-1, -1, -1):
        bit_sum = carry
        bit_sum += 1 if a[i] == '1' else 0
        bit_sum += 1 if b[i] == '1' else 0
        result = ('1' if bit_sum % 2 == 1 else '0') + result
        carry = 0 if bit_sum < 2 else 1
    if carry != 0:
        result = '1' + result
    return int(result, 2)

# Test qilish
a = 5  # 101
b = 3  # 011
print(binary_addition(a, b))  # 8
