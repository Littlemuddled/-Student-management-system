base_dir = './files/'


def read_file(filename):
    try:
        with open(base_dir + filename, 'r', encoding='utf8') as file:
            content = file.read()
            return content
    except FileExistsError:
        print('文件打开失败')


def write_json(filename, data):
    with open(base_dir + filename, 'w', encoding='utf8') as file:
        import json
        json.dump(data, file)


def read_json(filename, default_data):
    try:
        with open(base_dir + filename, 'r', encoding='utf8') as file:
            import json
            return json.load(file)
    except FileExistsError:
        print('文件打开失败')
        return default_data
