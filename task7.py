# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            print(x, 'or', y, 'or', z, '=', x, 'and', y, 'and', z,'  ',x or y or z == x and y and z)
