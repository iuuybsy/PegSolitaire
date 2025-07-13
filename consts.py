WIDTH: int = 7
HEIGHT: int = 7

FORBID_RANGE:int = 2
FORBID_AREA:list[list[int]] = []
for i in range(FORBID_RANGE):
    for j in range(FORBID_RANGE):
        FORBID_AREA.append([i, j])
        FORBID_AREA.append([i, HEIGHT - j - 1])
        FORBID_AREA.append([WIDTH - i - 1, j])
        FORBID_AREA.append([WIDTH - i - 1, HEIGHT - j - 1])

FREE_CORD: list[int] = [WIDTH // 2, HEIGHT // 2]

if __name__ == '__main__':
    print(f"WIDTH: {WIDTH}")
    print(f"HEIGHT: {HEIGHT}")
    print(f"FORBID_RANGE: {FORBID_RANGE}")
    print(f"FORBID_AREA: {FORBID_AREA}")
    print(f"FREE_CORD: {FREE_CORD}")
