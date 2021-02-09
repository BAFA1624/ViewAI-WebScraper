#include <iostream>
#include <fstream>
#include <chrono>
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
    
    std::string text = "";
    for (int i = 0; i < 20; ++i)
        text += open_file("test_soup2.txt");
    Parser test;
    test.setText(text);
    //std::cout << test.text() << std::endl;

    auto start = std::chrono::high_resolution_clock::now();
    test.replace_tokens(text);
    auto end = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();

    std::cout << duration << std::endl;



}
