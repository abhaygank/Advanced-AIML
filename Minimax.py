import math

def init_board(): return [[" "]*3 for _ in range(3)]

def display(board):
    print("\n")
    for i, row in enumerate(board):
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")
    print("\n")

def winner(b):
    for i in range(3):
        if b[i][0]==b[i][1]==b[i][2]!=" ": return b[i][0] 
        if b[0][i]==b[1][i]==b[2][i]!=" ": return b[0][i] 
    if b[0][0]==b[1][1]==b[2][2]!=" ": return b[1][1]  
    if b[0][2]==b[1][1]==b[2][0]!=" ": return b[1][1]  
    return None

def full(b): return all(c!=" " for r in b for c in r)

def minimax(b, maxm):
    w = winner(b)
    if w=="O": return 1
    if w=="X": return -1
    if full(b): return 0
    
    scores = []
    for r in range(3):
        for c in range(3):
            if b[r][c]==" ":
                b[r][c] = "O" if maxm else "X"
                scores.append(minimax(b, not maxm))
                b[r][c] = " "
    return max(scores) if maxm else min(scores)

def best_move(b):
    best, move = -math.inf, None
    for r in range(3):
        for c in range(3):
            if b[r][c]==" ":
                b[r][c]="O"
                s = minimax(b, False)
                b[r][c]=" "
                if s>best: 
                    best, move = s, (r,c)
    return move

# Count AI wins, Human wins, Draws from current node
def count_outcomes(b, is_ai):
    w = winner(b)
    if w=="O": return (1,0,0)
    if w=="X": return (0,1,0)
    if full(b): return (0,0,1)
    
    total_ai, total_human, total_draw = 0,0,0
    player = "O" if is_ai else "X"
    for r in range(3):
        for c in range(3):
            if b[r][c]==" ":
                b[r][c] = player
                ai, human, draw = count_outcomes(b, not is_ai)
                total_ai += ai
                total_human += human
                total_draw += draw
                b[r][c] = " "
    return (total_ai, total_human, total_draw)

# Main game loop
b = init_board()
display(b)
while True:
    try:
        r, c = map(int, input("Enter row,col (0-2,0-2): ").split(','))
        if not(0<=r<=2 and 0<=c<=2) or b[r][c]!=" ":
            print("Invalid move!")
            continue
        b[r][c] = "X"
        display(b)
        if winner(b) or full(b): break
        
        r, c = best_move(b)
        b[r][c] = "O"
        print(f"AI plays at {r},{c}")
        display(b)
        
        # Count outcomes from current board
        ai_wins, human_wins, draws = count_outcomes(b, True)
        print(f"From this position -> AI wins: {ai_wins}, Human wins: {human_wins}, Draws: {draws}\n")
        
        if winner(b) or full(b): break
    except (ValueError, IndexError):
        print("Enter as: row,col (e.g., 0,1)")

w = winner(b)
print("Draw!" if not w else f"{w} wins!")
