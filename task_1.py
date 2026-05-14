# Исходная строка с временными значениями
time_string = '1h 45m,360s,25m,30m 120s,2h 60s'

# Разделяем строку на отдельные временные элементы
time_elements = time_string.split(',')

# Инициализируем переменную для общего количества минут
total_minutes = 0

# Проходим по каждому элементу
for element in time_elements:
    # Убираем пробелы
    element = element.replace(' ', '')
    
    # Переменные для часов, минут и секунд
    hours = 0
    minutes = 0
    seconds = 0
    
    # Проверяем наличие часов (h)
    if 'h' in element:
        # Находим позицию 'h' и берём всё до неё
        h_index = element.find('h')
        hours = int(element[:h_index])
        # Удаляем обработанную часть из строки
        element = element[h_index + 1:]
    
    # Проверяем наличие минут (m)
    if 'm' in element:
        # Находим позицию 'm' и берём всё до неё
        m_index = element.find('m')
        minutes = int(element[:m_index])
        # Удаляем обработанную часть из строки
        element = element[m_index + 1:]
    
    # Проверяем наличие секунд (s)
    if 's' in element:
        # Находим позицию 's' и берём всё до неё
        s_index = element.find('s')
        seconds = int(element[:s_index])
    
    # Переводим всё в минуты и добавляем к общей сумме
    total_minutes += hours * 60 + minutes + seconds / 60

# Выводим результат
print(total_minutes)