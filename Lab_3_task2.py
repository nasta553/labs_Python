# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=','):
    # Разделяем строки по указанному разделителю и создаем множества
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))

    # находим общих участников
    common_participants = participants1.intersection(participants2)

    # Возвращаем отсортированный список общих участников
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group, "|")
print("Общие участники:", common_participants)
