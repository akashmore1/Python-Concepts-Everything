def prime_checker(number):
    if number == 1:
        print("It's neither prime nor composite number")
        return
    if number == 2:
        print("It's a prime number.")
        return

    if number % 2 == 0:
        print("It's not a prime number.")
        return

    divisor = 3
    while divisor < (number/2) + 0.5:
        if number % divisor == 0:
            print("It's not a prime number.")
            return
        divisor += 1

    print("It's a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
