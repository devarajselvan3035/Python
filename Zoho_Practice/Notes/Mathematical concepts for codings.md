Welcome. As a coach, I can tell you that mastering these foundational mathematical concepts is one of the highest-leverage investments you can make for competitive programming and technical interviews. While it's easy to get lost in complex data structures, math is often the "secret key" that reduces a complex $O(N)$ or $O(N^2)$ algorithm down to $O(\log N)$ or even $O(1)$.

Here is your comprehensive guide to the essential mathematical concepts, structured exactly as you requested.

### 1. Number Theory: Greatest Common Divisor (GCD) & Least Common Multiple (LCM)

**1. Core Mathematical Principle**

The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both numbers without leaving a remainder. The Least Common Multiple (LCM) is the smallest positive integer that is divisible by both numbers. The most efficient way to compute the GCD is the Euclidean Algorithm, which relies on the principle that the GCD of two numbers also divides their difference.

**2. The Mathematical Formulas**

The Euclidean Algorithm operates on the recursive principle:

$GCD(a, b) = GCD(b, a \pmod b)$

Base case: $GCD(a, 0) = a$

The LCM is directly derived from the GCD:

$LCM(a, b) = \frac{|a \cdot b|}{GCD(a, b)}$

**3. Why it Matters in Coding**

You will see this everywhere in fraction simplification, determining the periods of repeating events (like finding when two planets align in orbit), cycle detection, and solving Linear Diophantine Equations.

**4. Code Example**

```python
def gcd(a, b):
    # Euclidean Algorithm
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    # LCM using the GCD property
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

# Example usage:
print(f"GCD of 48 and 18 is {gcd(48, 18)}") # Output: 6
print(f"LCM of 48 and 18 is {lcm(48, 18)}") # Output: 144
```

- **Time Complexity:** $O(\log(\min(a, b)))$. The numbers decrease by at least half every two steps.
    
- **Space Complexity:** $O(1)$ for this iterative approach (recursive would use $O(\log(\min(a, b)))$ call stack space).
    

### 2. Number Theory: Prime Numbers & The Sieve of Eratosthenes

**1. Core Mathematical Principle**

A prime number is a natural number greater than 1 that has exactly two distinct positive divisors: 1 and itself. The Sieve of Eratosthenes is a highly efficient algorithm for finding all prime numbers up to a given limit $N$. It works by iteratively marking the multiples of each prime starting from 2.

**2. The Mathematical Formulas**

This concept is governed by the Fundamental Theorem of Arithmetic, which states that every integer $N > 1$ can be represented uniquely as a product of prime powers:

$N = p_1^{k_1} \cdot p_2^{k_2} \cdots p_m^{k_m}$

When searching for prime factors of $N$, you only need to check up to $\sqrt{N}$.

**3. Why it Matters in Coding**

Prime factorization is the bedrock of cryptography (like RSA). In competitive programming, primes are used for counting divisors, finding sums of divisors, hashing, and solving optimization problems that involve coprime conditions.

**4. Code Example**

```python
def sieve_of_eratosthenes(n):
    # Initialize a boolean array "is_prime" to True
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False # 0 and 1 are not primes
    
    p = 2
    # We only need to check up to the square root of n
    while (p * p <= n):
        if is_prime[p]:
            # Mark all multiples of p as False
            # Start at p*p because smaller multiples were marked by smaller primes
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
        
    # Return a list of all prime numbers
    return [p for p in range(n + 1) if is_prime[p]]

# Example usage:
print(sieve_of_eratosthenes(30))
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

- **Time Complexity:** $O(N \log(\log N))$. This is exceptionally fast and near-linear.
    
- **Space Complexity:** $O(N)$ to store the boolean array.
    

### 3. Number Theory: Modular Arithmetic & Modulo Inverse

**1. Core Mathematical Principle**

Modular arithmetic is a system of arithmetic for integers where numbers "wrap around" when reaching a certain value (the modulus). Because integers in coding problems can grow large enough to cause overflow in languages like C++ or Java (and slow down BigInt operations in Python), many questions ask for the answer "modulo $10^9 + 7$".

**2. The Mathematical Formulas**

Addition and Multiplication distribute over modulo operations nicely:

$(A + B) \pmod M = ((A \pmod M) + (B \pmod M)) \pmod M$

$(A \cdot B) \pmod M = ((A \pmod M) \cdot (B \pmod M)) \pmod M$

_Crucially_, division does **not** work the same way. To compute $(A / B) \pmod M$, you must multiply $A$ by the Modular Multiplicative Inverse of $B$. By Fermat's Little Theorem, if $M$ is prime:

$B^{M-1} \equiv 1 \pmod M$

$B^{-1} \equiv B^{M-2} \pmod M$

**3. Why it Matters in Coding**

It is mandatory for computing large factorials, combinations, or counting dynamic programming paths where the answer is astronomically huge.

**4. Code Example**

```python
def power_mod(base, exp, mod):
    # Computes (base^exp) % mod using Fast Binary Exponentiation
    result = 1
    base = base % mod
    
    while exp > 0:
        # If exp is odd, multiply base with result
        if exp % 2 == 1:
            result = (result * base) % mod
        
        # exp must be even now, so divide by 2
        exp = exp // 2
        base = (base * base) % mod
        
    return result

def mod_inverse(n, m):
    # Returns modulo inverse of n with respect to m using Fermat's Little Theorem.
    # Note: m MUST be a prime number!
    return power_mod(n, m - 2, m)

MOD = 10**9 + 7
# Equivalent to (10 / 2) % MOD, done via modular inverse
print((10 * mod_inverse(2, MOD)) % MOD) # Output: 5
```

- **Time Complexity:** $O(\log(\text{exp}))$. By squaring the base and halving the exponent, we calculate powers very quickly.
    
- **Space Complexity:** $O(1)$.
    

### 4. Combinatorics: Permutations & Combinations

**1. Core Mathematical Principle**

Combinatorics is the mathematics of counting.

- **Permutations** count the number of ways to arrange items where _order matters_ (e.g., race rankings).
    
- **Combinations** count the number of ways to select items where _order does not matter_ (e.g., choosing a committee).
    

**2. The Mathematical Formulas**

Permutations of $k$ items chosen from $n$ items:

$P(n, k) = \frac{n!}{(n-k)!}$

Combinations of $k$ items chosen from $n$ items (also known as "n choose k"):

$\binom{n}{k} = C(n, k) = \frac{n!}{k!(n-k)!}$

**3. Why it Matters in Coding**

Combinatorics frequently appears in probability questions, dynamic programming state counting, graph theory (counting spanning trees), and any problem asking "how many ways can you arrange/select...".

**4. Code Example**

_Note: In competitive programming, combinations are often requested modulo a prime._

```python
MOD = 10**9 + 7
MAX_N = 1000

# Precompute factorials for O(1) combinations retrieval
fact = [1] * (MAX_N + 1)
inv_fact = [1] * (MAX_N + 1)

# Populate factorials
for i in range(1, MAX_N + 1):
    fact[i] = (fact[i-1] * i) % MOD

# Populate inverse factorials (requires the power_mod function from above)
inv_fact[MAX_N] = power_mod(fact[MAX_N], MOD - 2, MOD)
for i in range(MAX_N - 1, -1, -1):
    inv_fact[i] = (inv_fact[i+1] * (i + 1)) % MOD

def nCr(n, r):
    if r < 0 or r > n:
        return 0
    # Equivalent to n! / (r! * (n-r)!) % MOD
    numerator = fact[n]
    denominator = (inv_fact[r] * inv_fact[n - r]) % MOD
    return (numerator * denominator) % MOD

print(f"5 choose 2 is {nCr(5, 2)}") # Output: 10
```

- **Time Complexity:** $O(N)$ for the precomputation step. $O(1)$ for each `nCr` query.
    
- **Space Complexity:** $O(N)$ to store the `fact` and `inv_fact` arrays.
    

### 5. Matrix Operations: Matrix Exponentiation

**1. Core Mathematical Principle**

Matrix exponentiation takes a linear recurrence relation (where the next term depends on previous terms, like the Fibonacci sequence) and transforms it into a matrix multiplication problem. By applying Fast Binary Exponentiation (the same logic used in modular arithmetic) to matrices, we can solve for the $N^{th}$ term in logarithmic time instead of linear time.

**2. The Mathematical Formulas**

For the Fibonacci sequence $F_n = F_{n-1} + F_{n-2}$, we can represent the transition between states as a matrix multiplication:

$$\begin{pmatrix} F_n \\ F_{n-1} \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^{n-1} \begin{pmatrix} F_1 \\ F_0 \end{pmatrix}$$

**3. Why it Matters in Coding**

If a problem asks you to find the $N^{th}$ term of a sequence or the number of paths in a graph of length $N$, and $N$ is massive (e.g., $10^{18}$), standard dynamic programming $O(N)$ will time out. Matrix exponentiation reduces the time complexity to $O(\log N)$, easily beating the time limit.

**4. Code Example**

Python

```
def multiply_matrices(A, B, mod=10**9+7):
    # Multiplies two 2x2 matrices
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % mod, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % mod],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % mod, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % mod]
    ]

def matrix_power(mat, exp, mod=10**9+7):
    # Fast exponentiation for 2x2 matrices
    result = [[1, 0], [0, 1]] # Identity matrix
    base = mat
    
    while exp > 0:
        if exp % 2 == 1:
            result = multiply_matrices(result, base, mod)
        base = multiply_matrices(base, base, mod)
        exp //= 2
        
    return result

def fibonacci_massive(n):
    if n == 0: return 0
    # The transformation matrix
    T = [[1, 1], [1, 0]]
    # Raise the matrix to the power of n-1
    T_n_minus_1 = matrix_power(T, n - 1)
    # The answer is T[0][0]*F_1 + T[0][1]*F_0 (where F_1=1, F_0=0)
    return T_n_minus_1[0][0]

print(f"10th Fibonacci modulo 10^9+7: {fibonacci_massive(10)}") # Output: 55
```

- **Time Complexity:** $O(K^3 \log N)$, where $K$ is the size of the matrix (here $K=2$, so practically $O(\log N)$).
    
- **Space Complexity:** $O(K^2)$ for storing the matrices.
    

### 6. Bitwise Operations: Bit Manipulation

**1. Core Mathematical Principle**

At the hardware level, everything is stored as binary bits. Bitwise operations directly manipulate these bits. Mathematical properties of bitwise operations (AND, OR, XOR, NOT, shifts) can be leveraged to execute operations much faster than standard arithmetic loops.

**2. The Mathematical Formulas / Properties**

- **XOR ($\oplus$):** $x \oplus x = 0$, $x \oplus 0 = x$. Reversing itself.
    
- **Check if power of 2:** $x > 0$ and $x \ \& \ (x - 1) == 0$.
    
- **Isolate lowest set bit:** $x \ \& \ -x$. (Due to Two's Complement representation).
    
- **Multiply/Divide by 2:** $x \ll 1$ (Multiply), $x \gg 1$ (Divide).
    

**3. Why it Matters in Coding**

Bit manipulation is essential for bitmasking (representing sets or states in DP), optimizing memory arrays, evaluating game theory states (like Nim), and solving "find the odd occurring element" logic puzzles.

**4. Code Example**

Python

```
def count_set_bits(n):
    # Brian Kernighan's Algorithm
    # Counts the number of 1s in the binary representation
    count = 0
    while n > 0:
        # n & (n - 1) clears the lowest set bit in n
        n = n & (n - 1)
        count += 1
    return count

def find_single_number(nums):
    # Finds the only number that appears once in an array 
    # where every other number appears exactly twice
    result = 0
    for num in nums:
        result ^= num # XOR
    return result

print(f"Set bits in 13 (1101): {count_set_bits(13)}") # Output: 3
print(f"Unique number in [4,1,2,1,2]: {find_single_number([4,1,2,1,2])}") # Output: 4
```

- **Time Complexity:** * `count_set_bits`: $O(K)$, where $K$ is the number of set bits (better than $O(\text{total bits})$).
    
    - `find_single_number`: $O(N)$ to traverse the array once.
        
- **Space Complexity:** $O(1)$ for both functions, as operations happen purely in registers/variables.