import pygame
import random
import os
pygame.init()


WIDTH, HEIGHT = 800, 600


WHITE = (255, 255, 255)


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Мем Вьюер")


categories = ["Категорія 1", "Категорія 2", "Категорія 3"]


image_folder = "images"


if not os.path.exists(image_folder):
    os.makedirs(image_folder)


for category in categories:
    category_folder = os.path.join(image_folder, category.lower())
    if not os.path.exists(category_folder):
        os.makedirs(category_folder)


images = {}
for category in categories:
    category_folder = os.path.join(image_folder, category.lower())
    category_images = [pygame.image.load(os.path.join(category_folder, filename)) for filename in os.listdir(category_folder) if (filename.endswith(".jpg") or filename.endswith(".png")) and os.path.isfile(os.path.join(category_folder, filename))]
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
        button_rect = pygame.Rect(50, button_y, 200, 30)
        pygame.draw.rect(window, (0, 0, 255), button_rect)
        font = pygame.font.Font(None, 24)
        text = font.render(category, True, WHITE)
        window.blit(text, (button_rect.x + 10, button_rect.y + 5))
        button_y += 40

# Головний цикл програми
game = True
while game:
    window.fill(WHITE)

    draw_buttons()

    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                button_y = 50
                for category in categories:
                    if 50 <= mouse_x <= 250 and button_y <= mouse_y <= button_y + 30:
                        show_random_mem(category)
                    button_y += 40

    # Відображення вибраного зображення
    if selected_image:
        window.blit(selected_image, ((WIDTH - selected_image.get_width()) // 2, (HEIGHT - selected_image.get_height()) // 2))

    pygame.display.update()  # Оновлення екрану

pygame.quit()