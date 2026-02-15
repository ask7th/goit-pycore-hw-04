def total_salary(path) :

    with open(path, "r", encoding="utf-8") as file:
        salaries_list = file.readlines()
        salaries = []
        for line in salaries_list:
            parts = line.strip().split(",")
            if len(parts) != 2:
                continue
            try:
                salaries.append(float(parts[1]))
            except ValueError:
                continue
        if not salaries:
            return 0, 0
        
        total = sum(salaries)
        avg_salary = total / len(salaries)
        return total, avg_salary


total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


print(f"\nFor wrong path:")
try:
    total, average = total_salary("salarys.txt")
except FileNotFoundError as e:
    print(f"File not found: {e.filename}")