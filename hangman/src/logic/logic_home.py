import random
import os

class AppState:
    WORDS = [
        "cpu", "mouse", "monitor", "teclado", "linux", "windows", "kernel", "json",
        "bug", "python", "java", "docker", "kubernetes", "github", "git", "ram",
        "ssd", "hdd", "router", "switch", "firewall", "sdk", "api", "cache",
        "thread", "stack", "queue", "binary", "hex", "xml", "html", "css",
        "regex", "debug", "compile", "runtime", "virtual", "cloud", "ethernet",
        "node", "react", "angular", "vue", "sql", "nosql", "array", "object",
        "thread", "socket", "middleware"
    ]

    word_guess = ""
    mask_word = ""
    attempt =  0
    max_attempts = 7
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    img_dir = os.path.join(base_dir, "statics", "image")
    game_over = False

    @classmethod
    def set_random_word(cls):
        """Elige una palabra al azar y resetea el estado."""
        # cls.word_guess = random.choice(cls.WORDS)
        cls.word_guess = "cpu"
        cls.attempt = 0
        # máscara inicial: un "_" por cada letra
        cls.masked_word = " ".join("_" for _ in cls.word_guess)
        cls.game_over = False
        return cls.masked_word

    @classmethod
    def reveal_letter(cls, letter: str):
        """
        Si la letra está en word_guess, la muestra en masked_word.
        Devuelve la nueva masked_word.
        """
        letter = letter.lower()
        # construimos una lista de caracteres reemplazando donde corresponda
        new_mask = []
        for real_char, mask_char in zip(cls.word_guess, cls.masked_word.split(" ")):
            if real_char == letter:
                new_mask.append(letter)
            else:
                new_mask.append(mask_char)
        cls.masked_word = " ".join(new_mask)
        return cls.masked_word

    @classmethod
    def get_word_hashed(cls):
        """
        Devuelve el estado actual del “hashed” con espacios: "_ i _ _ o r s"
        """
        return cls.masked_word

    @classmethod
    def get_image(cls):
        """
        Devuelve la ruta actualizada de la imagen según el número de intentos.
        """
        print(cls.attempt)
        return os.path.join(cls.img_dir, f"{cls.attempt}.png")


    @classmethod
    def get_current_attempt(cls):
        return 7 -cls.attempt

