import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ALIVE = 1
DEAD = 0

def randomGrid(N):
    
    return np.random.choice([ALIVE,DEAD], N*N, ).reshape(N, N)

def update(frameNum, img, current, N,):

    next_gen = current.copy()

    for r in range(N):

        for c in range(N):

            total = 0
        
            if r > 0 and r < N-1 and c > 0 and c < N-1:
                total = (current[r-1][c-1] + current[r-1][c] + current[r-1][c+1]
                    + current[r][c-1] + current[r][c+1]
                    + current[r+1][c-1] + current[r+1][c] + current[r+1][c+1])
        
            elif r == 0 and c > 0 and c < N-1:
                total = (current[r][c-1] + current[r][c+1]
                    + current[r+1][c-1] + current[r+1][c] + current[r+1][c+1])
            
            elif r == N - 1 and c > 0 and c < N - 1:
                total = (current[r-1][c-1] + current[r-1][c] + current[r-1][c+1] + current[r][c-1] + current[r][c+1])
                
            elif r > 0 and r < N - 1 and c == 0:
                total = (current[r-1][c] + current[r-1][c+1] + current[r][c+1] + current[r+1][c] + current[r+1][c+1])
            
            elif r > 0 and r < N - 1 and c == N - 1:
                total = (current[r-1][c-1] + current[r-1][c] + current[r][c-1] + current[r+1][c-1] + current[r+1][c])
            
            elif r == N - 1 and c > 0 and c < N - 1:
                total = (current[r][c+1] + current[r+1][c] + current[r+1][c+1])
            
            elif r == 0 and c == 0:
                total = (current[r][c-1] + current[r+1][c-1] + current[r+1][c])
            
            elif r == N - 1 and c == 0:
                total = (current[r-1][c] + current[r-1][c+1] + current[r][c+1])

            elif r == N - 1 and c == N - 1:
                total = (current[r][c-1] + current[r-1][c-1] + current[r-1][c])
            
            
            
            if current[r][c] == ALIVE:
                if (total < 2) or (total > 3):
                    next_gen[r][c] = DEAD
                else:
                    if total == 3:
                        next_gen[r][c] = ALIVE

    img.set_data(next_gen)
    current[:] = next_gen[:]
    
    return img,


def main():
    
    N = 0
    
    while N < 10 or N > 200:
        
        N = int(input("Enter grid size (10-200): "))
        
        updateInterval = 0
    
    while updateInterval < 10 or updateInterval > 200:
        
        updateInterval = int(input("Enter update speed in ms (10-200): "))
        
        grid = np.array([])
        grid = randomGrid(N)
        

        fig, ax = plt.subplots()
        img = ax.imshow(grid, interpolation='nearest')
        ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
        frames = 10,
        interval=updateInterval,
        save_count=50)
        
        plt.show()

if __name__ == '__main__':
    
    main()