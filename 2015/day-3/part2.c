#include <stdio.h>
#include <stdbool.h>


#define SANTA 1
#define ROBO -1


int
main(void)
{
    FILE *fptr = fopen("input.txt", "r");
    unsigned total_visited = 0;

    bool had_visited[1000][1000] = {false};

    unsigned santa_x = 500, santa_y = 500;
    unsigned robo_x = 500, robo_y = 500;

    had_visited[santa_x][santa_y] = true;

    char ch;
    int turn = SANTA;

    while((ch = fgetc(fptr)) != EOF) {
        switch(ch) {
            case '^':
                if(turn == SANTA) {
                    santa_y++;
                } else {
                    robo_y++;
                }

                break;

            case 'v':
                if(turn == SANTA) {
                    santa_y--;
                } else {
                    robo_y--;
                }

                break;

            case '>':
                if(turn == SANTA) {
                    santa_x++;
                } else {
                    robo_x++;
                }

                break;

            case '<':
                if(turn == SANTA) {
                    santa_x--;
                } else {
                    robo_x--;
                }
        }

        if(turn == SANTA) {
            had_visited[santa_x][santa_y] = true;
        } else {
            had_visited[robo_x][robo_y] = true;
        }

        turn *= -1;
    }

    for(int i = 0; i < 1000; i++) {
        for(int j = 0; j < 1000; j++) {
            if(had_visited[i][j]) total_visited++;
        }
    }

    printf("Total visited: %u\n", total_visited);

    return 0;
}