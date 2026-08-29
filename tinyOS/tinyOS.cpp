#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <direct.h>


void prompt(){
	char cwd[256];
	
	if (getcwd(cwd, sizeof(cwd)) != 0){
		char *folder = strrchr(cwd,'\\');
		
		if(folder != 0){
			printf("%s>",folder+1);
		}else{
			printf("%s>",cwd);
		}
	}else{
		printf("tinyOS>");
	}
}



void cd(const char* command){
	char folder[100];
	
	if (sscanf(command,"cd %s",folder)==1){
		
		if(chdir(folder)==0){
			printf("directory changed\n");
		}else{
			printf("cannot find that directiory\n");
		}
	}else{
		printf("invalid directory broo\n");
	}
}


void delete_folder(const char* command){
	char folder[100];
	
	if(sscanf(command,"delete %s",folder)==1){
		if(rmdir(folder)==0){
			printf("folder deleted\n");
		}else{
			printf("cannot delete sorry\n");
		}
	}else{
		printf("invalid broo\n");
	}
	
}

void folder(){
	char folder[100];
	printf("folder name>");
	scanf("%s",folder);
	while (getchar() != '\n');
	
	if(mkdir(folder)==0){
		printf("folder created\n");
	}
	else{
		printf("cannot create sorry\n");
	}
}


void note(){
	char text[100];
	printf("\n-------tiny note--------\n");
	printf("type your note here\n");
	while (1){
		printf("text>");
		
		fgets(text,sizeof(text),stdin);
		text[strcspn(text,"\n")]='\0';
		
		
		if(strcmp(text,"quit")==0){
			break;
		}
	}
}

void about(){
	printf("usable commands are \n");
	printf("whoami  \nhello   \n");
	printf("whomadeit   \n");
	printf("clear   \n");
	printf("shutdown \n");
	printf("ls  \nmkdir(for creating folder) \n");
	printf("delete(for deleting folder)\n");
	printf("cd(for changing direction)\nnote\n");
	printf("cd ..(for original directory \n)");
	
}

int main(){
	
	char command[100];
	char filename[100];
	
	
	printf("type about to learn more \n");
	
	while(1){
		
		
		prompt();
		
		fgets(command,sizeof(command),stdin);
		command[strcspn(command,"\n")]='\0';
		
		if(strcmp(command,"hello")==0)
		{
			printf("Hello, welcome bro \n");
		}
		
		else if(strcmp(command,"whoami")==0){
			printf("you are the goat for testing tinyOS");
		}
		
		
		else if(strcmp(command,"whomadeit")==0)
		{
			printf("DXQJ NKDQW \n");
		}
		
		else if(strcmp(command,"about")==0)
		{
			about();
		}
		
		else if(strcmp(command, "clear")==0)
		{
			system("cls");
		}
		
		else if(strcmp(command,"shutdown")==0)
		{
			printf("thanks for testing me :)");
			break;
			
		}
		
		else if(strcmp(command,"mkdir")==0)
		{
			folder();
		}
		
		
		else if(strncmp(command,"delete",6)==0)
		{
			delete_folder(command);
		}
		
		
		else if(strcmp(command,"ls")==0)
		{
			system("dir");
		}
		
		else if(strcmp(command,"note")==0)
		{
			note();
		}
		
		else if(strncmp(command,"cd ",3)==0)
		{
			cd(command);
		}
		
		
		
	}
	
}
