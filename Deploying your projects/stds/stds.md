Item 3 - CLI Ins and Outs
Lesson content
Item 4 of 16
# Exercise: Stds
## Intro

wincpy start 8c2e6882503c4baa9ce2e050497c3f2f

In this exercise you will learn to use stdin, stdout, stderr and exit codes with Python. Here is a link to the Python documentation that you will probably find very helpful:

Python Docs -- sys.stdin, sys.stdout and sys.stderr(opens in a new tab)

In particular, notice that the documentation says:

"These streams are regular text files(opens in a new tab) like those returned by the open() function."

This means you can use, among other methods, .read() and .readline() on sys.stdin and write() on sys.stderr and sys.stdout.

## Exercise

Write a Python program that reads text from stdin, filters a given character from it and writes the result to stdout. The number of characters removed should be written to stderr. For example:

```
$ echo 'abc' | python main.py a
bc
1

$ echo 'aabccc' | python main.py c
aab
3

$
```
💡 Tip

If it is not redirected in some way, stderr is printed to your terminal right along side of stdout. While you're working on debugging your program you can add some text that tells you which stream you're looking at. We will later discuss how to redirect I/O streams.

When you start the assignment with Wincpy, you should see a file named random.txt inside the stds directory. You can read this file with cat and feed it to the stdin of your program by using the pipe symbol (|):

```
# This shows the first line of random.txt with all occurences of `a` removed
$ cat random.txt | python main.py a | head -n 1
0000000 8294 e3 d6b3 4167 0ef b1c8 952 e78
```
You can use pytest to test your implementation with the tests supplied in test_main.py.