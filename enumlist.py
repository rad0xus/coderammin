start_value = int(input("Enter start value: "))
end_value = int(input("Enter end value: "))

with open("temp/list.txt", 'w') as file:
    for i in range(start_value, end_value + 1):
        file.write(f"{i}\n")

