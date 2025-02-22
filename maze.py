import time
import random
from cell import Cell

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._seed = random.seed(seed)
        self._cells = []

        self._create_cells()

    def _create_cells(self):
        for col in range(self.num_cols):
            columns = []
            for row in range(self.num_rows):
                columns.append(Cell(self.win))
            self._cells.append(columns)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[j][i].draw(x1, y1, x2, y2)
        self._animate()

    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        exit = self._cells[self.num_cols - 1][self.num_rows - 1]
        entrance.has_top_wall = False
        self._draw_cell(0, 0)
        exit.has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            visited = []
            left_cell = self._cells[i][j - 1]
            right_cell = self._cells[i][j + 1]
            top_cell = self._cells[i - 1][j]
            bottom_cell = self._cells[i + 1][j]
            if left_cell.visited == True:
                visited.append(left_cell)
            if right_cell.visited == True:
                visited.append(right_cell)
            if top_cell.visited == True:
                visited.append(top_cell)
            if bottom_cell.visited == True:
                visited.append(bottom_cell)
    
    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)
