import pygame
import random
import os

# Ініціалізація Pygame
pygame.init()

# Розміри вікна
WIDTH, HEIGHT = 800, 600

# Колір фону
WHITE = (255, 255, 255)

# Створення вікна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Мем Вьюер")

# Завантаження фонового зображення
background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Список категорій та шлях до папки з зображеннями для кожної категорії
categories = {
    "Категорія 1": "images/категорія_1",
    "Категорія 2": "images/категорія_2",
    "Категорія 3": "images/категорія_3"
}

# Створення папок для зображень, якщо вони не існують
for category_path in categories.values():
    if not os.path.exists(category_path):
        os.makedirs(category_path)

# Завантаження зображень з папок
images = {}
for category, category_path in categories.items():
    category_images = [pygame.image.load(os.path.join(category_path, filename)) for filename in os.listdir(category_path) if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif")) and os.path.isfile(os.path.join(category_path, filename))]
    images[category] = category_images

selected_image = None

def show_random_mem(selected_category):
    global selected_image
    if selected_category in images:
        selected_image = random.choice(images[selected_category])

# Функція для відображення кнопок
def draw_buttons():
    button_y = 50
    for category in categories:
        button_rect = pygame.Rect((WIDTH - 200) // 2, button_y, 200, 30)
        button_image = pygame.image.load("button_image.png")  # Завантаження зображення кнопки
        button_image = pygame.transform.scale(button_image, (200, 30))  # Зміна розміру зображення кнопки
        screen.blit(button_image, button_rect)  # Відображення зображення кнопки
        font = pygame.font.Font(None, 24)
        text = font.render(category, True, WHITE)
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect)
        button_y += 40


# Головний цикл програми
running = True
while running:
    screen.blit(background_image, (0, 0))

    draw_buttons()

    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                button_y = 50
                for category in categories:
                    if (WIDTH - 200) // 2 <= mouse_x <= (WIDTH + 200) // 2 and button_y <= mouse_y <= button_y + 30:
                        show_random_mem(category)
                    button_y += 40

    # Відображення вибраного зображення
    if selected_image:
        screen.blit(selected_image, ((WIDTH - selected_image.get_width()) // 2, (HEIGHT - selected_image.get_height()) // 2))

    pygame.display.flip()  # Оновлення екрану

pygame.quit()