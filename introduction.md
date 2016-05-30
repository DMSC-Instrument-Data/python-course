# Python introduction

## What is Python?

Python is a programming language that is:
 - Interpreted
 - Dynamically typed
 - Multi paradigm (procedural, object oriented, functional)
 - Open source (freely available)
 - Multi platform
 - Very friendly to use!

Lots of libraries for all sorts of tasks are available!

Installation:
 - Linux: Included in all distributions, can be installed through package manager
 - Mac OS X/Windows: Download from https://www.python.org/

## Interacting with the Python prompt, variables, modules

Start the Python prompt:

    Python 3.4.3 (default, Oct 14 2015, 20:28:29)
    [GCC 4.8.4] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Now you can enter expressions that are evaluated immediately when you press return. Enter some arithmetic expressions such as `1+1` or `4*6` to see the result:

    >>> 1+1
    2
    >>> 4*6
    24
    >>> 5/4
    1.25
    >>> 4/2
    2.0

Since Python 3, the result of an integer division is automatically a floating point value. You can see this by checking the type of these expressions:

    >>> type(4), type(2)
    (<class 'int'>, <class 'int'>)
    >>> type(4/2)
    <class 'float'>

The `type`-function is very useful. It tells you what kind of data you are dealing with. `int` and `float` are numeric types, another fundamental data type is `bool` that contains a boolean truth value:

    >>> 4 < 3
    False
    >>> 3 == 3 or 4 == 5
    True
    >>> 2 < 3 and 3 <= 3
    True
    >>> not 5 < 10
    False
    >>> type(2 < 5)
    <class 'bool'>

We're going to get to know other fundamental types later and even create our own types. So far we have used Python just for very simple arithmetic and boolean expressions. Let's try to perform some more advances math, say we would like to know the square root of 4:

    >>> sqrt(4)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'sqrt' is not defined

Oh no, Python does not support square roots! Well, that's not entirely true, so let's look at what happened here. An error like this is called an exception and it is just that - an "exception" from the normal runtime behavior was encountered by the interpreter so it doesn't know any reasonable way to continue program execution. Here the problem is a `NameError`, it tells us that Python does not know anything that is called `sqrt`. The reason is that in Python things are divided into modules. If you think about it, that makes a lot of sense, because it would be crazy if Python knew about absolutely every function anyone has ever defined. It would be a crowded mess and soon nobody would know what to call their functions anymore because all the names are taken. So what we need to do is to get the `sqrt` function from such a module:

    >>> from math import sqrt
    >>>

The `math`-module is part of the so called standard library, so it's installed together with the Python interpreter automatically. This library contains lots of useful modules, all the documentation can be found online https://docs.python.org/3/library/index.html. If you try to import something from a package you have not installed on your computer, Python will complain and throw another exception:

    >>> from problems import all_the_solutions
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ImportError: No module named 'problems'

We will get back to installing additional packages later on, now we have to get back to solving our `sqrt(4)` problem, let's see if it works now:

    >>> sqrt(4)
    2.0
    >>> sqrt(2)
    1.4142135623730951

Now it would be very useful if we could store that value somehow for later use so that we do not need to type it in every time. As many other languages, Python has so called variables for this purpose. It's very easy to use variables:

    >>> a = sqrt(2)
    >>> type(a)
    <class 'float'>

In contrast to many other languages, variables do not need to be declared before a value is assigned to them. Also note that we didn't tell Python anything about the type of data that we wanted to store in `a`. In fact, even now it doesn't matter if we change our mind and want to store something completely different in the variable. Say we suddenly remembered that in fact we did not want to store the floating point representation of the square root of 2 under the name `a` because we can look that up at any time, but instead we would rather store the name of the country we are currently in. Since Python knows nothing about geography and politics, we will just use a so called string to store that information:

    >>> a = 'Sweden'
    >>> type(a)
    <class 'str'>

Before the type stored in `a` was `float`, now it's `str` which is short for string. To see what strings can do, we can use the `help`-function to obtain a bit more information on the class `str`:

    >>> help(type(a))

This will display all methods that are available on an object of type `str`. You can scroll up and down and press q to quit the help and return to the prompt. One method is called `upper`, which returns the string but with all letters in upper case. A method is invoked like this:

    >>> a.upper()
    'SWEDEN'
    >>> a
    'Sweden'

Note that the method does not modify the string. Strings are immutable (they can never change), instead a new string is returned that you could store in another variable (or even the same variable).

A very useful method of `str` that we're going to come across later as well is `format`. As the name suggests, it is used to format data in a certain way. Say we want to explain to people what the value of square root of two is in different countries of the world. We could write out a sentence for each country but that would be a lot of work. Instead, we just specify a string that tells Python how to fill in missing bits:

    >>> sqrt_world = 'In {}, the square root of 2 is {:.3f}.'
    >>> sqrt_world.format(a, sqrt(2))
    In Sweden the square root of 2 is 1.414.
    >>> sqrt_world.format('Denmark', sqrt(2))
    In Denmark the square root of 2 is 1.414.

The `format`-method will take the arguments you give it and fill them into the places in curly brackets. The second one contains some weird characters. These tell Python that it should try to format that bit as a floating point number, but only with three decimals after the dot. If you're super interested in formatting data, take a look at the Python reference: https://docs.python.org/3/library/string.html#formatstrings.

Although the prompt automatically print the return value of the previous expression, scripts quickly become too complex for the prompt and the interpreter does not print anything by default. So to verify that we're in the right place we can print the value of `a` by passing the variable to the `print`-function:

    >>> print(a)
    Sweden

You can also concatenate strings easily using the `+`-operator:

    >>> print(a + ' & Denmark')
    Sweden & Denmark

Now all that was very useful and informative, but we may want to use our script again some time, so instead of re-typing everything into the prompt each time, we will start using files to store the script instead. You can exit the Python prompt by pressing Ctrl+D (or Ctrl+Z on Windows).

## Writing & Executing Python scripts, evaluating arguments

A Python script is nothing more than a plain text file containing 0 or more statements that you would otherwise enter into the prompt. You can use any text editor for creating Python scripts. Many of them have syntax highlighting which helps a lot when writing long and complex scripts. I'm using [PyCharm](https://www.jetbrains.com/pycharm/) for this, it has a lot of features and is too complex to explain here.

Anyway, getting back to important things, we want to produce a script that tells us what the square root of 2 is in Denmark and Sweden respectively. So we produce a file with the following contents:

    from math import sqrt

    a = 'Sweden'
    b = 'Denmark'
    c = sqrt(2)

    sqrt_world = 'In {}, the square root of 2 is {:.3f}.'

    print(sqrt_world.format(a, c))
    print(sqrt_world.format(b, c))
    
Save the file under the name `sqrts_of_southern_scandinavia.py` in a directory of your choice. Open a terminal, navigate to that directory and run the script by typing:

    $> python sqrts_of_southern_scandinavia.py
    In Sweden, the square root of 2 is 1.414.
    In Denmark, the square root of 2 is 1.414.
    
Very satisfying, the square roots seem to be the same in both countries. In fact we might suspect that the value is the same in any country. So let's modify the script to take an argument from the command line instead. There are different ways to do that, but the proper way to use is the [argparse](https://docs.python.org/3/library/argparse.html) module, so why not use it. Create a file called `sqrts_of_the_world.py` and fill it with this:

    from math import sqrt
    import argparse

    # Create a so called parser for the command line arguments.
    # The parser stores the argumeents and generates some useful help for users of the script.
    parser = argparse.ArgumentParser(description='Print the square root of 2 in various countries of the world.')

    # Specify that our script has one argument. We'll store it in a variable called 'country'.
    parser.add_argument('country', help='The country for which to print the square root of 2.')

    # This bit scans the command line arguments and checks if it finds what we specified.
    # If a country was specified, it is stored in arguments.country
    arguments = parser.parse_args()

    # We still have the same variables as before.
    sqrt_world = 'In {}, the square root of 2 is {:.3f}.'
    c = sqrt(2)

    print(sqrt_world.format(arguments.country, c))

This time we do not import a certain function from the argparse module as we do with the math module, instead we import the entire module. To use things that are provided by that module, you need to prefix the thing by the module name and a dot, just as `argparse.ArgumentParser` in the example above. Try the script:

    $> python sqrts_of_the_world.py Sweden
    In Sweden, the square root of 2 is 1.414.
    
    $> python sqrts_of_the_world.py Europe
    In Europe the square root of 2 is 1.414.
    
That seems to work quite well, even more useful than before! You might think writing all this argparse stuff is too much, but using argparse gives us some stuff for free, for example some error handling in case somebody tries to run our script without arguments at all or too many arguments:

    $> python sqrts_of_the_world.py
    usage: sqrts_of_the_world.py [-h] country
    sqrts_of_the_world.py: error: too few arguments
    
    $> python sqrts_of_the_world.py Denmark Sweden
    usage: sqrts_of_the_world.py [-h] country
    sqrts_of_the_world.py: error: unrecognized arguments: Sweden
    
Even better, it generates help so that users can learn about the purpose and options of our great program:

    $> python sqrts_of_the_world.py -h
    usage: sqrts_of_the_world.py [-h] country

    Print the square root of 2 in various countries of the world.

    positional arguments:
      country     The country for which to print the square root of 2.

    optional arguments:
      -h, --help  show this help message and exit

Wow, that is indeed useful! Now people can use our script without opening it and inspecting the code beforehand. The argparse module is really a great way of making scripts easier to use for others. But even with all the great command line help and so on, the functionality of the program is still pretty limited. In the next section we're going to change that and add some more complex behavior.

## Flow control, lists, maps and functions

An obvious thing we might want to do is checking whether the user has supplied a certain country where special rules regarding square roots apply. Imagine Sweden introduces a law that mandates all square roots of even numbers to be 0. In order to not get in trouble with the authorities, we should change our program to take this into account.

Save the previously edited file under a new name, `even_sqrts_have_exceptions.py` and make the following changes:

    # We still have the same variables as before.
    sqrt_world = 'In {}, the square root of 2 is {:.3f}.'
    c = sqrt(2)
    
    if arguments.country == 'Sweden':
        c = 0.0

    print(sqrt_world.format(arguments.country, c))
    
In Python, indentation is a syntax element. The code that is indented after the `if`-statement is indented, it the block that is executed when the condition specified in the `if`-statement is true. Test the script:

    $> python even_sqrts_have_exceptions.py Sweden
    In Sweden, the square root of 2 is 0.000.
    
    $> python even_sqrts_have_exceptions.py Denmark
    In Denmark, the square root of 2 is 1.414.
    
That seems to work as expected and our script complies with the new and updated regulations, good. Shortly after, Denmark passes a very similar law, but here the square root of even numbers should be 1. Again, changes are required, save the last script as `sqrts_with_more_exceptions.py` and make the following modification:

    # We still have the same variables as before.
    sqrt_world = 'In {}, the square root of 2 is {:.3f}.'
    c = sqrt(2)
    
    if arguments.country == 'Sweden':
        c = 0.0
    elif arguments.country == 'Denmark':
        c = 1.0

    print(sqrt_world.format(arguments.country, c))

The `elif`-block is executed if the `if`-statement was false, but the `elif`-statement is true. You could add a million `elif`-statements to cover all the different countries in the world, but that's usually not a good idea so we're not going to do that. A quick test to see if we are still compliant with all the laws in the different countries:

    $> python sqrts_with_more_exceptions.py Sweden
    In Sweden, the square root of 2 is 0.000.
    
    $> python sqrts_with_more_exceptions.py Denmark
    In Denmark, the square root of 2 is 1.000.
    
There is also an `else` statement that is executed when the `if` and all `elif`-statements were false, so the code could be changed to:

    # We still have the same variables as before.
    sqrt_world = 'In {}, the square root of 2 is {:.3f}.'
    
    if arguments.country == 'Sweden':
        c = 0.0
    elif arguments.country == 'Denmark':
        c = 1.0
    else:
        c = sqrt(2)

    print(sqrt_world.format(arguments.country, c))
    
The differing legislation is recognized as a problem by the nordic countries, so they have extensive meetings and agree on fixing the square root of even numbers to 2. Well, that could make our life much easier, now we only need to check if the user entered a nordic country. But as pointed out before, Python does not have an in-built understanding of geography and politics, so we need to spell it out. It could be done by coming up with some long and complex `if...elif...else`-monster, but nobody wants to read that kind of code, so instead we're going to make use of a very nice data type in Python, the list! Open a terminal with a Python prompt. Let's define a list of some nordic countries:

    >>> nordics = ['Sweden', 'Denmark', 'Norway', 'Finland']
    >>> nordics
    ['Sweden', 'Denmark', 'Norway', 'Finland']

Lists are very flexible. For example, we forgot Iceland, but they were part of the square root treaty, so they need to be in the list:

    >>> nordics.append('Iceland')
    >>> nordics
    ['Sweden', 'Denmark', 'Norway', 'Finland', 'Iceland']
    
You can also check how many elements there are in a list:

    >>> len(nordics)
    5

As you can see calling the `append`-method modified the list. Lists are mutable in Python. We could sort the list alphabetically do clean it up a bit. The `sorted`-function does that for us, but it returns a new list instead of modifying the old one. No problem:

    >>> nordics = sorted(nordics)
    >>> nordics
    ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    
Should anyone ever ask you what the third nordic country is, if sorted alphabetically, you could answer that question easily using the list we made and indices. An index i gives you the i-th element of the list, but Python starts counting at 0, so to get the third country you need to write:

    >>> nordics[2]
    'Iceland'
    
You could also think about the problem backwards and access the list from the end. So the third element in a list of 5 would be the third from the back as well. You can do that by specifying a negative index, which starts at -1 for the last item:

    >>> nordics[-3]
    'Iceland'
    
Python also supports so called slicing, which lets you cut out parts of a list. If you wanted to get all nordic countries except the first and the last in the list, that would be very easy to express, the same for all countries but the first or all but the last:

    >>> nordics[1:4]
    ['Finland', 'Iceland', 'Norway']
    
    >>> nordics[1:]
    ['Finland', 'Iceland', 'Norway', 'Sweden']
    
    >>> nordics[:4]
    ['Denmark', 'Finland', 'Iceland', 'Norway']

You can also check if an element is a member of the list by using the `in` keyword:

    >>> 'Denmark' in nordics
    True
    
    >>> 'Australia' in nordics
    False
    
This all we need to know about lists for now, in fact the `in` keyword is exactly what we need! Let's put that in the program, this time we call the file `sqrts_of_the_nordics.py` and modify the relevant part like so:

    # We still have the same variables as before.
    sqrt_world = 'In {}, the square root of 2 is {:.3f}.'

    nordics = ['Sweden', 'Denmark', 'Norway', 'Finland', 'Iceland']

    if arguments.country in nordics:
        c = 2.0
    else:
        c = sqrt(2)

    print(sqrt_world.format(arguments.country, c))

Much better, now we just need to update the list in case other countries become nordic or the nordic countries change their rules. A quick check if it's still working:

    $> python sqrts_of_the_nordics.py Denmark
    In Denmark, the square root of 2 is 2.000.
    
    $> python sqrts_of_the_nordics.py Sweden
    In Sweden, the square root of 2 is 2.000.
    
    $> python sqrts_of_the_nordics.py Australia
    In Australia, the square root of 2 is 1.414.
    
As our program is getting better and better it becomes harder to improve. One thing that might be nice though would be the option of entering more than one country, after all this is very useful data about different countries and we might save the users some typing. We will create a new version of our program, let's call it `many_sqrts.py` the following content:

    from math import sqrt
    import argparse

    parser = argparse.ArgumentParser(description='Print the square root of 2 in various countries of the world.')

    # Specify that our script has N arguments. We'll store them in a list called 'countries'.
    # The metavar option is used for generating the help.
    parser.add_argument('countries', nargs='+',
                        metavar='country', help='The countries for which to print the square root of 2.')

    arguments = parser.parse_args()

    sqrt_world = 'In {}, the square root of 2 is {:.3f}.'
    nordics = ['Sweden', 'Denmark', 'Norway', 'Finland', 'Iceland']

    for country in arguments.countries:
        if country in nordics:
            c = 2.0
        else:
            c = sqrt(2)

        print(sqrt_world.format(country, c))
        
Now there is a new control structure, called `for`. This is the main way of looping over things in Python. In the example, the loop goes through all elements of the list `arguments.countries` and makes the element available under the name `country` in the indented block. The block is executed once for each element of the list, so each country that is supplied to the script is checked whether it's nordic or not and the proper value is printed out:

    $> python many_sqrts_at_once.py Denmark Sweden Australia
    In Denmark, the square root of 2 is 2.000.
    In Sweden, the square root of 2 is 2.000.
    In Australia, the square root of 2 is 1.414.

After more discussions, the nordic countries agree that having a constant value for square roots of even numbers can get confusing because they are the same and also math exams become too easy. Indeed wouldn't it be much better to define the square root of an even number `x` as `2*x - 0.5`? We could modify our program in the appropriate place, but somehow we have the feeling that this definition might not be the last, so we should probably define our own function that behaves exactly like that so we only need to change that later on.

Defining functions in Python is very simple. In general a function consists of a name, a list of arguments and a body, which may or may not return a value. In this case we want to use our function in the sense of `y = f(x)`, so it should return a value. For functions, good naming is very important, so that it is immediately clear what the function does. Let's add this definition to the file (saved as `many_sqrts_function.py`), just after the import statements:

    def nordic_sqrt(x):
        return 2*x - 0.5
        
Then we can use the function later on in our `for`-loop:

    for country in arguments.countries:
        if country in nordics:
            c = nordic_sqrt(2)
        else:
            c = sqrt(2)

        print(sqrt_world.format(country, c))
        
Running our script again for Denmark, Sweden and Australia produces the result we expect:

    $> python many_sqrts_function.py Denmark Sweden Australia
    In Denmark, the square root of 2 is 3.500.
    In Sweden, the square root of 2 is 3.500.
    In Australia, the square root of 2 is 1.414.
    
Just as we thought our script was completely up to the challenges of modern day math regulations, the baltic countries adopt the nordic model, but of course in a slightly different way, namely `x/2 + 0.5`. Fair enough, we simply add a new function just as before:

    def baltic_sqrt(x):
        return x/2 + 0.5
        
We can also define a list of the baltic countries and modify the `for`-loop:

    baltics = ['Estonia', 'Latvia', 'Lithuania']
    
    for country in arguments.countries:
        if country in nordics:
            c = nordic_sqrt(2)
        elif country in baltics:
            c = baltic_sqrt(2)
        else:
            c = sqrt(2)

        print(sqrt_world.format(country, c))
        
This does the job, but now we somehow ended up in the same `if...elif...else`-mess as before. If we think more about the problem, what we need is a map which contains the right function for each country. In Python this is called a `dict` and is a collection of key-value-pairs. Creating an empty `dict` in a Python prompt is very easy:

    >>> a = {}
    >>> a
    {}
    
As many things, not very exciting. If we want a dictionary with some keys and values, that's also straightforward:

    >>> a = {'Denmark': 2, 'Sweden': 2, 'Estonia': 3}
    >>> a
    {'Sweden': 2, 'Denmark': 2, 'Estonia': 3}
    
Note that the order is not the same that we supplied. Dictionaries maintain their own order of the keys. Accessing elements is similar to lists, just that you have to specify a key that is in the dict:

    >>> a['Denmark']
    >>> 2
    
Adding elements is done exactly the same way as accessing existing ones:

    >>> a['Norway'] = 10
    >>> a
    {'Sweden': 2, 'Denmark': 2, 'Norway': 10, 'Estonia': 3}

You can construct the same dictionary from a list of so called `tuples`. A tuple is defined like this:

    >>> a = ('Sweden', 2)
    >>> a
    ('Sweden', 2)
    
Tuples are similar to lists, but they are immutable, so you can not change them. Making a dict from a list of tuples is done like this:

    >>> a = dict([('Sweden', 2), ('Denmark', 2)])
    >>> a
    {'Sweden': 2, 'Denmark': 2}
    
While this is much more typing than directly defining the dict, there is a very helpful function that can generate a list of tuples from two lists for us, it's called `zip`, because it "zips" the elements of two (or more) lists together like zipper:

    >>> a = ['Sweden', 'Denmark']
    >>> b = [2, 5]
    >>> c = dict(zip(a, b))
    {'Sweden': 2, 'Denmark': 5}
    
Very useful indeed! What's also useful to know is that some objects can't be used as keys in a `dict`, but common types are `str` or `int`. As a value you can store any object you want and, this is a very, very, very important concept, in Python everything is an object. Even the functions we wrote earlier are objects. Yes, that's right. That means we can also store them somewhere to call them later! How useful for our regulation-heavy square root script. This time we create and fill a map which contains a function for each country:

    sqrt_map = {}

    nordics = ['Sweden', 'Denmark', 'Norway', 'Finland', 'Iceland']

    for country in nordics:
        sqrt_map[country] = nordic_sqrt
        
    baltics = ['Estonia', 'Latvia', 'Lithuania']

    for country in baltics:
        sqrt_map[country] = baltic_sqrt

    for country in arguments.countries:
        sqrt_function = sqrt_map.get(country, sqrt)

        print(sqrt_world.format(country, sqrt_function(2)))

Instead of accessing the function in the last loop as `sqrt_map[country]`, which would produce an error if the country is not in the map, we use the `get`-method of the dictionary which returns a default if the key is not in the map. The function (which, remember, is an object) is stored in the `sqrt_function` variable and called later on. Now we got rid of the `if`-block entirely. Still, we have two very similar `for`-loops to build the country dict, it would be nicer to put them into another function. The function should return a dictionary that contains the same value for each element of a list passed to it, like this:

    def get_country_sqrt_map(countries, sqrt_function):
        return {country: sqrt_function for country in countries}
        
This is yet another way of creating a dictionary called "dict comprehension". The `for country in countries`-expression is similar to the `for`-loops we've written before, but in this context `country` is used as a key to the new dict that is being created. Now with this we can make the script a bit nicer again and store it in a file called `many_sqrts_map.py`:

    from math import sqrt
    import argparse

    def nordic_sqrt(x):
        return 2*x - 0.5

    def baltic_sqrt(x):
        return x/2 + 0.5

    def get_country_sqrt_map(countries, sqrt_function):
        return {country: sqrt_function for country in countries}

    parser = argparse.ArgumentParser(description='Print the square root of 2 in various countries of the world.')

    # Specify that our script has N arguments. We'll store them in a list called 'countries'.
    parser.add_argument('countries', nargs='+',
                        metavar='country', help='The countries for which to print the square root of 2.')

    arguments = parser.parse_args()

    sqrt_world = 'In {}, the square root of 2 is {:.3f}.'

    nordics = ['Sweden', 'Denmark', 'Norway', 'Finland', 'Iceland']
    baltics = ['Estonia', 'Latvia', 'Lithuania']

    sqrt_map = {}
    sqrt_map.update(get_country_sqrt_map(nordics, nordic_sqrt))
    sqrt_map.update(get_country_sqrt_map(baltics, baltic_sqrt))

    for country in arguments.countries:
        sqrt_function = sqrt_map.get(country, sqrt)

        print(sqrt_world.format(country, sqrt_function(2)))

Here we use another method of the dictionary, called `update` which essentially puts all key value pairs of the dict in the argument into the base dictionary. At this stage we cover three different cases of square root calculation:

    $> python many_sqrts_maps.py Denmark Sweden Estonia Australia
    In Denmark, the square root of 2 is 3.500.
    In Sweden, the square root of 2 is 3.500.
    In Estonia, the square root of 2 is 1.500.
    In Australia, the square root of 2 is 1.414
    
As an excersize, make the script correct so that accepts country names case insensitive. The output should be correctly written with a capital letter first. Refer to the documentation of [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) and go through the methods.

## Reading and writing files

In the last sections we have looked at some basic data types and principles of the Python language. Since we ultimately want to use Python for processing scientific data, we will now write a more useful script that reads some data, transforms it and writes a modified file. Furthermore, we will calculate and output some statistics about the data.

The file we want to load is called `poldi_2013_si.dat` and contains a correlation spectrum calculated from a powder diffraction measurement at the POLDI beamline at SINQ. Later on we will also plot the data, but for now we just want to look at it. Open the file in your text editor. It's CSV-data with a header that has a `#`-character to indicate a comment:

    #X , Y0 , E0
    1.54973 163.685 0
    1.54996 136.049 0
    1.55019 235.999 0
    1.55043 106.544 0
    1.55066 34.1962 0
    1.55089 126.983 0
    
The file contains three columns (x, y and error). X is Q in reciprocal Angström, Y is correlation counts. Our script should read the file, ignore the comment line and produce three lists of floating point numbers containing the respective data. You've probably noticed that the error-column is zero, so we want to calculate error estimates. The new data we're writing out into a different file are x, y (unmodified) and the calculated errors. The output file should have the same number of significant places.

Let's start by setting up the argument parser to deal with the input and output requirements. Put the script into a file called `data_convert_unmodified.py`:

    import argparse

    parser = argparse.ArgumentParser(description='Read a file with 3 space separated columns, calculate an error estimate from the second column and write the modified file.')
    
    parser.add_argument('input', help='Name of the input file.')
    parser.add_argument('output', help='Name of the output file.')
    
    arguments = parser.parse_args()
    
Test that the script does the right thing (run it with the `-h`-flag, try specifying only one argument or three arguments). As a first step we will read the file into x-, y-, and error lists and write those out unmodified into the new file. For reading a file, the file has to be opened using the `open`-function. It accepts the file name and a so called mode as arguments. The most commonly used modes are `r` for "read-only", `w` for "write-only" or `r+` for reading and writing.

    x_data = []
    y_data = []
    e_data = []

    infile = open(arguments.input, 'r')

    # Go through the file line by line
    for line in infile:
        # Remove whitespace characters at the beginning and end
        stripped_line = line.strip()
        
        # If it's not a comment and not an empty line, try to convert it to three floats.
        if not stripped_line.startswith('#') and not len(stripped_line) == 0:
            x, y, e = [float(x) for x in line.split(' ')]
            
            x_data.append(x)
            y_data.append(y)
            e_data.append(e)
        
    infile.close()

    # This is the format we want to use for the output
    lineformat = '{:.6g} {:.6g} {:.6g}\n'

    # Open the output file, overwrite existing file
    outfile = open(arguments.output, 'w')

    # Use zip to iterate over the three arrays simultaneously.
    for x, y, e in zip(x_data, y_data, e_data):
        outfile.write(lineformat.format(x, y, e))
        
    outfile.close()
                        
The behavior of the open file is similar to a list that can be iterated over line by line. Try the script and check that it works correctly. Now we can look at the second requirement and calculate the error estimates from y. Maybe you noticed that there are negative y-values, which would pose a problem for the square root function. So instead of calculating the error from y, we calculate it from the absolute value of y. We can use the `abs`-function which is available by default, so we just need to add `from math import sqrt` at the top of the script (save it as `data_convert_sqrt_errors.py`) and calculate the error:

    infile.close()
    
    # A list comprehension to calculate the error from y_data
    e_data = [sqrt(abs(y)) for y in y_data]

    # This is the format we want to use for the output
    lineformat = '{:.6g} {:.6g} {:.6g}\n'

The rest of the script stays exactly the same. Run the script and check that the calculated errors are reasonable at a few points. So far the script is very silent, we want to offer the user an option to calculate and print some statistics:

- Number of data points
- x-range
- Minimum and maximum value for y
- Mean and median for y
- Mean I/sigma

First, let's save the file script as a new file called `data_convert_statistics.py` so we can work on the statistics part. We'll modify the argument parser a bit to add an optional flag to the script that outputs the statistics. Probably we should also make writing the file optional in case we just need some statistics. While we're at it, we can also make calculating the errors optional:

    parser.add_argument('input', help='Name of the input file.')
    parser.add_argument('output', nargs='?', default=None,
                        help='Name of the output file.')
    parser.add_argument('-s', '--square-root-errors', action='store_true', default=False,
                        help='Calculate errors as sqrt(|y|), otherwise leave errors unmodified.')               
    parser.add_argument('-p', '--print-statistics', action='store_true', default=False,
                        help='Calculate and print some statistics from the data.')

    arguments = parser.parse_args()
    
With these modified options, calculation of errors is optional, so is storing the data in a new file. We need to modify the logic a bit so that the options are processed correctly:

    if arguments.square_root_errors:
        e_data = [sqrt(abs(y)) for y in y_data]

    if arguments.output is not None:
        lineformat = '{:.6g} {:.6g} {:.6g}\n'

        outfile = open(arguments.output, 'w')

        for x, y, e in zip(x_data, y_data, e_data):
            outfile.write(lineformat.format(x, y, e))
            
        outfile.close()

Lastly, we need to add the statistics computations and print them if the option has been specified:

    if arguments.print_statistics:
        print('Statistics for file {}:'.format(arguments.input))
        
        number_of_points = len(x_data)
        print('Number of data points: {}'.format(number_of_points))
        
        print('x-range: {:.6g} - {:.6g}'.format(min(x_data), max(x_data)))
        print('y-range: {:.6g} - {:.6g}'.format(min(y_data), max(y_data)))
        
        mean_y = sum(y_data) / number_of_points    
        print('Mean y: {:.6g}'.format(mean_y))
        
        median_y = sorted(y_data)[int(number_of_points/2)]
        print('Median y: {:.6g}'.format(median_y))
        
        # If there is a 0.0 in the errors, don't perform the calculation and print Inf instead.
        if not 0.0 in e_data:
            mean_i_over_sigma = sum([abs(y) / e for y, e in zip(y_data, e_data)]) / number_of_points
            print('Mean I/sigma: {:.6g}'.format(mean_i_over_sigma))
        else:
            print('Mean I/sigma: Inf')

            
Now the script can be used in quite a few different ways. For example to calculate the statistics from the input file with errors calculated as `sqrt(|y|)`:

    $> python data_convert_statistics.py -p -s poldi_2013_si.dat
    Statistics for file poldi_2013_si.dat:
    Number of data points: 5531
    x-range: 1.54973 - 8.95682
    y-range: -283.502 - 3263.52
    Mean y: 138.63
    Median y: 126.048
    Mean I/sigma: 11.2182
    
Or to silently calculate those errors and write the data to a different file:
    
    $> python data_convert_statistics.py -s poldi_2013_si.dat poldi_2013_si_errors.dat
    $>
    
Now that we have a data file with error estimates, we can proceed to the next section, where we'll look into plotting the data.

## Numpy, scipy, matplotlib

So far we've used plain Python and the standard library, but there are some modules that make our lives much easier. Scipy is part of a stack of libraries that play together very well. Possibly the most important one is [numpy](http://www.numpy.org/). It introduces arrays to hold data (similar to what some of the mathematics packages offer) and defines lots of functions for numerical computations.

Let's see whether we can load the data we produced with our conversion script in a Python prompt.

    >>> import numpy as np
    >>> x, y, e = numpy.loadtxt('poldi_2013_si_errors.dat', unpack=True)
    >>> x
    array([ 1.54973,  1.54996,  1.55019, ...,  8.94137,  8.94909,  8.95682])
    
That is a lot easier than looping through the file, checking for comments and empty lines. Now we don't have a list though, but a numpy-array. It still behaves like a list in many aspects, at least when it's a 1D-array like in this case. We can for example still get slices out of it and access single elements:

    >>> x[2:10]
    array([ 1.55019,  1.55043,  1.55066,  1.55089,  1.55112,  1.55135,
            1.55159,  1.55182])
    >>> x[-1]
    8.9568200000000004

Maybe before going to the plotting we should take another look at our last script and make some modifications to use numpy functions were possible. Save the file as `data_convert_numpy.py` and make the following modifications:

    import argparse
    import numpy as np
    
    # The parser definition does not change ...

    # The unpack argument extracts the three columns into separate arrays like we had before
    x_data, y_data, e_data = np.loadtxt(arguments.input, unpack=True)

    if arguments.square_root_errors:
        e_data = np.sqrt(np.abs(y_data))

    if arguments.output is not None:
        # For saving we need to create an array 
        np.savetxt(arguments.output, np.array([x_data, y_data, e_data]).T, fmt='%.6g')

    if arguments.print_statistics:
        print('Statistics for file {}:'.format(arguments.input))
        
        number_of_points = len(x_data)
        print('Number of data points: {}'.format(number_of_points))
        
        print('x-range: {:.6g} - {:.6g}'.format(min(x_data), max(x_data)))
        print('y-range: {:.6g} - {:.6g}'.format(min(y_data), max(y_data)))
        
        mean_y = np.mean(y_data)
        print('Mean y: {:.6g}'.format(mean_y))
        
        median_y = np.median(y_data)
        print('Median y: {:.6g}'.format(median_y))
        
        if not 0.0 in e_data:
            mean_i_over_sigma = np.mean(np.abs(y_data) / e_data)
            print('Mean I/sigma: {:.6g}'.format(mean_i_over_sigma))
        else:
            print('Mean I/sigma: Inf')

That shortens it quite a bit. One nice thing about numpy arrays is that you can do arithmetic operations with them with no effort. For example the error calculation - the numpy sqrt- and abs-functions know that they can iterate over the argument they get and perform the operation on all elements of the sequence, yielding a new sequence. How convenient! Or the mean I/sigma calculation, where the element wise division is simply done by writing the `/`-operator. Also, numpy already implements mean, median and so on, so this does not need to be re-implemented manually again.

But anyway, we wanted to write a small script to plot the data, so let's get back to that. A very popular package for plotting in Python is [matplotlib](http://matplotlib.org/users/pyplot_tutorial.html). We'll setup a small script first to load and plot the data, called `plot_diffractogram.py`:

    import argparse
    import numpy as np
    import matplotlib.pyplot as plt

    parser = argparse.ArgumentParser(description='Plot the supplied file.')
    
    parser.add_argument('input', help='Name of the input file.')
    
    arguments = parser.parse_args()
    
    x,y,e = np.loadtxt(arguments.input, unpack=True)
    
    plt.errorbars(x,y,e)
    plt.show()
    
That should produce a diffractogram with some very nice and sharp Bragg-peaks and some background noise. You can try and zoom in a bit on the different peaks. As the file name indicates, this data produced from a silicon measurement. Silicon has a cubic crystal structure and thus one lattice parameter `a=5.43119`. We could use that information to improve our script to make it plot a small region in Q with the Bragg peak at the center by giving the script the lattice parameter and an index HKL to specify which reflection to plot.

To calculate Q from HKL and lattice parameters, we use the following equation:

    Q = 2*pi*sqrt(h'.G*.h)
    
Here, G* is a 3x3-matrix describing the reciprocal lattice of the crystal and for cubic cases it's very easy to construct from the lattice parameter a. h' denotes hkl as a row-vector and the . is the dot-product. Expressed as a function that's:

    def get_q(hkl, g_star):
        return 2 * np.pi * np.sqrt(hkl.T.dot(g_star.dot(h)))
        
Numpy has a lot to offer with respect to linear algebra. There's a sub-module called `linalg` which has most things you would expect such as matrix inversion and so on. To calculate G* for the cubic case we write a function like this:

    def get_g_star(a):
        return np.eye(3) * 1/a**2
        
Then we add two options to the new script (`plot_hkl_cubic.py`) to let the user specify HKL and a:

    parser.add_argument('-a', help='Lattice parameter of a cubic crystal structure in Angström.', type=float)
    parser.add_argument('-m', help='Miller indices HKL given in the format h,k,l.')
    
The plotting part now looks like this:

    plt.errorbar(x,y,e,fmt='.')
    plt.xlabel('Q')
    plt.ylabel('I')

    if arguments.a is not None and arguments.b is not None:
        hkl = np.array([float(x) for x in arguments.b.split(',')])
        
        g_star = get_g_star(arguments.a)
        q = get_q(hkl, g_star)
        
        xlimits = (q-0.05, q+0.05)
        
        plt.title('HKL = ' + arguments.b)
        plt.xlim(xlimits)

    plt.show()
    
Now we can invoke the script to plot the 220-reflection:

    $> python plot_hkl_cubic.py -a 5.43119 -b 2,2,0 poldi_2013_si_errors.dat
    
The matplotlib libraries has tons of options and different plot types, too much to cover in this introduction. One convenient feature we may want to add to the script is the possibility to save the plot to a file instead of showing a window.

We'll add a second positional argument that, if specified, let's the script write the plot to a file instead:

    parser.add_argument('output', nargs='?', default=None,
                        help='If supplied, write plot to this file instead of displaying')
    
Saving the figure is then very easy:

    if arguments.output is not None:
        plt.savefig(arguments.output)
    else:
        plt.show()
