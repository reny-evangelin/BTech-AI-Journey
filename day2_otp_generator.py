import random

while True:
    num = random.randint(1000, 9999)
    print(num)

    if num % 7 == 0:
        print(f"Found your lucky OTP: {num}")
        break
