import random

class Cube:
    COLORS = {
        'W': (240, 240, 240),
        'Y': (255, 237, 128),
        'B': (128, 179, 255),
        'R': (255, 133, 133),
        'G': (128, 255, 128),
        'O': (255, 192, 128),
    }

    def __init__(self):
        self.faces = {
            'U': ['W'] * 9,
            'D': ['Y'] * 9,
            'F': ['G'] * 9,
            'B': ['B'] * 9,
            'L': ['O'] * 9,
            'R': ['R'] * 9
        }
        self.adjacent = {
            'U': [('B', 0, 1, 2), ('R', 0, 1, 2), ('F', 0, 1, 2), ('L', 0, 1, 2)],
            'D': [('F', 6, 7, 8), ('R', 6, 7, 8), ('B', 6, 7, 8), ('L', 6, 7, 8)],
            'F': [('U', 6, 7, 8), ('R', 0, 3, 6), ('D', 2, 1, 0), ('L', 8, 5, 2)],
            'B': [('U', 2, 1, 0), ('L', 0, 3, 6), ('D', 6, 7, 8), ('R', 8, 5, 2)],
            'L': [('U', 0, 3, 6), ('F', 0, 3, 6), ('D', 0, 3, 6), ('B', 8, 5, 2)],
            'R': [('U', 8, 5, 2), ('B', 0, 3, 6), ('D', 8, 5, 2), ('F', 8, 5, 2)]
        }

    def colorize(self, code):
        r, g, b = self.COLORS[code]
        return f"\033[48;2;{r};{g};{b}m  \033[0m"

    def display(self):
        for i in range(0, 9, 3):
            print("      " + "".join(self.colorize(c) for c in self.faces['U'][i:i+3]))
        for i in range(0, 9, 3):
            print("".join(self.colorize(c) for c in self.faces['L'][i:i+3]) +
                  "".join(self.colorize(c) for c in self.faces['F'][i:i+3]) +
                  "".join(self.colorize(c) for c in self.faces['R'][i:i+3]) +
                  "".join(self.colorize(c) for c in self.faces['B'][i:i+3]))
        for i in range(0, 9, 3):
            print("      " + "".join(self.colorize(c) for c in self.faces['D'][i:i+3]))

    def rotate_face(self, face, clockwise=True):
        old = self.faces[face][:]
        if clockwise:
            self.faces[face][0] = old[6]
            self.faces[face][1] = old[3]
            self.faces[face][2] = old[0]
            self.faces[face][3] = old[7]
            self.faces[face][4] = old[4]
            self.faces[face][5] = old[1]
            self.faces[face][6] = old[8]
            self.faces[face][7] = old[5]
            self.faces[face][8] = old[2]
        else:
            self.faces[face][0] = old[2]
            self.faces[face][1] = old[5]
            self.faces[face][2] = old[8]
            self.faces[face][3] = old[1]
            self.faces[face][4] = old[4]
            self.faces[face][5] = old[7]
            self.faces[face][6] = old[0]
            self.faces[face][7] = old[3]
            self.faces[face][8] = old[6]

        adj = self.adjacent[face]
        strips = []
        for f, *idx in adj:
            strips.append([self.faces[f][i] for i in idx])
        if clockwise:
            strips = [strips[-1]] + strips[:-1]
        else:
            strips = strips[1:] + [strips[0]]
        for (f, *idx), strip in zip(adj, strips):
            for i, v in zip(idx, strip):
                self.faces[f][i] = v

    def apply_move(self, move):
        if move.endswith("'"):
            self.rotate_face(move[0], False)
        else:
            self.rotate_face(move, True)

    def randomize(self, moves=20):
        sequence = []
        options = ['U', 'D', 'F', 'B', 'L', 'R']
        suffixes = ['', "'"]
        for _ in range(moves):
            move = random.choice(options) + random.choice(suffixes)
            self.apply_move(move)
            sequence.append(move)
        print("Moves applied:", " ".join(sequence), "\n")


def menu():
    cube = Cube()
    while True:
        print("\033[H\033[J")
        print("Rubik's Cube Simulator\n")
        cube.display()
        print("\nMenu:")
        print("1. Randomize Cube")
        print("2. Reset Cube")
        print("3. Make a Move")
        print("4. Exit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            print("\nRandomizing cube...")
            cube.randomize()
        elif choice == '2':
            cube = Cube()
            print("\nCube reset.")
        elif choice == '3':
            while True:
                print("\033[H\033[J")
                print("Rubik's Cube Simulator\n")
                cube.display()
                move = input("\nEnter a move (e.g. R, U', F2), or press Enter to return to menu: ").strip()
                if not move:
                    break
                if len(move) == 2 and move[1] == '2':
                    cube.apply_move(move[0])
                    cube.apply_move(move[0])
                elif move.endswith("'"):
                    cube.apply_move(move)
                elif move in ['U', 'D', 'F', 'B', 'L', 'R']:
                    cube.apply_move(move)
                else:
                    print(f"\nInvalid move: {move}")
                    input("Press Enter to continue...")

        elif choice == '4':
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice. Please try again.")



if __name__ == "__main__":
    menu()
