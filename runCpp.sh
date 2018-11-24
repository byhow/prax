#! /bin/bash
echo ** Running C++ on clang
clang++ -std=c++11 -stdlib=libc++ -Weverything ./cpp/KMP.cpp
echo ** Compile Succeed! 
./a.out