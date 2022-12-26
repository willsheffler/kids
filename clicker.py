import pygame

pygame.init()

WIDTH = 1200
HEIGHT = 1200
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
cash = 1_000_000

font = pygame.font.SysFont('monospace', 22)
bigfont = pygame.font.SysFont('monospace', 60)
background_color = (40, 40, 40)
#Main Screen for drawing buttons
surface = pygame.Surface((WIDTH, HEIGHT))

surface.fill(background_color)

_num_buttons = 0


class CashGenerator:

    def __init__(self,
                 cash_add,
                 add_time,
                 cost,
                 max_levels,
                 color=(255, 255, 255)):
        super(CashGenerator, self).__init__()
        global _num_buttons
        self.index = _num_buttons
        _num_buttons += 1
        self.cash_add = cash_add
        self.cost = cost
        self.max_levels = max_levels
        self.color = color
        self.timer = add_time
        self.level = 0
        self.event = pygame.USEREVENT + self.index
        self.rect = pygame.draw.rect(
            surface, self.color,
            pygame.Rect(100, 200 + 70 * self.index, 300, 60), 1)

    def level_up(self):
        pygame.time.set_timer(self.event, self.timer)
        self.timer -= 100
        self.level += 1

    def add_cash(self):
        global cash
        cash += self.cash_add

    def show(self):
        global window, font, surface

        self.label = font.render(f'{self.cost} for +{self.cash_add}', 1,
                                 self.color)

        label2 = font.render(
            f'Level(+{self.cash_add}):  {self.level} / {self.max_levels} -  ${self.cash_add} per {self.timer/1000} seconds',
            1, self.color)
        window.blit(label2, (440, 216 + 70 * self.index))
        window.blit(self.label, (130, 216 + 70 * self.index))




buttons = list()
for i in range(1000):
    for r in (0, 128, 255):
        for g in (0, 128, 255):
            for b in (0, 128, 255):
                buttons.append(
                    CashGenerator(cash_add=10,
                           add_time=1100,
                           cost=100,
                           max_levels=10,
                           color=(r, g, b)))



# buttons = [
# CashGenerator(cash_add=10, add_time=1100, cost=100, max_levels=10, color=(255,255,0)),
# CashGenerator(cash_add=100, add_time=5100, cost=1000, max_levels=50, color=(255,0,0)),
# CashGenerator(cash_add=1000, add_time=10100, cost=10000, max_levels=100,color=(0,255,0)),
# ]

buttons[0].level_up()

button_is_pressed = False


def handle_events():
    event_dict = {pygame.QUIT: exit}
    for b in buttons:
        event_dict[b.event] = b.add_cash

    for event in pygame.event.get():
        if event.type in event_dict:
            func = event_dict[event.type]
            func()


def handle_mouse_clicks():
    global cash, PROFITS, GEN1_TIMER, GEN2_TIMER, GEN3_TIMER, level_10, level_100, level_1000, button_is_pressed, buttons
    if pygame.mouse.get_focused():
        left_button_pressed = pygame.mouse.get_pressed()[0]
        if not button_is_pressed:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            for button in buttons:
                if all([
                        left_button_pressed,
                        button.rect.collidepoint(mouse_x, mouse_y),
                        cash >= button.cost,
                        button.timer > 100,
                ]):
                    cash -= button.cost
                    button.level_up()
                    button_is_pressed = True

        if not left_button_pressed:
            button_is_pressed = False


def update_text():

    window.blit(surface, (0, 0))

    cash_label = bigfont.render(f'Total Cash: {cash}', 1, (255, 255, 0))
    window.blit(cash_label, (300, 50))

    for b in buttons:
        b.show()

    pygame.display.flip()


def game_loop():
    while True:
        handle_events()
        handle_mouse_clicks()
        update_text()


def main():
    pygame.display.set_caption('Clicker fart?')

    game_loop()


if __name__ == '__main__':
    main()
