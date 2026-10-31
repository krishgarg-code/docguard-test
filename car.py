"""Car simulation module."""

DEFAULT_SPEED = 30
MAX_SPEED = 120


class Car:
    """Represents a vehicle with speed control."""

    def __init__(self, speed: int = DEFAULT_SPEED):
        self.speed = speed

    def accelerate(self, amount: int = 10) -> int:
        """Accelerate the car by a given amount up to MAX_SPEED."""
        self.speed = min(self.speed + amount, MAX_SPEED)
        return self.speed

    def brake(self, amount: int = 10) -> int:
        """Slow down the car by a given amount."""
        self.speed = max(self.speed - amount, 0)
        return self.speed

    def get_speed(self) -> int:
        """Return the current speed."""
        return self.speed
