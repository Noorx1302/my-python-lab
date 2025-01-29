def tables(n):
    table = ""
    for i in range (1, 11):
        table += f"{n} X {i} = {n*i}\n"

    with open(f"table_of_{n}.txt", "w") as f:
        f.write(table)


for i in range (2, 21):
    tables(i)