# Discussion
- Improve Implementing skills by implementing compact complex operations that cannot be simplified
- Every problem helps you to tackle a different challenge so that you focus more on things you are not keeping in mind currently to improve your overall thinking of software problem solving
- Learn to always handle special cases (Program must not crash under any circumstance)
- Least astonishment rule says that a good implementation means that it matches the expected solution design that first comes into your mind. This can be accomplished by implementing typically the design in your head without any side operations
- Learn about off-by-one errors and its sibling problems by applying the following
  1. Focus on inclusive and exclusive loop ranges
  2. Always search for edge cases
- Use mnemonic naming to help you typically implement the design in your mind

### Problem 2: Mathematical Expression
Need to handle division by zero error
> Lesson: Handling Edge Cases
1. put c = 0
2. put f+g = 0
3. put d+e = 0


### Factorial
> Lesson: Handling Edge Cases

Have a look at the guide
1. I am happy you handled large numbers but I don't know why you specified 12 as the limit 
2. Need to handle negative inputs as they cause infinite loop.

### Prime
> Lesson: Edge Cases
1. Program does exit silently for all digits below 9
2. The problem exits silently when you enter negative, 0, or 1 instead of just saying they are not prime.

### Sin
Have a look at the guide. I cannot find problem this in the submitted solutions

### Circular Shift
> Lesson: Readability and Edge Cases

Have a look at the guide
1. Readability is hard (Some literals are arrays, and others are iterators)
2. if steps is larger than n. Just apply steps % n (nothing happens without informing)
3. If steps is negative. Left shift should be applied or just say it's not allowed but it appears that the program ran with invalid output

### Transpose
> Lesson: هتعرفه لوحدك ;)

1. No need to initialize python arrays with zeroes as they are dynamically allocated and can be easily extended. I know you mapped the numpy code into custom methods blindly :D and that's why I hate using utilities in problem solving classes. That was astonishing :D :D. However, Good job

### Merge of sorted arrays
Can't find it :(
Have a look at the guide

### GCD
> Performance and edge cases

Have a look at the guide
1. No need to get both numbers divisors. Just evaluate divisors for the smaller
2. No need to loop over all numbers from i up to n. i to n / 2 are needed only
3. range method has inclusive start and exclusive end meaning that the compare loop doesn't check for the smallest item in both divisors array. What saved the logic from failure is storing a useless item in the divisors list which is the 1 :D 

### Union
> Lesson: Edge Cases and Performance

Have a look at the guide
1. Sets is a powerful datastrcture. That's not what we meant by the app. It's not about delivering the task in any form. Sets do have predefined union and intersect operators and you could've just appliied (set1 | set2) but we are learning to implement details by ourselves so that we can easily write slightly complex algorithms. This problem can be implemented using normal for loops and indexing

### Max Row
Numpy is not allowed. Don't name a variable with the same name used for a function

### Matrix Multiplication
Same transpose comment.

### Convert to base n
> Lesson: Different Scenario Handling. You must study the domain for your problem before testing in order to ensure that you cover the whole domain of operation

Have a look at the guide
1. Working good with binary but not with other bases. 

### Circular Subarry Shift
Have a look at the guide. Not found in submitted responses

### Sum of digits
Have a look at the guide.
> Lesson: Keep it simple
1. used too many excess loops
2. used additional space as well

### Big Integer Multiplication
Not found. Have a look at the guide

### fibonacci
Not found. Have a look at the guide