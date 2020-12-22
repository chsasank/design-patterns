import time
from datetime import datetime


class Subject(object):
    """Maintains state data and notifies observers to change."""
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(changed_subject=self)


class Observer(object):
    """Updates based on state data in Subject."""
    def __init__(self):
        pass

    def update(self, changed_subject):
        pass


class ClockTimer(Subject):
    """Store and maintain the time of day.""" 
    def __init__(self):
        self.time = datetime.now()
        super().__init__()

    def get_hour(self):
        return self.time.hour

    def get_minute(self):
        return self.time.minute

    def get_second(self):
        return self.time.second

    def tick(self):
        """Called by an internal timer to provide accurate time base."""
        self.time = datetime.now()
        self.notify()


class DigitalClock(Observer):
    """Digital clock observer for ClockTimer."""
    def __init__(self, clock_timer):
        super().__init__()
        self.subject = clock_timer
        self.subject.attach(observer=self)

    def __delete__(self):
        self.subject.detach(Observer=self)
        super().__delete__()

    def update(self, changed_subject):
        """Overrides the update of Observer."""
        if changed_subject == self.subject:
            self.draw()

    def draw(self):
        print(f"Drew digital timer for {self.subject.get_hour()}:"
              f"{self.subject.get_minute()}:{self.subject.get_second()}")


class AnalogClock(DigitalClock):
    """Same as Digital clock except change in the draw."""
    def draw(self):
        print(f"Drew analog timer for {self.subject.get_hour()}:"
              f"{self.subject.get_minute()}:{self.subject.get_second()}")


if __name__ == "__main__":
    timer = ClockTimer()
    analog_clock = AnalogClock(timer)
    digital_clock = DigitalClock(timer)

    # tick will automatically draw both analog and digital clock
    for _ in range(10):
        timer.tick()
        time.sleep(2)
