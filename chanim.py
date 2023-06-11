from manim import *
import numpy as np

class Chessboard(VMobject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a1, self.a2, self.a3, self.a4, self.a5, self.a6, self.a7, self.a8 = Square(),  Square(), Square(), Square(), Square(), Square(), Square(), Square()
        self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8 = Square(),  Square(), Square(), Square(), Square(), Square(), Square(), Square()
        self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8 = Square(),  Square(), Square(), Square(), Square(), Square(), Square(), Square()
        self.d1, self.d2, self.d3, self.d4, self.d5, self.d6, self.d7, self.d8 = Square(),  Square(), Square(), Square(), Square(), Square(), Square(), Square()
        self.e1, self.e2, self.e3, self.e4, self.e5, self.e6, self.e7, self.e8 = Square(),  Square(), Square(), Square(), Square(), Square(), Square(), Square()
        self.f1, self.f2, self.f3, self.f4, self.f5, self.f6, self.f7, self.f8 = Square(),  Square(), Square(), Square(), Square(), Square(), Square(), Square()
        self.g1, self.g2, self.g3, self.g4, self.g5, self.g6, self.g7, self.g8 = Square(),  Square(), Square(), Square(), Square(), Square(), Square(), Square()
        self.h1, self.h2, self.h3, self.h4, self.h5, self.h6, self.h7, self.h8 = Square(),  Square(), Square(), Square(), Square(), Square(), Square(), Square()

        self.a1.scale(0.5)
        self.a2.scale(0.5)
        self.a3.scale(0.5)
        self.a4.scale(0.5)
        self.a5.scale(0.5)
        self.a6.scale(0.5)
        self.a7.scale(0.5)
        self.a8.scale(0.5)

        self.b1.scale(0.5)
        self.b2.scale(0.5)
        self.b3.scale(0.5)
        self.b4.scale(0.5)
        self.b5.scale(0.5)
        self.b6.scale(0.5)
        self.b7.scale(0.5)
        self.b8.scale(0.5)

        self.c1.scale(0.5)
        self.c2.scale(0.5)
        self.c3.scale(0.5)
        self.c4.scale(0.5)
        self.c5.scale(0.5)
        self.c6.scale(0.5)
        self.c7.scale(0.5)
        self.c8.scale(0.5)

        self.d1.scale(0.5)
        self.d2.scale(0.5)
        self.d3.scale(0.5)
        self.d4.scale(0.5)
        self.d5.scale(0.5)
        self.d6.scale(0.5)
        self.d7.scale(0.5)
        self.d8.scale(0.5)

        self.e1.scale(0.5)
        self.e2.scale(0.5)
        self.e3.scale(0.5)
        self.e4.scale(0.5)
        self.e5.scale(0.5)
        self.e6.scale(0.5)
        self.e7.scale(0.5)
        self.e8.scale(0.5)

        self.f1.scale(0.5)
        self.f2.scale(0.5)
        self.f3.scale(0.5)
        self.f4.scale(0.5)
        self.f5.scale(0.5)
        self.f6.scale(0.5)
        self.f7.scale(0.5)
        self.f8.scale(0.5)

        self.g1.scale(0.5)
        self.g2.scale(0.5)
        self.g3.scale(0.5)
        self.g4.scale(0.5)
        self.g5.scale(0.5)
        self.g6.scale(0.5)
        self.g7.scale(0.5)
        self.g8.scale(0.5)

        self.h1.scale(0.5)
        self.h2.scale(0.5)
        self.h3.scale(0.5)
        self.h4.scale(0.5)
        self.h5.scale(0.5)
        self.h6.scale(0.5)
        self.h7.scale(0.5)
        self.h8.scale(0.5)



        
        
        self.e5.move_to(UP * 0.5 + RIGHT * 0.5)
        self.e4.next_to(self.e5, DOWN, buff=0)
        self.e3.next_to(self.e4, DOWN, buff=0)
        self.e2.next_to(self.e3, DOWN, buff=0)
        self.e1.next_to(self.e2, DOWN, buff=0)
        self.e6.next_to(self.e5, UP, buff=0)
        self.e7.next_to(self.e6, UP, buff=0)
        self.e8.next_to(self.e7, UP, buff=0)

        self.d1.next_to(self.e1, LEFT, buff=0)
        self.c1.next_to(self.d1, LEFT, buff=0)
        self.b1.next_to(self.c1, LEFT, buff=0)
        self.a1.next_to(self.b1, LEFT, buff=0)
        self.f1.next_to(self.e1, RIGHT, buff=0)
        self.g1.next_to(self.f1, RIGHT, buff=0)
        self.h1.next_to(self.g1, RIGHT, buff=0)


        self.a2.next_to(self.a1, UP, buff=0)
        self.a3.next_to(self.a2, UP, buff=0)
        self.a4.next_to(self.a3, UP, buff=0)
        self.a5.next_to(self.a4, UP, buff=0)
        self.a6.next_to(self.a5, UP, buff=0)
        self.a7.next_to(self.a6, UP, buff=0)
        self.a8.next_to(self.a7, UP, buff=0)

        
        self.b2.next_to(self.b1, UP, buff=0)
        self.b3.next_to(self.b2, UP, buff=0)
        self.b4.next_to(self.b3, UP, buff=0)
        self.b5.next_to(self.b4, UP, buff=0)
        self.b6.next_to(self.b5, UP, buff=0)
        self.b7.next_to(self.b6, UP, buff=0)
        self.b8.next_to(self.b7, UP, buff=0)

        
        self.c2.next_to(self.c1, UP, buff=0)
        self.c3.next_to(self.c2, UP, buff=0)
        self.c4.next_to(self.c3, UP, buff=0)
        self.c5.next_to(self.c4, UP, buff=0)
        self.c6.next_to(self.c5, UP, buff=0)
        self.c7.next_to(self.c6, UP, buff=0)
        self.c8.next_to(self.c7, UP, buff=0)

        
        self.d2.next_to(self.d1, UP, buff=0)
        self.d3.next_to(self.d2, UP, buff=0)
        self.d4.next_to(self.d3, UP, buff=0)
        self.d5.next_to(self.d4, UP, buff=0)
        self.d6.next_to(self.d5, UP, buff=0)
        self.d7.next_to(self.d6, UP, buff=0)
        self.d8.next_to(self.d7, UP, buff=0)
        
        
        self.f2.next_to(self.f1, UP, buff=0)
        self.f3.next_to(self.f2, UP, buff=0)
        self.f4.next_to(self.f3, UP, buff=0)
        self.f5.next_to(self.f4, UP, buff=0)
        self.f6.next_to(self.f5, UP, buff=0)
        self.f7.next_to(self.f6, UP, buff=0)
        self.f8.next_to(self.f7, UP, buff=0)

        
        self.g2.next_to(self.g1, UP, buff=0)
        self.g3.next_to(self.g2, UP, buff=0)
        self.g4.next_to(self.g3, UP, buff=0)
        self.g5.next_to(self.g4, UP, buff=0)
        self.g6.next_to(self.g5, UP, buff=0)
        self.g7.next_to(self.g6, UP, buff=0)
        self.g8.next_to(self.g7, UP, buff=0)

        
        self.h2.next_to(self.h1, UP, buff=0)
        self.h3.next_to(self.h2, UP, buff=0)
        self.h4.next_to(self.h3, UP, buff=0)
        self.h5.next_to(self.h4, UP, buff=0)
        self.h6.next_to(self.h5, UP, buff=0)
        self.h7.next_to(self.h6, UP, buff=0)
        self.h8.next_to(self.h7, UP, buff=0)

        

        

       
       
        
        
        self.a1.set_fill(GREEN, opacity=0.7)
        self.a2.set_fill(WHITE, opacity=0.7)
        self.a3.set_fill(GREEN, opacity=0.7)
        self.a4.set_fill(WHITE, opacity=0.7)
        self.a5.set_fill(GREEN, opacity=0.7)
        self.a6.set_fill(WHITE, opacity=0.7)
        self.a7.set_fill(GREEN, opacity=0.7)
        self.a8.set_fill(WHITE, opacity=0.7)

        self.b1.set_fill(WHITE, opacity=0.7)
        self.b2.set_fill(GREEN, opacity=0.7)
        self.b3.set_fill(WHITE, opacity=0.7)
        self.b4.set_fill(GREEN, opacity=0.7)
        self.b5.set_fill(WHITE, opacity=0.7)
        self.b6.set_fill(GREEN, opacity=0.7)
        self.b7.set_fill(WHITE, opacity=0.7)
        self.b8.set_fill(GREEN, opacity=0.7)

        self.c1.set_fill(GREEN, opacity=0.7)
        self.c2.set_fill(WHITE, opacity=0.7)
        self.c3.set_fill(GREEN, opacity=0.7)
        self.c4.set_fill(WHITE, opacity=0.7)
        self.c5.set_fill(GREEN, opacity=0.7)
        self.c6.set_fill(WHITE, opacity=0.7)
        self.c7.set_fill(GREEN, opacity=0.7)
        self.c8.set_fill(WHITE, opacity=0.7)

        self.d1.set_fill(WHITE, opacity=0.7)
        self.d2.set_fill(GREEN, opacity=0.7)
        self.d3.set_fill(WHITE, opacity=0.7)
        self.d4.set_fill(GREEN, opacity=0.7)
        self.d5.set_fill(WHITE, opacity=0.7)
        self.d6.set_fill(GREEN, opacity=0.7)
        self.d7.set_fill(WHITE, opacity=0.7)
        self.d8.set_fill(GREEN, opacity=0.7)

        self.e1.set_fill(GREEN, opacity=0.7)
        self.e2.set_fill(WHITE, opacity=0.7)
        self.e3.set_fill(GREEN, opacity=0.7)
        self.e4.set_fill(WHITE, opacity=0.7)
        self.e5.set_fill(GREEN, opacity=0.7)
        self.e6.set_fill(WHITE, opacity=0.7)
        self.e7.set_fill(GREEN, opacity=0.7)
        self.e8.set_fill(WHITE, opacity=0.7)

        self.f1.set_fill(WHITE, opacity=0.7)
        self.f2.set_fill(GREEN, opacity=0.7)
        self.f3.set_fill(WHITE, opacity=0.7)
        self.f4.set_fill(GREEN, opacity=0.7)
        self.f5.set_fill(WHITE, opacity=0.7)
        self.f6.set_fill(GREEN, opacity=0.7)
        self.f7.set_fill(WHITE, opacity=0.7)
        self.f8.set_fill(GREEN, opacity=0.7)

        self.g1.set_fill(GREEN, opacity=0.7)
        self.g2.set_fill(WHITE, opacity=0.7)
        self.g3.set_fill(GREEN, opacity=0.7)
        self.g4.set_fill(WHITE, opacity=0.7)
        self.g5.set_fill(GREEN, opacity=0.7)
        self.g6.set_fill(WHITE, opacity=0.7)
        self.g7.set_fill(GREEN, opacity=0.7)
        self.g8.set_fill(WHITE, opacity=0.7)

        self.h1.set_fill(WHITE, opacity=0.7)
        self.h2.set_fill(GREEN, opacity=0.7)
        self.h3.set_fill(WHITE, opacity=0.7)
        self.h4.set_fill(GREEN, opacity=0.7)
        self.h5.set_fill(WHITE, opacity=0.7)
        self.h6.set_fill(GREEN, opacity=0.7)
        self.h7.set_fill(WHITE, opacity=0.7)
        self.h8.set_fill(GREEN, opacity=0.7)

        self.labelA = Text("a", font="Gill Sans MT").move_to(self.a1.get_center() + DOWN * 0.35 + RIGHT * 0.35).scale(0.3)
        self.labelB = Text("b", font="Gill Sans MT", color="#0d8018").move_to(self.b1.get_center() + DOWN * 0.35 + RIGHT * 0.35).scale(0.3)
        self.labelC = Text("c", font="Gill Sans MT").move_to(self.c1.get_center() + DOWN * 0.35 + RIGHT * 0.35).scale(0.3)
        self.labelD = Text("d", font="Gill Sans MT", color="#0d8018").move_to(self.d1.get_center() + DOWN * 0.35 + RIGHT * 0.35).scale(0.3)
        self.labelE = Text("e", font="Gill Sans MT").move_to(self.e1.get_center() + DOWN * 0.35 + RIGHT * 0.35).scale(0.3)
        self.labelF = Text("f", font="Gill Sans MT", color="#0d8018").move_to(self.f1.get_center() + DOWN * 0.35 + RIGHT * 0.35).scale(0.3)
        self.labelG = Text("g", font="Gill Sans MT").move_to(self.g1.get_center() + DOWN * 0.35 + RIGHT * 0.35).scale(0.3)
        self.labelH = Text("h", font="Gill Sans MT", color="#0d8018").move_to(self.h1.get_center() + DOWN * 0.35 + RIGHT * 0.35).scale(0.3)
        self.label1 = Text("1", font="Gill Sans MT").move_to(self.a1.get_center() + UP * 0.35 + LEFT * 0.35).scale(0.3)
        self.label2 = Text("2", font="Gill Sans MT", color="#0d8018").move_to(self.a2.get_center() + UP * 0.35 + LEFT * 0.35).scale(0.3)
        self.label3 = Text("3", font="Gill Sans MT").move_to(self.a3.get_center() + UP * 0.35 + LEFT * 0.35).scale(0.3)
        self.label4 = Text("4", font="Gill Sans MT", color="#0d8018").move_to(self.a4.get_center() + UP * 0.35 + LEFT * 0.35).scale(0.3)
        self.label5 = Text("5", font="Gill Sans MT").move_to(self.a5.get_center() + UP * 0.35 + LEFT * 0.35).scale(0.3)
        self.label6 = Text("6", font="Gill Sans MT", color="#0d8018").move_to(self.a6.get_center() + UP * 0.35 + LEFT * 0.35).scale(0.3)
        self.label7 = Text("7", font="Gill Sans MT").move_to(self.a7.get_center() + UP * 0.35 + LEFT * 0.35).scale(0.3)
        self.label8 = Text("8", font="Gill Sans MT", color="#0d8018").move_to(self.a8.get_center() + UP * 0.35 + LEFT * 0.35).scale(0.3)


        self.board = Group(
                    self.a1, self.a2, self.a3, self.a4, self.a5, self.a6, self.a7, self.a8, 
                    self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, 
                    self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8, 
                    self.d1, self.d2, self.d3, self.d4, self.d5, self.d6, self.d7, self.d8, 
                    self.e1, self.e2, self.e3, self.e4, self.e5, self.e6, self.e7, self.e8,
                    self.f1, self.f2, self.f3, self.f4, self.f5, self.f6, self.f7, self.f8,
                    self.g1, self.g2, self.g3, self.g4, self.g5, self.g6, self.g7, self.g8,
                    self.h1, self.h2, self.h3, self.h4, self.h5, self.h6, self.h7, self.h8,
                    self.label1, self.label2, self.label3, self.label4, self.label5, self.label6, self.label7, self.label8,
                    self.labelA, self.labelB, self.labelC, self.labelD, self.labelE, self.labelF, self.labelG, self.labelH)
class Pawn(Mobject):
    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
        self.color = color
        self.createpiece()

    def createpiece(self):
        if self.color == WHITE:
            self.add(ImageMobject("./images/pawn_w").scale(2.3))
        else:
            self.add(ImageMobject("./images/pawn_b").scale(2.3))

class King(Mobject):
    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
        self.color = color
        self.createpiece()

    def createpiece(self):
        if self.color == WHITE:
            self.add(ImageMobject("./images/king_w").scale(2.3))
        else:
            self.add(ImageMobject("./images/king_b").scale(2.3))

class Queen(Mobject):
    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
        self.color = color
        self.createpiece()

    def createpiece(self):
        if self.color == WHITE:
            self.add(ImageMobject("./images/queen_w").scale(2.3))
        else:
            self.add(ImageMobject("./images/queen_b").scale(2.3))

class Knight(Mobject):
    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
        self.color = color
        self.createpiece()

    def createpiece(self):
        if self.color == WHITE:
            self.add(ImageMobject("./images/knight_w").scale(2.3))
        else:
            self.add(ImageMobject("./images/knight_b").scale(2.3))

class Bishop(Mobject):
    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
        self.color = color
        self.createpiece()

    def createpiece(self):
        if self.color == WHITE:
            self.add(ImageMobject("./images/bishop_w").scale(2.3))
        else:
            self.add(ImageMobject("./images/bishop_b").scale(2.3))

class Rook(Mobject):
    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
        self.color = color
        self.createpiece()

    def createpiece(self):
        if self.color == WHITE:
            self.add(ImageMobject("./images/rook_w").scale(2.3))
        else:
            self.add(ImageMobject("./images/rook_b").scale(2.3))
