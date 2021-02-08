#include "simple_format_text.h"
#include <time.h>

int main()
{
    int n = 1000;
    clock_t start;
    double diff;
    FILE *fp = fopen("test_soup.txt", "r");
    if (!fp)
    {
        printf("\nFailed to open file\n");
        exit(1);
    }
    unsigned long fSize = FileSize(fp);

    char *tmp = (char *)malloc(fSize * sizeof(char));
    char *text = (char *)malloc(fSize * sizeof(char) * n);
    fread((void *)tmp, sizeof(char), fSize, fp);
    for (size_t i = 0, j = 0; j < fSize * n; ++i, ++j)
    {
        if (i == fSize)
            i = 0;
        text[j] = tmp[i];
    }

    char **test = NULL;
    start = clock();
    unsigned long len = simple_format_text(&test, text, fSize);
    diff = ((double)(clock() - start)) / CLOCKS_PER_SEC;

    if (test)
    {
        unsigned long i;
        for (i = 0; i < len; ++i)
        {
            printf("\n%s\n", test[i]);
        }
    }

    printf("\nlen = %lu; Time taken = %lf seconds.\n", len, diff);

    fclose(fp);
}
