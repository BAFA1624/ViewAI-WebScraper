#ifndef SIMPLE_FORMAT_TEXT_H
#define SIMPLE_FORMAT_TEXT_H

#include <stdio.h>
#include <stdlib.h>

unsigned long simple_format_text(char ***ptr, char *text, unsigned long size);
char *ConcatArr(char *arr, unsigned long idx_ini, unsigned long idx_fin);
unsigned long FileSize(FILE *f);

/*
char **simple_format_text(char *text, unsigned long size)
{

    unsigned long i, fullstop_count = 0;

    for (i = 0; i < size; ++i)
    {
        if (text[i] == '.')
        {
            fullstop_count++;
        }
    }

    unsigned long n_strings = (fullstop_count / 2) + (fullstop_count % 2);

    unsigned long result_size = 0;
    char **result = (char **)malloc(n_strings * sizeof(char *));

    unsigned long start_idx = 0, final_idx = size;
    short flag = 0;

    for (i = 0; i < size; ++i)
    {
        if (text[i] == '.')
        {
            if (flag == 0)
            {
                flag = 1;
            }
            else
            {
                char *new_string = ConcatArr(text, start_idx, i);
                result[result_size++] = new_string;
                flag = 0;
                if (text[i + 1] != '\0' && text[i + 1] != ' ')
                {
                    start_idx = i + 1;
                }
                else if (text[i + 1] == ' ')
                {
                    start_idx = i + 2;
                }
                else if (text[i + 1] == '\0')
                {
                    final_idx = i;
                }
            }
        }
    }

    if (result_size != n_strings)
    {
        char *new_string = ConcatArr(text, start_idx, final_idx);
        result[result_size++] = new_string;
    }

    if (result_size != n_strings)
    {
        printf("\nSomething went v. wrong, result_size != n_strings.\n");
    }

    return result;

}
*/

#endif