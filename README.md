# Chanim - Chess animation library for manim. 


## To use, you can either create a scene in the chanim.py file, or copy and paste the entire chanim file at the top of your file that you want to use to animate.

### BOARD 


To use a board, you can create a Chessboard object using the Board() instantiator. 

```
my_board = Board()
```

Boards have an instance variable for every square, which you can refer to, shown in the following block of code.

```
starting_king_square = my_board.e1
```

You can also refer to the entire board at once if you want to select everything with .board. The following code uses the Create animation to animate the entire board appearing at once.

```
self.play(Create(my_board.board))
```

