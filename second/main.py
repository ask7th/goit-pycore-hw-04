from pathlib import Path

def get_cats_info(path) :
    file_path = Path(path)

    if not file_path.exists() or not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    cats = []
    with open(file_path, "r", encoding="utf-8") as file:
        for cat in file:
            parts = cat.strip().split(",")
            if len(parts) != 3:
                continue 
            else:
                cat_dic = {
                    "id": parts[0],
                    "name": parts[1],
                    "age": parts[2]
                }
                cats.append(cat_dic)

    return cats


cats_info = "path/to/cats.txt"
print(get_cats_info(cats_info))

print(f"\nFor wrong path:")
try:
    result = get_cats_info("wrong/path")
except FileNotFoundError as e:
    print(e) 
    result = str(e)
assert result == "File not found: wrong/path"