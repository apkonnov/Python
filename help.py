# Консоль
# dir([object]) - Список имен объекта, а если объект не указан, список имен в текущей локальной области видимости.
dir('Text')

# help([object]) - Вызов встроенной справочной системы.
help(len)

# Встроенные функции
import builtins

dir(builtins)

# ключевые слова
import keyword

keyword.kwlist
