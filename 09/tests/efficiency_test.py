import time
import cjson
import ujson
import json

start_time = time.time()
with open('test.txt', 'r') as file:
    for line in file:
        loaded_dict = cjson.loads(line)
        dumped_string = cjson.dumps(loaded_dict)

end_time = time.time()
elapsed_time = (end_time - start_time) * 1000  # Преобразование в миллисекунды
print(f"Время выполнения программы с библиотекой cjson: {elapsed_time:.3f} мс")

start_time = time.time()
with open('test.txt', 'r') as file:
    for line in file:
        loaded_dict = ujson.loads(line)
        dumped_string = ujson.dumps(loaded_dict)
end_time = time.time()
elapsed_time = (end_time - start_time) * 1000  # Преобразование в миллисекунды
print(f"Время выполнения программы с библиотекой ujson: {elapsed_time:.3f} мс")

start_time = time.time()
with open('test.txt', 'r') as file:
    for line in file:
        loaded_dict = json.loads(line)
        dumped_string = json.dumps(loaded_dict)
end_time = time.time()
elapsed_time = (end_time - start_time) * 1000  # Преобразование в миллисекунды
print(f"Время выполнения программы с библиотекой json: {elapsed_time:.3f} мс")
