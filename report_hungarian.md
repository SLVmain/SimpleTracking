## TRACKER STRONG

## Трекер использует IOU и венгерский алгоритм.

## Эксперименты:

Самые простые случаи, bb_skip_percent = 0:

количество объектов
tracks_amount = 1

на сколько пикселей рамка объектов может ложно смещаться (эмуляция не идеальной детекции)
random_range = 10

с какой вероятностью объект на фрейме может быть не найдет детектором
bb_skip_percent = 0

Метрика:

Track: k=0 max_occur_value=1 amount_of_entrance=40 0.8695652173913043
Overall: 0.87
______________________________________________

количество объектов
tracks_amount = 3

на сколько пикселей рамка объектов может ложно смещаться (эмуляция не идеальной детекции)
random_range = 10

с какой вероятностью объект на фрейме может быть не найдет детектором
bb_skip_percent = 0

Метрика:

Track: k=0 max_occur_value=0 amount_of_entrance=43 1.0\
Track: k=1 max_occur_value=1 amount_of_entrance=32 1.0\
Track: k=2 max_occur_value=2 amount_of_entrance=35 1.0\
Overall: 1.00

______________________________________________


количество объектов
tracks_amount = 10

на сколько пикселей рамка объектов может ложно смещаться (эмуляция не идеальной детекции)
random_range = 10

с какой вероятностью объект на фрейме может быть не найдет детектором
bb_skip_percent = 0

Метрика:

Track: k=0 max_occur_value=0 amount_of_entrance=22 1.0\
Track: k=1 max_occur_value=32 amount_of_entrance=12 0.41379310344827586\
Track: k=2 max_occur_value=34 amount_of_entrance=19 0.48717948717948717\
Track: k=3 max_occur_value=3 amount_of_entrance=30 0.8823529411764706\
Track: k=4 max_occur_value=8 amount_of_entrance=11 0.3548387096774194\
Track: k=5 max_occur_value=21 amount_of_entrance=5 0.25\
Track: k=6 max_occur_value=33 amount_of_entrance=21 0.5833333333333334\
Track: k=7 max_occur_value=7 amount_of_entrance=13 0.6190476190476191\
Track: k=8 max_occur_value=11 amount_of_entrance=27 0.574468085106383\
Track: k=9 max_occur_value=31 amount_of_entrance=5 0.23809523809523808\
Overall: 0.55

______________________________________________

Добавим bb_skip_percent = .1

количество объектов
tracks_amount = 10\
на сколько пикселей рамка объектов может ложно смещаться (эмуляция не идеальной детекции)\
random_range = 10\
с какой вероятностью объект на фрейме может быть не найдет детектором\
bb_skip_percent = 0.1\

Track: k=0 max_occur_value=39 amount_of_entrance=18 0.4090909090909091\
Track: k=1 max_occur_value=26 amount_of_entrance=14 0.4375\
Track: k=2 max_occur_value=28 amount_of_entrance=16 0.43243243243243246\
Track: k=3 max_occur_value=27 amount_of_entrance=11 0.36666666666666664\
Track: k=4 max_occur_value=23 amount_of_entrance=17 0.37777777777777777\
Track: k=5 max_occur_value=4 amount_of_entrance=10 0.2564102564102564\
Track: k=6 max_occur_value=29 amount_of_entrance=14 0.34146341463414637\
Track: k=7 max_occur_value=25 amount_of_entrance=7 0.2916666666666667\
Track: k=8 max_occur_value=17 amount_of_entrance=19 0.5\
Track: k=9 max_occur_value=37 amount_of_entrance=13 0.4482758620689655\
Overall: 0.39\

Увеличим bb_skip_percent = 0.15\

Track: k=0 max_occur_value=28 amount_of_entrance=5 0.25\
Track: k=1 max_occur_value=1 amount_of_entrance=4 0.16\
Track: k=2 max_occur_value=25 amount_of_entrance=15 0.32608695652173914\
Track: k=3 max_occur_value=3 amount_of_entrance=14 0.35\
Track: k=4 max_occur_value=1 amount_of_entrance=11 0.2972972972972973\
Track: k=5 max_occur_value=21 amount_of_entrance=14 0.6363636363636364\
Track: k=6 max_occur_value=31 amount_of_entrance=13 0.29545454545454547\
Track: k=7 max_occur_value=26 amount_of_entrance=9 0.3333333333333333\
Track: k=8 max_occur_value=58 amount_of_entrance=12 0.2553191489361702\
Track: k=9 max_occur_value=23 amount_of_entrance=12 0.375\
Overall: 0.32\

Увеличим bb_skip_percent = 0.20\

Track: k=0 max_occur_value=53 amount_of_entrance=14 0.2\
Track: k=1 max_occur_value=1 amount_of_entrance=16 0.16326530612244897\
Track: k=2 max_occur_value=31 amount_of_entrance=26 0.3333333333333333\
Track: k=3 max_occur_value=50 amount_of_entrance=21 0.27631578947368424\
Track: k=4 max_occur_value=1 amount_of_entrance=20 0.2631578947368421\
Track: k=5 max_occur_value=22 amount_of_entrance=5 0.10416666666666667\
Track: k=6 max_occur_value=1 amount_of_entrance=10 0.20833333333333334\
Track: k=7 max_occur_value=1 amount_of_entrance=14 0.21212121212121213\
Track: k=8 max_occur_value=1 amount_of_entrance=18 0.32142857142857145\
Track: k=9 max_occur_value=36 amount_of_entrance=12 0.16666666666666666\
Overall: 0.23

______________________________________________
Еще увеличим до bb_skip_percent = .25

Метрика:

Track: k=0 max_occur_value=2 amount_of_entrance=30 0.2857142857142857\
Track: k=1 max_occur_value=1 amount_of_entrance=21 0.28\
Track: k=2 max_occur_value=1 amount_of_entrance=13 0.21666666666666667\
Track: k=3 max_occur_value=1 amount_of_entrance=12 0.2\
Track: k=4 max_occur_value=49 amount_of_entrance=18 0.15\
Track: k=5 max_occur_value=1 amount_of_entrance=33 0.3548387096774194\
Track: k=6 max_occur_value=1 amount_of_entrance=39 0.325\
Track: k=7 max_occur_value=1 amount_of_entrance=24 0.18604651162790697\
Track: k=8 max_occur_value=1 amount_of_entrance=33 0.2391304347826087\
Track: k=9 max_occur_value=1 amount_of_entrance=36 0.25\
Overall: 0.25\

# Выводы:
## Хорошо справляется с изменением параметра random_range (на сколько пикселей рамка объектов может ложно смещаться (эмуляция не идеальной детекции)
## Сложнее с пересечением путей и пропусками детектора.
## В целом справляется со сложными условиями, намного лучше простого варианта 
## на центроидах и евклидовой дистанции
