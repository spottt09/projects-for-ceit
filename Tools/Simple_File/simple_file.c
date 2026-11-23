#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){

	printf("===========xXx===========\n");
	printf("    SMALL TEXT MAKER\n");
	printf("===========xXx===========\n");
	
	char loc[50];

	printf("\n");

	printf("enter location or file name\n");
	printf("$:> ");
	fgets(loc, sizeof(loc), stdin);

	printf("\n");

	loc[strcspn(loc, "\n")] = '\0';

	FILE *p = fopen(loc, "w");

	char word[50];
	printf("enter the text to store\n");
	printf("$:> ");
	fgets(word, sizeof(word), stdin);

	printf("\n");
	
	if (p == NULL){
		printf("can't create a file \n");
		return 1;
	}
	
	fprintf(p, "%s",word);

	printf("file is created\n");
	printf("\n");

	int j;
	printf("KEEP (0) OR DELETE (1)\n");
	printf("$:> ");
	scanf("%d",&j);
	printf("\n");
	fclose(p);

	if(j == 1){
		remove(loc);
		printf("file is deleted\n");
		printf("\n");	
	}else{
		printf("file is created\n");
		printf("\n");
	}
	return 0;
}



