import requests
import re

def print_unicode_grid_from_doc(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch document.")
        return

    text = response.text

    pattern = r'(.),\s*(\d+),\s*(\d+)'  # matches: char, x, y
    matches = re.findall(pattern, text)
    print(f"\nFound {len(matches)} character entries.")

    grid_data = []
    max_x = 0
    max_y = 0

    for char, x_str, y_str in matches:
        x = int(x_str)
        y = int(y_str)

        # Skip garbage data
        if x > 1000 or y > 1000:
            continue

        grid_data.append((x, y, char))
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    print(f"Grid dimensions: {max_x + 1} columns x {max_y + 1} rows")

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in grid_data:
        grid[y][x] = char

    print("\n--- Secret Grid ---")
    for row in grid:
        print(''.join(row).upper())

    # Extract only alphabetic characters (after converting to uppercase)
    message = ''
    for col in range(max_x + 1):
        for row in range(max_y + 1):
            char = grid[row][col].upper()
            if char.isalpha():
                message += char

    print("\nSecret Message:", message)

# Run the function
print_unicode_grid_from_doc("https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub")
