import hashlib

# base58 알파벳 정의
BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'


def base58_encode(data):
    num = int.from_bytes(data, 'big')
    # print(num)
    base58_string = ''

    while num > 0:
        num, remainder = divmod(num, 58)  # 58로 숫자를 계속 나누며 나머지로 인코딩
        base58_string = BASE58_ALPHABET[remainder] + base58_string

    zero_bytes = 0
    for byte in data:  # 앞 자리수에 연속되는 0 개수만큼 1을 덧붙임(base58_alphabet[0])
        if byte == 0:
            zero_bytes += 1
        else:
            break

    return '1' * zero_bytes + base58_string


data = b'hello, base58!'
hash_obeject = hashlib.sha256(data)
hash_bytes = hash_obeject.digest()
result = base58_encode(hash_bytes)

print(f"원본 데이터: {data}")
print(f"SHA-256 해시: {hash_bytes.hex()}")
print(f"Base58 인코딩 결과: {result}")
