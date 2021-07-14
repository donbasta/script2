import requests
import os

base = "https://xdoxd.vidstream.pro/585T8MTzQv1nefXtp+Wb3RbCTeNU6fMRs1Cpyl69TDP2ofdvzNVQuKQ+x7Ga_Lgnu5lI1_pSbhKXhWSCfVKhTBx7uLevgWiTq05VxIOMoEsPKQf5TBZQgzvEwnq8dB8X_udIWbhxd2+4sCSorpolV_mF6fqamWPfs5WCLyU6e5s/v/hls/720/"

class LimitException(Exception):
    pass

def pad_zero_front(n, cnt):
    n = str(n)
    if len(n) > cnt: 
        raise LimitException()
        return
    while len(n) < cnt:
        n = ''.join(['0', n])
    return n

current_chunk = 0
directory = "josee"
directory_path = f"./{directory}"

if not os.path.isdir(directory_path):
    os.makedirs(directory_path)

while True:
    try:
        current = pad_zero_front(current_chunk, 4)
        print(f"downloading {current}.ts ...")
        response = requests.get(f"{base}{current}.ts")
        with open(f"./{directory}/{current}.ts", "wb+") as file:
            file.write(response.content)
    except Exception as e:
        print(e)
        break
    current_chunk += 1