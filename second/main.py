from pathlib import Path

def get_cats_info(path) :
    file_path = Path(path)

    cats = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for cat in file:
                parts = cat.strip().split(",")

                if len(parts) != 3:
                    return "File is corrupted"
                
                try:
                    int(parts[2]) #перевіряю на число, хоча вік зберігаю як str, як у прикладі. Якщо не здійснити таку перевірку, то у вік можна покласти довільний str 
                except ValueError:
                    return "File is corrupted"
                
                cat_dic = {
                    "id": parts[0],
                    "name": parts[1],
                    "age": parts[2]
                }
                cats.append(cat_dic)
    except FileNotFoundError:
        return "File not found"
         
    except UnicodeDecodeError:
        return "File is corrupted"
    
    return cats


cats_info = "path/to/cats.txt"
print(get_cats_info(cats_info))


assert get_cats_info("wrong/path") == "File not found"
assert get_cats_info("path/err_data.txt") == "File is corrupted"