# Задание 1: Реализация простой хэш-таблицы
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        key = str(key)
        hash_value = 0
        prime = 31
        for i, c in enumerate(key):
            hash_value += ord(c) * (prime ** i)
        return hash_value % self.size

    def insert(self, key, value):
        hash_idx = self._hash(key)
        for item in self.table[hash_idx]:
            if item[0] == key:
                item[1] = value
                return True
        self.table[hash_idx].append([key, value])
        return False

    def get(self, key):
        hash_idx = self._hash(key)
        for item in self.table[hash_idx]:
            if item[0] == key:
                return item[1]
        return

    def delete(self, key):
        hash_idx = self._hash(key)
        bucket = self.table[hash_idx]
        for i, item in enumerate(bucket):
            if item[0] == key:
                bucket.pop(i)
                return 'OK'
        return 'NOT_FOUND'

    def __str__(self):
        result = []
        for i, bucket in enumerate(self.table):
            if bucket:
                result.append(f"{i}: {bucket}")
        return "\n".join(result)


# ht = HashTable()
# ht.insert('apple', 5)
# ht.insert('pineapple', 3)
# print(ht.get('apple'))
# print(ht.get('pineapple'))
# ht.delete('apple')
# print(ht.get('apple'))
# print(ht)


# Задание 2: Поиск дубликатов в массиве


# def get_dublicates(lis: list):
#     value_count = dict()
#     for i in lis:
#         if i in value_count:
#             value_count[i] += 1
#         else:
#             value_count[i] = 1

#     return [key for key, value in value_count.items() if value > 1]


from collections import Counter


def get_dublicates(lis: list):
    return [key for key, value in Counter(lis).items() if value > 1]


# print(get_dublicates([3, 5, 2, 3, 8, 5]))


# Задание 3: Подсчет частоты слов в тексте


def get_dublicate_words(string: str):
    return dict(Counter(string.split()))


# print(get_dublicate_words('hello world hello'))
