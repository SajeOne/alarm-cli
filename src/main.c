#include "../include/main.h"

int main(int argc, char* argv[]){
    parseArgs(argc, argv);

    return 0;
}

void displayHelp(){
	char* displayStr = "alarm-cli [-h, -m, -s]\n\nOptions:\n-h <HOURS>\n-m <MINUTES>\n-s <SECONDS>";

	printf("%s\n", displayStr);
}

void parseArgs(int argc, char* argv[]){

	int gnuargs;

	struct option long_options[] = 
	{
		{"hours", optional_argument, 0, 'h'}, 
		{"minutes", optional_argument, 0, 'm'},
		{"seconds", optional_argument, 0, 's'},
		{0, 0, 0, 0}
	};

	int option_index;

    while(1){
        gnuargs = getopt_long(argc, argv, "h:m:s:", long_options, &option_index);

        if(gnuargs == -1){
            break;
        }else{
            
            switch(gnuargs){
                case 'h':
                    printf("option -h with value `%s'\n", optarg);
                    break;
                case 'm':
                    printf("option -m with value `%s'\n", optarg);
                    break;
                case 's':
                    printf("option -s with value `%s'\n", optarg);
                    break; 
                default:
                    printf("No args");
            }
        }
    }
	
}
