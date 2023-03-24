class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.seconds = seconds
        self.minutes = minutes

    
    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
    

class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2


    def __str__(self):
        float_delta = self.clock1.get_time() - self.clock2.get_time()
        if float_delta <= 0:
            return '00: 00: 00'
        hours = str(float_delta // 3600)
        float_delta -= int(float(hours) * 3600)
        if len(hours) == 1: hours = '0' + hours

        minutes = str(float_delta // 60)
        float_delta -= int(float(minutes) * 60)
        if len(minutes) == 1: minutes = '0' + minutes

        seconds = str(float_delta)
        if len(seconds) == 1: seconds = '0' + seconds

        return hours + ': ' + minutes + ': ' + seconds
    

    def __len__(self):
        float_delta = self.clock1.get_time() - self.clock2.get_time()
        if float_delta <= 0:
            return 0
        return float_delta
    

dt = DeltaClock(Clock(2, 2, 0), Clock(2, 2, 2))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
print(len_dt)