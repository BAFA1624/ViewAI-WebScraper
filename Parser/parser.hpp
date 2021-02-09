#pragma once

#include <string>
#include <vector>
#include <map>
//#include <regex>
//#include <algorithm>

#define TOKEN_CHECK_RANGE 3

template <class X, class Y>
bool in_iterable(const std::map<X, Y> &map, const X key);

template <class X, class Y>
const Y &get_value(std::map<X, Y> &map, X &key);

class Parser
{
private:
    // Private member attributes.
    std::string text_;
    std::vector<std::string> tokens_;

    // Hashmaps to convert problematic characters to understandable versions.
    static inline const std::map<std::string, std::string> ForwardFormatMap_{
        {"...", "__ELLIPSE"},
        {".\"", "__ENDQUOTE"}};
    static inline const std::map<std::string, std::string> BackwardFormatMap_{
        {"__ELLIPSE", "..."},
        {"__ENDQUOTE", ".\""}};
    static inline const std::map<std::string, std::string> SentenceEndPointMap_{
        {"__ENDQUOTE", ".\""}};

    // Private member functions:
    std::string replace_tokens(const std::string &text);

public:
    // Constructors, destructors, etc.
    Parser();
    Parser(const std::string& text) : text_ {text} {};
    Parser(const std::vector<std::string>& tokens) : tokens_ {tokens} {};

    // Getters / setters
    std::string text() { return text_; };
    std::vector<std::string> tokens() { return tokens_; };
    void setText(std::string text) { text_ = text; };
    void setText(char *text)
    {
        std::string tmp(text);
        text_ = tmp;
    };

    // Public member functions:

    // Only public while testing
    std::vector<std::string> replace_tokens(std::vector<std::string> &tokens);

    // Convert to sentence tokens.
    std::vector<std::string> sentence_tokenize();
    std::vector<std::string> sentence_tokenize(const std::string &text);
    std::vector<std::string> sentence_tokenize(char *text);

    // Convert to word & punctuation tokens.
    std::vector<std::string> word_tokenize(std::string text);
    std::vector<std::string> word_tokenize(char *text);
};

std::vector<std::string> format_text(std::string text, char delimiter);
