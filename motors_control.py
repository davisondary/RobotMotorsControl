"""Управление двигателями робота."""

import time


def set_motor_speed(left_speed, right_speed):
    """Устанавливает скорость левого и правого двигателей."""
    print(f"Левый двигатель: {left_speed}%")
    print(f"Правый двигатель: {right_speed}%")


def change_speed_smoothly(start_speed, end_speed, step=10):
    """Плавно изменяет скорость обоих двигателей."""
    print("Начинается плавное изменение скорости")

    for speed in range(start_speed, end_speed + step, step):
        set_motor_speed(speed, speed)
        time.sleep(0.5)

    print("Необходимая скорость достигнута")


def stop_motors():
    """Останавливает оба двигателя."""
    set_motor_speed(0, 0)
    print("Двигатели остановлены")


if __name__ == "__main__":
    print("Запуск системы управления двигателями")
    change_speed_smoothly(0, 50)
    stop_motors()
