import tkinter as tk
from tkinter import ttk
import random


COLOR_MAP = {
    'W': '#F0F0F0',
    'Y': '#FFE780',
    'B': '#80B3FF',
    'R': '#FF8585',
    'G': '#80FF80',
    'O': '#FFC080',
}

class Cube:
    def __init__(self):
        self.faces = {
            'U': ['W'] * 9,
            'D': ['Y'] * 9,
            'F': ['G'] * 9,
            'B': ['B'] * 9,
            'L': ['O'] * 9,
            'R': ['R'] * 9,
        }

    def rotate_face_cw(self, face):
        f = self.faces[face]
        self.faces[face] = [f[6], f[3], f[0], f[7], f[4], f[1], f[8], f[5], f[2]]

    def rotate_face_ccw(self, face):
        f = self.faces[face]
        self.faces[face] = [f[2], f[5], f[8], f[1], f[4], f[7], f[0], f[3], f[6]]

    def apply_move(self, move):
        if move == 'U': self.move_U()
        elif move == "U'": self.move_U_prime()
        elif move == 'D': self.move_D()
        elif move == "D'": self.move_D_prime()
        elif move == 'R': self.move_R()
        elif move == "R'": self.move_R_prime()
        elif move == 'L': self.move_L()
        elif move == "L'": self.move_L_prime()
        elif move == 'F': self.move_F()
        elif move == "F'": self.move_F_prime()
        elif move == 'B': self.move_B()
        elif move == "B'": self.move_B_prime()

    def move_U(self):
        self.rotate_face_cw('U')
        F, R, B, L = self.faces['F'], self.faces['R'], self.faces['B'], self.faces['L']
        temp = L[0:3]
        L[0:3] = B[0:3]
        B[0:3] = R[0:3]
        R[0:3] = F[0:3]
        F[0:3] = temp

    def move_U_prime(self):
        self.rotate_face_ccw('U')
        F, R, B, L = self.faces['F'], self.faces['R'], self.faces['B'], self.faces['L']
        temp = L[0:3]
        L[0:3] = F[0:3]
        F[0:3] = R[0:3]
        R[0:3] = B[0:3]
        B[0:3] = temp

    def move_D(self):
        self.rotate_face_cw('D')
        F, R, B, L = self.faces['F'], self.faces['R'], self.faces['B'], self.faces['L']
        temp = L[6:9]
        L[6:9] = F[6:9]
        F[6:9] = R[6:9]
        R[6:9] = B[6:9]
        B[6:9] = temp

    def move_D_prime(self):
        self.rotate_face_ccw('D')
        F, R, B, L = self.faces['F'], self.faces['R'], self.faces['B'], self.faces['L']
        temp = L[6:9]
        L[6:9] = B[6:9]
        B[6:9] = R[6:9]
        R[6:9] = F[6:9]
        F[6:9] = temp

    def move_R(self):
        self.rotate_face_cw('R')
        U, F, D, B = self.faces['U'], self.faces['F'], self.faces['D'], self.faces['B']
        temp = [U[2], U[5], U[8]]
        U[2], U[5], U[8] = F[2], F[5], F[8]
        F[2], F[5], F[8] = D[2], D[5], D[8]
        D[2], D[5], D[8] = B[6], B[3], B[0]
        B[6], B[3], B[0] = temp

    def move_R_prime(self):
        self.rotate_face_ccw('R')
        U, F, D, B = self.faces['U'], self.faces['F'], self.faces['D'], self.faces['B']
        temp = [U[2], U[5], U[8]]
        U[2], U[5], U[8] = B[6], B[3], B[0]
        B[6], B[3], B[0] = D[2], D[5], D[8]
        D[2], D[5], D[8] = F[2], F[5], F[8]
        F[2], F[5], F[8] = temp

    def move_L(self):
        self.rotate_face_cw('L')
        U, F, D, B = self.faces['U'], self.faces['F'], self.faces['D'], self.faces['B']
        temp = [U[0], U[3], U[6]]
        U[0], U[3], U[6] = B[8], B[5], B[2]
        B[8], B[5], B[2] = D[0], D[3], D[6]
        D[0], D[3], D[6] = F[0], F[3], F[6]
        F[0], F[3], F[6] = temp

    def move_L_prime(self):
        self.rotate_face_ccw('L')
        U, F, D, B = self.faces['U'], self.faces['F'], self.faces['D'], self.faces['B']
        temp = [U[0], U[3], U[6]]
        U[0], U[3], U[6] = F[0], F[3], F[6]
        F[0], F[3], F[6] = D[0], D[3], D[6]
        D[0], D[3], D[6] = B[8], B[5], B[2]
        B[8], B[5], B[2] = temp

    def move_F(self):
        self.rotate_face_cw('F')
        U, R, D, L = self.faces['U'], self.faces['R'], self.faces['D'], self.faces['L']
        temp = [U[6], U[7], U[8]]
        U[6], U[7], U[8] = L[8], L[5], L[2]
        L[8], L[5], L[2] = D[2], D[1], D[0]
        D[2], D[1], D[0] = R[0], R[3], R[6]
        R[0], R[3], R[6] = temp

    def move_F_prime(self):
        self.rotate_face_ccw('F')
        U, R, D, L = self.faces['U'], self.faces['R'], self.faces['D'], self.faces['L']
        temp = [U[6], U[7], U[8]]
        U[6], U[7], U[8] = R[0], R[3], R[6]
        R[0], R[3], R[6] = D[2], D[1], D[0]
        D[2], D[1], D[0] = L[8], L[5], L[2]
        L[8], L[5], L[2] = temp

    def move_B(self):
        self.rotate_face_cw('B')
        U, R, D, L = self.faces['U'], self.faces['R'], self.faces['D'], self.faces['L']
        temp = [U[0], U[1], U[2]]
        U[0], U[1], U[2] = R[2], R[5], R[8]
        R[2], R[5], R[8] = D[8], D[7], D[6]
        D[8], D[7], D[6] = L[6], L[3], L[0]
        L[6], L[3], L[0] = temp

    def move_B_prime(self):
        self.rotate_face_ccw('B')
        U, R, D, L = self.faces['U'], self.faces['R'], self.faces['D'], self.faces['L']
        temp = [U[0], U[1], U[2]]
        U[0], U[1], U[2] = L[6], L[3], L[0]
        L[6], L[3], L[0] = D[8], D[7], D[6]
        D[8], D[7], D[6] = R[2], R[5], R[8]
        R[2], R[5], R[8] = temp

class CubeGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rubik's Cube Simulator")
        self.cube = Cube()
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack()
        self.controls()
        self.margin_top = 20
        self.margin_left = 20
        moves = ['u', 'd', 'r', 'l', 'f', 'b']
        for move in moves:
            self.bind(f'<{move}>', lambda e, m=move.upper(): self.handle_move(e, m))
            self.bind(f'<{move.upper()}>', lambda e, m=move.upper(): self.handle_move(e, m))
        self.bind('<s>', lambda e: self.scramble_cube())
        self.draw_cube()

    def controls(self):
        frame = ttk.Frame(self)
        frame.pack(pady=10)
        moves = ['U', "U'", 'D', "D'", 'F', "F'", 'B', "B'", 'L', "L'", 'R', "R'"]
        for move in moves:
            ttk.Button(frame, text=move, command=lambda m=move: self.apply_move(m)).pack(side=tk.LEFT)

        ttk.Button(frame, text="Scramble (S)", command=self.scramble_cube).pack(side=tk.LEFT, padx=10)

    def scramble_cube(self):
        scramble_moves = ['U', "U'", 'D', "D'", 'F', "F'", 'B', "B'", 'L', "L'", 'R', "R'"]
        sequence = [random.choice(scramble_moves) for _ in range(25)]
        for move in sequence:
            self.cube.apply_move(move)
        self.draw_cube()

    def apply_move(self, move):
        self.cube.apply_move(move)
        self.draw_cube()

    def draw_face(self, face, x_off, y_off):
        facelets = self.cube.faces[face]
        for i, color_code in enumerate(facelets):
            row, col = divmod(i, 3)
            x = x_off + col * 30
            y = y_off + row * 30
            self.canvas.create_rectangle(x, y, x + 30, y + 30, fill=COLOR_MAP[color_code], outline="black")

    def draw_cube(self):
        self.canvas.delete("all")
        m_top = self.margin_top
        m_left = self.margin_left
        self.draw_face('U', m_left + 90, m_top + 0)
        self.draw_face('L', m_left + 0, m_top + 90)
        self.draw_face('F', m_left + 90, m_top + 90)
        self.draw_face('R', m_left + 180, m_top + 90)
        self.draw_face('B', m_left + 270, m_top + 90)
        self.draw_face('D', m_left + 90, m_top + 180)

if __name__ == "__main__":
    app = CubeGUI()
    app.mainloop()