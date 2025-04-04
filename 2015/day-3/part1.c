#include <stdio.h>
#include <stdbool.h>


int
main(void)
{
    FILE *fptr = fopen("input.txt", "r");
    unsigned total_visited = 0;

    bool had_visited[1000][1000] = {false};

    unsigned current_x = 500, current_y = 500;
    char ch;

    had_visited[current_x][current_y] = true;

    while((ch = fgetc(fptr)) != EOF) {
        switch(ch) {
            case '^':
                current_y++;
                break;

            case 'v':
                current_y--;
                break;

            case '>':
                current_x++;
                break;

            case '<':
                current_x--;
                break;
        }

        had_visited[current_x][current_y] = true;
    }

    for(int i = 0; i < 1000; i++) {
        for(int j = 0; j < 1000; j++) {
            if(had_visited[i][j]) total_visited++;
        }
    }

    printf("Total visited: %u\n", total_visited);
}