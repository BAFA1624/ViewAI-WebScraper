#include <fstream>
#include <iostream>
#include <string>
#include "parser.hpp"

std::string open_file(std::string filename)
{
    std::string result;
    std::ifstream file(filename);
    if (file.is_open())
    {
        //std::cout << "Successfully opened " << filename << '.' << std::endl;
        while(getline(file, result, '\n'));
        file.close();
    }
    else
    {
        result = "";
        //std::cout << "Failed to open " << filename << '.' << std::endl;
    }
    //std::cout << "Finished open_file" << std::endl;
    return result;
}

int main()
{
    std::string test = open_file("test_soup.txt");
    
    //std::cout << test << std::endl;

    std::vector<std::string> formatted_str = format_text(test, '.');
    for (auto i = formatted_str.begin(); i != formatted_str.end(); ++i)
    {
        std::cout << *i << "\n\n";
    }
}
