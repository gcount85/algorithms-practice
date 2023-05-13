import base64

# 바이너리 데이터를 Base64 인코딩
data = b'Hello, world!'  # type: bytes
print(data)
encoded_data = base64.b64encode(data)  # type: bytes
print(f'Encoded data: {encoded_data}')  # Encoded data: b'SGVsbG8sIHdvcmxkIQ=='

# Base64 인코딩된 데이터를 디코딩
decoded_data = base64.b64decode(encoded_data)  # type: bytes
print(f'Decoded data: {decoded_data}')  # b'Hello, world!'


"""
html에서 이런 식으로 표현 가능
<img src="data:image/png;base64,iVBORw0KGg..." />

"""
