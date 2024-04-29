def total_salary(path):
    try:
        with open(path, 'r') as file:
            data_list = file.readlines()
            salary_sum = 0
            number_of_workers = len(data_list)
            for line in data_list:
                _, salary_str = line.strip().split(',')
                salary_sum += float(salary_str)
            total_salary_result = (salary_sum, salary_sum / number_of_workers)
            return total_salary_result
    except (ValueError, FileNotFoundError):
        print("Файл пошкоджений або не підходить за форматом")
        return None
