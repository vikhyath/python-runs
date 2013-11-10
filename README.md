Various interesting problems solved in python.
-----------------------------------------
TODO: need to write 1 line description of all files in the below format, here is a start.

- static-and-inheritance - Program illustrating static and inheritance.

- custom-dictionary-sort - Sort the input character array based on the dictionary given.

- repeated-elements - Finding a maximum of k-1 most repeated elements, repeated n/k times from a set n. Run time O(n) and space complexity O(k).

- hr-two-arrays - https://www.hackerrank.com/challenges/two-arrays
You are given two integer arrays, A and B, each containing N integers. The size of the array is <= 1000. You are free to permute the order of the elements in the arrays.
Now for the real question - is there an arrangement of the arrays such that Ai+Bi>=K for all i where Ai denotes the ith element in the array A.

- hr-pairs - https://www.hackerrank.com/challenges/pairs
Given N integers [N<=10^5], count the total pairs of integers that have a difference of K. [K>0 and K<1e9]. Each of the N integers will be greater than 0 and at least K away from 2^31-1 (Everything can be done with 32 bit integers).

- code-formatter - program acts as code formatter
      1. reads an input file named input.txt and ensures no more than SIZE number of chars per line are present
      2. if more chars than SIZE(max_limit) are present then split at space, insert / wherever we want to split
      3. if space is found after the SIZE allowed chars, split after. Let us say SIZE is 5 and space is found at 7th, split at 7th . output is written to output.txt
      4. see code and input.txt for various cases

- hr-regex-ide-comment-extractor - https://www.hackerrank.com/contests/regex-practice-1/challenges/ide-identifying-comments
 Your task is to write a program, which accepts as input, a C or C++ or Java program and outputs only the comments from those programs. Your program will be tested on source codes of not more than 200 lines.

- hr-regex-latitude-longitude - https://www.hackerrank.com/contests/regex-practice-1/challenges/detecting-valid-latitude-and-longitude
Determine valid latitude/longitude pairs. Given a line of text which possibly contains the latitude and longitude of a point, can you use regular expressions to identify the latitude and longitude referred to.

- custom-hashing - 
    1. custom hashmap in python, TODO: change dict to a list to better reflect array
    2. SIZE is the max size of hashmap
    3. collisions resolved using linear probing

- language-checker - http://www.careercup.com/question?id=4774716350922752<br>In a language, there are only 4 characters h, i, r, e. and we have to write a function which takes a string as input and returns whether the given input string is a valid-word or not.<br>
Runs in O(n) time, constant size space, the check terminates ones it determines that an alien character not present in our language definition has been found.<br>
Definition of valid word : 
    1. A given word is a valid word if it is of the form h^n i^n r^n e^n where n >=1. (eg: hhiirree) 
    2. Valid words has concatenation property i.e. if w1 and w2 are valid words w1w2 is also a valid word.

- integer-array-sum: You have two integer arrays. Treat these arrays as if they were big numbers,
with one digit in each slot. Perform addition on these two arrays and store the results in a new array. Ref: http://www.careercup.com/question?id=6330205329162240

- http://codercareer.blogspot.com/2011/10/no-09-numbers-with-given-sum.html | Given an increasingly sorted array and a number s, please find two numbers whose sum is s. If there are multiple pairs with sum s, just output any one of them.

- Dynamic programming: Longest increasing subsequence. Given an unsorted array, find the max length of subsequence in which the numbers are in incremental order. Refer http://stackoverflow.com/questions/2631726/how-to-determine-the-longest-increasing-subsequence-using-dynamic-programming for a great discussion.
