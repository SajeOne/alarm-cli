#include "../include/main.h"

int main(int argc, char* argv[]){
    parseArgs(argc, argv);

    return 0;
}

void displayHelp(){
	char* displayStr = "Alarm CLI v1.0 : Shane Brown\n\nusage: [-h HOURS, -m MINS, -s SECS] TIME [-d] DAEMON [-n NAME] [-i ALARM INFO]";

	printf("%s\n", displayStr);
}

void parseArgs(int argc, char* argv[]){
	int anyArgs = 0;

	int opt;
	while((opt = getopt(argc, argv, "h:m:s:dn:i:")) != -1){
		anyArgs = 1;
		switch(opt){
			case 'h':
				printf(optarg);
				break;
			case 'm':
				printf(optarg);
				break;
			case 's':
				printf(optarg);
				break;
			case 'd':
				printf("DAEMON MODE");
				break;
			case 'n':
				printf("Name: %s\n", optarg);
				break;
			case 'i':
				printf("Info: %s\n", optarg);
				break;
			default:
				printf("Invalid Arg");
		}

	}

	if(anyArgs < 1){
		displayHelp();
	}
}
