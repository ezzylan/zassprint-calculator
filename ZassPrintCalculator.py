from rebullet import Bullet, Numbers, colors, VerticalPrompt

A4_BLACK_WHITE = 0.1
A3_BLACK_WHITE = 0.5
A4_COLOR = 1.5
A3_COLOR = 3.0
A4_LAMINATE = 1.5
A3_LAMINATE = 3.0

printing_price = 0.0
laminate_price = 0.0
total_price = 0.0

print("Welcome to ZassPrint Calculator!")

while True:
    printing_color_prompt = Bullet(
        prompt="\nColor type?",
        choices=["Black N White", "Color", "Skip"],
        bullet=">",
        margin=2,
        bullet_color=colors.bright(colors.foreground["cyan"]),
        background_color=colors.background["black"],
        background_on_switch=colors.background["black"],
        word_color=colors.foreground["white"],
        word_on_switch=colors.foreground["white"],
    )
    printing_color = printing_color_prompt.launch()

    if printing_color == "Skip":
        break

    printing_prompt = VerticalPrompt(
        [
            Bullet(
                prompt="Paper size?",
                choices=["A4", "A3"],
                bullet=">",
                margin=2,
                bullet_color=colors.bright(colors.foreground["cyan"]),
                background_color=colors.background["black"],
                background_on_switch=colors.background["black"],
                word_color=colors.foreground["white"],
                word_on_switch=colors.foreground["white"],
            ),
            Numbers("How many copies? ", type=int),
        ],
        spacing=0,
    )
    printing = printing_prompt.launch()

    if printing_color == "Black N White":
        printing_price = A4_BLACK_WHITE if printing[0][1] == "A4" else A3_BLACK_WHITE
    elif printing_color == "Color":
        printing_price = A4_COLOR if printing[0][1] == "A4" else A3_COLOR
    total_price += printing_price * printing[1][1]

print("\nHow many copies are laminated?")
laminate_copies_prompt = VerticalPrompt(
    [Numbers("A4: ", type=int), Numbers("A3: ", type=int)], spacing=0
)
laminate_copies = laminate_copies_prompt.launch()

if laminate_copies[0][1]:
    laminate_price += A4_LAMINATE * laminate_copies[0][1]
if laminate_copies[1][1]:
    laminate_price += A3_LAMINATE * laminate_copies[1][1]
total_price += laminate_price

print("-" * 30 + "\nTotal: RM" + str(round(total_price, 2)))
input("Press Enter to exit...")
