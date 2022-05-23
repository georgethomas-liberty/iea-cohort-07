def test_life_init_blank_grid():
    grid = [
        [False, False],
        [False, False],
    ]

    game = Life(grid)
    assert game.grid == grid

 def test_life_init_single_cell():
    grid = [
        [True, False],
        [False, False],
    ]

    game = Life(grid)
    assert game.grid == grid

def test_life_empty_next_generation():
    grid = [
        [False, False],
        [False, False],
    ]

    game = Life(grid)
    next_gen = game.next_generation()
