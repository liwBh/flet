import flet
from flet import *
import random
import time


class GenerateGrid():
    def __init__(self, difficulty, game_mode: int = 0):
        self.grid = Column(opacity=1, animate_opacity=300)
        self.blue_tiles: int = 0
        self.difficulty: int = difficulty
        self.correct: int = 0
        self.incorrect: int = 0
        self.order: list = []
        self.game_mode = game_mode
        self.picked_order: list = []
        super().__init__()

    def show_color(self, e):
        if self.game_mode == 0:
            if e.control.data["state"] == 1:
                e.control.bgcolor = "#4cbbb5"
                e.control.opacity = 1
                e.control.update()
                self.correct += 1
                e.page.update()
            else:
                e.control.bgcolor = "#982c33"
                e.control.opacity = 1
                e.control.update()
                self.incorrect += 1
                e.page.update()
        else:
            print("Valor real state:", e.control.data["state"])
            print("Valor real orden:", self.order[len(self.picked_order)])
            print("¿Son iguales?", e.control.data["state"] == self.order[len(self.picked_order)])

            if e.control.data["step"] == self.order[len(self.picked_order)]:
                self.picked_order.append(e.control.data["step"])
                e.control.bgcolor = "#4cbbb5"
                e.control.opacity = 1
                e.control.update()
                e.page.update()
            else:
                self.lose_game()

    def lose_game(self):
        for row in self.grid.controls:
            for container in row.controls:
                container.bgcolor = "#982c33"
                container.opacity = 1
                container.update()

    def reset_game(self):
        for row in self.grid.controls:
            for container in row.controls:
                container.bgcolor = "#5c443b"
                container.opacity = 1
                container.update()

    def build(self):
        rows: list = [
            Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Container(
                        width=54,
                        height=54,
                        animate=300,
                        border=border.all(1, Colors.TRANSPARENT),
                        on_click=lambda e: self.show_color(e),
                        data={"step": 0, "state": 0, "order": 0}
                    )
                    for _ in range(5)

                ]
            )
            for _ in range(5)
        ]

        colors: list = ["#5c443b", "#4cbbb5"]
        step = 0
        for row in rows:
            for container in row.controls[:]:
                # Modificar este metodo pedorro para que la dificultad sea progresiva
                if self.game_mode == 0:
                    container.bgcolor = random.choices(colors, weights=[10, self.difficulty])[0]
                else:
                    container.bgcolor = colors[0]

                if container.bgcolor == "#4cbbb5":
                    container.data["state"] = 1
                    self.blue_tiles += 1
                container.data["step"] = step
                step = step + 1

        self.grid.controls = rows
        return self.grid

    def insert_new_step(self, difficulty):
        rows = self.grid.controls
        position = random.randrange(0, 24)
        enabled_position = True
        while enabled_position:
            for row in rows:
                for container in row.controls:
                    if container.data["step"] == position:
                        if container.data["order"] == 0:
                            container.data["order"] = difficulty + 1
                            self.order.append(position)
                            enabled_position = False
                            break
                        else:
                            break
                if not enabled_position:
                    break
        # Ahora iniciamos el siguiente paso


def main(page: Page):
    page.horizontal_alignment = alignment.center
    page.vertical_alignment = alignment.center

    stage = Text(size=13, weight=FontWeight.BOLD, color=Colors.WHITE)
    result = Text(size=16, weight=FontWeight.BOLD, color=Colors.WHITE)

    start_button = Container(
        content=ElevatedButton(
            on_click=lambda e: start_game(e, GenerateGrid(2), ),
            content=Text("start", size=13, weight=FontWeight.BOLD, color=Colors.WHITE),
            style=ButtonStyle(
                shape={ControlState.DEFAULT: RoundedRectangleBorder(radius=8)},
                color={ControlState.DEFAULT: Colors.WHITE},
            ),
            height=45,
            width=255,
        ),
    )

    start_button_mode_2 = Container(
        content=ElevatedButton(
            on_click=lambda e: start_game_mode_2(e, GenerateGrid(2, 1)),
            content=Text("Start mode 2", size=13, weight=FontWeight.BOLD, color=Colors.WHITE),
            style=ButtonStyle(
                shape={ControlState.DEFAULT: RoundedRectangleBorder(radius=8)},
                color={ControlState.DEFAULT: Colors.WHITE},
            ),
            height=45,
            width=255,
        )
    )

    def print_order(e, level):
        grid = level
        for order in grid.order:
            print("Orden", order)
            for row in grid.grid.controls:
                for container in row.controls:
                    if order == container.data["step"]:
                        container.bgcolor = "#4cbbb5"
                        page.update()
                        time.sleep(0.5)
                        container.bgcolor = "#5c443b"
                        page.update()
        grid.grid.controls[0].opacity = 1
        grid.grid.controls[0].update()
        stage.value = f"Stage: {grid.difficulty - 1}"
        stage.update()
        start_button_mode_2.disabled = True
        start_button_mode_2.update()

    def start_game_mode_2(e, level):
        grid = level
        page.controls.insert(3, grid.build())
        page.update()
        grid.insert_new_step(0)
        grid.insert_new_step(1)
        grid.insert_new_step(2)
        print_order(e, grid)
        while True:
            if len(grid.order) == len(grid.picked_order):
                grid.grid.controls[0].disabled = True
                grid.grid.controls[0].update()

                result.value = "You win!"
                result.color = Colors.GREEN_700
                result.update()

                time.sleep(2)
                result.value = ""
                grid.reset_game()
                page.update()

                grid.insert_new_step(len(grid.order) + 1)
                grid.picked_order = []

                print_order(e, grid)

    def start_game(e, level):
        grid_obj = level
        grid = grid_obj.build()
        page.controls.insert(3, grid)
        page.update()
        grid.controls[0].opacity = 1
        grid.controls[0].update()
        stage.value = f"Stage: {grid_obj.difficulty - 1}"
        stage.update()
        start_button.disabled = True
        start_button.update()

        time.sleep(1.5)

        for rows in grid.controls[:]:
            for container in rows.controls[:]:
                if container.data["state"] == 1:
                    container.bgcolor = "#5c443b"
                    container.update()

        while True:
            if grid_obj.correct == grid_obj.blue_tiles:
                grid.controls[0].disabled = True
                grid.controls[0].update()

                result.value = "You win!"
                result.color = Colors.GREEN_700
                result.update()

                time.sleep(2)
                result.value = ""
                page.controls.remove(grid)
                page.update()

                difficulty = grid_obj.difficulty + 1
                print(grid_obj.difficulty)
                print(difficulty)
                start_game(e, GenerateGrid(difficulty))
                break

            if grid_obj.incorrect > 3:
                result.value = "You lose!"
                result.color = Colors.RED_700
                result.update()

                time.sleep(2)
                result.value = ""
                page.controls.remove(grid)
                page.update()

                start_button.disabled = False
                start_button.update()
                break

    page.add(
        Row(alignment=MainAxisAlignment.CENTER, controls=[
            Text("Memory Matrix", size=22, weight=FontWeight.BOLD, )
        ]),
        # resultado del row
        Row(alignment=MainAxisAlignment.CENTER, controls=[result, ]),
        Divider(height=10, color=Colors.TRANSPARENT),
        Divider(height=10, color=Colors.TRANSPARENT),
        # estado del juego
        Row(alignment=MainAxisAlignment.CENTER, controls=[stage, ]),
        Divider(height=10, color=Colors.TRANSPARENT),
        # boton de empezar
        Row(alignment=MainAxisAlignment.CENTER, controls=[start_button, ]),
        Divider(height=10, color=Colors.TRANSPARENT),
        Row(alignment=MainAxisAlignment.CENTER, controls=[start_button_mode_2, ]),

    )
    page.update()


if __name__ == '__main__':
    flet.app(target=main)
