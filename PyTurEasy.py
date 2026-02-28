import turtle

# Скрытая настройка холста и пера
_экран = turtle.Screen()
_т = turtle.Turtle()
_т.speed(7)

# Переводчик цветов для русской души
_РУ_ЦВЕТА = {
    "красный": "red", "синий": "blue", "зеленый": "green", 
    "желтый": "yellow", "черный": "black", "белый": "white",
    "оранжевый": "orange", "фиолетовый": "purple", "розовый": "pink",
    "серый": "gray", "голубой": "cyan", "золотой": "gold"
}

class Command:
    def __init__(self, action):
        self.action = action

    def PyTurEasy(self, *args):
        # Магия перевода: если передали русский цвет — подменяем его
        обработанные = [(_РУ_ЦВЕТА[a.lower()] if isinstance(a, str) and a.lower() in _РУ_ЦВЕТА else a) for a in args]
        self.action(*обработанные)
        return self

# Базовые движения
вперед = Command(_т.forward)
назад = Command(_т.backward)
влево = Command(_т.left)
вправо = Command(_т.right)

# Настройки стиля
цвет = Command(_т.color)
размер = Command(_т.pensize)
фон = Command(_экран.bgcolor)

# Рисование
круг = Command(_т.circle)
точка = Command(_т.dot)
поднять = Command(_т.up)
опустить = Command(_т.down)

# Финишная команда
стоп = Command(turtle.done)
