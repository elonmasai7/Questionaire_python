import html
import pygame
import sys
import requests
import json

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Topics and questions
topics = ["Technology", "Football", "Politics"]
current_topic_index = 0
questions_per_topic = 15
current_question_index = 0
questions = []

# User score
score = 0

# Text input settings
input_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 32)
input_active = False
input_text = ""
font = pygame.font.Font(None, 32)
text_color = WHITE

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trivia Game")
clock = pygame.time.Clock()

# Function to fetch questions from the Open Trivia Database API
def fetch_questions(topic, amount=15):
    url = f"https://opentdb.com/api.php?amount=15&category=18&difficulty=medium&type=multiple"
    url = f""
    url = f"https://opentdb.com/api.php?amount=15&category=24&difficulty=medium"
    response = requests.get(url)
    data = response.json()

    # Check if the response contains the expected key
    if 'results' in data:
        return data['results']
    else:
        print("Error: 'results' key not found in API response.")
        return []

# Function to draw text on the screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Function to display the current question
def display_question():
    question_text = html.unescape(questions[current_question_index]["question"])
    draw_text(question_text, pygame.font.Font(None, 36), WHITE, WIDTH // 2, HEIGHT // 2 - 50)

# Function to display the user's score
def display_score():
    draw_text(f"Score: {score}", pygame.font.Font(None, 36), WHITE, WIDTH // 2, 50)

# Function to handle text input events
# ...

# Function to handle text input events
def handle_input_events():
    global input_text, text_color, current_question_index, score, current_topic_index

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                input_active = not input_active
            else:
                input_active = False

            text_color = WHITE if input_active else (150, 150, 150)

        if event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_RETURN:
                    # Check the user's answer
                    user_answer = input_text.lower().strip()
                    correct_answer = questions[current_question_index]["correct_answer"].lower().strip()

                    if user_answer == correct_answer:
                        score += 1

                    # Move to the next question
                    reset_input()
                    current_question_index += 1

                    # Check if all questions for the current topic have been asked
                    if current_question_index == questions_per_topic:
                        # Move to the next topic
                        reset_input()
                        current_question_index = 0
                        current_topic_index += 1
                        if current_topic_index == len(topics):
                            # End the game if all topics are completed
                            print("Game Over! Your final score:", score)
                            pygame.quit()
                            sys.exit()

                        # Fetch questions for the new topic
                        current_topic = topics[current_topic_index]
                        questions.extend(fetch_questions(current_topic, questions_per_topic))

                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

# ...

# Main game loop
def game_loop():
    global current_question_index, score, current_topic_index, input_text

    # Fetch questions for the current topic if needed
    while current_topic_index < len(topics):
        current_topic = topics[current_topic_index]
        if current_question_index >= len(questions):
            questions.extend(fetch_questions(current_topic, questions_per_topic))

        # Handle text input events
        handle_input_events()

        # Clear the screen
        screen.fill((0, 0, 0))

        # Display the current question
        display_question()

        # Display the text input box
        pygame.draw.rect(screen, text_color, input_rect, 2)
        draw_text(input_text, font, WHITE, input_rect.x + 5, input_rect.y + 5)

        # Display the user's score
        display_score()

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

# ...


              

# Function to reset text input
def reset_input():
    global input_text
    input_text = ""

# Main game loop
# Main game loop
def game_loop():
    global current_question_index, score, current_topic_index, input_text

    # Fetch questions for the current topic if needed
    while current_topic_index < len(topics):
        current_topic = topics[current_topic_index]
        if current_question_index >= len(questions):
            questions.extend(fetch_questions(current_topic, questions_per_topic))

        # Handle text input events
        handle_input_events()

        # Clear the screen
        screen.fill((0, 0, 0))

        # Display the current question
        display_question()

        # Display the text input box
        pygame.draw.rect(screen, text_color, input_rect, 2)
        draw_text(input_text, font, WHITE, input_rect.x + 5, input_rect.y + 5)

        # Display the user's score
        display_score()

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

# ...
        # Clear the screen
        screen.fill((0, 0, 0))

        # Display the current question
        display_question()

        # Display the text input box
        pygame.draw.rect(screen, text_color, input_rect, 2)
        draw_text(input_text, font, WHITE, input_rect.x + 5, input_rect.y + 5)

        # Display the user's score
        display_score()

        # Handle text input events
       # ...

# Function to handle text input events
def handle_input_events():
    global input_text, text_color, current_question_index, score, current_topic_index

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                input_active = not input_active
            else:
                input_active = False

            text_color = WHITE if input_active else (150, 150, 150)

        if event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_RETURN:
                    # Check the user's answer
                    user_answer = input_text.lower().strip()
                    correct_answer = questions[current_question_index]["correct_answer"].lower().strip()

                    if user_answer == correct_answer:
                        score += 1

                    # Move to the next question
                    reset_input()
                    current_question_index += 1

                    # Check if all questions for the current topic have been asked
                    if current_question_index == questions_per_topic:
                        # Move to the next topic
                        reset_input()
                        current_question_index = 0
                        current_topic_index += 1
                        if current_topic_index == len(topics):
                            # End the game if all topics are completed
                            print("Game Over! Your final score:", score)
                            pygame.quit()
                            sys.exit()

                        # Fetch questions for the new topic
                        current_topic = topics[current_topic_index]
                        questions.extend(fetch_questions(current_topic, questions_per_topic))

                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

# Main game loop
def game_loop():
    global current_question_index, score, current_topic_index, input_text

    # Fetch questions for the current topic if needed
    while current_topic_index < len(topics):
        current_topic = topics[current_topic_index]
        if current_question_index >= len(questions):
            questions.extend(fetch_questions(current_topic, questions_per_topic))

        # Clear the screen
        screen.fill((0, 0, 0))

        # Display the current question
        display_question()

        # Display the text input box
        pygame.draw.rect(screen, text_color, input_rect, 2)
        draw_text(input_text, font, WHITE, input_rect.x + 5, input_rect.y + 5)

        # Display the user's score
        display_score()

        # Update the display
        pygame.display.flip()

        # Handle text input events
        handle_input_events()

        # Cap the frame rate
        clock.tick(FPS)

# ...

