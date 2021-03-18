def appearance(intervals):
    total_match_time = 0

    # Цикл по всем отрезкам времени присутствия учителя
    for tutor_index in range(0, len(intervals['tutor']), 2):

        # Поиск пересечения времени присутствия учителя и времени занятия
        start_tutor_lesson, end_tutor_lesson, match_tutor = match_segment(intervals['lesson'][0],
                                                                          intervals['lesson'][1],
                                                                          intervals['tutor'][tutor_index],
                                                                          intervals['tutor'][tutor_index + 1])
        # Если пересечение найдено
        if match_tutor:

            # Цикл по всем отрезкам времени присутствия ученика
            for pupil_index in range(0, len(intervals['pupil']), 2):

                # Поиск пересечения времени присутствия учителя и ученика
                start_pupil_tutor, end_pupil_tutor, match_pupil_tutor = match_segment(start_tutor_lesson,
                                                                                      end_tutor_lesson,
                                                                                      intervals['pupil'][pupil_index],
                                                                                      intervals['pupil'][pupil_index + 1])
                # Если пересечение найдено
                if match_pupil_tutor:

                    # Вычисление общего временеи присутствия ученика и учителя на занятии
                    total_match_time = total_match_time + (end_pupil_tutor - start_pupil_tutor)

    return total_match_time


def match_segment(start_first, end_first, start_second, end_second):
    '''
    Функция принимает 4 аргумента:
    начало и конец первого отрезка,
    начало и конец второго отрезка.
    Возвращает при наличии пересечения общее начало, конец отрезка и True.
    При отсутствии пересечения возвращает нулевые начало, конец и False.
    '''

    start = 0
    end = 0
    match = False

    # Условие наличия пересечения отрезков
    if start_first <= end_second and start_second <= end_first:
        match = True

        # Общее начало отрезков
        if start_first >= start_second:
            start = start_first
        else:
            start = start_second

        # Общий конец отрезков
        if end_first >= end_second:
            end = end_second
        else:
            end = end_first

    return start, end, match


print(appearance({
    'lesson': [1594663200, 1594666800],
    'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
    'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
}))
