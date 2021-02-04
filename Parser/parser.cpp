#include "parser.hpp"
#include <iostream>

std::vector<std::string> format_text(std::string text, char delimiter)
{
    int count = 0;
    for (auto i = text.begin(); i != text.end(); ++i)
    {
        if (*i == delimiter) count++;
    }
    int n_sentences = (count / 2) + (count % 2);
    bool flag = false;
    auto last_pos = 0;
    std::vector<std::string> result(n_sentences);
    for (auto i = 0; i != text.size(); ++i)
    {
        if (text[i] == delimiter && flag)
        {
            std::cout << "last_pos = " << last_pos << " i = " << i << "\n\n";
            result.push_back(text.substr(last_pos, i+1));
            flag = false;
            last_pos = i + 1;
        }
        else if (text[i] == delimiter && !flag)
        {
            //std::cout << "\nFlipping flag -> true." << std::endl;
            flag = true;
        }
    }
    if (result.size() != n_sentences)
    {
        result.push_back(text.substr(last_pos, text.npos - 1));
    }
    return result;
}

