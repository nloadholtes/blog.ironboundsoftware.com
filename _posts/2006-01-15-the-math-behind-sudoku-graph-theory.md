---
layout:     post
title:      "The math behind Sudoku: Graph Theory"
date:       2006-01-15 12:46:25
categories: blogging
---
[Dr. Dobb's](http://www.ddj.com/) magazine this month has an article entitled "[Sudoku & Graph Theory](http://www.ddj.com/documents/s=9948/ddj0602i/0602i.html)" which caught my eye. The article describes a logical Sudoku solver the authors built that uses graph theory techniques to analyze the puzzle. This really got my attention because graph theory is an important field of mathematics that has a number of applications (network traffic flows for example), and it is something that I'm always interested to learn more about. The first thing the article does is assume the 81 cells of a sudoku puzzle represent a vertex on a graph. They then point out that the numbers that can be assigned to each row, column, or 3x3 square can be thought of as a node of a [bipartite graph](http://mathworld.wolfram.com/BipartiteGraph.html). That node contains a [array](http://en.wikipedia.org/wiki/Array) of numbers that could possibly be in that position on the puzzle. This is exactly what I do when trying to solve a sudoku puzzle, but expressed in mathematical/topological terms. (This is what I was trying to get across in my post about [Sudoku Strategy](http://ironboundsoftware.com/blog/2005/10/20/sudoku-strategy/).)  The article then goes on to present two methods of logically eliminating number from the array to find the correct answer: Pile Exclusion and Chain Exclusion. Sadly, I can not find any links on the web to explain these algorithms in more detail, but the article does an ok job of showing how they work. I do want to point out that if you read the full article, beware that the sample sudoku puzzle they present does not seem to match up with the sample arrays (or vectors as they call them) when they are demonstrating the chain and pile exclusions! My own personal preference seems to be the Pile Exclusion, that seems to match up with how I solve puzzles. It is basically a system where you find groups of numbers that are common across several squares (usually in a 3x3 section, but I often expand it to include the row and column). Usually this works out so that you have two squares where the numbers could be 1,3,7 in one and 1,7 in the other. Then you look at the other squares and if you see that 1 and 7 aren't a choice in any of them, then 1 and 7 must be in the two squares you are looking at. This means that the 3 is not a possible answer, so you can mark it out. This usually winds up helping you figure out where the 3 is supposed to go. The Chain Exclusion is similar in that you are looking for groupings of numbers, but with this algorithm you are looking for the numbers to be shared in other parts of the array in order to rule out other locations. For example, if you have 1,3 and 3,4 and 4,1 as the possible answers in three cells, then other locations in the puzzle that contain a 3 can be ruled out. Personally I find the Chain Exclusion method to be more of a leap than the Pile Exclusion. Both of these methods basically boil down to using logic to reduce (or outright find) the possible numbers that could be the answer. Using both, as the program written for the article does, makes for a powerful set of tools to work your way through the puzzle. The alternative is to do a "[brute force search](http://en.wikipedia.org/wiki/Brute-force_search)" which means simply trying every possible number in ever possible cell until you get the solution. Since there are 81 cells and 9 possible numbers per cell that means there are 9^81 possible answers (in plain english this means 19 followed by 76 zeros) give or take a few depending how many numbers were already filled in for you. Needless to say, using Pile and Chain Exclusions will help you get the puzzle solved **_much_** sooner. So go check out the article in the Feb 2006 issue of Dr. Dobb's magazine, it's a great read. 