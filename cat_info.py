def get_cats_info(path):
    try:
        cats_info = []
        with open(path, 'r') as file:
            for line in file:
                cat_data = line.strip().split(',')
                if len(cat_data) == 3:
                    cat = {'id': cat_data[0], 'name': cat_data[1], 'age': int(cat_data[2])}
                    cats_info.append(cat)
        return cats_info
    except (ValueError, FileNotFoundError):
        print("Файл пошкоджений або не підходить за форматом")
        return None

