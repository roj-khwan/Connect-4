import enum

class GameState(enum.Enum):
    PlayerOneWin = 1
    PlayerTwoWin = 2
    NotOver = 3
    Full = 4

table = {
    -1 : ' ',
     0 : 'O',
     1 : 'X',
}

inputString = "Enter Column to play (1-7)"

def StartGame():
    global inputString
    grid = [
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
    ]
    columnsHeight = [-6, -6, -6, -6, -6, -6, -6]

    turn = 0

    while Evaluate(grid, columnsHeight) == GameState.NotOver:
        print(f"{table[turn]} Turn")
        DisplayGrid(grid)

        col = input(f"{inputString} : ")

        try:
            col = int(col[0]) - 1
        except:
            inputString = "Please Enter a Valid Input"
            continue

        if col < 0 or col >= 7:
            inputString = "Please Enter Value Between 1 - 7"
            continue

        if columnsHeight[col] == 0:
            inputString ="That's Line is comepletely full"
            continue

        #insert coin into board
        grid[columnsHeight[col]][col] = turn
        columnsHeight[col] += 1

        #swap the turn
        turn = abs(turn - 1)

        inputString = "Enter Column to play (1-7)"

    DisplayGrid(grid)

    match Evaluate(grid, columnsHeight):
        case GameState.Full:
            print("It's a Tie")
        case GameState.PlayerOneWin:
            print("Player One Winning!")
        case GameState.PlayerTwoWin:
            print("Bye Bye Bitch")


def DisplayGrid(data : list):
    for i in range(6)[::-1]:
        print('{'+'|'.join(table[i] for i in data[i])+'}')

def Evaluate(data : list, dataHeight):
    patterns = [
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (1, 1), (2, 2), (3, 3)],
        [(0, 0), (-1, 1), (-2, 2), (-3, 3)],
    ]

    if sum(dataHeight) == 0:
        return GameState.Full

    for cell in range(6 * 7):

        x = cell % 7
        y = cell // 7

        for pattern in patterns:
            connect = []
            
            for localX, localY in pattern:
                worldX = localX + x
                worldY = localY + y

                if worldX >= 7 or worldX < 0 or worldY >= 6 or worldY < 0: break

                connect.append(data[worldY][worldX])

            if len(connect) != 4: break

            if len(set(connect)) == 1 and connect[0] != -1: 
                if connect == 0:
                    return GameState.PlayerOneWin
                else:
                    return GameState.PlayerTwoWin
    
    return GameState.NotOver

if __name__ == "__main__":
    StartGame()
    input("-- Enter to End --")