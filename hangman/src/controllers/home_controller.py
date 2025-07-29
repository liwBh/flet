from views import page_home
from logic.logic_home import AppState
from config.settings import app_color


def update_screen(page, text_word, text_attemp):
    text_word.value = AppState.get_word_hashed()
    text_attemp.value = f"❤️  {AppState.get_current_attempt()} "
    page.update()

def press_letter(letter, page, text_word, text_attemp, text_game, image):
    AppState.reveal_letter(letter)

    if AppState.game_over:
        # Fin del juego - Reiniciar
        print("Reiniciando el juego")
        text_game.value = "🚀 Restart the game"
        text_game.color = app_color["primary"]
        page.update()
        return

    if letter is not AppState.word_guess and AppState.attempt < AppState.max_attempts:
        AppState.attempt += 1
        image.src = AppState.get_image()

    if AppState.attempt >= AppState.max_attempts:
        # Fin del juego - Perdido
        text_game.value = f"😱 Gamer Over\n 💡 The word was: {AppState.word_guess}"
        text_game.color = app_color["danger"]
        AppState.game_over = True

    if AppState.attempt < AppState.max_attempts and  "_" not in AppState.get_word_hashed():
        # Fin del juego - Ganado
        text_game.value = f"🎉 You Win!\n 💡 The word was: {AppState.word_guess}"
        text_game.color = app_color["success"]
        AppState.game_over = True


    update_screen(page, text_word, text_attemp)


def reset_game(page, text_word, text_attemp, text_game, image):
    AppState.set_random_word()
    text_game.value = ""
    image.src = AppState.get_image()
    update_screen(page, text_word, text_attemp)


def init_game(page):
    AppState.set_random_word()
    page_home.init_page(page, press_letter, reset_game)
    page.update()