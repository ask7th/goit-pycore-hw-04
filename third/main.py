import sys
from pathlib import Path
from log_inf import log_error, color_file, color_dir, color_root

def show_dir(path=".", prefix=""):
    dir_path = Path(path)

    if not dir_path.exists() or not dir_path.is_dir():
        error_msg = f"File not found: {dir_path}"
        log_error(error_msg)
        return {"error": error_msg}
    
    if prefix == "":
        print(color_root(f"{dir_path.name}/"))

    items = [item for item in dir_path.iterdir() if not item.name.startswith(".")]
    items.sort(key=lambda x: (x.is_file(), x.name.lower()))

    if not items:
        return {"path": str(dir_path.absolute()), "contents": []}

    result = []
    for index, item in enumerate(items):
        last = index == len(items) - 1
        connector = "└──" if last else "├──"

        if item.is_file():
            line = f"{prefix}{connector} {item.name}"
            print(color_file(line))
            result.append({
                "name": item.name,
                "type": "file"
            })
        elif item.is_dir():
            line = f"{prefix}{connector} {item.name}/"
            print(color_dir(line))
            extension = "    " if last else "│   "
            sub_result = show_dir(item, prefix + extension)
            result.append({
                "name": item.name,
                "type": "dir",
                "contents": sub_result.get("contents") if sub_result else []
            })

    return {"path": str(dir_path.absolute()), "contents": result}


if __name__ == "__main__":
    folder_path = sys.argv[1] if len(sys.argv) > 1 else "."
    result = show_dir(folder_path)

    print("\nFor wrong path:")
    wrong_result = show_dir("wrong/path")
    assert wrong_result.get("error") == "File not found: wrong/path"
