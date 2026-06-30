num = int(input())
deno = int(input())

try:
    if deno == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")

    print("Result:", num / deno)

except ZeroDivisionError as message:
    print(message)