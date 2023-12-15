def sort_colors(colors):

    red = 0
    white = 0
    blue = len(colors) - 1

    if len(colors) < 3:
        return colors

    while blue >= white:
        if colors[white] == 0:
            if colors[red] != 0:
                colors[red], colors[white] = colors[white], colors[red]
            red += 1
            white += 1
        elif colors[white] == 1:
            white += 1
        elif colors[white] == 2:
            if colors[blue] != 2:
                colors[blue], colors[white] = colors[white], colors[blue]
            blue -= 1

    return colors


def main():
    inputs = [
        [0, 1, 0],
        [1, 1, 0, 2],
        [2, 1, 1, 0, 0],
        [2, 2, 2, 0, 1, 0],
        [2, 1, 1, 0, 1, 0, 2],
    ]

    # Iterate over the inputs and print the sorted array for each
    for i in range(len(inputs)):
        print(
            i + 1,
            ".\tcolors:",
            inputs[i].copy(),
            "\n\n\tThe sorted array is:",
            sort_colors(inputs[i]),
        )
        print("-" * 100)


if __name__ == "__main__":
    main()
