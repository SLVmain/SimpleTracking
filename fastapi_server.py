from fastapi import FastAPI, WebSocket
from track_7 import track_data, country_balls_amount
from collections import Counter
import asyncio
import glob
from utils import extract_boxes, from_tracker
from simple_tracker import SimpleTracker

app = FastAPI(title='Tracker assignment')
imgs = glob.glob('imgs/*')
country_balls = [{'cb_id': x, 'img': imgs[x % len(imgs)]} for x in range(country_balls_amount)]
id_obj_track_list = {}
tracked_list = []
print('Started')
simple_tracker = SimpleTracker()
def get_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def center_bb(bbox:list):
    return (bbox[0] + bbox[2] / 2, bbox[1] + bbox[3] / 2)


def tracker_soft(el):
    """
    Необходимо изменить у каждого словаря в списке значение поля 'track_id' так,
    чтобы как можно более длительный период времени 'track_id' соответствовал
    одному и тому же кантри болу.

    Исходные данные: координаты рамки объектов

    Ограничения:
    - необходимо использовать как можно меньше ресурсов (представьте, что
    вы используете embedded устройство, например Raspberri Pi 2/3).
    -значение по ключу 'cb_id' является служебным, служит для подсчета метрик качества
    вашего трекера, использовать его в алгоритме трекера запрещено
    - запрещается присваивать один и тот же track_id разным объектам на одном фрейме
    """

    frame_data = el['data']  # frame_data:list
    frame_id = el['frame_id']

    if frame_id == 1:  # первоначальные айди присваиваем
        for i, obj in enumerate(frame_data):  # obj:dict
            obj['track_id'] = i
            bbox = obj['bounding_box']
            if bbox:
                obj['center'] = center_bb(bbox)
            else:
                obj['center'] = ()
        return {'frame_id': frame_id, 'data': frame_data}

    for i, obj in enumerate(frame_data):  # obj:dict

        bbox = obj['bounding_box']
        if bbox:
            obj['center'] = center_bb(bbox)
        else:
            obj['center'] = ()

    prev_frame = tracked_list[-1]['data']
    current_frame = frame_data
    distans_list = []
    for i, cr_obj in enumerate(current_frame):
        if cr_obj['center']:
            distans_list = []
            for j, pr_obj in enumerate(prev_frame):
                if pr_obj['center']:
                    dist = get_distance(pr_obj['center'], cr_obj['center'])
                    elem = (dist, pr_obj['track_id'])
                    # print(elem)
                    distans_list.append(elem)

        if distans_list:
            d_list = [x[0] for x in distans_list]
            tr_list = [x[1] for x in distans_list]
            idx_min = d_list.index(min(d_list))
            cr_obj['track_id'] = tr_list[idx_min]

    return {'frame_id': frame_id, 'data': current_frame}


def tracker_strong(el):
    """
    Необходимо изменить у каждого словаря в списке значение поля 'track_id' так,
    чтобы как можно более длительный период времени 'track_id' соответствовал
    одному и тому же кантри болу.

    Исходные данные: координаты рамки объектов, скриншоты прогона

    Ограничения:
    - вы можете использовать любые доступные подходы, за исключением
    откровенно читерных, как например захардкодить заранее правильные значения
    'track_id' и т.п.
    - значение по ключу 'cb_id' является служебным, служит для подсчета метрик качества
    вашего трекера, использовать его в алгоритме трекера запрещено
    - запрещается присваивать один и тот же track_id разным объектам на одном фрейме

    P.S.: если вам нужны сами фреймы, измените в index.html значение make_screenshot
    на true для первого прогона, на повторном прогоне можете читать фреймы из папки
    и по координатам вырезать необходимые регионы.
    TODO: Ужасный костыль, на следующий поток поправить
    """
    if el['frame_id'] == 1:
        # mapping elements like (index_tracker, index_service)
        mapping, boxes = extract_boxes(el['data'])
        simple_tracker.initialize(boxes)
        el['data'] = from_tracker(el['data'], simple_tracker.previous_state, mapping)
        return el

    mapping, boxes = extract_boxes(el['data'])
    if len(boxes) == 0:  # 0 non-empty boxes
        return el
    simple_tracker.get_iou(boxes)
    matches, unmatched_detections, unmatched_trackers = simple_tracker.estimate_hungarian()
    new_state = simple_tracker.update_states(boxes, matches, unmatched_detections)

    for cb in new_state:
        bbox_cb = cb['bbox'].tolist()
        for i, cb_service in enumerate(el['data']):
            if bbox_cb == cb_service['bounding_box']:
                el['data'][i]['track_id'] = cb['track_id']

    return el

def make_track_for_obj(el):

    global id_obj_track_list
    for obj in el['data']:
        if obj['cb_id'] in id_obj_track_list:
            id_obj_track_list[obj['cb_id']].append(obj['track_id'])
        else:
            id_obj_track_list[obj['cb_id']] = [obj['track_id']]


def calc_tracker_metrics(id_obj_track_list):
    #print(id_obj_track_list)
    right_track = 0
    total_len = 0
    for k, v in id_obj_track_list.items():
        occurence_count = Counter(v)
        max_occur_value, amount_of_entrance = occurence_count.most_common(1)[0]
        if max_occur_value is None:
            amount_of_entrance = 0
        right_track += amount_of_entrance
        total_len += len(v)
        print(f'Track: {k=} {max_occur_value=} {amount_of_entrance=} {amount_of_entrance/len(v)}')
    print(f'Overall: {right_track/total_len:.02f}')

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    print('Accepting client connection...')
    await websocket.accept()
    # отправка служебной информации для инициализации объектов
    # класса CountryBall на фронте
    await websocket.send_text(str(country_balls))
    for el in track_data:
        await asyncio.sleep(0.5)
        # TODO: part 1
        #el = tracker_soft(el)
        tracked_list.append(el)
        #print(el)
        # TODO: part 2
        el = tracker_strong(el)
        tracked_list.append(el)
        # отправка информации по фрейму
        await websocket.send_json(el)
        make_track_for_obj(el)
    calc_tracker_metrics(id_obj_track_list)

    print('Bye..')
