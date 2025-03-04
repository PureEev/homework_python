import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------
plt.figure(figsize=(8, 4))
x = [0, 5, 10, 15, 20]
y = [1, 10, 8, 10, 14][:len(x)]
y2 = [5, 3, 2, 9, 15][:len(x)]

# предположение для заполнения
plt.plot(x, y, label='Line 1')
plt.plot(x, y2, linestyle='--', label='Line 1 (dashed)')  # повтор для второй линии
plt.legend()
plt.grid(True)
plt.show()

# --------------------------------------
x = np.array([1, 2, 3, 4, 5])
y1 = np.array([2, 5, 7, 6, 4])
y2 = np.array([9, 6, 3, 6, 9])
y3 = np.array([-7, -4, 1, -4, -7])

# Создаем фигуру и оси
fig = plt.figure(figsize=(8, 6))

# Верхний график на всю ширину
ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=2)
ax1.plot(x, y1)

# Нижний левый график
ax2 = plt.subplot2grid((2, 2), (1, 0))
ax2.plot(x, y2)

# Нижний правый график
ax3 = plt.subplot2grid((2, 2), (1, 1))
ax3.plot(x, y3)

# Подгоняем отображение
plt.tight_layout()
plt.show()
# --------------------------------------


x = np.linspace(-5, 5, 10)
y = x**2 + 3

plt.figure(figsize=(6, 4))
plt.plot(x, y)

# Минимум функции
xmin, ymin = 0, 3
plt.annotate("min", xy=(xmin, ymin), xytext=(xmin, ymin + 5),
             arrowprops=dict(facecolor='green', edgecolor='green', width=2, headwidth=10),
             fontsize=12, ha='center')

plt.show()

# Второй график: тепловая карта
data = np.random.rand(8, 8) * 10  # 8x8 случайные данные

plt.figure(figsize=(6, 4))
plt.imshow(data, cmap='viridis', aspect='auto')
plt.colorbar()
plt.xticks(range(8))
plt.yticks(range(8))

plt.show()

# --------------------------------------

x = np.linspace(0, 5, 100)
y = np.sin(np.pi * x)  # Частота подобрана по образцу

# Первый график с заливкой
plt.figure(figsize=(6, 4))
plt.plot(x, y, color='red')
plt.fill_between(x, y, where=(y > 0), color='blue', alpha=0.5)
plt.fill_between(x, y, where=(y < 0), color='blue', alpha=0.5)
plt.ylim(-1, 1)
plt.show()

# --------------------------------------

# Второй график без заливки
plt.figure(figsize=(6, 4))
plt.plot(x, np.abs(y))
plt.ylim(-1, 1)
plt.show()

# --------------------------------------
x = np.arange(7)
y = np.arange(7)

fig, axs = plt.subplots(1, 3, figsize=(12, 4))

# Первый график: ступени "слева" (where='pre')
axs[0].step(x, y, where='pre', color='green')
axs[0].plot(x, y, 'o', color='green')  # добавляем точки

# Второй график: ступени "по центру" (where='mid')
axs[1].step(x, y, where='mid', color='green')
axs[1].plot(x, y, 'o', color='green')

# Третий график: ступени "справа" (where='post')
axs[2].step(x, y, where='post', color='green')
axs[2].plot(x, y, 'o', color='green')

# Настройки осей и сетки
for ax in axs:
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)
    ax.set_xticks(range(7))
    ax.set_yticks(range(7))
    ax.grid(True)

plt.tight_layout()
plt.show()

# --------------------------------------
x = np.linspace(0, 10, 100)
y1 = x * (10 - x) / 2   # для примера - парабола
y2 = x * (10 - x) / 4
y3 = x * (10 - x) / 5

plt.figure(figsize=(8, 6))
plt.stackplot(x, y1, y2, y3, labels=['y1', 'y2', 'y3'],
              colors=['orange', 'green', 'blue'])
plt.legend(loc='upper right')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
# ------------------- Page 9/10: Столбчатая диаграмма брендов -------------------
labels = ['Toyota', 'Ford', 'Jaguar', 'BMW', 'AUDI']
sizes = [25, 15, 20, 25, 15]

# Параметр explode определяет, какой сегмент и насколько будет вынесен из центра
explode = [0, 0.1, 0, 0, 0]  # Ford (второй элемент) вынесен на 0.1

plt.figure(figsize=(6, 6))
plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=140,
    explode=explode  # передаём массив explode
)
plt.show()
# --------------------------------------

labels = ['Toyota', 'Ford', 'Jaguar', 'BMV', 'AUDI']
sizes = [25, 15, 20, 25, 15]  # Пример произвольных значений

fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

# Создаём белый круг в центре, чтобы получился "бублик"
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')  # делаем диаграмму кругом (равные оси)
plt.show()