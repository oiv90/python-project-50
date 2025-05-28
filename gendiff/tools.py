import json


def read_file(filepath):
    with open(filepath, 'r') as f:
        return f.read()
    

def determine_data_type(filepath):
    if filepath.endswith('.json'):
        return 'json'


def read_data(raw_data, data_type):
    if data_type == 'json':
        return json.loads(raw_data)
    

def format_value(value):
    """Форматирует значение для вывода"""
    if isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return value
    else:
        return str(value)


def generate_difference(file1, file2, format):
    file1_data = read_data(
        read_file(file1), 
        determine_data_type(file1)
    )
    file2_data = read_data(
        read_file(file2), 
        determine_data_type(file2)
    )
    
    # Получаем все уникальные ключи из обоих файлов
    all_keys = sorted(set(file1_data.keys()) | set(file2_data.keys()))
    
    result_lines = ["{"]
    
    for key in all_keys:
        key1_exists = key in file1_data
        key2_exists = key in file2_data
        
        if key1_exists and key2_exists:
            # Ключ есть в обоих файлах
            value1 = file1_data[key]
            value2 = file2_data[key]
            
            if value1 == value2:
                # Значения одинаковые - без префикса
                result_lines.append(f"    {key}: {format_value(value1)}")
            else:
                # Значения разные - сначала из первого файла, потом из второго
                result_lines.append(f"  - {key}: {format_value(value1)}")
                result_lines.append(f"  + {key}: {format_value(value2)}")
        elif key1_exists:
            # Ключ есть только в первом файле
            result_lines.append(f"  - {key}: {format_value(file1_data[key])}")
        else:
            # Ключ есть только во втором файле
            result_lines.append(f"  + {key}: {format_value(file2_data[key])}")
    
    result_lines.append("}")
    
    return "\n".join(result_lines)