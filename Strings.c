#include "stdio.h"

/*
-- Reading and Writing Strings
-- Combining Strings Togeather
-- Coping One String to Another
-- Comparing Strings for Equality
-- Extracing a portion of a string
*/

#define ARRAY_SIZE 10

void main()
{
    char string_name[ARRAY_SIZE] = "StringName";
    char city[] = "Bangalore";
    char city2[] = {'B', 'A', 'N', 'G', 'A', 'L', 'O', 'R', 'E'};

    printf("city = %s\n", city);
    printf("City2 =%s\n", city2);
    printf("string Name = %s\n", string_name);
}
