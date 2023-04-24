# Отчет по трекеру.

Команда: Сбитнева Людмила, Гринкевич Павел


### Трекер построен на основе центроидов и евклидова расстояния между ними.


Хорошо справляется с изменением параметра random_range (на сколько пикселей рамка объектов может ложно смещаться (эмуляция не идеальной детекции)


В целом приемлемо работает только тогда, когда есть детекция на каждом фрейме каждого объекта и их траектории не пересекаются. Во всех остальных случаях работает плохо.








## Эксперименты:
Провели эксперименты на 9 треках:

tracks = 3, random_range = 10, skip_percent = 0

![alt text](tracks/3_10_0.png)

tracks = 3, random_range = 10, skip_percent = 25

![alt text](tracks/3_10_25.png)

tracks = 3, random_range = 25, skip_percent = 0

![alt text](tracks/3_25_0.png)

tracks = 5, random_range = 10, skip_percent = 0

![alt text](tracks/5_10_0.png)

tracks = 5, random_range = 10, skip_percent = 25

![alt text](tracks/5_10_25.png)

tracks = 5, random_range = 25, skip_percent = 0

![alt text](tracks/5_25_0.png)

tracks = 10, random_range = 10, skip_percent = 0

![alt text](tracks/10_10_0.png)

tracks = 10, random_range = 10, skip_percent = 25

![alt text](tracks/10_10_25.png)

tracks = 10, random_range = 25, skip_percent = 0

![alt text](tracks/10_25_0.png)

## Таблица

| Tracks amount | Random range | Skip Percent | Result hungarian | Result hungarian + kalman |
|---------------|--------------|--------------|------------------|---------------------------|
| 3             | 10           | 0            | 0                | 0                         |
| 3             | 10           | 25           | 0                | 0                         |
| 3             | 25           | 0            | 0                | 0                         |
| 5             | 10           | 0            | 0                | 0                         |
| 5             | 10           | 25           | 0                | 0                         |
| 5             | 25           | 0            | 0                | 0                         |
| 10            | 10           | 0            | 0                | 0                         |
| 10            | 10           | 25           | 0                | 0                         |
| 10            | 25           | 0            | 0                | 0                         |
