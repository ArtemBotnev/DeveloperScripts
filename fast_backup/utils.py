# Fast backup
# Copyright Artem Botnev 2019
# MIT License

import time


class Timer:
    _start_time = 0
    _finish_time = 0

    def start(self):
        self._start_time = time.time()
        return self

    def stop(self):
        self._finish_time = time.time()
        return self

    def show_time(self):
        _time = self._finish_time - self._start_time
        sec = float(_time) % 60
        sec_string = format('%.2f seconds' % sec)
        minutes = int(_time) // 60
        minutes_string = ''
        hours_string = ''
        if minutes > 0:
            hours = minutes // 60
            minutes %= 60
            minutes_string = format('%d minutes ' % minutes)
            if hours > 0:
                hours_string = format('%d hours ' % hours)

        return 'It has taken ' + hours_string + minutes_string + sec_string


class DataMeasure:
    
    @staticmethod
    def show_data_size(count):
        m = ['bytes', 'kB', 'mB', 'gB']

        for s in m:
            result = count / 1024
            if result < 1:
                if s == 'bytes':
                    return format('%.0f %s' % (count, s))
                else:
                    return format('%.3f %s' % (count, s))
            else:
                count = result

        return format('%.3f tB' % count)
