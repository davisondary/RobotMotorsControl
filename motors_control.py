"""Управление двигателями робота."""


def set_motor_speed(left_speed, right_speed):
    """Устанавливает скорость левого и правого двигателей."""
    print(f"Левый двигатель: {left_speed}%")
    print(f"Правый двигатель: {right_speed}%")


def stop_motors():
    """Останавливает оба двигателя."""
    set_motor_speed(0, 0)
    print("Двигатели остановлены")


if __name__ == "__main__":
    print("Запуск системы управления двигателями")
    set_motor_speed(50, 50)
    stop_motors()
