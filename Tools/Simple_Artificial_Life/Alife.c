#include <stdio.h>
#include <time.h>
#include <windows.h>
#include <stdlib.h>

struct Organism{
    int x;
    int y;
    char name;

    int age;                    //how many second it has lived
    int lifespam;               //how long can it live
    time_t birth_time;          //when was it created
};

int main(){
    
    srand(time(NULL));
    int x = 1;
    int y = 1;

    struct Organism organism[5];
    char map[10][10];

    //organism O
    organism[0].x = 4;
    organism[0].y = 6;
    organism[0].name = 'O';
    organism[0].age = 0;
    organism[0].lifespam = 15;
    organism[0].birth_time = time(NULL);

    //organism 1
    organism[1].x = 2;
    organism[1].y = 2;
    organism[1].name = '1';
    organism[1].age = 0;
    organism[1].lifespam = 10;
    organism[1].birth_time = time(NULL);

    //organism 2
    organism[2].x = 5;
    organism[2].y = 5;
    organism[2].name = '2';
    organism[2].age = 0;
    organism[2].lifespam = 5;
    organism[2].birth_time = time(NULL);

    //map
    for(int i=0;i<10;i++){
        for(int j=0;j<10;j++){
            map[i][j] = '_';
        }
    }
    Sleep(1000);


    while (1)
    {
        
        map[y][x] = '_';
        system("cls");
        

        for(int i=0;i<10;i++){
            for(int j=0;j<10;j++){
                map[i][j] = '_';
                printf(" %c ",map[i][j]);
            }printf("\n");
        }
        
        for(int i=0;i<3;i++){
            organism[i].age = (int)difftime(time(NULL), organism[i].birth_time);

            if(organism[i].age < organism[i].lifespam){
                map[organism[i].y][organism[i].x] = organism[i].name;
            }
        }
        
        
        //organism 0 movement
        int dir0 = rand() % 4;
        if(dir0 == 0) organism[0].x++;
        else if(dir0 == 1) organism[0].x--;
        else if(dir0 == 2) organism[0].y++;
        else if(dir0 == 3) organism[0].y--;

        if(organism[0].x < 0) organism[0].x = 0;
        if(organism[0].x > 9) organism[0].x = 9;
        if(organism[0].y < 0) organism[0].y = 0;
        if(organism[0].y > 9) organism[0].y = 9;



        //organism 1 movement

        int dir1 = rand() % 4;
        if(dir1 == 0) organism[1].x++;
        else if(dir1 == 1) organism[1].x--;
        else if(dir1 == 2) organism[1].y++;
        else if(dir1 == 3) organism[1].y--;

        if(organism[1].x < 0) organism[1].x = 0;
        if(organism[1].x > 9) organism[1].x = 9;
        if(organism[1].y < 0) organism[1].y = 0;
        if(organism[1].y > 9) organism[1].y = 9;
        



        //organism 2 movement

        int dir2 = rand() % 4;
        if(dir2 == 0) organism[2].x++;
        else if(dir2 == 1) organism[2].x--;
        else if(dir2 == 2) organism[2].y++;
        else if(dir2 == 3) organism[2].y--;

        if(organism[2].x < 0) organism[2].x = 0;
        if(organism[2].x > 9) organism[2].x = 9;
        if(organism[2].y < 0) organism[2].y = 0;
        if(organism[2].y > 9) organism[2].y = 9;
    


        for(int i=0;i<3;i++){
            map[organism[i].y][organism[i].x] = organism[i].name;
        }

        for(int y=0;y<10;y++){
            for(int x=0;x<10;x++){
                printf(" %c ",map[y][x]);
            }
            printf("\n");
        }
        Sleep(1000);
        
        
        
        

    }
    
}
