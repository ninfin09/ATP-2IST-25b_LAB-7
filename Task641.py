def check_sublist(main_list, sub_list):
    main_str = str(main_list).strip('[]')
    sub_str = str(sub_list).strip('[]')
    
    return sub_str in main_str

list_1 = list(map(int, input("Список: ").split()))
list_2 = list(map(int, input("Шукаємо: ").split()))

print(check_sublist(list_1, list_2))