#! /bin/bash
echo ** Running C++ on clang
clang++ -std=c++11 -stdlib=libc++ -Weverything ./cpp/LongestPalidrome
echo ** Compile Succeed! 
./a.out