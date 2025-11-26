import os
import re
from textwrap import dedent

BASE_DIR = "java_practice_problems"


def slugify(title: str) -> str:
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9]+", "_", slug)
    slug = re.sub(r"_+", "_", slug).strip("_")
    return slug or "problem"


def make_comment_block(problem_number, title, description, sample_input, sample_output):
    return dedent(
        f"""\
        /*
        Problem {problem_number}: {title}

        Description:
        {description.strip()}

        Sample Input:
        {sample_input.strip()}

        Sample Output:
        {sample_output.strip()}
        */
        """
    )


# ============ DEFINE PROBLEMS ============

java_basics_problems = [
    # 1–10: Syntax, variables, conditionals, loops
    {
        "number": 1,
        "title": "Hello World and CLI Arguments",
        "description": "Write a program that prints 'Hello, <name>!' where <name> is passed as a command-line argument. If no argument is passed, print 'Hello, World!'.",
        "sample_input": "No arguments\nor\nargs: Alice",
        "sample_output": "Hello, World!\nor\nHello, Alice!",
        "is_folder": False,
    },
    {
        "number": 2,
        "title": "Simple Calculator with Primitive Types",
        "description": "Read two integers and a character representing an operator (+, -, *, /) from standard input and print the result. Handle division as integer division.",
        "sample_input": "10\n3\n+\n",
        "sample_output": "13",
        "is_folder": False,
    },
    {
        "number": 3,
        "title": "Even or Odd",
        "description": "Read an integer and print whether it is EVEN or ODD.",
        "sample_input": "7",
        "sample_output": "ODD",
        "is_folder": False,
    },
    {
        "number": 4,
        "title": "Maximum of Three Numbers",
        "description": "Read three integers and print the maximum using nested if-else statements (do not use Math.max).",
        "sample_input": "3 9 5",
        "sample_output": "9",
        "is_folder": False,
    },
    {
        "number": 5,
        "title": "Grading System with Else-If Ladder",
        "description": "Read a score between 0 and 100 and print the grade (A, B, C, D, F) using else-if ladder. Include input validation for out-of-range scores.",
        "sample_input": "85",
        "sample_output": "B",
        "is_folder": False,
    },
    {
        "number": 6,
        "title": "Sum of First N Natural Numbers",
        "description": "Read an integer N and print the sum of the first N natural numbers using a for loop.",
        "sample_input": "5",
        "sample_output": "15",
        "is_folder": False,
    },
    {
        "number": 7,
        "title": "Factorial Using While Loop",
        "description": "Compute the factorial of a non-negative integer N using a while loop. For N=0, factorial is 1.",
        "sample_input": "4",
        "sample_output": "24",
        "is_folder": False,
    },
    {
        "number": 8,
        "title": "Multiplication Table",
        "description": "Read an integer N and print its multiplication table from 1 to 10 using a loop.",
        "sample_input": "3",
        "sample_output": "3 x 1 = 3\n...\n3 x 10 = 30",
        "is_folder": False,
    },
    {
        "number": 9,
        "title": "Reverse the Digits of an Integer",
        "description": "Read an integer and print its digits in reverse order. Preserve the sign for negative numbers.",
        "sample_input": "-123",
        "sample_output": "-321",
        "is_folder": False,
    },
    {
        "number": 10,
        "title": "Check Prime Number",
        "description": "Read an integer N and print whether it is PRIME or NOT PRIME. Use a basic loop-based primality test.",
        "sample_input": "11",
        "sample_output": "PRIME",
        "is_folder": False,
    },

    # 11–20: Arrays, methods, overloading, strings
    {
        "number": 11,
        "title": "Find Minimum in an Array",
        "description": "Read N followed by N integers and print the minimum element in the array.",
        "sample_input": "5\n4 2 9 1 7",
        "sample_output": "1",
        "is_folder": False,
    },
    {
        "number": 12,
        "title": "Linear Search in an Array",
        "description": "Read N, then N integers, then a target value. Print the index of the first occurrence of the target or -1 if not found.",
        "sample_input": "5\n1 4 2 4 5\n4",
        "sample_output": "1",
        "is_folder": False,
    },
    {
        "number": 13,
        "title": "Array Reversal In-Place",
        "description": "Read N and an array of N integers and reverse the array in-place. Print the reversed array.",
        "sample_input": "4\n1 2 3 4",
        "sample_output": "4 3 2 1",
        "is_folder": False,
    },
    {
        "number": 14,
        "title": "Method Overloading for Area Calculation",
        "description": "Create overloaded methods named area() to calculate area of a circle (radius), rectangle (length and breadth), and square (side). Use them in main.",
        "sample_input": "Circle radius: 2.0\nRectangle: 3.0 4.0\nSquare: 5.0",
        "sample_output": "Area of circle: 12.56\nArea of rectangle: 12.0\nArea of square: 25.0",
        "is_folder": False,
    },
    {
        "number": 15,
        "title": "Pass-by-Value Demonstration",
        "description": "Demonstrate Java's pass-by-value behavior by writing a method that tries to swap two integers and show that original variables in main are unchanged.",
        "sample_input": "a = 5, b = 10",
        "sample_output": "Before swap: a=5, b=10\nInside method: a=10, b=5\nAfter method: a=5, b=10",
        "is_folder": False,
    },
    {
        "number": 16,
        "title": "String Palindrome Check",
        "description": "Read a string and check if it is a palindrome, ignoring case and spaces.",
        "sample_input": "Never odd or even",
        "sample_output": "PALINDROME",
        "is_folder": False,
    },
    {
        "number": 17,
        "title": "Count Vowels and Consonants",
        "description": "Given a line of text, count the number of vowels and consonants (letters only). Ignore case and non-letter characters.",
        "sample_input": "Hello, World!",
        "sample_output": "Vowels: 3\nConsonants: 7",
        "is_folder": False,
    },
    {
        "number": 18,
        "title": "String Tokenizer for Words",
        "description": "Read a sentence and split it into words based on spaces and punctuation. Print each word on a new line.",
        "sample_input": "Java, Spring Boot & LLMs!",
        "sample_output": "Java\nSpring\nBoot\nLLMs",
        "is_folder": False,
    },
    {
        "number": 19,
        "title": "2D Array Matrix Addition",
        "description": "Read dimensions of two matrices and their elements, then print the element-wise sum matrix.",
        "sample_input": "2 2\n1 2\n3 4\n5 6\n7 8",
        "sample_output": "6 8\n10 12",
        "is_folder": False,
    },
    {
        "number": 20,
        "title": "Transpose of a Matrix",
        "description": "Read a matrix and print its transpose. Use a 2D array.",
        "sample_input": "2 3\n1 2 3\n4 5 6",
        "sample_output": "1 4\n2 5\n3 6",
        "is_folder": False,
    },

    # 21–30: OOP basics: classes, objects, constructors, static, encapsulation
    {
        "number": 21,
        "title": "Simple Bank Account Class",
        "description": "Create a BankAccount class with fields for accountNumber and balance, and methods deposit and withdraw with basic validation (no negative balance). Demonstrate usage in main.",
        "sample_input": "Initial balance: 1000\nDeposit: 500\nWithdraw: 2000",
        "sample_output": "Deposit successful. Balance: 1500\nWithdrawal failed. Insufficient funds. Balance: 1500",
        "is_folder": False,
    },
    {
        "number": 22,
        "title": "Constructor Overloading",
        "description": "Create a Student class with overloaded constructors: no-arg, id-only, id-and-name. Print properties of different students in main.",
        "sample_input": "N/A (hard-code objects in main)",
        "sample_output": "Student{id=0, name='Unknown'}\nStudent{id=1, name='Unknown'}\nStudent{id=2, name='Alice'}",
        "is_folder": False,
    },
    {
        "number": 23,
        "title": "Static vs Instance Members",
        "description": "Create a class with a static counter to track how many objects have been created. Print the counter after creating multiple instances.",
        "sample_input": "Create 3 objects",
        "sample_output": "Instances created: 3",
        "is_folder": False,
    },
    {
        "number": 24,
        "title": "Encapsulation with Getters and Setters",
        "description": "Create a Product class with private fields name, price, quantity and public getters/setters with basic validation (e.g., no negative price).",
        "sample_input": "Set price: -10",
        "sample_output": "Invalid price. Keeping old value.",
        "is_folder": False,
    },
    {
        "number": 25,
        "title": "Immutable Class Example",
        "description": "Design a simple immutable class (e.g., ImmutablePoint) with final fields, no setters, and only getters and constructors. Demonstrate that values cannot be changed after creation.",
        "sample_input": "Create point (2,3)",
        "sample_output": "Point: (2,3)\nNo way to modify x or y after creation.",
        "is_folder": False,
    },
    {
        "number": 26,
        "title": "This Keyword for Constructor Chaining",
        "description": "Use this() to chain constructors in a class and avoid code duplication. Demonstrate the chaining sequence via print statements.",
        "sample_input": "Create object with 1-arg constructor",
        "sample_output": "Inside no-arg constructor\nInside 1-arg constructor",
        "is_folder": False,
    },
    {
        "number": 27,
        "title": "Basic Enum Usage",
        "description": "Define an enum for OrderStatus (NEW, PROCESSING, SHIPPED, DELIVERED, CANCELLED). Write a program that reads a status string and prints a friendly message.",
        "sample_input": "SHIPPED",
        "sample_output": "Your order has been shipped.",
        "is_folder": False,
    },
    {
        "number": 28,
        "title": "Enum with Fields and Methods",
        "description": "Enhance the OrderStatus enum with a numeric code and a description field, plus a method getByCode(int). Demonstrate looking up by code.",
        "sample_input": "Code: 2",
        "sample_output": "PROCESSING",
        "is_folder": False,
    },
    {
        "number": 29,
        "title": "Simple Package and Class Separation",
        "description": "Create a small program where main class is in one package and a utility class is in another. Demonstrate importing and using the utility.",
        "sample_input": "Call utility method from main",
        "sample_output": "Utility method executed.",
        "is_folder": False,
    },
    {
        "number": 30,
        "title": "Command-Line Argument Parsing",
        "description": "Accept multiple command-line arguments representing integers and print their sum and average. Handle the case when no arguments are passed.",
        "sample_input": "args: 10 20 30",
        "sample_output": "Sum = 60\nAverage = 20.0",
        "is_folder": False,
    },

    # 31–40: Inheritance, polymorphism, interfaces, abstract classes
    {
        "number": 31,
        "title": "Single Inheritance Example",
        "description": "Create a base class Person and a subclass Employee that adds employeeId and salary. Demonstrate accessing inherited and subclass fields.",
        "sample_input": "Person: Alice, Employee: Alice, id=101, salary=50000",
        "sample_output": "Name: Alice, EmployeeId: 101, Salary: 50000",
        "is_folder": False,
    },
    {
        "number": 32,
        "title": "Method Overriding and super Keyword",
        "description": "Override a method in a subclass and use super to call the parent implementation, then extend it. Demonstrate runtime polymorphism with a base-class reference.",
        "sample_input": "Base describe(), then subclass describe()",
        "sample_output": "Base: I am a vehicle.\nCar: I am a car.",
        "is_folder": False,
    },
    {
        "number": 33,
        "title": "Interface Implementation",
        "description": "Define an interface PaymentProcessor with methods pay and refund. Implement it in two classes (CardPayment and UpiPayment) and demonstrate polymorphic behavior.",
        "sample_input": "Process 100 using Card\nProcess 200 using UPI",
        "sample_output": "Card payment of 100 processed.\nUPI payment of 200 processed.",
        "is_folder": False,
    },
    {
        "number": 34,
        "title": "Multiple Interface Implementation",
        "description": "Create two interfaces Logger and Formatter. Implement both in a class ConsoleLogger and show how a class can implement multiple interfaces.",
        "sample_input": "Log message: 'Hello'",
        "sample_output": "[INFO] Hello",
        "is_folder": False,
    },
    {
        "number": 35,
        "title": "Abstract Class and Template Method",
        "description": "Create an abstract class DataProcessor with a template method process() calling read, transform, write. Implement two subclasses (FileDataProcessor and ApiDataProcessor). Demonstrate calling process on each.",
        "sample_input": "Run process() on both implementations",
        "sample_output": "File: read-transform-write\nAPI: read-transform-write",
        "is_folder": False,
    },
    {
        "number": 36,
        "title": "Upcasting and Downcasting",
        "description": "Demonstrate upcasting a subclass to a superclass reference and safely downcasting back. Show what happens if you downcast incorrectly using instanceof.",
        "sample_input": "Create Animal and Dog, cast references",
        "sample_output": "Safe downcast succeeded.\nInvalid downcast prevented by instanceof.",
        "is_folder": False,
    },
    {
        "number": 37,
        "title": "Polymorphic Array of Objects",
        "description": "Create an array of base-class references (e.g., Shape) storing different subclass objects (Circle, Rectangle). Loop and call an abstract method like area().",
        "sample_input": "Circle radius=2, Rectangle 3x4",
        "sample_output": "Circle area: 12.56\nRectangle area: 12.0",
        "is_folder": False,
    },
    {
        "number": 38,
        "title": "Final Keyword Usage",
        "description": "Demonstrate final for variables (constants), methods (cannot override), and classes (cannot extend). Write a small example showing each case.",
        "sample_input": "N/A (hard-coded examples)",
        "sample_output": "Shows compile-time restrictions via comments.",
        "is_folder": False,
    },
    {
        "number": 39,
        "title": "Overriding equals and hashCode",
        "description": "Create a class representing a User with id and email. Override equals and hashCode so that two users with same id are considered equal. Demonstrate using a HashSet.",
        "sample_input": "Users: (1, a@x), (1, b@y)",
        "sample_output": "Set size: 1",
        "is_folder": False,
    },
    {
        "number": 40,
        "title": "toString Override for Debugging",
        "description": "Override toString in a class (e.g., Order) to print its fields in a readable format. Show how it helps in logging and debugging.",
        "sample_input": "Order{id=101, amount=500}",
        "sample_output": "Order{id=101, amount=500.0, status='NEW'}",
        "is_folder": False,
    },

    # 41–50: Exceptions, basic collections, file I/O intro
    {
        "number": 41,
        "title": "Basic Exception Handling with try-catch",
        "description": "Read two integers and divide them. Handle ArithmeticException when dividing by zero and print a user-friendly message.",
        "sample_input": "10 0",
        "sample_output": "Cannot divide by zero.",
        "is_folder": False,
    },
    {
        "number": 42,
        "title": "Checked Exception with File Reading (Conceptual)",
        "description": "Simulate reading a file path from input and demonstrate how to handle checked exceptions using try-catch and throws (you may not actually read a file, but show the structure).",
        "sample_input": "data.txt",
        "sample_output": "Either file content or 'File not found' message.",
        "is_folder": False,
    },
    {
        "number": 43,
        "title": "Custom Exception for Validation",
        "description": "Create a custom exception InvalidAgeException and throw it if age < 18 when registering a user. Catch it in main to show an error message.",
        "sample_input": "Age: 16",
        "sample_output": "Registration failed: age must be at least 18.",
        "is_folder": False,
    },
    {
        "number": 44,
        "title": "Using ArrayList for Dynamic Collection",
        "description": "Read names until an empty line is entered, store them in an ArrayList, then print them with their index.",
        "sample_input": "Alice\nBob\n\n",
        "sample_output": "0: Alice\n1: Bob",
        "is_folder": False,
    },
    {
        "number": 45,
        "title": "Remove Duplicates Using Set",
        "description": "Read N integers and print unique values using a Set (e.g., HashSet). Preserve no specific ordering.",
        "sample_input": "5\n1 2 2 3 1",
        "sample_output": "1 2 3 (order may vary)",
        "is_folder": False,
    },
    {
        "number": 46,
        "title": "Word Frequency Counter with Map (Intro)",
        "description": "Read a line of text and count occurrences of each word using a Map. Print word and count.",
        "sample_input": "hello world hello",
        "sample_output": "hello: 2\nworld: 1",
        "is_folder": False,
    },
    {
        "number": 47,
        "title": "Basic File Writing (Conceptual)",
        "description": "Conceptually demonstrate writing some text to a file (e.g., using FileWriter/PrintWriter). Include proper closing of resources or try-with-resources in comments.",
        "sample_input": "Log message: 'App started'",
        "sample_output": "File 'log.txt' contains: App started",
        "is_folder": False,
    },
    {
        "number": 48,
        "title": "Command-Line Options Parsing (Flags)",
        "description": "Parse command-line arguments like --verbose or --help and behave differently based on the flags.",
        "sample_input": "args: --verbose",
        "sample_output": "Verbose mode enabled.",
        "is_folder": False,
    },
    {
        "number": 49,
        "title": "Simple Menu-Driven Console App",
        "description": "Implement a loop that shows a menu of options (add, list, exit) for a small in-memory list of tasks. Use switch-case.",
        "sample_input": "1:Add 'Learn Java'\n2:List\n3:Exit",
        "sample_output": "1. Learn Java",
        "is_folder": False,
    },
    {
        "number": 50,
        "title": "Basic Date and Time Usage",
        "description": "Use java.time.LocalDate and LocalTime to print the current date and time and calculate age given a birth date.",
        "sample_input": "Birth date: 2000-01-01",
        "sample_output": "Age: (current_year - 2000)",
        "is_folder": False,
    },
]

advanced_java_problems = [
    # 1–10: Collections framework & generics deeper
    {
        "number": 1,
        "title": "Sorting a List with Comparator",
        "description": "Create a list of User objects with name and age. Sort them by age ascending and then by name using Comparator.",
        "sample_input": "Users: (Alice,25), (Bob,20), (Charlie,25)",
        "sample_output": "(Bob,20), (Alice,25), (Charlie,25)",
        "is_folder": False,
    },
    {
        "number": 2,
        "title": "Generic Pair Class",
        "description": "Implement a generic Pair<T,U> class with getters and a nice toString. Demonstrate using it with different type parameters.",
        "sample_input": "Pair<Integer,String> (1,'one')",
        "sample_output": "Pair{first=1, second=one}",
        "is_folder": False,
    },
    {
        "number": 3,
        "title": "Wildcard Generics with Upper Bounds",
        "description": "Write a method that sums a List<? extends Number> and returns the result as double.",
        "sample_input": "[1,2,3.5]",
        "sample_output": "6.5",
        "is_folder": False,
    },
    {
        "number": 4,
        "title": "Wildcard Generics with Lower Bounds",
        "description": "Write a method that adds Integer values into a List<? super Integer>. Show how lower bounds are useful for adding elements.",
        "sample_input": "List<Number>",
        "sample_output": "List after adding integers: [1,2,3]",
        "is_folder": False,
    },
    {
        "number": 5,
        "title": "HashMap vs LinkedHashMap vs TreeMap",
        "description": "Create three maps with the same key-value pairs and show differences in iteration order using HashMap, LinkedHashMap, and TreeMap.",
        "sample_input": "Keys: 3,1,2",
        "sample_output": "HashMap: random order\nLinkedHashMap: 3,1,2\nTreeMap: 1,2,3",
        "is_folder": False,
    },
    {
        "number": 6,
        "title": "Implementing Comparable",
        "description": "Create a Task class that implements Comparable<Task> based on priority. Store tasks in a sorted collection (e.g., TreeSet).",
        "sample_input": "Tasks: p3, p1, p2",
        "sample_output": "p1, p2, p3",
        "is_folder": False,
    },
    {
        "number": 7,
        "title": "Using PriorityQueue for Scheduling",
        "description": "Use a PriorityQueue to simulate a simple task scheduler where tasks with the smallest deadline are executed first.",
        "sample_input": "Tasks with deadlines: 5,1,3",
        "sample_output": "Execute deadlines in order: 1,3,5",
        "is_folder": False,
    },
    {
        "number": 8,
        "title": "LRU Cache Using LinkedHashMap",
        "description": "Implement a simple LRU cache by extending LinkedHashMap and overriding removeEldestEntry.",
        "sample_input": "Capacity=2, put(1,A), put(2,B), get(1), put(3,C)",
        "sample_output": "Cache contains keys: 1,3",
        "is_folder": False,
    },
    {
        "number": 9,
        "title": "Multi-Map Using Map and List",
        "description": "Implement a simple MultiMap<String, String> using Map<String,List<String>>. Demonstrate adding multiple values for the same key.",
        "sample_input": "add('tag','java'), add('tag','spring')",
        "sample_output": "tag -> [java, spring]",
        "is_folder": False,
    },
    {
        "number": 10,
        "title": "Group By Field Using Streams",
        "description": "Given a list of Employee objects with department field, group them by department using streams and collect to Map<String,List<Employee>>.",
        "sample_input": "Employees across IT, HR",
        "sample_output": "{IT=[...], HR=[...]}",
        "is_folder": False,
    },

    # 11–20: Streams, lambdas, Optional, functional style
    {
        "number": 11,
        "title": "Filter-Map-Reduce Pipeline",
        "description": "Given a list of integers, filter even numbers, square them, and compute the sum using streams.",
        "sample_input": "[1,2,3,4]",
        "sample_output": "20",
        "is_folder": False,
    },
    {
        "number": 12,
        "title": "Find First Matching Element with Optional",
        "description": "Use streams and Optional to find the first user whose email ends with '@gmail.com'. Print a default message if not found.",
        "sample_input": "Users with different emails",
        "sample_output": "Found: user@example@gmail.com or 'No Gmail user found'",
        "is_folder": False,
    },
    {
        "number": 13,
        "title": "Custom Collector for Joining Strings",
        "description": "Implement a custom Collector to join strings with a prefix, delimiter, and suffix (similar to Collectors.joining).",
        "sample_input": "['a','b','c']",
        "sample_output": "<a|b|c>",
        "is_folder": False,
    },
    {
        "number": 14,
        "title": "Parallel Streams vs Sequential Streams",
        "description": "Given a large range of numbers, compare execution time between sequential and parallel streams for summing them. Print times.",
        "sample_input": "1 to 1_000_000",
        "sample_output": "Sequential: X ms\nParallel: Y ms",
        "is_folder": False,
    },
    {
        "number": 15,
        "title": "FlatMap for Nested Collections",
        "description": "Given a list of users, each with a list of roles, flatten all roles into a single list using flatMap.",
        "sample_input": "User1:[ADMIN,USER], User2:[USER]",
        "sample_output": "[ADMIN, USER, USER]",
        "is_folder": False,
    },
    {
        "number": 16,
        "title": "Partitioning Using Streams",
        "description": "Partition a list of integers into even and odd using Collectors.partitioningBy.",
        "sample_input": "[1,2,3,4,5]",
        "sample_output": "{true=[2,4], false=[1,3,5]}",
        "is_folder": False,
    },
    {
        "number": 17,
        "title": "Handling Nulls with Optional",
        "description": "Wrap possibly null values in Optional, demonstrate orElse, orElseGet, orElseThrow. Implement a method findUserById that returns Optional<User>.",
        "sample_input": "findUserById(1) exists, findUserById(99) missing",
        "sample_output": "User found vs default message vs exception.",
        "is_folder": False,
    },
    {
        "number": 18,
        "title": "Method References Instead of Lambdas",
        "description": "Refactor a stream pipeline to use method references (Class::method) where possible instead of lambdas.",
        "sample_input": "List of strings",
        "sample_output": "Same output, cleaner code using method references.",
        "is_folder": False,
    },
    {
        "number": 19,
        "title": "Immutability with Streams",
        "description": "Given a list, produce a new list of transformed values using streams without modifying the original list. Show both lists.",
        "sample_input": "[1,2,3]",
        "sample_output": "Original: [1,2,3]\nNew: [2,4,6]",
        "is_folder": False,
    },
    {
        "number": 20,
        "title": "Stream Error Handling Pattern",
        "description": "Demonstrate how to handle checked exceptions inside a stream (e.g., reading lines from files) using wrapper methods or custom functional interfaces.",
        "sample_input": "List of file paths",
        "sample_output": "Either file content or error message per file.",
        "is_folder": False,
    },

    # 21–30: Concurrency, threads, executors
    {
        "number": 21,
        "title": "Creating Threads with Runnable",
        "description": "Create multiple threads using Runnable that print their names and count from 1 to 5. Show interleaving of output.",
        "sample_input": "3 threads",
        "sample_output": "Thread-1:1\nThread-2:1\n...",
        "is_folder": False,
    },
    {
        "number": 22,
        "title": "Thread Sleep and Join",
        "description": "Start a worker thread that sleeps for some time and then prints a message. In main, wait for it using join before exiting.",
        "sample_input": "Worker sleeps 2 seconds",
        "sample_output": "Main waits until worker finishes.",
        "is_folder": False,
    },
    {
        "number": 23,
        "title": "Synchronized Counter",
        "description": "Implement a thread-safe counter using synchronized methods or blocks. Start multiple threads incrementing the same counter.",
        "sample_input": "1000 increments from 10 threads",
        "sample_output": "Final count: 10000",
        "is_folder": False,
    },
    {
        "number": 24,
        "title": "Producer-Consumer with wait/notify",
        "description": "Implement a bounded buffer with producer and consumer threads using wait and notifyAll to coordinate.",
        "sample_input": "Producer adds items, consumer removes",
        "sample_output": "No lost or duplicated items, buffer size within bounds.",
        "is_folder": False,
    },
    {
        "number": 25,
        "title": "Using ExecutorService and Callable",
        "description": "Submit multiple Callable tasks to an ExecutorService that return results (e.g., square of an integer). Collect and print the results.",
        "sample_input": "Tasks for [1,2,3,4]",
        "sample_output": "Results: [1,4,9,16]",
        "is_folder": False,
    },
    {
        "number": 26,
        "title": "ScheduledExecutorService for Periodic Tasks",
        "description": "Use ScheduledExecutorService to run a task periodically (e.g., every second) for a fixed number of executions.",
        "sample_input": "Run heartbeat 5 times",
        "sample_output": "Heartbeat 1\n...\nHeartbeat 5",
        "is_folder": False,
    },
    {
        "number": 27,
        "title": "Deadlock Demonstration",
        "description": "Create a simple example of deadlock with two threads and two locks. Explain in comments how to avoid it.",
        "sample_input": "Two threads locking resources in opposite order",
        "sample_output": "Program hangs (deadlock) unless fixed.",
        "is_folder": False,
    },
    {
        "number": 28,
        "title": "Using ConcurrentHashMap",
        "description": "Simulate multiple threads updating a shared map of counters using ConcurrentHashMap without explicit synchronization.",
        "sample_input": "Threads increment different keys",
        "sample_output": "Final map with correct counts.",
        "is_folder": False,
    },
    {
        "number": 29,
        "title": "AtomicInteger for Lock-Free Counter",
        "description": "Use AtomicInteger to implement a lock-free counter incremented by multiple threads. Compare with non-atomic version.",
        "sample_input": "10 threads, 1000 increments each",
        "sample_output": "Atomic: 10000, Non-atomic: often less than 10000",
        "is_folder": False,
    },
    {
        "number": 30,
        "title": "CompletableFuture for Async Composition",
        "description": "Use CompletableFuture to compose asynchronous tasks (e.g., fetch user, then fetch orders for that user). Show thenApply/thenCompose usage.",
        "sample_input": "Fetch user 1 then orders",
        "sample_output": "User 1 with list of orders printed after async completion.",
        "is_folder": False,
    },

    # 31–40: I/O, serialization, reflection, annotations, logging
    {
        "number": 31,
        "title": "Reading Large Files with Buffered Streams",
        "description": "Demonstrate reading a large text file line by line using BufferedReader, counting total lines.",
        "sample_input": "path: data.txt",
        "sample_output": "Total lines: N",
        "is_folder": False,
    },
    {
        "number": 32,
        "title": "Object Serialization and Deserialization",
        "description": "Create a Serializable class, write an object to a file using ObjectOutputStream, then read it back using ObjectInputStream.",
        "sample_input": "User object with id=1, name='Alice'",
        "sample_output": "Deserialized: User{id=1, name='Alice'}",
        "is_folder": False,
    },
    {
        "number": 33,
        "title": "Try-With-Resources for Auto-Closeables",
        "description": "Demonstrate using try-with-resources for streams/readers to ensure they are closed automatically.",
        "sample_input": "Read file and print contents",
        "sample_output": "Contents printed without manual close() calls.",
        "is_folder": False,
    },
    {
        "number": 34,
        "title": "Basic Reflection to Inspect Class",
        "description": "Given a class, use reflection to print its fields, methods, and constructors at runtime.",
        "sample_input": "Class: java.lang.String",
        "sample_output": "List of methods, fields, constructors.",
        "is_folder": False,
    },
    {
        "number": 35,
        "title": "Instantiate Class Dynamically with Reflection",
        "description": "Use Class.forName and newInstance/constructors to create instances dynamically based on class name string.",
        "sample_input": "Class name: com.example.MyService",
        "sample_output": "Instance of MyService created.",
        "is_folder": False,
    },
    {
        "number": 36,
        "title": "Custom Annotation for Validation",
        "description": "Define a custom annotation @NotEmpty and use reflection to validate annotated String fields in a DTO.",
        "sample_input": "DTO with empty name field",
        "sample_output": "Validation error: name must not be empty.",
        "is_folder": False,
    },
    {
        "number": 37,
        "title": "Logging with SLF4J (Conceptual)",
        "description": "Demonstrate using a logging facade like SLF4J instead of System.out.println. Show different log levels (INFO, WARN, ERROR).",
        "sample_input": "Simulate a process with info and error logs",
        "sample_output": "INFO ...\nERROR ...",
        "is_folder": False,
    },
    {
        "number": 38,
        "title": "Internationalization with ResourceBundle",
        "description": "Use ResourceBundle to load messages in different languages based on locale and print a greeting.",
        "sample_input": "Locale: en, fr",
        "sample_output": "Hello vs Bonjour",
        "is_folder": False,
    },
    {
        "number": 39,
        "title": "Properties File for Configuration",
        "description": "Load configuration from a .properties file (e.g., db.url, db.user) and print the values.",
        "sample_input": "config.properties with db.url=jdbc:mysql://...",
        "sample_output": "db.url=jdbc:mysql://...",
        "is_folder": False,
    },
    {
        "number": 40,
        "title": "Basic JDBC Query Execution (Conceptual)",
        "description": "Demonstrate connecting to a database with JDBC, preparing a statement, executing a query, and iterating over ResultSet (focus on structure, not actual DB).",
        "sample_input": "Query: SELECT id,name FROM users",
        "sample_output": "id=1, name=Alice\nid=2, name=Bob",
        "is_folder": False,
    },

    # 41–50: Design patterns & architecture (folder-based problems)
    {
        "number": 41,
        "title": "Strategy Pattern for Payment Methods",
        "description": "Design a folder structure implementing the Strategy pattern for different payment methods (CreditCardPayment, UpiPayment, NetBankingPayment). The client should be able to switch strategies at runtime. Create interfaces and concrete strategies in separate files. Demonstrate usage in a main class.",
        "sample_input": "Select payment strategy: card, upi, or netbanking; amount=1000",
        "sample_output": "Processing 1000 via selected payment strategy.",
        "is_folder": True,
    },
    {
        "number": 42,
        "title": "Observer Pattern for Event Notifications",
        "description": "Design classes for an Observer pattern where a Subject (e.g., Order) notifies observers (EmailNotifier, SmsNotifier) on state changes (CREATED, SHIPPED, DELIVERED). Place interfaces and implementations in appropriate subpackages.",
        "sample_input": "Order status changes from CREATED to SHIPPED",
        "sample_output": "Email sent: Your order is shipped.\nSMS sent: Your order is shipped.",
        "is_folder": True,
    },
    {
        "number": 43,
        "title": "Factory Method for Creating Cloud Clients",
        "description": "Implement the Factory Method pattern to create different CloudClient implementations (AwsClient, AzureClient, GcpClient) based on a configuration or input. Organize interfaces, concrete classes, and factory in a clear package structure.",
        "sample_input": "cloud=aws",
        "sample_output": "Using AwsClient to perform cloud operation.",
        "is_folder": True,
    },
    {
        "number": 44,
        "title": "Singleton Pattern for Configuration Manager",
        "description": "Implement a thread-safe Singleton for a ConfigurationManager that loads properties once and provides getters. Show different singleton implementations (eager, lazy with double-checked locking) in separate classes.",
        "sample_input": "Access config from multiple parts of code",
        "sample_output": "ConfigurationManager instance reused everywhere.",
        "is_folder": True,
    },
    {
        "number": 45,
        "title": "Builder Pattern for Complex Request Objects",
        "description": "Use the Builder pattern to construct a complex HttpRequest object with many optional fields (headers, query params, body). Organize builder and main class in separate files.",
        "sample_input": "Build GET request with header X-Request-Id and query param page=1",
        "sample_output": "HttpRequest{method=GET, url='...', headers=..., queryParams=...}",
        "is_folder": True,
    },
    {
        "number": 46,
        "title": "Adapter Pattern for Logging APIs",
        "description": "You have an existing Logger interface but need to integrate with a third-party logging library that has a different API. Use Adapter pattern to bridge them. Create adapter classes in their own package.",
        "sample_input": "Call oldLogger.logInfo('Hello')",
        "sample_output": "Underlying third-party logger receives appropriate call.",
        "is_folder": True,
    },
    {
        "number": 47,
        "title": "Repository Pattern for Data Access Layer",
        "description": "Design a simple repository interface for a User entity and create an in-memory implementation. Organize domain model, repository interface, and implementation classes in different packages to mimic a layered architecture.",
        "sample_input": "Save user, findById, findAll",
        "sample_output": "Users retrieved from in-memory store.",
        "is_folder": True,
    },
    {
        "number": 48,
        "title": "DTO and Mapper Pattern for API Layer",
        "description": "Create domain entities and DTOs (Data Transfer Objects) and implement a mapper class to convert between them. Organize entities, DTOs, and mappers in separate folders. Focus on immutability and null-safety.",
        "sample_input": "UserEntity{id=1, name='Alice'}",
        "sample_output": "UserDto{id=1, fullName='Alice'}",
        "is_folder": True,
    },
    {
        "number": 49,
        "title": "Validation Layer with Custom Exceptions",
        "description": "Design a validation layer that validates incoming DTOs and throws custom exceptions like ValidationException with error codes. Organize validators, exceptions, and models in separate packages.",
        "sample_input": "UserDto with empty name and invalid email",
        "sample_output": "ValidationException with messages about name and email.",
        "is_folder": True,
    },
    {
        "number": 50,
        "title": "Layered Architecture Mini-Skeleton",
        "description": "Create a mini layered architecture skeleton with packages: controller, service, repository, model. Implement simple method flow (controller -> service -> repository) without any framework, using plain Java classes. Include a main class to demonstrate a use case.",
        "sample_input": "Call controller.createUser('Alice')",
        "sample_output": "User created via service and repository layers.",
        "is_folder": True,
    },
]


# ============ GENERATION LOGIC ============

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)


def write_java_problem(root_dir: str, prefix: str, problem: dict):
    num = problem["number"]
    title = problem["title"]
    description = problem["description"]
    sample_input = problem["sample_input"]
    sample_output = problem["sample_output"]

    slug = slugify(title)
    file_name = f"{prefix}{num:02d}_{slug}.java"
    file_path = os.path.join(root_dir, file_name)

    content = make_comment_block(num, title, description, sample_input, sample_output)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


def write_folder_problem(root_dir: str, prefix: str, problem: dict):
    num = problem["number"]
    title = problem["title"]
    description = problem["description"]
    sample_input = problem["sample_input"]
    sample_output = problem["sample_output"]

    slug = slugify(title)
    folder_name = f"{prefix}{num:02d}_{slug}"
    folder_path = os.path.join(root_dir, folder_name)
    ensure_dir(folder_path)

    text_path = os.path.join(folder_path, "problem.txt")
    text_content = dedent(
        f"""\
        Problem {num}: {title}

        Description:
        {description.strip()}

        Sample Input:
        {sample_input.strip()}

        Sample Output:
        {sample_output.strip()}
        """
    )

    with open(text_path, "w", encoding="utf-8") as f:
        f.write(text_content)


def generate_section(base_dir: str, subfolder: str, prefix: str, problems: list[dict]):
    root = os.path.join(base_dir, subfolder)
    ensure_dir(root)
    for p in problems:
        if p.get("is_folder"):
            write_folder_problem(root, prefix, p)
        else:
            write_java_problem(root, prefix, p)


def main():
    ensure_dir(BASE_DIR)
    generate_section(BASE_DIR, "01_java_basics", "JB", java_basics_problems)
    generate_section(BASE_DIR, "02_advanced_java", "AJ", advanced_java_problems)
    print(f"Generated {len(java_basics_problems)} Java basics problems and {len(advanced_java_problems)} advanced Java problems under '{BASE_DIR}'.")


if __name__ == "__main__":
    main()
