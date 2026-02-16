def total_salary(path) :
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries_list = file.readlines()
            salaries = []
            for line in salaries_list:
                parts = line.strip().split(",")
                if len(parts) != 2:
                    return("File is corrupted")
                                  
                try:
                    salaries.append(float(parts[1]))
                except ValueError:
                    return("File is corrupted")                
                
            if not salaries:
                return 0, 0
            
            total = sum(salaries)
            avg_salary = total / len(salaries)
            return total, avg_salary
    
    except FileNotFoundError:
        return("File not found")
         
    except UnicodeDecodeError:
        return("File is corrupted")
     

result = total_salary("salary.txt")
if isinstance(result, tuple):
    total, average = result
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
else:
    print(result)


assert total_salary("salarys.txt") == "File not found"
assert total_salary("err_data.txt") == "File is corrupted"