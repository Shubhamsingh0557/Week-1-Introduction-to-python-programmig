# Week-1-Introduction-to-python-programmig

--introducing Python-
  * Python is a high-level, general-purpose and very popular programming language.
  * It is being used in web development, machine learning applications etc.
  * Python programs are generally smaller than the other programmig language.
  * Programmers have to type relatively less and the indentation requirement of the language, makes them readable at the time.
  * Python have  very simple syntax and easy to learn.

1. Variables in Python:
    * Variables are used to store data values.
    * Variable is a name that is used to refer to memory location .
    * Python variable is also known as an indentation and used to hold value.
    * In Python, we don’t need to specify the data type explicitly—Python infers it automatically.
    * x = 10        (Integer value)
    * name = "Ram"  (String value)
    * pi = 3.14     (Float value)

- Dynamic Typing: Python allows variables to change type during execution.
- Naming Rules: Variable names must start with a letter or underscore and cannot use reserved keywords.

2. Data Types:
 * Python supports several built-in data types-
   1. int: Stores the integer numbers, Example: x=5
   2. float: Stores the decimal numbers, Example: pi=3.24
   3. str: Stores the text or string, Example: name="Ram"
   4. bool: Stores boolean values either true or false, Example: is_valid=True
   5. list: Stores the ordered,mutable collection, Example: nums=[1,2,3]
   6. tuple: Stores the ordered,immutable collection, Example: t=(1,2)
   7. dict: Stores the key-value pairs, Example: d={"a":1}
   8. set: Stores the unordered, unique elements, Example: s={1,2,3}


3. Operators:
* Operators perform operations on variables and values.

    a. Arithmetic Operators:
      They are used to perform mathematical operations like additional,subtraction,multiplication,division.
  
      +, -, *, /, //, %, **
  
    b. Comparison Operators:
     They are used to compare two operands (values or variables) and determine the relationship between them.
  
        ==, !=, >, <, >=, <=
  
    c. Logical Operators:
      Logical operators in Python are used to combine or modify conditional statements and expressions, enabling more complex decision-making within programs. They work with Boolean values (True or False) and return a Boolean result.
  
        and, or, not
  
    d. Assignment Operators: Assignment operators are used to assign or update the value of a variable. 
      
        =, +=, -=, *=, /=
  
    e. Membership Operators:Membership operators in Python are used to test for the presence of a value within a sequence. 
      
        in, not in
  

🔹 4. Input and Output
➤ Input
Used to take user input from the console.
name = input("Enter your name: ")


➤ Output
Used to display information.
print("Hello,", name)



🔹 5. Conditional Statements (if-else)
Conditional statements control the flow of execution based on conditions.
age = 18
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")


- You can also use elif for multiple conditions.

🔹 6. Loops
Loops are used to execute a block of code repeatedly.
➤ For Loop
for i in range(5):
    print(i)


- Iterates over a sequence (like list, tuple, string, or range).
➤ While Loop
count = 0
while count < 5:
    print(count)
    count += 1


- Continues as long as the condition is True.

✅ Summary
These core concepts are essential for writing Python programs. Mastering them allows you to build logic, handle data, and control program flow effectively. Whether you're automating tasks, analyzing data, or building applications, these fundamentals are your first step into the world of Python programming.

Would you like me to help you format this into a Markdown file or add a sample project structure for GitHub?
