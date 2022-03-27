def your_function(cases):   
    text = cases[0]  #Сначала берем из списка cases первое значение и принимаем его за text 
    reversed_text = cases[1] #Дальше делаем тоже самое только со вторым значением и это теперь у нас reversed_text
    char_list = [] # Дальше объявляем пустой список и при помощи цикла for делаем так чтоб буквы  отдельно добавлялись в список
    for c in text:
        char_list.append(c)
    char_list = [i for i in char_list if i.isalpha() == True] # После чего удаляем все символы
    char_list.reverse()  # переворачиваем
    char_list.insert(0, '!') # добавляем !
    text = char_list # после чего переводим наш список в text и превращаем его в стоку
    text1 = "".join(text)
    print(text1)
    print(reversed_text) # и все готово
    if text1 == reversed_text:
        print("Кулл")
    else:
        print("gg")


if __name__ == '__main__':    #Здесь я переписал чтоб было понятнее лично для меня 
    cases = ['!сон', '!нос']
    your_function(cases)        



