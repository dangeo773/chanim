# Chanim - Chess animation library for manim. 


##
![384210533_2372771042932836_696436315772457726_n](https://github.com/dangeo773/chanim/assets/78292895/ac0855a7-1ef9-49c5-a6d4-7dc54cbf5343)
### BOARD 


To use a board, you can create a Chessboard object using the Board() instantiator. 

```
my_board = Board()
```

Boards have an instance variable for every square, which you can refer to, shown in the following block of code.

```
starting_king_square = my_board.e1
```

You can also refer to the entire board at once if you want to select everything with .board. The following code uses the Create animation 
to animate the entire board appearing at once.

```
self.play(Create(my_board.board))
```

### PIECES 

You can create a piece object by calling their respective methods, and pass in the color to specify the pieces' color.

```
white_pawn = Pawn(WHITE)
black_bishop = Bishop(BLACK)
white_rook = Rook(WHITE)
black_queen = Queen(BLACK)
white_king = King(WHITE)
black_knight = Knight(BLACK)
```
