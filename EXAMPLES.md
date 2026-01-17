# Examples and Tutorials

## Пример 1: Исследование Mandelbrot

### Шаг за шагом

1. **Запустите приложение**
   ```bash
   python main.py
   ```

2. **Выберите Mandelbrot**
   - Найдите розовый пончик с надписью "Mandelbrot"
   - Кликните на него

3. **Исследуйте главную кардиоиду**
   - Центр находится в точке (0, 0)
   - Медленно увеличивайте масштаб
   - Наблюдайте повторяющиеся паттерны

4. **Найдите долину морских коньков**
   - Переместитесь к точке (-0.75, 0.1)
   - Увеличьте масштаб в 100 раз
   - Насладитесь спиральными структурами

5. **Сохраните результат**
   - Нажмите кнопку "💾 Save"
   - Выберите место сохранения

## Пример 2: Создание коллекции Julia

### Исследование различных параметров

```python
# Интересные параметры для Julia Set
parameters = [
    {"name": "Dendrite", "c": (-0.4, 0.6)},
    {"name": "Dragon", "c": (-0.8, 0.156)},
    {"name": "Douady Rabbit", "c": (-0.123, 0.745)},
]

# Для каждого параметра:
# 1. Выберите Julia Set
# 2. Измените параметр C в настройках
# 3. Исследуйте и сохраните
```

## Пример 3: 3D Mandelbulb тур

### Лучшие углы обзора

1. **Фронтальный вид**
   - Rotation X: 0°, Y: 0°
   - Zoom: 3.0
   - Power: 8

2. **Вид сверху**
   - Rotation X: 90°, Y: 0°
   - Zoom: 2.5
   - Power: 8

3. **Диагональный вид**
   - Rotation X: 45°, Y: 45°
   - Zoom: 2.8
   - Power: 8

## Пример 4: Создание художественного изображения

### Настройка для лучшего качества

1. **Откройте config.json**
   ```json
   {
     "rendering": {
       "max_iterations": 1024,
       "quality": "ultra",
       "antialiasing": true
     },
     "window": {
       "width": 2560,
       "height": 1440
     }
   }
   ```

2. **Выберите цветовую схему**
   ```json
   {
     "colors": {
       "default_scheme": "galaxy"
     }
   }
   ```

3. **Найдите интересную область**
   - Используйте малое количество итераций для поиска
   - Когда найдете - увеличьте итерации

4. **Сохраните в высоком разрешении**

## Пример 5: Программное использование

### Использование фракталов в своем коде

```python
from src.fractals.fractal_2d.mandelbrot import Mandelbrot
import numpy as np

# Создание экземпляра
mandelbrot = Mandelbrot()

# Генерация координат
x = np.linspace(-2, 1, 1000)
y = np.linspace(-1.5, 1.5, 1000)

# Вычисление фрактала
result = mandelbrot.calculate(x, y, max_iter=256)

# result теперь содержит массив значений итераций
print(f"Shape: {result.shape}")
print(f"Min iterations: {result.min()}")
print(f"Max iterations: {result.max()}")
```

### Создание анимации

```python
from src.rendering.renderer_2d import Renderer2D
from PyQt6.QtCore import QSize

# Создание рендерера
renderer = Renderer2D(QSize(800, 600), config)

# Анимация зума
for zoom in range(1, 100):
    renderer.zoom = zoom
    image = renderer.render_mandelbrot(max_iter=256)
    image.save(f"frame_{zoom:03d}.png")
    
# Используйте FFmpeg для создания видео:
# ffmpeg -i frame_%03d.png -c:v libx264 -r 30 output.mp4
```

## Пример 6: Кастомная цветовая схема

### Создание собственной палитры

```python
import numpy as np
from PyQt6.QtGui import QColor

def custom_colormap(value, max_value):
    """
    Создает RGB цвет на основе значения итерации
    
    Args:
        value: Количество итераций (0 to max_value)
        max_value: Максимальное количество итераций
    
    Returns:
        Tuple (r, g, b)
    """
    if value >= max_value:
        return (0, 0, 0)  # Черный для точек в множестве
    
    # Нормализация значения
    t = value / max_value
    
    # Пользовательский градиент
    r = int(255 * np.sin(t * np.pi * 2))
    g = int(255 * np.cos(t * np.pi * 3))
    b = int(255 * np.sin(t * np.pi * 4 + np.pi/2))
    
    return (abs(r), abs(g), abs(b))

# Использование в renderer
# Модифицируйте метод apply_colormap в renderer_2d.py
```

## Пример 7: Batch рендеринг

### Создание множества изображений

```python
from src.fractals.fractal_registry import FractalRegistry
from src.rendering.renderer_2d import Renderer2D

# Получить все 2D фракталы
fractals = FractalRegistry.get_2d_fractals()

# Рендерить каждый
for name, info in fractals.items():
    print(f"Rendering {name}...")
    
    renderer = Renderer2D(QSize(1920, 1080), config)
    image = renderer.render(info, max_iterations=512)
    
    filename = f"fractals/{name.lower().replace(' ', '_')}.png"
    image.save(filename)
    
    print(f"Saved to {filename}")
```

## Пример 8: Интерактивный тур

### Создание виртуального тура по фракталу

```python
class FractalTour:
    def __init__(self, fractal_name):
        self.fractal = FractalRegistry.get_fractal(fractal_name)
        self.waypoints = []
        
    def add_waypoint(self, x, y, zoom, duration=2.0):
        """Добавить точку остановки"""
        self.waypoints.append({
            'x': x,
            'y': y,
            'zoom': zoom,
            'duration': duration
        })
    
    def play(self):
        """Воспроизвести тур"""
        for waypoint in self.waypoints:
            # Плавно переместиться к waypoint
            # Задержаться на duration секунд
            # Перейти к следующему
            pass

# Использование
tour = FractalTour("Mandelbrot")
tour.add_waypoint(0, 0, 1, duration=3)
tour.add_waypoint(-0.75, 0.1, 100, duration=5)
tour.add_waypoint(-0.1, 0.65, 50, duration=4)
tour.play()
```

## Пример 9: Статистический анализ

### Анализ распределения итераций

```python
import matplotlib.pyplot as plt

# Вычислить фрактал
result = mandelbrot.calculate(x, y, max_iter=256)

# Создать гистограмму
plt.figure(figsize=(10, 6))
plt.hist(result.flatten(), bins=50, color='#FFB6C1', edgecolor='#FF69B4')
plt.xlabel('Iterations')
plt.ylabel('Frequency')
plt.title('Mandelbrot Iteration Distribution')
plt.grid(True, alpha=0.3)
plt.savefig('iteration_distribution.png')
```

## Пример 10: Экспорт для печати

### Подготовка высококачественного изображения

```python
# Настройки для печати
print_config = {
    "rendering": {
        "max_iterations": 2048,
        "quality": "ultra",
        "antialiasing": true
    },
    "export": {
        "dpi": 300,
        "format": "png",
        "color_depth": 48  # 16-bit per channel
    }
}

# Рендеринг в высоком разрешении
renderer = Renderer2D(QSize(7200, 10800), print_config)  # A4 at 300 DPI
image = renderer.render_mandelbrot(max_iter=2048)

# Сохранение для печати
image.save("mandelbrot_print.png", quality=100, dpi=(300, 300))
```

## Советы и трюки

### Оптимизация производительности

```python
# 1. Используйте меньшее разрешение для исследования
renderer = Renderer2D(QSize(640, 480), config)

# 2. Увеличивайте итерации только при необходимости
iterations = 128  # Для исследования
iterations = 1024  # Для финального рендера

# 3. Кэшируйте результаты
cache = {}
def get_fractal_cached(x, y, max_iter):
    key = (x, y, max_iter)
    if key not in cache:
        cache[key] = mandelbrot.calculate(x, y, max_iter)
    return cache[key]
```

---

## Дополнительные ресурсы

- [Fractal Mathematics on Wikipedia](https://en.wikipedia.org/wiki/Fractal)
- [Mandelbrot Set Explorer](https://www.mandelbrot-set.com/)
- [3D Fractal Gallery](https://www.fractalforums.com/)

---

**Экспериментируйте и создавайте! 🍩✨**
