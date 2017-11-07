from exponential_distribution import exponential_number


class Channel:
    def __init__(self, intensity):
        self._intensity = intensity
        self._ticks_for_process = 0
        self.work_time = 0
        self.processed_claims = 0
        self.is_first_claim = True

    def add(self):
        self._ticks_for_process = exponential_number(self._intensity)
        if self.is_first_claim:
            self.is_first_claim = False
        else:
            self.processed_claims += 1

    def is_processed(self):
        return self._ticks_for_process <= 0

    def tick(self):
        if self._ticks_for_process > 0:
            self._ticks_for_process -= 1
            self.work_time += 1
