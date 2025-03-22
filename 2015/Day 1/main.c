#include <stdio.h>

int
main(void)
{
    FILE *fptr;
    char ch;
    int floor = 0;

    fptr = fopen("1.txt", "r");

    while((ch = fgetc(fptr)) != EOF) {
        if(ch == '(') {
            floor++;
        } else {
            floor--;
        }
    }

    printf("Floor: %d\n", floor);

    fseek(fptr, 0, SEEK_SET);

    int count = 0;
    floor = 0;
    while((ch = fgetc(fptr)) != EOF && floor != -1) {
        if(ch == '(') {
            floor++;
        } else {
            floor--;
        }

        count++;
    }

    printf("Count: %d\n", count);


    return 0;
}