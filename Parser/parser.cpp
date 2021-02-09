#include "parser.hpp"

// -----------------------------------------
// Function implementations for class Parser
// -----------------------------------------

// Tested.
template <class X, class Y>
bool in_iterable(const std::map<X, Y> &map, const X key)
{
    for (auto it = map.begin(); it != map.end(); ++it)
    {
        if (it->first == key)
            return true;
    }
    return false;
}

// Tested.
template <class X, class Y>
const Y &get_value(const std::map<X, Y> &map, const X &key)
{
    for (auto it = map.begin(); it != map.end(); ++it)
    {
        if (it->first == key)
            return it->second;
    }
    return key;
}

// Tested.
std::string Parser::replace_tokens(const std::string &text)
{
    std::string temp = text;
    for (size_t i = 0; i != text.size(); ++i)
    {
        if (text[i] == '.')
        {
            size_t max = i + TOKEN_CHECK_RANGE;
            if (max > text.npos)
                max = text.npos;
            for (size_t j = i; j < max; ++j)
            {
                std::string key = text.substr(i, j - i + 1);
                bool existing_key = in_iterable(ForwardFormatMap_, key);
                if (existing_key)
                {
                    std::string value = get_value(ForwardFormatMap_, key);
                    temp.replace(i, j - i + 1, value);
                }
            }
        }
    }
    return temp;
}
// Untested.
std::vector<std::string> Parser::replace_tokens(std::vector<std::string> &tokens)
{
    for (auto it = tokens.begin(); it != tokens.end(); ++it)
    {
        auto token = it;
        for (int i = 0; i < token->npos - TOKEN_CHECK_RANGE; ++i)
        {
            for (int j = 0; j < i + TOKEN_CHECK_RANGE; ++j)
            {
                std::string key = token->substr(i, j - i + 1);
                bool existing_key = in_iterable(BackwardFormatMap_, key);
                if (existing_key)
                {
                    std::string value = get_value(BackwardFormatMap_, key);
                    token->replace(i, j - i + 1, value);
                }
            }
        }
    }
    return tokens;
}

// Untested.
std::vector<std::string> sentence_tokenize(const std::string &text);

// -----------------------------------------

// Testing a simplistic formatting function
std::vector<std::string> format_text(std::string text, char delimiter)
{
    int count = 0;
    for (auto i = text.begin(); i != text.end(); ++i)
    {
        if (*i == delimiter)
            count++;
    }
    int n_sentences = (count / 2) + (count % 2);
    bool flag = false;
    auto last_pos = 0;
    std::vector<std::string> result(n_sentences);
    for (auto i = 0; i != text.size(); ++i)
    {
        if (text[i] == delimiter && flag)
        {
            result.push_back(text.substr(last_pos, i + 1));
            flag = false;
            last_pos = i + 1;
        }
        else if (text[i] == delimiter && !flag)
        {
            flag = true;
        }
    }
    if (result.size() != n_sentences)
    {
        result.push_back(text.substr(last_pos, text.npos - 1));
    }
    return result;
}
