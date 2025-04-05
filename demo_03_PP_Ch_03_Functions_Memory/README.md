# Chapter 3, Part A: Using Functions

## Functions That Python Provides

Some functions are *built-in*

```python 
>>> abs(-9)
9
>>> abs(3.3)
3.3
``` 

A *function call* is of the form
```function_name(argument_1, argument_2, argument_3, ...)```.
Arguments can be any value stored in memory. 
That is, any variable or value that is defined before the function call. 


```python 
>>> day_temperature = 10
>>> night_temperature = 3
>>> abs(day_temperature - night_temperature)
7
>>> day_temperature = 3
>>> night_temperature = 10
>>> abs(day_temperature - night_temperature)
7

``` 
You can combine the outputs of functions as operands in
arithmetic operators: 
```python 
>>> abs(-7) + abs(3.3)
10.3
``` 


```python 
>>> 3 + 5 / abs(-2)
5.5

``` 
or as arguments in other functions

```python 
>>> pow(abs(-2), round(4.3))
16

``` 

Some functions convert from one type to another

```python 
>>> int(34.6)
34
>>> int(-4.3)
-4
>>> float(21)
21.0

``` 
The ```help``` function will show documentation for a function.

```python 
>>> help(abs)
Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.

``` 
The ```round``` function also converts a floating-point number 
into an integer:

```python 
>>> round(3.8)
4
>>> round(3.3)
3
>>> round(3.5)
4
>>> round(-3.3)
-3
>>> round(-3.5)
-4

``` 
but it can also be used to convert to a float with fewer significant digits.

```python 
>>> round(3.141592653, 2)
3.14

``` 


```python 
>>> help(round)
Help on built-in function round in module builtins:

round(...)
    round(number[, ndigits]) -> number

    Round a number to a given precision in decimal digits (default 0 digits).
    This returns an int when called with one argument, otherwise the
    same type as the number. ndigits may be negative.

``` 
There is more than one way to calculate exponents. 

```python 
>>> help(pow)
Help on built-in function pow in module builtins:

pow(x, y, z=None, /)
    Equivalent to x**y (with two arguments) or x**y % z (with three arguments)

    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.

``` 
If you pass only two arguments, it takes the empty value ```None``` by default.

```python 
>>> pow(2, 4)
16
``` 
If the third argument is provided, it performs the additional calculation. 

```python 
>>> pow(2, 4, 3)
1
``` 


## Memory Addresses: How Python Keeps Track of Values

The name of each variable corresponds to a location in memory.
The ```id``` function returns an integer that identifies that location in memory.

```python 
>>> help(id)
Help on built-in function id in module builtins:

id(obj, /)
    Return the identity of an object.

    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)

``` 

Some values are already stored in memory.

```python 
>>> id(-9)
4301189552
>>> id(23.1)
4298223160
```

Other variables that you create are immediately assiggned to locations in memory.
```python
>>> shoe_size = 8.5
>>> id(shoe_size)
4298223112
>>> fahrenheit = 77.7
>>> id(fahrenheit)
4298223064

``` 
Even functions are classified as objects in memory and 
are assigned to locations in memory. 
```python 
>>> id(abs)
4297868712
>>> id(round)
4297871160

``` 

### Python Remembers and Reuses Some Objects

Python stores some very common numbers in special places in memory
and reuses these locations as needed. 
```python 
>>> i = 3
>>> j = 3
>>> k = 4 - 1
>>> id(i)
4296861792
>>> id(j)
4296861792
>>> id(k)
4296861792

``` 
This is not the case for larger integers or floats. 
```python 
>>> i = 30000000000
>>> j = 30000000000
>>> id(i)
4301190928
>>> id(j)
4302234864
>>> f = 0.0
>>> g = 0.0
>>> id(f)
4298223040
>>> id(g)
4298223016

``` 



## Defining Our Own Functions

You might want to have a function that can convert temperature from
Fahrenheit to Celsius.
It should work as follows.

```python 
>>> convert_to_celsius(212)
100.0
>>> convert_to_celsius(78.8)
26.0
>>> convert_to_celsius(10.4)
-12.0

``` 
But if you run those function calls before the function is defined, 
Python throws an error:

```python 
>>> convert_to_celsius(212)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'convert_to_celsius' is not defined

``` 
So, you have to define the function. 
Function definitions take the following format:

```python 
>>> def convert_to_celsius(fahrenheit):
...     return (fahrenheit - 32) * 5 / 9
...

``` 
The indenting is important because that is how Python
knows when the function definition is complete. 

```python 
>>> def convert_to_celsius(fahrenheit):
... return (fahrenheit - 32) * 5 / 9
  File "<stdin>", line 2
    return (fahrenheit - 32) * 5 / 9
         ^
IndentationError: expected an indented block

``` 
After the function is defined, you can use it
just as you would for built-in functions. 

```python 
>>> def convert_to_celsius(fahrenheit):
...     return (fahrenheit - 32) * 5 / 9
... 
>>> convert_to_celsius(80)
26.666666666666668

``` 
When you use a function to calculate its output from the arguments, 
it is called *calling* the function.
Test it with a few values.

```python 
def convert_to_celsius(fahrenheit):
	return (fahrenheit - 32) * 5 / 9

convert_to_celsius(80)
convert_to_celsius(78.8)
convert_to_celsius(10.4)

``` 

Look for some documentation, just as you would for built-in finctions.

```python 
>>> help(convert_to_celsius)
Help on function convert_to_celsius in module __main__:

convert_to_celsius(fahrenheit)

``` 

There is no documentation. 
*You* made the function, *you* provide the documentation. 
You do that by including a docstring, a description
enclosed in triple quotes, which includes a written 
description and some examples. 

```python 
def convert_to_celsius(fahrenheit: float) -> float:
    """Return the number of Celsius degrees equivalent to fahrenheit
    degrees.

    >>> convert_to_celsius(75)
    23.88888888888889
    """

    return (fahrenheit - 32.0) * 5.0 / 9.0


convert_to_celsius(80)
convert_to_celsius(78.8)
convert_to_celsius(10.4)

``` 

Now try the ```help``` function again. 



### Keywords Are Words That Are Special to Python

Because the ```def``` keyword was used to define a function, 
it cannot be used as a variable. 

```python 
>>> def = 3
  File "<stdin>", line 1
    def = 3
        ^
SyntaxError: invalid syntax
```
The same applies to built-in function names that are already defined. 

```python
>>> def return(x):
  File "<stdin>", line 1
    def return(x):
             ^
SyntaxError: invalid syntax

``` 

But be careful: this does not apply to functions that *you* define. 
When you overwrite your own function, the original definition 
is discarded and replaced with the new function. 




## Using Local Variables for Temporary Storage

It often helps make code more clear when you use separate 
local variables for intermediate calculations. 
These are called *local* variables because they are only 
defined in the memory allocated within the function. 

```python 
>>> def quadratic(a, b, c, x):
...     first = a * x ** 2
...     second = b * x
...     third = c
...     return first + second + third
...
>>> quadratic(2, 3, 4, 0.5)
6.0
>>> quadratic(2, 3, 4, 1.5)
13.0

``` 

After you run the function, these variables 
no longer exist outside of the function. 

```python 
>>> quadratic(2, 3, 4, 1.3)
11.280000000000001
>>> first
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'first' is not defined
```

Even the arguments are only defined within the function. 
Try calling a value that was defined within the quadratic function. 
```python
>>> a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined

``` 

These arguments, without a default value, must be provided, 
even if you assigned them a value in a previous function call. 
```python 
>>> quadratic(1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: quadratic() takes exactly 4 arguments (3 given)

``` 
The more errors you see, the easier it will be for you to 
identify what the problem is and how to fix it. 

## Tracing Function Calls in the Memory Model

What do you think this function does?

```python 
>>> def f(x):
...     x = 2 * x
...     return x
...
>>> x = 1
>>> x = f(x + 1) + f(x + 2)
``` 

Python keeps track of all the intermediate calculations
in separate places in memory, one for each of the different ```x```'s above.


# Chapter 3, Part B: Designing Functions



## Designing New Functions: A Recipe



In this demo, we will study the process of designing functions. 
We will follow the 5-step process in the textbook *Practical Programming*, 
Chapter 3, called the *Function Design Recipe*. 
It is called a recipe because it guides you to follow a systematic approach to designing your function. 
Every time you write a function, you need to answer the following questions:

* What do you name the function? 
* What are the arguments, and what types of information do they represent?
* What calculations does the function do with that information?
* What does the function return?
* Does the function work as expected?

You will address these questions by following the recipe shown next. 

## The Function Design Recipe

The five steps are as follows:

1. **Examples** Type a few example calls and determine what the function should return for those values. 
The examples define a name of your function that should indicate what is being calculated in your examples. 
1. **Description** Write one or more sentences to describe what your function does. 
1. **Header** Type some documentation relating to your function. 
It should be clear to the reader what arguments it takes as input, what value is returned and the type of each variable. 
1. **Body** By now, you should be clear about how your function will work. 
Now type the code to perform the calculations. 
1. **Test** Run the examples from step 1 to verify that your function works as expected. 


## Function Design Example


Consider the simple example of the function ```add_two_numbers``` that, well, adds two numbers.

```python
# Define a function without documentation.
>>> def add_two_numbers(first_number, second_number):
...    
...    total = first_number + second_number
...    
...    return total
...
...
```

The function is fine but how does the user know how it works. 
Guessing is only reasonable if the function is simple. 

```python
>>> add_two_numbers(3,4)
7
```

That makes sense and it appears to work. 
If your users want to know for sure, they can
search for documentation, as they would for any other function.

```python
>>> help(add_two_numbers)
Help on function add_two_numbers in module __main__:

add_two_numbers(first_number, second_number)
```
There's nothing there yet.

You could print the entire function object but that
is not very convenient for long and complex functions.
```python
>>> add_two_numbers
<function __main__.add_two_numbers(first_number, second_number)>
```

Instead, add documentation to the function in a docstring, 
which is a string of text enclosed in triple quotes
at the top of the function.


```python
>>> def add_two_numbers(first_number, second_number):
...    """ Add two numbers together and return the sum.
...    
...    """
...    
...    total = first_number + second_number
...    
...    return total
...
```



Now test the documentation by calling for help:
```python
>>> help(add_two_numbers)
Help on function add_two_numbers in module __main__:

add_two_numbers(first_number, second_number)
    Add two numbers together and return the sum.
```

Notice the content from the description in the docstring.

We can improve the docstring by including examples,
so now let's cover all of these step by following
the *function design recipe*.



## Function Design Recipe

Now apply the function design recipe to the ```add_two_numbers``` example.

### Examples

Try to think of some examples that will test the limits of your function.
Note that we can run the tests only because we have already defined the
function in the examples above.

```python
>>> add_two_numbers(3,4)
7
>>> add_two_numbers(0,4)
4
>>> add_two_numbers(-3,3)
0

```

Now you know that your function will have a form like this.

```python
>>> def add_two_numbers(first_number, second_number):
...    
...    
...    
...    return total
...
...
```
In mathematics, it is common to use Roman and Greek letters of the
alphabet to define the arguments to your function. 
In contrast, in computer programming it is customary to define names that
are more descriptive. 
For example, a function that estimates a linear regression model
might have a type contract such as 

```python
>>> def linear_reg(y, x):
...    
...    # Calculate beta_hat.
...    
...    return beta_hat
...
...
```

Notice that you would not enter Greek letters such as &alpha; or &beta; 
in your script because that would require a larger set of characters
and cause bugs on some platforms. 
You might, however, elect to define variable names that spell
out these symbols if it matches the related terminology. 
For maximum functionality, keep your code within the Roman alphabet, 
possibly using underscores for spaces and numbers to differentiate variables. 


### Header

Write a header to contain information about the
the types of variables in your function.


```python
>>> def add_two_numbers(first_number: float, second_number: float) -> float:
...    
...    
...    
...    return total
...
...
```
The header contains a *type contract* that not only defines 
the names of the variables but also the types of the variables
passed as arguments and returned by the function. 


### Description

Add a description of what your function does, in words.
Include the list of your examples.

```python
>>> def add_two_numbers(first_number: float, second_number: float) -> float:
...    """ Add two numbers together and return the sum.
...    >>> add_two_numbers(3,4)
...    7
...    >>> add_two_numbers(0,4)
...    4
...    >>> add_two_numbers(-3,3)
...    0
...    """
...    
...    
...    return total
...
...
```

Note the particular format of the examples:
the function call is preceded by the string 
```>>> ``` (with a trailing space)
and the next line contains the output expected.
Although following convention is important 
for the convenience of you users, 
this format allows for automated testing of your function
using the examples you provide. 

### Body

In this case, the body is simple; however, this is often the most work
in designing a function. 
For more complex functions, 
following the previous steps will clarify your understanding 
of the function before you write the body that performs the calculation. 


```python
>>> def add_two_numbers(first_number: float, second_number: float) -> float:
...    """ Add two numbers together and return the sum.
...    >>> add_two_numbers(3,4)
...    7
...    >>> add_two_numbers(0,4)
...    4
...    >>> add_two_numbers(-3,3)
...    0
...    """
...    
...    total = first_number + second_number
...    
...    return total
...
...
```

This may seems like a lot of work to do to prepare to write one line of code.
With more elaborate functions, having clearly stated the 
examples, header and description, 
you should be clear about what it is you will compute and the planning will pay off. 
Think of these steps as you would when you write an outline for an essay:
even very talented writers rarely write a passage from beginning to end.
Instead, most writers start with a plan for what they want to write
before they write it. 


### Test

Finally, test your functions to confirm accuracy. 

```python
>>> add_two_numbers(3,4)
7
>>> add_two_numbers(0,4)
4
>>> add_two_numbers(-3,3)
0

```

If all goes well, these examples should all return
the values you expect.
If not, be sure that your examples are correct
or modify your function definition.
Most of the work in coding is detecting your mistakes
and correcting them.


## Tips

You will get better at writing functions as you gain more experience but the following tips can help you improve more quickly. 
* Start off with a simple case. 
  * Save the corner cases for after your base cases work. 
* Start off with a simple approach.
  * You can adjust the code for faster computation once it is working. 
* Type the comments first.
  * Describe to the first user (you!) how the calculations will be performed. 
  * For lengthier calculations, 
  split the calculation into checkpoints where you can determine the format 
  of intermediate calculations.
  * Type in the code one block at a time. 
  * Assign values to the arguments (but hide them in comments, so as not to interfere) 
  and run blocks of code in the IDE to test one section at a time.
* If you find it is getting too complicated, consider breaking up the calculation 
into separate parts.  
  * Is there a natural checkpoint where you can test with examples? 
  * Should you consider splitting up the function into separate functions?
* Choose examples that provide good testing cases. 
  * Does your function work with negative values? 
  * Does it work with missing values? 
  * Does it work with the wrong data types? 
  * Are there any knife-edge cases when the procedure will change? 
  * Are there any obvious boundaries?
* After making any significant changes to a partially-working function, 
re-run all of your test cases to make sure they are still correct.
  * Did you break any of the test cases that were working before?
  * Did you fix any that were not working? 
  * Keeping score is good motivation.
  * With regular testing, you can make changes with more confidence. 


