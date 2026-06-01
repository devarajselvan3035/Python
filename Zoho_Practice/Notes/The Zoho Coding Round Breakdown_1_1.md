Zoho’s software engineering recruitment process heavily prioritizes clean, optimized code logic, raw problem-solving capability, and algorithmic fundamentals over library dependencies. They often require you to implement solutions from scratch without relying on high-level built-in parsing functions.

## The Zoho Coding Round Breakdown

The assessment is generally divided into three sequential, eliminatory phases:  

- **Round 1 (Basic Coding & Aptitude):** Short logic puzzles, core loop mechanics, and basic array/string validations.  
- **Round 2 (Advanced Coding):** 4–5 complex multi-pointer, matrix, dynamic tracking, or decoding algorithms over 2–3 hours.
- **Round 3 (Low-Level Design):** Designing a complete, modular console application (e.g., an automated ticketing system) within 2–3 hours.

## Core Topics & Sample Questions

### 1. String Manipulation & Custom Parsing

Zoho is famous for testing precise string manipulation, character frequency analysis, and custom data formatting constraints.

- **Beginner:** Given a sentence, remove all words that are palindromes and return the modified string. *(Example: "He did a good deed" $\rightarrow$ "He good")*  
- **Intermediate:** **The Classic Zoho String Expansion.** Given a compressed input string like `a1b10c2`, expand it to output `abbbbbbbbbbcc`. The repetition factor can be up to 2 digits.
- **Intermediate:** Print an odd-length string in an "X" format layout using nested loops.

### 2. Custom Array Sorting & Matrix Manipulations

Standard array implementations are tested using atypical sorting conditions or spatial adjustments.

- **Beginner:** Separate 0s and 1s in an array in a single traversal pass using O(1) extra space.  
- **Intermediate:** **Alternating Sort.** Sort an array such that odd numbers are positioned in ascending order, and even numbers are sorted in descending order within the same array structure.  
- **Intermediate:** Given a two-dimensional matrix and two coordinate indices representing opposite corners, extract the defined sub-rectangle area and calculate its total mathematical sum.

### 3. Mathematical Logic & Discrete Math

These questions test your ability to translate logical arithmetic rules into clean conditional control statements.

- **Beginner:** Write a function to check if a provided number is an Armstrong number (equal to the sum of its own digits each raised to the power of the total number of digits).  
- **Intermediate:** Given two calendar dates as input structures (day, month, year), calculate the exact number of days between them from scratch, handling leap years without date libraries.  
- **Intermediate:** Given a sequence of digits (e.g., "121"), count the number of possible alphabetical decodings if 1 represents 'A', 2 represents 'B', up to 26 for 'Z'.

### 4. Applied Data Structures (Stacks & Linked Lists)

Linear structures are routinely tested to evaluate how safely you manipulate dynamic memory and pointers.

- **Beginner:** Find the exact middle node of a single linked list in a single pass traversal.  
- **Intermediate:** Implement an expression validator that ensures every parenthesis type `(` has a matching closing `)` and that brackets are nested correctly.

## The Advanced Phase: Low-Level Design (LLD)

If you pass the core algorithms, you will transition directly into building a working CLI system. Focus heavily on modular object relations and entity state tracking.

| **Common LLD Problems**         | **Core Focus Areas**                                         |
| ------------------------------- | ------------------------------------------------------------ |
| **Railway Reservation System**  | Berth allocation rules, waiting list queues, and cancellations. |
| **Taxi Booking App**            | Fleet tracking, calculating minimum distance dispatch, and fare metering. |
| **Inventory Management System** | Real-time stock counts, supplier triggers, and transaction histories. |