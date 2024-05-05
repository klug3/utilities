#include <stdio.h>
#include <string.h>
#define LENGTH 1024

char ExtractFeature()
{

    return 0;
}

int main()
{
    char line[LENGTH];

    while (fgets(line, LENGTH, stdin) != NULL)
    {
        if (strlen(line) < LENGTH || line[strlen(line) - 1] == '/0') // Check if full line got loaded
        {
            /* code */
        }
        else // Line was too long
        {
            /* Report error and suggest to increase LENGTH using -n param. Exit. */
        }
    }

    return 0;
}
