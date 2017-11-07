from exponential_distribution import exponential_number


class Generator:
    def __init__(self, intensity):
        self._intensity = intensity
        self._ticks_for_generate = 0

    def start_generate(self):
        self._ticks_for_generate = exponential_number(self._intensity)

    def is_generated(self):
        return self._ticks_for_generate <= 0

    def tick(self):
        if self._ticks_for_generate > 0:
            self._ticks_for_generate -= 1
