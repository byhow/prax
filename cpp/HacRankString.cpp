#include <bits/stdc++.h>

using namespace std;

// Complete the hackerrankInString function below.
// https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
// We say that a string contains the word hackerrank if a subsequence of its characters spell the word hackerrank. For example, if string  it does contain hackerrank, but  does not. In the second case, the second r is missing. If we reorder the first string as , it no longer contains the subsequence due to ordering.

// More formally, let  be the respective indices of h, a, c, k, e, r, r, a, n, k in string . If  is true, then  contains hackerrank.

// For each query, print YES on a new line if the string contains hackerrank, otherwise, print NO.

// Function Description

// Complete the hackerrankInString function in the editor below. It must return YES or NO.

// hackerrankInString has the following parameter(s):

// s: a string
// Input Format

// The first line contains an integer , the number of queries.
// Each of the next  lines contains a single query string .

// Constraints

// Output Format

// For each query, print YES on a new line if  contains hackerrank, otherwise, print NO.

// Sample Input 0

// 2
// hereiamstackerrank
// hackerworld
// Sample Output 0

// YES
// NO
// Explanation 0

// We perform the following  queries:


// The characters of hackerrank are bolded in the string above. Because the string contains all the characters in hackerrank in the same exact order as they appear in hackerrank, we print YES on a new line.
//  does not contain the last three characters of hackerrank, so we print NO on a new line.
// Sample Input 1

// 2
// hhaacckkekraraannk
// rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt
// Sample Output 1

// YES
// NO


string hackerrankInString(string s) {
    string target = "hackerrank";
    if (s.length() < target.length()) return "NO";
    int j = 0;
    for (int i = 0; i< s.length(); i++) {
        if (j < s.length() && s[i] == target[j]) {
            j++;
        }
    }
    return j==target.length()?"YES":"NO";

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int q;
    cin >> q;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string s;
        getline(cin, s);

        string result = hackerrankInString(s);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}
