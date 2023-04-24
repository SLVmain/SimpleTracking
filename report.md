# Отчет по трекеру.


### Трекер построен на основе центроидов и евклидова расстояния между ними.


Хорошо справляется с изменением параметра random_range (на сколько пикселей рамка объектов может ложно смещаться (эмуляция не идеальной детекции)


В целом приемлемо работает только тогда, когда есть детекция на каждом фрейме каждого объекта и их траектории не пересекаются. Во всех остальных случаях работает плохо.








## Эксперименты:


количество объектов
tracks_amount = 1

на сколько пикселей рамка объектов может ложно смещаться (эмуляция не идеальной детекции)
random_range = 10

с какой вероятностью объект на фрейме может быть не найдет детектором
bb_skip_percent = 0

Метрика:

Track: k=0 max_occur_value=0 amount_of_entrance=46 1.0
Overall: 1.00
______________________________________________

количество объектов
tracks_amount = 3

на сколько пикселей рамка объектов может ложно смещаться (эмуляция не идеальной детекции)
random_range = 10

с какой вероятностью объект на фрейме может быть не найдет детектором
bb_skip_percent = 0

Метрика:

Track: k=0 max_occur_value=0 amount_of_entrance=42 1.0
Track: k=1 max_occur_value=1 amount_of_entrance=31 1.0
Track: k=2 max_occur_value=2 amount_of_entrance=34 1.0
Overall: 1.00

______________________________________________


количество объектов
tracks_amount = 10

на сколько пикселей рамка объектов может ложно смещаться (эмуляция не идеальной детекции)
random_range = 10

с какой вероятностью объект на фрейме может быть не найдет детектором
bb_skip_percent = 0

Метрика:

Track: k=0 max_occur_value=7 amount_of_entrance=20 0.9090909090909091
Track: k=1 max_occur_value=4 amount_of_entrance=18 0.6206896551724138
Track: k=2 max_occur_value=8 amount_of_entrance=24 0.6153846153846154
Track: k=3 max_occur_value=6 amount_of_entrance=19 0.5588235294117647
Track: k=4 max_occur_value=4 amount_of_entrance=20 0.6451612903225806
Track: k=5 max_occur_value=8 amount_of_entrance=8 0.4
Track: k=6 max_occur_value=4 amount_of_entrance=27 0.75
Track: k=7 max_occur_value=7 amount_of_entrance=13 0.6190476190476191
Track: k=8 max_occur_value=4 amount_of_entrance=28 0.5957446808510638
Track: k=9 max_occur_value=8 amount_of_entrance=12 0.5714285714285714
Overall: 0.63

______________________________________________


количество объектов
tracks_amount = 10

на сколько пикселей рамка объектов может ложно смещаться (эмуляция не идеальной детекции)
random_range = 10

с какой вероятностью объект на фрейме может быть не найдет детектором
bb_skip_percent = .25

Метрика:

Track: k=0 max_occur_value=0 amount_of_entrance=19 0.7916666666666666
Track: k=1 max_occur_value=0 amount_of_entrance=24 0.5581395348837209
Track: k=2 max_occur_value=0 amount_of_entrance=17 0.6538461538461539
Track: k=3 max_occur_value=0 amount_of_entrance=36 0.8571428571428571
Track: k=4 max_occur_value=0 amount_of_entrance=22 0.6470588235294118
Track: k=5 max_occur_value=0 amount_of_entrance=31 0.6326530612244898
Track: k=6 max_occur_value=0 amount_of_entrance=19 0.8260869565217391
Track: k=7 max_occur_value=0 amount_of_entrance=40 0.8333333333333334
Track: k=8 max_occur_value=0 amount_of_entrance=26 0.7647058823529411
Track: k=9 max_occur_value=0 amount_of_entrance=14 0.56
Overall: 0.71
