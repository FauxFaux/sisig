import numpy as np


class Source(object):
    @staticmethod
    def tone(freq: int, sample_rate: int, time: float) -> "ToneSource":
        return ToneSource(freq, sample_rate, time)


class ToneSource(Source):
    def __init__(self, freq: int, rate: int, time: float):
        self.freq = freq
        self.rate = rate
        self.samples = round(rate * time)
