# task 1 Створіть функцію для обчислення факторіала числа. Запустіть декілька завдань, використовуючи Thread, і заміряйте швидкість їхнього виконання,
# а потім заміряйте швидкість обчислення, використовуючи той же набір завдань на ThreadPoolExecutor. Як приклади використовуйте останні значення,
# від мінімальних і до максимально можливих, щоб побачити приріст або втрату продуктивності.

import threading
import time
from concurrent.futures import ThreadPoolExecutor

def facto_rial(n):
    # n = int(input("Введіть число: "))
    factorial = 1
    for i in range (2 , n + 1):
        factorial *= i
    # print(f"Факторіал числа {n} є:", factorial)

start_time1 = time.time()
facto_rial(678)
facto_rial(789)
facto_rial(890)
print(time.time() - start_time1)

start_time2 = time.time()
stream1 = threading.Thread(target=facto_rial, args=(678,))
stream2 = threading.Thread(target=facto_rial, args=(789,))
stream3 = threading.Thread(target=facto_rial, args=(890,))
stream1.start()
stream2.start()
stream3.start()
print(time.time() - start_time2)

start_time3 = time.time()
stream1.join()
stream2.join()
stream3.join()
print(time.time() - start_time3)

start_time4 = time.time()

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(facto_rial, 678),
               executor.submit(facto_rial, 789),
               executor.submit(facto_rial, 890)]

print(time.time() - start_time3)

# task 2 Створіть три функції, одна з яких читає файл на диску із заданим ім'ям та перевіряє наявність рядка «Wow!».
# Якщо файлу немає, то засипає на 5 секунд, а потім знову продовжує пошук по файлу. Якщо файл є, то відкриває його і шукає рядок «Wow!».
# За наявності цього рядка закриває файл і генерує подію, а інша функція чекає на цю подію і у разі її виникнення виконує видалення цього файлу.
# Якщо рядки «Wow!» не було знайдено у файлі, то засипати на 5 секунд. Створіть файл руками та перевірте виконання програми.

import threading
import time

event = threading.Event()

def read_file():
    with open('wow.txt', 'r') as f:
        a = f.read()
        print(a)
        if "Wow" in a:
            print("Знайдено 'Wow!' в файлі!")
            event.set()
        else:
            print("Рядок 'Wow!' не знайдений, чекаю 5 секунд...")
            start_time = time.time()
            time.sleep(5)
            print(time.time() - start_time)

def delete_file():
    pass


file_content = read_file()
print(file_content)

reader_thread = threading.Thread(target=read_file)
deleter_thread = threading.Thread(target=delete_file)

reader_thread.start()
deleter_thread.start()

reader_thread.join()
deleter_thread.join()
