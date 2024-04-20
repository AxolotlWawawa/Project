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
    if not os.path.exists(category_path):  # Перевірка чи папка існує
        os.makedirs(category_path)

# Завантаження зображень з папок
images = {}
for category, category_path in categories.items():
    category_images = [pygame.image.load(os.path.join(category_path, filename)) for filename in os.listdir(category_path) if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif")) and os.path.isfile(os.path.join(category_path, filename))]
    images[category] = category_images

selected_image = None

# Завантаження музики
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)  # Грати музику постійно

# Список доступних треків
available_tracks = ["background_music.mp3", "background_music_2.mp3", "background_music_3.mp3"]
current_track_index = 0

# Функція для відтворення наступного треку
def play_next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(available_tracks)
    pygame.mixer.music.load(available_tracks[current_track_index])
    pygame.mixer.music.play(-1)

def show_random_mem(selected_category):
    global selected_image
    if selected_category in images:
        selected_image = random.choice(images[selected_category])

# Функція для відображення кнопок
def draw_buttons():
    button_y = 50
    for category in categories:
        button_rect = pygame.Rect((WIDTH - 200) // 2, button_y, 200, 30)
        pygame.draw.rect(screen, (200, 55, 55), button_rect)  # Червоний колір тла кнопки
        font = pygame.font.Font(None, 24)
        text = font.render(category, True, (0, 0, 0))  # Чорний колір тексту
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect)
        button_y += 40

    # Кнопка для зміни треку
    change_track_button_rect = pygame.Rect(WIDTH - 220, HEIGHT - 80, 200, 50)
    pygame.draw.rect(screen, (0, 255, 0), change_track_button_rect)  # Зелений колір тла кнопки
    font = pygame.font.Font(None, 24)
    text = font.render("Змінити трек", True, (0, 0, 0))  # Чорний колір тексту
    text_rect = text.get_rect(center=change_track_button_rect.center)
    screen.blit(text, text_rect)
    return change_track_button_rect

# Головний цикл програми
game = True
while game:
    screen.blit(background_image, (0, 0))

    change_track_button_rect = draw_buttons()

    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                button_y = 50
                for category in categories:
                    if (WIDTH - 200) // 2 <= mouse_x <= (WIDTH + 200) // 2 and button_y <= mouse_y <= button_y + 30:
                        show_random_mem(category)
                    button_y += 40
                # Перевірка натискання кнопки "Змінити трек"
                if change_track_button_rect.collidepoint(mouse_x, mouse_y):
                    play_next_track()

    # Відображення вибраного зображення
    if selected_image:
        screen.blit(selected_image, ((WIDTH - selected_image.get_width()) // 2, (HEIGHT - selected_image.get_height()) // 2))

    pygame.display.update()  # Оновлення екрану

pygame.quit()