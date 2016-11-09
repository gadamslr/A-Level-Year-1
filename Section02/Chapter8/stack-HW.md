#Chapter 8: Stacks Homework
Before attempting the questions, read Chapter 8 of your textbook (http://my.dynamic-learning.co.uk/).

##Question 1

1. Draw a diagram of the state of a stack after Jones, Smith, Peters, Franklin and Taylor have been added to the stack, in the order given. (**2 marks**)
2. Draw another diagram showing the state of the stack after two names have been popped off the stack. (**1 mark**)

##Question 2

1. Draw a diagram showing the array implementation (maximum 6 elements) of a circular queue after Jones, Smith, Peters, Franklin and Taylor have joined the queue, in the order given. You should also show the Front and Rear pointers. (**2 marks**)
2. Draw another diagram showing the state of the queue after 2 people have left from the front of the queue. Also show the Front and Rear pointers. (**2 marks**)
3. Draw a third diagram showing the state of the queue after 3 more people have joined the queue from **Q2.2** above. (**2 marks**)

##Question 3

A *recursively-defined* `function B`, which takes an integer as its single parameter, is defined below. The operators `//` and `%` perform integer arithmetic.

``x // y`` 'Floor Division' calculates how many times y divides exactly into x. For example `7 // 3 = 2`.

`x % y` 'Modulus' calculates the remainder that results. For example `7 % 3 = 1`.

````python
def B(number):
    if number == 0 or number == 1:
        print(number)
    else:
        B(number // 2)
        print(number % 2)
````

1. What is meant be recursively-defined? (**1 mark**)
2. Why is a stack necessary to execute procedure `B` recursively? (**1 mark**)
3. Dry run procedure call `B(53)` showing clearly the values of the parameter and the printed output for the six calls of `B`. (**6 marks**)

    |Call Number|Parameter|Output|
    |:---------:|:-------:|:----:|
    |1|53| |
    |2|26| |
    |3|13| |
    |4| | |
    |5| | |
    |6| | |

    **Final output**:

4. What process does procedure B describe? (**1 mark**)


**Total 18 marks**
