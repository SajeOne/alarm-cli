#include "../include/main.h"

int main(int argc, char* argv[]){
    parseArgs(argc, argv);

    return 0;
}

void displayHelp(){

	char* displayStr = "alarm-cli -t <TIMESPAN>\n\nRequired:\n-t <TIMESPAN> Ex. 10h13m1s\n\nOptional:";

	printf("%s\n", displayStr);
}

void parseArgs(int argc, char* argv[]){

	int gnuargs;

	struct option long_options[] = 
	{
		{"timespan", required_argument, 0, 't'},
		{0, 0, 0, 0}
	};

	int option_index;

	gnuargs = getopt_long(argc, argv, "t:", long_options, &option_index);

	if(gnuargs == -1){
		displayHelp();
	}else{
		
		switch(gnuargs){
			case 't':
				printf("option -t with value `%s'\n", optarg);
				break;
			default:
				printf("No args");
		}
	}
	
}
