#include <stdio.h>
#include <stdlib.h>
#include <time.h>


/*Default seed every time, so it generator same random number on every run*/
#ifdef SAME_SEED
int main() {
    printf("First run:\n");
    for (int i = 0; i < 5; i++) {
        printf("%d ", rand());  // Generates the same sequence every time
    }
    printf("\n");

    return 0;
}
#endif /*SAME_SEED*/

#ifndef RANDOM_SEED
int main()
{
    int count = 0;
    srand(time(NULL));   // Seed the random number generator with current time
    int rand_numb = 0;

    for(int i = 1; i < 20; i++)
    {
        rand_numb = rand();
        printf("Random number = %d\n", rand_numb);
        count++;
    }
    printf("Number of cycles : %d\n", count);z

    return 0;
}
#endif

