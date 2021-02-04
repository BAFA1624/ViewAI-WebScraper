#include "simple_format_text.h"

int main()
{
    FILE *fp = fopen("test_soup.txt", "r");
    unsigned long fSize = FileSize(fp);

    char *text = (char *)malloc(fSize * sizeof(char));
    fread((void *)text, sizeof(char), fSize, fp);

    char **test = NULL;
    unsigned long len = simple_format_text(test, text, fSize);

    unsigned long i;
    for (i = 0; i < len; ++i)
    {
        printf("\n%s\n", test[i]);
    }

    fclose(fp);
}
