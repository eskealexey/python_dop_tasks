# Определите класс Student с атрибутами для имени студента и списком курсов, на которые он записан.
# Методы класса должны позволять добавлять и удалять курсы из списка.

class Student:
    def __init__(self, name, kurs = []):
        self.name = name
        self.kurs = kurs


    def add_kurs(self, name_kurs):
        self.kurs.append(name_kurs)


    def delete_kurs(self, name_kurs):
        self.kurs.remove(name_kurs)

    def __str__(self):
        return f'{'*' * 30}\nСтудент: {self.name} \nСписок курсов - {self.kurs}'


st = Student('Alex', ['Java'])
print(st)
st.add_kurs('Python')
print(st)
st.add_kurs('PHP')
print(st)
st.delete_kurs('PHP')
print(st)
st.add_kurs('C++')
print(st)
st2 = Student('Pavel', ['Java', 'Python', 'PHP'])
print(st2)