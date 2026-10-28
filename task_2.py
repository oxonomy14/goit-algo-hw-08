'''
Завдання 2

Напишіть алгоритм (функцію), який знаходить суму всіх значень у двійковому дереві пошуку або в AVL-дереві. Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.
'''
from module.binary_search_tree import Node, insert, sum_tree


# Додаємо вузли до дерева
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

#root = delete(root, 7)
print(root)



# Обчислення суми
total = sum_tree(root)

print(f"Сума всіх значень дерева: {total}")