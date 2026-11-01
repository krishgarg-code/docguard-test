# Car Module Documentation

## Overview
This document specifies the behavior and default settings for the `Car` class in `car.py`.

## Configuration Constants
- **Default Speed (`DEFAULT_SPEED`)**: `30` km/h (The initial speed if none is provided).
- **Maximum Speed (`MAX_SPEED`)**: `150` km/h.
- **Minimum Speed**: `0` km/h.

## Class: `Car`

### Initializer
`Car(speed: int = 30)`
- Sets the car's initial speed. Defaults to `30`.

### Methods
- `accelerate(amount: int = 10)`: Increases speed by `amount` up to `MAX_SPEED` (`150`).
- `brake(amount: int = 10)`: Decreases speed by `amount` down to `0`.
- `get_speed()`: Returns the current speed of the car.

