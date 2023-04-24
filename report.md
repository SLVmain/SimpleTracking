# Отчет по трекеру.

Команда: Сбитнева Людмила, Гринкевич Павел


### Спавнение двух трекеров: IOU + Hungarian и IOU + Hungarian + Kalman



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
| 3             | 10           | 0            | 1.00             | 0.92                      |
| 3             | 10           | 25           | 0.24             | 0.52                      |
| 3             | 25           | 0            | 0.85             | 0.81                      |
| 5             | 10           | 0            | 0.66             | 0.56                      |
| 5             | 10           | 25           | 0.10             | 0.41                      |
| 5             | 25           | 0            | 0.81             | 0.60                      |
| 10            | 10           | 0            | 0.56             | 0.37                      |
| 10            | 10           | 25           | 0.23             | 0.29                      |
| 10            | 25           | 0            | 0.61             | 0.32                      |

## Выводы

### Хорошо справляется с изменением параметра random_range (на сколько пикселей рамка объектов может ложно смещаться (эмуляция не идеальной детекции)


### В целом хорошо работают только тогда, когда есть детекция на каждом фрейме каждого объекта и их траектории не пересекаются. В остальных случаях работают хуже.

### Самые сложные условия для трекера, это увеличение bb_skip_percent, метрики сразу падают.

### Интересно, что при увеличении bb_skip_percent существенно лучше работает трекер iou+hungarian+kalman,
### но при bb_skip_percent = 0, лучше метрики у iou+hungarian

...
