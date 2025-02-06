import os

my_folder = "Tables"

if not os.path.exists(my_folder):
    os.makedirs(my_folder)

for i in range(2, 21):
    file_name = f"Table_of_{i}"
    file_path = os.path.join(my_folder, file_name)

    with open(file_path, "w") as f:
        for j in range(1, 11):
            s = f"{i} x {j} = {i * j}\n"
            f.write(s)

    print(f"Created file: {file_path}")