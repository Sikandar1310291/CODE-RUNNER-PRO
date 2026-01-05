import os
import urllib.parse

# This dictionary will store the language specific terminology and solutions
# Structure: { slug: { name, ext, intro, problems: [ { title, code, exp, time, space } ] } }
LANG_DATA = {
    "python": {
        "name": "Python",
        "ext": ".py",
        "intro": "Python is known for its readability and simplicity. These 17 problems cover fundamental algorithms and data structures that every Python developer should master.",
        "problems": [
            {
                "title": "Swap Variables",
                "code": "a = 5\nb = 10\na, b = b, a\nprint(f'a: {a}, b: {b}')",
                "exp": "Python allows multiple assignments in one line, making variable swapping elegant without a temporary variable.",
                "time": "O(1)",
                "space": "O(1)"
            },
            {
                "title": "Factorial (recursive)",
                "code": "def factorial(n):\n    if n == 0:\n        return 1\n    return n * factorial(n-1)\n\nprint(factorial(5))",
                "exp": "A function that calls itself until it reaches the base case (n=0).",
                "time": "O(n)",
                "space": "O(n) due to recursion stack"
            },
            {
                "title": "Fibonacci",
                "code": "def fib(n):\n    if n <= 1:\n        return n\n    return fib(n-1) + fib(n-2)\n\nprint([fib(i) for i in range(10)])",
                "exp": "Computes the nth Fibonacci number. Every number is the sum of the two preceding ones.",
                "time": "O(2^n)",
                "space": "O(n)"
            },
            {
                "title": "Prime Check",
                "code": "def is_prime(n):\n    if n < 2: return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return False\n    return True\n\nprint(is_prime(17))",
                "exp": "Checks if a number is divisible only by 1 and itself by testing divisors up to the square root.",
                "time": "O(sqrt(n))",
                "space": "O(1)"
            },
            {
                "title": "Reverse Array/List",
                "code": "arr = [1, 2, 3, 4, 5]\nreversed_arr = arr[::-1]\nprint(reversed_arr)",
                "exp": "Uses Python's slicing syntax to create a copy of the list in reverse order.",
                "time": "O(n)",
                "space": "O(n)"
            },
            {
                "title": "Binary Search",
                "code": "def binary_search(arr, x):\n    low, high = 0, len(arr) - 1\n    while low <= high:\n        mid = (low + high) // 2\n        if arr[mid] < x:\n            low = mid + 1\n        elif arr[mid] > x:\n            high = mid - 1\n        else:\n            return mid\n    return -1\n\nprint(binary_search([1, 2, 3, 4, 5], 4))",
                "exp": "Efficiently finds an element in a sorted array by repeatedly dividing the search interval in half.",
                "time": "O(log n)",
                "space": "O(1)"
            },
            {
                "title": "GCD",
                "code": "import math\nprint(math.gcd(48, 18))",
                "exp": "Finds the Greatest Common Divisor using the Euclidean algorithm (via built-in math module).",
                "time": "O(log(min(a,b)))",
                "space": "O(1)"
            },
            {
                "title": "Power Function",
                "code": "def power(base, exp):\n    if exp == 0: return 1\n    res = power(base, exp // 2)\n    if exp % 2 == 0:\n        return res * res\n    return res * res * base\n\nprint(power(2, 10))",
                "exp": "Calculates base^exp using binary exponentiation, significantly faster than linear multiplication.",
                "time": "O(log n)",
                "space": "O(log n)"
            },
            {
                "title": "Sum of Array/List",
                "code": "arr = [1, 2, 3, 4, 5]\nprint(sum(arr))",
                "exp": "Uses the built-in sum() function to iterate and aggregate elements.",
                "time": "O(n)",
                "space": "O(1)"
            },
            {
                "title": "Max Element",
                "code": "arr = [10, 5, 20, 8]\nprint(max(arr))",
                "exp": "Finds the largest value in an iterable using the max() function.",
                "time": "O(n)",
                "space": "O(1)"
            },
            {
                "title": "Sort",
                "code": "arr = [5, 2, 9, 1, 5, 6]\nprint(sorted(arr))",
                "exp": "Uses Timsort (Python's built-in sorting algorithm) which is stable and hybrid.",
                "time": "O(n log n)",
                "space": "O(n)"
            },
            {
                "title": "Remove Duplicates",
                "code": "arr = [1, 2, 2, 3, 4, 4, 5]\nprint(list(set(arr)))",
                "exp": "Converting a list to a set automatically removes duplicates because sets only store unique values.",
                "time": "O(n)",
                "space": "O(n)"
            },
            {
                "title": "Factorial (iterative)",
                "code": "def factorial_iter(n):\n    res = 1\n    for i in range(2, n + 1):\n        res *= i\n    return res\n\nprint(factorial_iter(5))",
                "exp": "Calculates factorial using a simple loop, avoiding recursion limits and overhead.",
                "time": "O(n)",
                "space": "O(1)"
            },
            {
                "title": "Armstrong Number",
                "code": "def is_armstrong(n):\n    s = str(n)\n    p = len(s)\n    return n == sum(int(digit)**p for digit in s)\n\nprint(is_armstrong(153))",
                "exp": "Checks if the sum of digits raised to the power of number of digits equals the number itself.",
                "time": "O(d) where d is digits",
                "space": "O(d)"
            },
            {
                "title": "Palindrome",
                "code": "def is_palindrome(s):\n    s = str(s)\n    return s == s[::-1]\n\nprint(is_palindrome('racecar'))",
                "exp": "Compares a string or number with its reversed version.",
                "time": "O(n)",
                "space": "O(n)"
            },
            {
                "title": "Largest of 3 numbers",
                "code": "a, b, c = 10, 25, 15\nprint(max(a, b, c))",
                "exp": "Finds the maximum value among three variables using built-in logic.",
                "time": "O(1)",
                "space": "O(1)"
            },
            {
                "title": "Even/Odd Count",
                "code": "arr = [1, 2, 3, 4, 5, 6]\neven = len([x for x in arr if x % 2 == 0])\nodd = len(arr) - even\nprint(f'Even: {even}, Odd: {odd}')",
                "exp": "Filters the list to find even numbers and calculates the remainder for odds.",
                "time": "O(n)",
                "space": "O(n)"
            }
        ]
    },
    "javascript": {
        "name": "JavaScript",
        "ext": ".js",
        "intro": "JavaScript is the heartbeat of the web. These 17 problems will sharpen your ES6+ skills and logic for frontend and backend roles.",
        "problems": [
            {"title": "Swap Variables", "code": "let a = 5, b = 10;\n[a, b] = [b, a];\nconsole.log(`a: ${a}, b: ${b}`);", "exp": "Uses array destructuring to swap variables without a temporary one.", "time": "O(1)", "space": "O(1)"},
            {"title": "Factorial (recursive)", "code": "function fact(n) {\n  return n <= 1 ? 1 : n * fact(n-1);\n}\nconsole.log(fact(5));", "exp": "Implementation using recursion for a clean mathematical look.", "time": "O(n)", "space": "O(n)"},
            {"title": "Fibonacci", "code": "function fib(n) {\n  return n < 2 ? n : fib(n-1) + fib(n-2);\n}\nconsole.log(fib(7));", "exp": "Recursive calculation of the Fibonacci sequence.", "time": "O(2^n)", "space": "O(n)"},
            {"title": "Prime Check", "code": "function isPrime(n) {\n  if (n < 2) return false;\n  for(let i=2; i<=Math.sqrt(n); i++) if(n%i === 0) return false;\n  return true;\n}\nconsole.log(isPrime(19));", "exp": "Efficient prime check iterating up to the square root.", "time": "O(sqrt(n))", "space": "O(1)"},
            {"title": "Reverse Array/List", "code": "const arr = [1, 2, 3, 4];\nconsole.log(arr.reverse());", "exp": "Uses built-in reverse() method which modifies the array in-place.", "time": "O(n)", "space": "O(1)"},
            {"title": "Binary Search", "code": "function bs(arr, x) {\n  let l = 0, r = arr.length - 1;\n  while(l <= r) {\n    let m = Math.floor((l+r)/2);\n    if(arr[m] === x) return m;\n    if(arr[m] < x) l = m + 1; else r = m - 1;\n  }\n  return -1;\n}\nconsole.log(bs([1,2,3,4,5], 4));", "exp": "Classic binary search implementation for sorted arrays.", "time": "O(log n)", "space": "O(1)"},
            {"title": "GCD", "code": "function gcd(a, b) {\n  return b === 0 ? a : gcd(b, a % b);\n}\nconsole.log(gcd(48, 18));", "exp": "Euclidean algorithm using recursion.", "time": "O(log(min(a,b)))", "space": "O(log n)"},
            {"title": "Power Function", "code": "function pow(b, e) {\n  return Math.pow(b, e);\n}\nconsole.log(pow(2, 10));", "exp": "Using built-in Math.pow for precision and performance.", "time": "O(1)", "space": "O(1)"},
            {"title": "Sum of Array/List", "code": "const sum = [1, 2, 3].reduce((a, b) => a + b, 0);\nconsole.log(sum);", "exp": "Using reduce() to aggregate values in a clean functional style.", "time": "O(n)", "space": "O(1)"},
            {"title": "Max Element", "code": "console.log(Math.max(...[10, 5, 20]));", "exp": "Spread operator combined with Math.max to find the peak value.", "time": "O(n)", "space": "O(n)"},
            {"title": "Sort", "code": "console.log([5, 2, 9].sort((a, b) => a - b));", "exp": "Numerical sort using a comparator function (required in JS).", "time": "O(n log n)", "space": "O(n)"},
            {"title": "Remove Duplicates", "code": "console.log([...new Set([1, 2, 2, 3])]);", "exp": "Using the Set object to filter out duplicates in one line.", "time": "O(n)", "space": "O(n)"},
            {"title": "Factorial (iterative)", "code": "function factIter(n) {\n  let r = 1;\n  for(let i=2; i<=n; i++) r *= i;\n  return r;\n}\nconsole.log(factIter(5));", "exp": "Loop-based factorial to avoid call stack limits.", "time": "O(n)", "space": "O(1)"},
            {"title": "Armstrong Number", "code": "function isArm(n) {\n  let s = n.toString();\n  let p = s.length;\n  let sum = [...s].reduce((a, d) => a + Math.pow(parseInt(d), p), 0);\n  return sum === n;\n}\nconsole.log(isArm(153));", "exp": "Calculates if sum of digits^power equals number.", "time": "O(d)", "space": "O(d)"},
            {"title": "Palindrome", "code": "function isPal(s) {\n  let rev = s.split('').reverse().join('');\n  return s === rev;\n}\nconsole.log(isPal('racecar'));", "exp": "String reversal and comparison for palindrome check.", "time": "O(n)", "space": "O(n)"},
            {"title": "Largest of 3 numbers", "code": "console.log(Math.max(10, 25, 15));", "exp": "Native Math utility for finding the largest value.", "time": "O(1)", "space": "O(1)"},
            {"title": "Even/Odd Count", "code": "let arr = [1, 2, 3, 4, 5];\nlet e = arr.filter(x => x % 2 === 0).length;\nconsole.log(`Even: ${e}, Odd: ${arr.length - e}`);", "exp": "Functional filtering to count even and odd numbers.", "time": "O(n)", "space": "O(n)"}
        ]
    },
    "java": {
        "name": "Java",
        "ext": ".java",
        "intro": "Java's strong typing and OOP principles are essential for scalable apps. Here are 17 problems implemented in modern Java style.",
        "problems": [
            {"title": "Swap Variables", "code": "int a = 5, b = 10;\na = a ^ b;\nb = a ^ b;\na = a ^ b;\nSystem.out.println(\"a: \" + a + \", b: \" + b);", "exp": "Using XOR bitwise swap to save memory (no temporary variable).", "time": "O(1)", "space": "O(1)"},
            {"title": "Factorial (recursive)", "code": "public class Main {\n  static int fact(int n) { return n<=1 ? 1 : n * fact(n-1); }\n  public static void main(String[] args) { System.out.println(fact(5)); }\n}", "exp": "Static recursive method for factorial calculation.", "time": "O(n)", "space": "O(n)"},
            {"title": "Fibonacci", "code": "public class Main {\n  static int fib(int n) { return n<2 ? n : fib(n-1)+fib(n-2); }\n  public static void main(String[] args) { System.out.println(fib(7)); }\n}", "exp": "Classic recursive Fibonacci implementation.", "time": "O(2^n)", "space": "O(n)"},
            {"title": "Prime Check", "code": "public class Main {\n  public static void main(String[] args) {\n    int n = 17; boolean p = true;\n    for(int i=2; i<=Math.sqrt(n); i++) if(n%i==0) p=false;\n    System.out.println(p);\n  }\n}", "exp": "Looping through divisors up to the square root for efficiency.", "time": "O(sqrt(n))", "space": "O(1)"},
            {"title": "Reverse Array/List", "code": "import java.util.*;\npublic class Main {\n  public static void main(String[] args) {\n    Integer[] arr = {1, 2, 3}; Collections.reverse(Arrays.asList(arr));\n    System.out.println(Arrays.toString(arr));\n  }\n}", "exp": "Using Collections.reverse() to flip the array logic.", "time": "O(n)", "space": "O(1)"},
            {"title": "Binary Search", "code": "import java.util.*;\npublic class Main {\n  public static void main(String[] args) {\n    int[] arr = {1, 2, 3, 4, 5};\n    System.out.println(Arrays.binarySearch(arr, 4));\n  }\n}", "exp": "Leveraging Java's built-in Arrays.binarySearch utility.", "time": "O(log n)", "space": "O(1)"},
            {"title": "GCD", "code": "public class Main {\n  static int gcd(int a, int b) { return b==0 ? a : gcd(b, a%b); }\n  public static void main(String[] args) { System.out.println(gcd(48, 18)); }\n}", "exp": "Euclidean GCD algorithm in Java.", "time": "O(log(min(a,b)))", "space": "O(log n)"},
            {"title": "Power Function", "code": "public class Main {\n  public static void main(String[] args) {\n    System.out.println(Math.pow(2, 10));\n  }\n}", "exp": "Built-in Math.pow for double precision results.", "time": "O(1)", "space": "O(1)"},
            {"title": "Sum of Array/List", "code": "import java.util.stream.*;\npublic class Main {\n  public static void main(String[] args) {\n    int[] arr = {1, 2, 3};\n    System.out.println(IntStream.of(arr).sum());\n  }\n}", "exp": "Using Java Streams for elegant data aggregation.", "time": "O(n)", "space": "O(1)"},
            {"title": "Max Element", "code": "import java.util.stream.*;\npublic class Main {\n  public static void main(String[] args) {\n    int[] arr = {10, 5, 20};\n    System.out.println(IntStream.of(arr).max().getAsInt());\n  }\n}", "exp": "Stream API used to find the maximum value.", "time": "O(n)", "space": "O(1)"},
            {"title": "Sort", "code": "import java.util.*;\npublic class Main {\n  public static void main(String[] args) {\n    int[] arr = {5, 2, 9}; Arrays.sort(arr);\n    System.out.println(Arrays.toString(arr));\n  }\n}", "exp": "Arrays.sort() uses Dual-Pivot Quicksort for primitives.", "time": "O(n log n)", "space": "O(log n)"},
            {"title": "Remove Duplicates", "code": "import java.util.*;\npublic class Main {\n  public static void main(String[] args) {\n    List<Integer> list = Arrays.asList(1, 2, 2, 3);\n    System.out.println(new HashSet<>(list));\n  }\n}", "exp": "HashSet implementation to automatically distinct values.", "time": "O(n)", "space": "O(n)"},
            {"title": "Factorial (iterative)", "code": "public class Main {\n  public static void main(String[] args) {\n    long r=1; for(int i=2; i<=5; i++) r*=i;\n    System.out.println(r);\n  }\n}", "exp": "Iterative approach to handle larger factorial without overflow.", "time": "O(n)", "space": "O(1)"},
            {"title": "Armstrong Number", "code": "public class Main {\n  public static void main(String[] args) {\n    int n=153, temp=n, sum=0, p=String.valueOf(n).length();\n    while(temp>0) { sum+=Math.pow(temp%10, p); temp/=10; }\n    System.out.println(sum==n);\n  }\n}", "exp": "Calculates digit powers using a while loop.", "time": "O(d)", "space": "O(1)"},
            {"title": "Palindrome", "code": "public class Main {\n  public static void main(String[] args) {\n    String s=\"racecar\";\n    String rev=new StringBuilder(s).reverse().toString();\n    System.out.println(s.equals(rev));\n  }\n}", "exp": "StringBuilder reversal for string comparison.", "time": "O(n)", "space": "O(n)"},
            {"title": "Largest of 3 numbers", "code": "public class Main {\n  public static void main(String[] args) {\n    System.out.println(Math.max(10, Math.max(25, 15)));\n  }\n}", "exp": "Nested Math.max calls for clean logic.", "time": "O(1)", "space": "O(1)"},
            {"title": "Even/Odd Count", "code": "public class Main {\n  public static void main(String[] args) {\n    int[] arr = {1, 2, 3, 4, 5};\n    long e = Arrays.stream(arr).filter(x -> x%2==0).count();\n    System.out.println(\"Even: \"+e+\", Odd: \"+(arr.length-e));\n  }\n}", "exp": "Stream counting for even and odd distribution.", "time": "O(n)", "space": "O(1)"}
        ]
    },
    "cpp": {
        "name": "C++",
        "ext": ".cpp",
        "intro": "C++ offers manual memory control and blazing speed. These 17 problems demonstrate modern C++ STL and optimized logic.",
        "problems": [
            {"title": "Swap Variables", "code": "#include <iostream>\n#include <algorithm>\nint main() {\n  int a=5, b=10;\n  std::swap(a, b);\n  std::cout << \"a: \" << a << \", b: \" << b;\n  return 0;\n}", "exp": "Using std::swap for efficient variable exchange.", "time": "O(1)", "space": "O(1)"},
            {"title": "Factorial (recursive)", "code": "long long fact(int n) { return n<=1 ? 1 : n * fact(n-1); }", "exp": "Recursive implementation with long long for overflow safety.", "time": "O(n)", "space": "O(n)"},
            {"title": "Fibonacci", "code": "int fib(int n) { return n < 2 ? n : fib(n-1) + fib(n-2); }", "exp": "Standard recursive Fibonacci.", "time": "O(2^n)", "space": "O(n)"},
            {"title": "Prime Check", "code": "bool isPrime(int n) {\n  if(n < 2) return false;\n  for(int i=2; i*i<=n; i++) if(n%i==0) return false;\n  return true;\n}", "exp": "Looping up to sqrt(n) for fast prime detection.", "time": "O(sqrt(n))", "space": "O(1)"},
            {"title": "Reverse Array/List", "code": "#include <algorithm>\n#include <vector>\nvoid rev(std::vector<int>& v) { std::reverse(v.begin(), v.end()); }", "exp": "STL reverse utility for vectors.", "time": "O(n)", "space": "O(1)"},
            {"title": "Binary Search", "code": "#include <algorithm>\nbool check(int arr[], int n, int x) {\n  return std::binary_search(arr, arr+n, x);\n}", "exp": "Using STL binary_search on sorted range.", "time": "O(log n)", "space": "O(1)"},
            {"title": "GCD", "code": "#include <numeric>\nint main() {\n  std::cout << std::gcd(48, 18);\n}", "exp": "Using std::gcd available in <numeric> (C++17+).", "time": "O(log(min(a,b)))", "space": "O(1)"},
            {"title": "Power Function", "code": "#include <cmath>\nint main() { std::cout << std::pow(2, 10); }", "exp": "Standard library pow function.", "time": "O(1)", "space": "O(1)"},
            {"title": "Sum of Array/List", "code": "#include <numeric>\n#include <vector>\nint sum(std::vector<int>& v) {\n  return std::accumulate(v.begin(), v.end(), 0);\n}", "exp": "std::accumulate for summing numeric sequences.", "time": "O(n)", "space": "O(1)"},
            {"title": "Max Element", "code": "#include <algorithm>\n#include <vector>\nint getMax(std::vector<int>& v) {\n  return *std::max_element(v.begin(), v.end());\n}", "exp": "std::max_element returns iterator to the peak value.", "time": "O(n)", "space": "O(1)"},
            {"title": "Sort", "code": "#include <algorithm>\n#include <vector>\nvoid Sort(std::vector<int>& v) { std::sort(v.begin(), v.end()); }", "exp": "std::sort uses Introsort (Quick+Heap+Insertion sort).", "time": "O(n log n)", "space": "O(log n)"},
            {"title": "Remove Duplicates", "code": "#include <set>\n#include <vector>\nstd::set<int> uniq(std::vector<int>& v) {\n  return std::set<int>(v.begin(), v.end());\n}", "exp": "Using std::set to filter unique elements.", "time": "O(n log n)", "space": "O(n)"},
            {"title": "Factorial (iterative)", "code": "long long fact(int n) {\n  long long r=1; for(int i=2;i<=n;i++) r*=i; return r;\n}", "exp": "Iterative factorial with long long support.", "time": "O(n)", "space": "O(1)"},
            {"title": "Armstrong Number", "code": "bool isArm(int n) {\n  int s=0, t=n, d=std::to_string(n).length();\n  while(t) { s += std::pow(t%10, d); t/=10; }\n  return s==n;\n}", "exp": "Loop-based power aggregation of digits.", "time": "O(d)", "space": "O(1)"},
            {"title": "Palindrome", "code": "bool isPal(std::string s) {\n  std::string t=s; std::reverse(t.begin(), t.end());\n  return s==t;\n}", "exp": "String reversal comparison for palindromes.", "time": "O(n)", "space": "O(n)"},
            {"title": "Largest of 3 numbers", "code": "std::max({a, b, c})", "exp": "Initializer list with std::max for multi-variate peak finding.", "time": "O(1)", "space": "O(1)"},
            {"title": "Even/Odd Count", "code": "int e=std::count_if(v.begin(), v.end(), [](int x){return x%2==0;});", "exp": "std::count_if for condition-based tallying.", "time": "O(n)", "space": "O(1)"}
        ]
    },
    "c": {
        "name": "C",
        "ext": ".c",
        "intro": "The foundation of modern computing. C requires precise control. Here are the 17 problems in standard C (C99+).",
        "problems": [
            {"title": "Swap Variables", "code": "#include <stdio.h>\nint main() {\n  int a=5, b=10; a=a+b; b=a-b; a=a-b;\n  printf(\"a: %d, b: %d\", a, b);\n}", "exp": "Arithmetical swap without temporary variable.", "time": "O(1)", "space": "O(1)"},
            {"title": "Factorial (recursive)", "code": "long fact(int n) { return n<=1 ? 1 : n * fact(n-1); }", "exp": "Standard recursive implementation.", "time": "O(n)", "space": "O(n)"},
            {"title": "Fibonacci", "code": "int fib(int n) { return n < 2 ? n : fib(n-1) + fib(n-2); }", "exp": "Recursive Fibonacci.", "time": "O(2^n)", "space": "O(n)"},
            {"title": "Prime Check", "code": "int isPrime(int n) {\n  if(n<2) return 0;\n  for(int i=2; i*i<=n; i++) if(n%i==0) return 0;\n  return 1;\n}", "exp": "Divide and conquer primality check.", "time": "O(sqrt(n))", "space": "O(1)"},
            {"title": "Reverse Array/List", "code": "void rev(int arr[], int n) {\n  for(int i=0; i<n/2; i++) {\n    int t=arr[i]; arr[i]=arr[n-1-i]; arr[n-1-i]=t;\n  }\n}", "exp": "In-place reversal using two pointers logic.", "time": "O(n)", "space": "O(1)"},
            {"title": "Binary Search", "code": "int bs(int arr[], int n, int x) {\n  int l=0, r=n-1;\n  while(l<=r) {\n    int m=l+(r-l)/2;\n    if(arr[m]==x) return m;\n    if(arr[m]<x) l=m+1; else r=m-1;\n  }\n  return -1;\n}", "exp": "Iterative binary search logic.", "time": "O(log n)", "space": "O(1)"},
            {"title": "GCD", "code": "int gcd(int a, int b) { return b==0 ? a : gcd(b, a%b); }", "exp": "Euclidean algorithm via recursion.", "time": "O(log n)", "space": "O(log n)"},
            {"title": "Power Function", "code": "#include <math.h>\n// Use pow(b, e)", "exp": "Math library utility.", "time": "O(1)", "space": "O(1)"},
            {"title": "Sum of Array/List", "code": "int sum(int arr[], int n) {\n  int s=0; for(int i=0;i<n;i++) s+=arr[i]; return s;\n}", "exp": "Manual traversal for summation.", "time": "O(n)", "space": "O(1)"},
            {"title": "Max Element", "code": "int max(int arr[], int n) {\n  int m=arr[0]; for(int i=1;i<n;i++) if(arr[i]>m) m=arr[i]; return m;\n}", "exp": "Standard linear scan for max value.", "time": "O(n)", "space": "O(1)"},
            {"title": "Sort", "code": "// Qsort from stdlib.h", "exp": "Using standard library qsort.", "time": "O(n log n)", "space": "O(log n)"},
            {"title": "Remove Duplicates", "code": "// Requires manual sorting and pointer logic", "exp": "Usually handled by sorting and sliding duplicate elements.", "time": "O(n log n)", "space": "O(1)"},
            {"title": "Factorial (iterative)", "code": "long fact(int n) { \n  long r=1; for(int i=2;i<=n;i++) r*=i; return r;\n}", "exp": "Loop-based factorial.", "time": "O(n)", "space": "O(1)"},
            {"title": "Armstrong Number", "code": "// Digit extraction loop + pow()", "exp": "Standard digit-by-digit extraction and power sum.", "time": "O(d)", "space": "O(1)"},
            {"title": "Palindrome", "code": "// Pointer comparison from start and end", "exp": "Two-pointer check for symmetric strings.", "time": "O(n)", "space": "O(1)"},
            {"title": "Largest of 3 numbers", "code": "int m = (a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c);", "exp": "Nested ternary operators for maximum finding.", "time": "O(1)", "space": "O(1)"},
            {"title": "Even/Odd Count", "code": "int e=0; for(int i=0;i<n;i++) if(arr[i]%2==0) e++;", "exp": "Simple counter loop.", "time": "O(n)", "space": "O(1)"}
        ]
    },
    "csharp": {
        "name": "C#",
        "ext": ".cs",
        "intro": "C# powering enterprise and games. These 17 problems utilize modern C# 12 and .NET 8 features for efficient coding.",
        "problems": [
            {"title": "Swap Variables", "code": "int a = 5, b = 10;\n(a, b) = (b, a);\nConsole.WriteLine($\"a: {a}, b: {b}\");", "exp": "Tuple-based swapping, supported in modern C#.", "time": "O(1)", "space": "O(1)"},
            {"title": "Factorial (recursive)", "code": "long Fact(int n) => n <= 1 ? 1 : n * Fact(n - 1);\nConsole.WriteLine(Fact(5));", "exp": "Expression-bodied recursive member.", "time": "O(n)", "space": "O(n)"},
            {"title": "Fibonacci", "code": "int Fib(int n) => n < 2 ? n : Fib(n-1) + Fib(n-2);", "exp": "Standard recursive Fibonacci relation.", "time": "O(2^n)", "space": "O(n)"},
            {"title": "Prime Check", "code": "bool IsPrime(int n) {\n  if(n<2) return false;\n  for(int i=2; i*i<=n; i++) if(n%i==0) return false;\n  return true;\n}", "exp": "Square root complexity primality testing.", "time": "O(sqrt(n))", "space": "O(1)"},
            {"title": "Reverse Array/List", "code": "int[] arr = {1, 2, 3};\nArray.Reverse(arr);", "exp": "Using the built-in static Array utility.", "time": "O(n)", "space": "O(1)"},
            {"title": "Binary Search", "code": "int[] sorted = {1, 2, 3, 4, 5};\nConsole.WriteLine(Array.BinarySearch(sorted, 4));", "exp": "Standard library binary search on arrays.", "time": "O(log n)", "space": "O(1)"},
            {"title": "GCD", "code": "int Gcd(int a, int b) => b == 0 ? a : Gcd(b, a % b);", "exp": "Recursive implementation of Euclidean logic.", "time": "O(log n)", "space": "O(log n)"},
            {"title": "Power Function", "code": "Console.WriteLine(Math.Pow(2, 10));", "exp": "Standard Math library power function.", "time": "O(1)", "space": "O(1)"},
            {"title": "Sum of Array/List", "code": "using System.Linq;\nint[] arr = {1, 2, 3};\nConsole.WriteLine(arr.Sum());", "exp": "Using LINQ Sum() extension method.", "time": "O(n)", "space": "O(1)"},
            {"title": "Max Element", "code": "using System.Linq;\nint[] arr = {10, 5, 20};\nConsole.WriteLine(arr.Max());", "exp": "Using LINQ Max() for aggregation.", "time": "O(n)", "space": "O(1)"},
            {"title": "Sort", "code": "int[] arr = {5, 2, 9}; Array.Sort(arr);", "exp": "In-place array sort utility.", "time": "O(n log n)", "space": "O(log n)"},
            {"title": "Remove Duplicates", "code": "using System.Linq;\nint[] arr = {1, 2, 2, 3};\nvar uniq = arr.Distinct().ToArray();", "exp": "LINQ Distinct() removes duplicates lazily.", "time": "O(n)", "space": "O(n)"},
            {"title": "Factorial (iterative)", "code": "long r=1; for(int i=2; i<=5; i++) r*=i;", "exp": "For-loop based factorial calculation.", "time": "O(n)", "space": "O(1)"},
            {"title": "Armstrong Number", "code": "int n=153, s=0, t=n, p=n.ToString().Length;\nwhile(t>0) { s+=(int)Math.Pow(t%10, p); t/=10; }", "exp": "Calculates sum of digits powered by length.", "time": "O(d)", "space": "O(1)"},
            {"title": "Palindrome", "code": "string s=\"racecar\";\nbool isPal = s.SequenceEqual(s.Reverse());", "exp": "Using LINQ SequenceEqual with Reverse().", "time": "O(n)", "space": "O(n)"},
            {"title": "Largest of 3 numbers", "code": "Math.Max(a, Math.Max(b, c))", "exp": "Nested Math.Max for triple comparison.", "time": "O(1)", "space": "O(1)"},
            {"title": "Even/Odd Count", "code": "using System.Linq;\nint e = arr.Count(x => x % 2 == 0);", "exp": "LINQ Count with predicate logic.", "time": "O(n)", "space": "O(1)"}
        ]
    },
    "typescript": {
        "name": "TypeScript",
        "ext": ".ts",
        "intro": "TypeScript brings type safety to the JS world. These solutions emphasize clean types and modern syntax.",
        "problems": [
            {"title": "Swap Variables", "code": "let a: number = 5, b: number = 10;\n[a, b] = [b, a];", "exp": "Type-safe destructuring swap.", "time": "O(1)", "space": "O(1)"},
            {"title": "Factorial (recursive)", "code": "const fact = (n: number): number => n <= 1 ? 1 : n * fact(n-1);", "exp": "Typed recursive arrow function.", "time": "O(n)", "space": "O(n)"},
            {"title": "Fibonacci", "code": "const fib = (n: number): number => n < 2 ? n : fib(n-1) + fib(n-2);", "exp": "Standard recursive model with type annotations.", "time": "O(2^n)", "space": "O(n)"},
            {"title": "Prime Check", "code": "function isPrime(n: number): boolean {\n  if (n < 2) return false;\n  for(let i=2; i*i<=n; i++) if(n%i===0) return false;\n  return true;\n}", "exp": "Mathematical prime check with boolean return type.", "time": "O(sqrt(n))", "space": "O(1)"},
            {"title": "Reverse Array/List", "code": "const arr: number[] = [1, 2, 3];\narr.reverse();", "exp": "In-place reversal on typed arrays.", "time": "O(n)", "space": "O(1)"},
            {"title": "Binary Search", "code": "function bs(arr: number[], x: number): number {\n  let l=0, r=arr.length-1;\n  while(l<=r) {\n    let m=Math.floor((l+r)/2);\n    if(arr[m]===x) return m;\n    if(arr[m]<x) l=m+1; else r=m-1;\n  }\n  return -1;\n}", "exp": "Classic binary search with explicit parameter types.", "time": "O(log n)", "space": "O(1)"},
            {"title": "GCD", "code": "const gcd = (a: number, b: number): number => b === 0 ? a : gcd(b, a % b);", "exp": "Recursive Euclidean logic with type safety.", "time": "O(log n)", "space": "O(log n)"},
            {"title": "Power Function", "code": "Math.pow(2, 10);", "exp": "Standard library call.", "time": "O(1)", "space": "O(1)"},
            {"title": "Sum of Array/List", "code": "const sum = [1, 2, 3].reduce((a, b) => a + b, 0);", "exp": "Functional aggregation with reduce.", "time": "O(n)", "space": "O(1)"},
            {"title": "Max Element", "code": "Math.max(...[10, 5, 20]);", "exp": "Spread syntax for finding Maximum.", "time": "O(n)", "space": "O(n)"},
            {"title": "Sort", "code": "[5, 2, 9].sort((a, b) => a - b);", "exp": "Numerical comparator sort.", "time": "O(n log n)", "space": "O(n)"},
            {"title": "Remove Duplicates", "code": "[...new Set([1, 2, 2, 3])];", "exp": "Set-based unique element extraction.", "time": "O(n)", "space": "O(n)"},
            {"title": "Factorial (iterative)", "code": "let r=1; for(let i=2; i<=5; i++) r*=i;", "exp": "Loop-based factorial.", "time": "O(n)", "space": "O(1)"},
            {"title": "Armstrong Number", "code": "// Conversion to string and reduce logic", "exp": "Checking digit power sums.", "time": "O(d)", "space": "O(d)"},
            {"title": "Palindrome", "code": "s.split('').reverse().join('') === s;", "exp": "Reversal comparison.", "time": "O(n)", "space": "O(n)"},
            {"title": "Largest of 3 numbers", "code": "Math.max(10, 25, 15);", "exp": "Built-in max utility.", "time": "O(1)", "space": "O(1)"},
            {"title": "Even/Odd Count", "code": "arr.filter(x => x % 2 === 0).length;", "exp": "Filter-based even counting.", "time": "O(n)", "space": "O(n)"}
        ]
    },
    "go": {
        "name": "Go",
        "ext": ".go",
        "intro": "Go is built for concurrency and simplicity. These solutions follow 'idiomatic Go' patterns.",
        "problems": [
            {"title": "Swap Variables", "code": "a, b := 5, 10\na, b = b, a", "exp": "Idiomatic multiple assignment swap.", "time": "O(1)", "space": "O(1)"},
            {"title": "Factorial (recursive)", "code": "func fact(n int) int {\n  if n <= 1 { return 1 }\n  return n * fact(n-1)\n}", "exp": "Recursive factorial function.", "time": "O(n)", "space": "O(n)"},
            {"title": "Fibonacci", "code": "func fib(n int) int {\n  if n < 2 { return n }\n  return fib(n-1) + fib(n-2)\n}", "exp": "Recursive Fibonacci implementation.", "time": "O(2^n)", "space": "O(n)"},
            {"title": "Prime Check", "code": "func isPrime(n int) bool {\n  if n < 2 { return false }\n  for i := 2; i*i <= n; i++ {\n    if n%i == 0 { return false }\n  }\n  return true\n}", "exp": "Optimized prime test in Go.", "time": "O(sqrt(n))", "space": "O(1)"},
            {"title": "Reverse Array/List", "code": "for i, j := 0, len(a)-1; i < j; i, j = i+1, j-1 {\n  a[i], a[j] = a[j], a[i]\n}", "exp": "Standard swap-based in-place reversal.", "time": "O(n)", "space": "O(1)"},
            {"title": "Binary Search", "code": "import \"sort\"\ni := sort.SearchInts([]int{1, 2, 3, 4, 5}, 4)", "exp": "Using Go's 'sort' package functionality.", "time": "O(log n)", "space": "O(1)"},
            {"title": "GCD", "code": "func gcd(a, b int) int {\n  for b != 0 { a, b = b, a%b }\n  return a\n}", "exp": "Iterative Euclidean algorithm.", "time": "O(log n)", "space": "O(1)"},
            {"title": "Power Function", "code": "import \"math\"\nmath.Pow(2, 10)", "exp": "Standard library power.", "time": "O(1)", "space": "O(1)"},
            {"title": "Sum of Array/List", "code": "s := 0; for _, v := range arr { s += v }", "exp": "Range-based iteration sum.", "time": "O(n)", "space": "O(1)"},
            {"title": "Max Element", "code": "m := arr[0]; for _, v := range arr { if v > m { m = v } }", "exp": "Manual traversal for Max.", "time": "O(n)", "space": "O(1)"},
            {"title": "Sort", "code": "import \"sort\"\nsort.Ints(arr)", "exp": "In-place sorting using sort package.", "time": "O(n log n)", "space": "O(log n)"},
            {"title": "Remove Duplicates", "code": "// Requires manual map or sort + filter", "exp": "Using a map to Track uniqueness.", "time": "O(n)", "space": "O(n)"},
            {"title": "Factorial (iterative)", "code": "r := 1; for i := 2; i <= n; i++ { r *= i }", "exp": "Loop-based factorial.", "time": "O(n)", "space": "O(1)"},
            {"title": "Armstrong Number", "code": "// Digit loop with math.Pow", "exp": "Standard Armstrong check logic.", "time": "O(d)", "space": "O(1)"},
            {"title": "Palindrome", "code": "// String symmetry check loop", "exp": "Manual string index comparison.", "time": "O(n)", "space": "O(1)"},
            {"title": "Largest of 3 numbers", "code": "// Nested if/else for max", "exp": "Comparison logic.", "time": "O(1)", "space": "O(1)"},
            {"title": "Even/Odd Count", "code": "e := 0; for _, v := range arr { if v%2 == 0 { e++ } }", "exp": "Iterative counter.", "time": "O(n)", "space": "O(1)"}
        ]
    },
    "rust": {
        "name": "Rust",
        "ext": ".rs",
        "intro": "Rust focuses on safety and performance. These 17 problems showcase zero-cost abstractions and safe memory patterns.",
        "problems": [
            {"title": "Swap Variables", "code": "let mut a = 5; let mut b = 10;\nstd::mem::swap(&mut a, &mut b);", "exp": "Safe memory swap using standard library primitives.", "time": "O(1)", "space": "O(1)"},
            {"title": "Factorial (recursive)", "code": "fn fact(n: u64) -> u64 {\n  if n <= 1 { 1 } else { n * fact(n-1) }\n}", "exp": "Recursive factorial with typed returns.", "time": "O(n)", "space": "O(n)"},
            {"title": "Fibonacci", "code": "fn fib(n: u32) -> u32 {\n  if n < 2 { n } else { fib(n-1) + fib(n-2) }\n}", "exp": "Recursive Fibonacci implementation.", "time": "O(2^n)", "space": "O(n)"},
            {"title": "Prime Check", "code": "fn is_prime(n: u64) -> bool {\n  if n < 2 { return false }\n  for i in 2..=((n as f64).sqrt() as u64) {\n    if n % i == 0 { return false }\n  }\n  true\n}", "exp": "Range-based prime test.", "time": "O(sqrt(n))", "space": "O(1)"},
            {"title": "Reverse Array/List", "code": "let mut v = vec![1, 2, 3]; v.reverse();", "exp": "In-place vector reversal.", "time": "O(n)", "space": "O(1)"},
            {"title": "Binary Search", "code": "let v = vec![1, 2, 3, 4, 5];\nv.binary_search(&4);", "exp": "Standard library binary search on slices.", "time": "O(log n)", "space": "O(1)"},
            {"title": "GCD", "code": "fn gcd(mut a: u64, mut b: u64) -> u64 {\n  while b != 0 { a %= b; std::mem::swap(&mut a, &mut b); } a\n}", "exp": "Efficient iterative GCD.", "time": "O(log n)", "space": "O(1)"},
            {"title": "Power Function", "code": "2u32.pow(10);", "exp": "Native integer power function.", "time": "O(log n)", "space": "O(1)"},
            {"title": "Sum of Array/List", "code": "let s: i32 = vec![1, 2, 3].iter().sum();", "exp": "Iterator-based summation.", "time": "O(n)", "space": "O(1)"},
            {"title": "Max Element", "code": "let m = vec![10, 5, 20].iter().max();", "exp": "Safe iterator max (returns Option).", "time": "O(n)", "space": "O(1)"},
            {"title": "Sort", "code": "let mut v = vec![5, 2, 9]; v.sort();", "exp": "In-place sorting (stable).", "time": "O(n log n)", "space": "O(log n)"},
            {"title": "Remove Duplicates", "code": "v.sort(); v.dedup();", "exp": "Sort followed by dedup for efficient removal.", "time": "O(n log n)", "space": "O(1) after sort"},
            {"title": "Factorial (iterative)", "code": "(1..=n).product()", "exp": "Elegant range product calculation.", "time": "O(n)", "space": "O(1)"},
            {"title": "Armstrong Number", "code": "// Digit extraction loop", "exp": "Manual digit checking.", "time": "O(d)", "space": "O(1)"},
            {"title": "Palindrome", "code": "s.chars().rev().eq(s.chars())", "exp": "Efficient iterator equality test.", "time": "O(n)", "space": "O(1)"},
            {"title": "Largest of 3 numbers", "code": "a.max(b).max(c)", "exp": "Method chaining for maximum.", "time": "O(1)", "space": "O(1)"},
            {"title": "Even/Odd Count", "code": "v.iter().filter(|&&x| x % 2 == 0).count();", "exp": "Iterator filtering.", "time": "O(n)", "space": "O(1)"}
        ]
    },

    "ruby": {
        "name": "Ruby",
        "ext": ".rb",
        "intro": "Ruby is a programmer's best friend. These solutions are concise, expressive, and purely object-oriented.",
        "problems": [
            {"title": "Swap Variables", "code": "a, b = 5, 10\na, b = b, a", "exp": "Concise parallel assignment swap.", "time": "O(1)", "space": "O(1)"},
            {"title": "Factorial (recursive)", "code": "def fact(n) n <= 1 ? 1 : n * fact(n-1) end", "exp": "Simple recursive method.", "time": "O(n)", "space": "O(n)"},
            {"title": "Fibonacci", "code": "def fib(n) n < 2 ? n : fib(n-1) + fib(n-2) end", "exp": "Mathematical recursion.", "time": "O(2^n)", "space": "O(n)"},
            {"title": "Prime Check", "code": "require 'prime'\n17.prime?", "exp": "Using Ruby's built-in Prime library.", "time": "O(sqrt(n))", "space": "O(1)"},
            {"title": "Reverse Array/List", "code": "[1, 2, 3].reverse", "exp": "Standard array reversal.", "time": "O(n)", "space": "O(n)"},
            {"title": "Binary Search", "code": "[1, 2, 3, 4, 5].bsearch { |x| 4 <=> x }", "exp": "Native binary search with block logic.", "time": "O(log n)", "space": "O(1)"},
            {"title": "GCD", "code": "48.gcd(18)", "exp": "Ruby's integer GCD utility.", "time": "O(log n)", "space": "O(1)"},
            {"title": "Power Function", "code": "2 ** 10", "exp": "Exponentiation operator.", "time": "O(1)", "space": "O(1)"},
            {"title": "Sum of Array/List", "code": "[1, 2, 3].sum", "exp": "Native sum method.", "time": "O(n)", "space": "O(1)"},
            {"title": "Max Element", "code": "[10, 5, 20].max", "exp": "Array maximum finder.", "time": "O(n)", "space": "O(1)"},
            {"title": "Sort", "code": "[5, 2, 9].sort", "exp": "Quick and stable sort.", "time": "O(n log n)", "space": "O(n)"},
            {"title": "Remove Duplicates", "code": "[1, 2, 2, 3].uniq", "exp": "Expressive uniq method.", "time": "O(n)", "space": "O(n)"},
            {"title": "Factorial (iterative)", "code": "(1..5).inject(1, :*)", "exp": "Functional range reduction.", "time": "O(n)", "space": "O(1)"},
            {"title": "Armstrong Number", "code": "// Digit loop with ** operator", "exp": "Calculation of digit power sum.", "time": "O(d)", "space": "O(d)"},
            {"title": "Palindrome", "code": "s == s.reverse", "exp": "Inherent string reversal comparison.", "time": "O(n)", "space": "O(n)"},
            {"title": "Largest of 3 numbers", "code": "[a, b, c].max", "exp": "Max call on implicit array.", "time": "O(1)", "space": "O(1)"},
            {"title": "Even/Odd Count", "code": "arr.count(&:even?)", "exp": "Elegant count with symbol-to-proc.", "time": "O(n)", "space": "O(1)"}
        ]
    },
    "php": {
        "name": "PHP",
        "ext": ".php",
        "intro": "PHP powers a massive portion of the web. These 17 problems demonstrate modern PHP 8 attributes and functional patterns.",
        "problems": [
            {"title": "Swap Variables", "code": "[$a, $b] = [$b, $a];\necho \"a: $a, b: $b\";", "exp": "Using list/array destructuring to swap variables concisely.", "time": "O(1)", "space": "O(1)"},
            {"title": "Factorial (recursive)", "code": "function fact($n) { return $n <= 1 ? 1 : $n * fact($n - 1); }", "exp": "Traditional recursive implementation.", "time": "O(n)", "space": "O(n)"},
            {"title": "Fibonacci", "code": "function fib($n) { return $n < 2 ? $n : fib($n-1) + fib($n-2); }", "exp": "Recursive Fibonacci sequence calculation.", "time": "O(2^n)", "space": "O(n)"},
            {"title": "Prime Check", "code": "function isPrime($n) {\n  if ($n < 2) return false;\n  for($i=2; $i*$i<=$n; $i++) if($n%$i==0) return false;\n  return true;\n}", "exp": "Efficient prime test iterating through divisors.", "time": "O(sqrt(n))", "space": "O(1)"},
            {"title": "Reverse Array/List", "code": "$arr = [1, 2, 3];\n$rev = array_reverse($arr);", "exp": "Standard library array_reverse utility.", "time": "O(n)", "space": "O(n)"},
            {"title": "Binary Search", "code": "function bs($arr, $x) {\n  $l = 0; $r = count($arr)-1;\n  while($l <= $r) {\n    $m = floor(($l+$r)/2);\n    if($arr[$m] == $x) return $m;\n    if($arr[$m] < $x) $l = $m+1; else $r = $m-1;\n  }\n  return -1;\n}", "exp": "Iterative search implementation.", "time": "O(log n)", "space": "O(1)"},
            {"title": "GCD", "code": "function gcd($a, $b) { return $b == 0 ? $a : gcd($b, $a % $b); }", "exp": "Euclidean GCD recursive implementation.", "time": "O(log n)", "space": "O(log n)"},
            {"title": "Power Function", "code": "echo pow(2, 10);", "exp": "Internal pow function for exponentiation.", "time": "O(1)", "space": "O(1)"},
            {"title": "Sum of Array/List", "code": "echo array_sum([1, 2, 3]);", "exp": "Aggregation via array_sum.", "time": "O(n)", "space": "O(1)"},
            {"title": "Max Element", "code": "echo max([10, 5, 20]);", "exp": "Standard library max finding utility.", "time": "O(n)", "space": "O(1)"},
            {"title": "Sort", "code": "$arr = [5, 2, 9]; sort($arr);", "exp": "In-place quicksort implementation.", "time": "O(n log n)", "space": "O(log n)"},
            {"title": "Remove Duplicates", "code": "print_r(array_unique([1, 2, 2, 3]));", "exp": "Built-in array_unique for filtering.", "time": "O(n)", "space": "O(n)"},
            {"title": "Factorial (iterative)", "code": "$r = 1; for($i=2;$i<=5;$i++) $r *= $i;", "exp": "Simple loop for factorial.", "time": "O(n)", "space": "O(1)"},
            {"title": "Armstrong Number", "code": "// Extraction loop and pow call", "exp": "Standard Armstrong calculation logic.", "time": "O(d)", "space": "O(1)"},
            {"title": "Palindrome", "code": "$s == strrev($s);", "exp": "String reversal and equality check.", "time": "O(n)", "space": "O(n)"},
            {"title": "Largest of 3 numbers", "code": "max($a, $b, $c);", "exp": "Variadic max function arguments.", "time": "O(1)", "space": "O(1)"},
            {"title": "Even/Odd Count", "code": "count(array_filter($arr, fn($x) => $x % 2 == 0));", "exp": "Filter-based counting.", "time": "O(n)", "space": "O(1)"}
        ]
    },
    "swift": {
        "name": "Swift",
        "ext": ".swift",
        "intro": "Swift is fast, safe, and expressive. These 17 problems use functional Swift patterns and protocol-oriented logic.",
        "problems": [
            {"title": "Swap Variables", "code": "var a = 5, b = 10\n(a, b) = (b, a)", "exp": "Tuple-based swapping in Swift.", "time": "O(1)", "space": "O(1)"},
            {"title": "Factorial (recursive)", "code": "func fact(_ n: Int) -> Int {\n  return n <= 1 ? 1 : n * fact(n - 1)\n}", "exp": "Standard recursive function.", "time": "O(n)", "space": "O(n)"},
            {"title": "Fibonacci", "code": "func fib(_ n: Int) -> Int {\n  return n < 2 ? n : fib(n-1) + fib(n-2)\n}", "exp": "Recursive Fibonacci relation.", "time": "O(2^n)", "space": "O(n)"},
            {"title": "Prime Check", "code": "func isPrime(_ n: Int) -> Bool {\n  if n < 2 { return false }\n  for i in 2..<Int(Double(n).squareRoot())+1 {\n    if n % i == 0 { return false }\n  }\n  return true\n}", "exp": "Efficient square root loop primality check.", "time": "O(sqrt(n))", "space": "O(1)"},
            {"title": "Reverse Array/List", "code": "let arr = [1, 2, 3]\nlet rev = arr.reversed()", "exp": "Using Swift's reversed() sequence wrapper.", "time": "O(n)", "space": "O(n)"},
            {"title": "Binary Search", "code": "// Recursive or iterative implementation", "exp": "Splitting the search space repeatedly.", "time": "O(log n)", "space": "O(1)"},
            {"title": "GCD", "code": "func gcd(_ a: Int, _ b: Int) -> Int {\n  return b == 0 ? a : gcd(b, a % b)\n}", "exp": "Euclidean algorithm via recursion.", "time": "O(log n)", "space": "O(log n)"},
            {"title": "Power Function", "code": "pow(2.0, 10.0)", "exp": "Foundation library power function.", "time": "O(1)", "space": "O(1)"},
            {"title": "Sum of Array/List", "code": "let sum = [1, 2, 3].reduce(0, +)", "exp": "Using reduce with addition operator.", "time": "O(n)", "space": "O(1)"},
            {"title": "Max Element", "code": "let max = [10, 5, 20].max()", "exp": "Optional return from collection peak finder.", "time": "O(n)", "space": "O(1)"},
            {"title": "Sort", "code": "let sorted = [5, 2, 9].sorted()", "exp": "Standard Timsort-based implementation.", "time": "O(n log n)", "space": "O(n)"},
            {"title": "Remove Duplicates", "code": "Array(Set([1, 2, 2, 3]))", "exp": "Using Set to eliminate duplicates.", "time": "O(n)", "space": "O(n)"},
            {"title": "Factorial (iterative)", "code": "let r = (2...5).reduce(1, *)", "exp": "Range reduction for factorial calculation.", "time": "O(n)", "space": "O(1)"},
            {"title": "Armstrong Number", "code": "// Digit loop with pow()", "exp": "Calculation through digit isolation.", "time": "O(d)", "space": "O(1)"},
            {"title": "Palindrome", "code": "String(s.reversed()) == s", "exp": "String reversal and equality logic.", "time": "O(n)", "space": "O(n)"},
            {"title": "Largest of 3 numbers", "code": "max(a, b, c)", "exp": "Inherent max function with variadic args.", "time": "O(1)", "space": "O(1)"},
            {"title": "Even/Odd Count", "code": "arr.filter { $0 % 2 == 0 }.count", "exp": "Closure-based filtering count.", "time": "O(n)", "space": "O(1)"}
        ]
    },
    "dart": {
        "name": "Dart",
        "ext": ".dart",
        "intro": "Dart is optimized for UI development and fast execution. These 17 problems are essential for Flutter and server-side Dart.",
        "problems": [
            {"title": "Swap Variables", "code": "var a = 5, b = 10; var t = a; a = b; b = t;", "exp": "Standard variable swapping with temporary storage.", "time": "O(1)", "space": "O(1)"},
            {"title": "Factorial (recursive)", "code": "int fact(int n) => n <= 1 ? 1 : n * fact(n - 1);", "exp": "Concise arrow function recursion.", "time": "O(n)", "space": "O(n)"},
            {"title": "Fibonacci", "code": "int fib(int n) => n < 2 ? n : fib(n-1) + fib(n-2);", "exp": "Recursive Fibonacci implementation.", "time": "O(2^n)", "space": "O(n)"},
            {"title": "Prime Check", "code": "bool isPrime(int n) {\n  if(n < 2) return false;\n  for(var i=2; i*i<=n; i++) if(n%i==0) return false;\n  return true;\n}", "exp": "Looping divisors to square root.", "time": "O(sqrt(n))", "space": "O(1)"},
            {"title": "Reverse Array/List", "code": "List<int> arr = [1, 2, 3];\nvar rev = arr.reversed.toList();", "exp": "Using Iterable reversed getter.", "time": "O(n)", "space": "O(n)"},
            {"title": "Binary Search", "code": "// Standard iterative implementation", "exp": "Index manipulation for search.", "time": "O(log n)", "space": "O(1)"},
            {"title": "GCD", "code": "int gcd(int a, int b) => b == 0 ? a : gcd(b, a % b);", "exp": "Recursive Euclidean logic.", "time": "O(log n)", "space": "O(log n)"},
            {"title": "Power Function", "code": "import 'dart:math';\npow(2, 10);", "exp": "math library utility.", "time": "O(1)", "space": "O(1)"},
            {"title": "Sum of Array/List", "code": "int sum = [1, 2, 3].reduce((a, b) => a + b);", "exp": "Aggregation via reduce.", "time": "O(n)", "space": "O(1)"},
            {"title": "Max Element", "code": "import 'dart:math';\nvar maxVal = [10, 5, 20].reduce(max);", "exp": "Using reduce with max utility.", "time": "O(n)", "space": "O(1)"},
            {"title": "Sort", "code": "var arr = [5, 2, 9]; arr.sort();", "exp": "In-place quicksort.", "time": "O(n log n)", "space": "O(log n)"},
            {"title": "Remove Duplicates", "code": "[1, 2, 2, 3].toSet().toList();", "exp": "Converting to Set to ensure uniqueness.", "time": "O(n)", "space": "O(n)"},
            {"title": "Factorial (iterative)", "code": "int r=1; for(var i=2; i<=5; i++) r*=i;", "exp": "For-loop factorial.", "time": "O(n)", "space": "O(1)"},
            {"title": "Armstrong Number", "code": "// Digit loop with pow()", "exp": "Standard Armstrong check logic.", "time": "O(d)", "space": "O(1)"},
            {"title": "Palindrome", "code": "s.split('').reversed.join('') == s;", "exp": "String manipulation reversal.", "time": "O(n)", "space": "O(n)"},
            {"title": "Largest of 3 numbers", "code": "max(a, max(b, c));", "exp": "Nested max calls.", "time": "O(1)", "space": "O(1)"},
            {"title": "Even/Odd Count", "code": "arr.where((x) => x % 2 == 0).length;", "exp": "Predicate filtering.", "time": "O(n)", "space": "O(1)"}
        ]
    },
    "scala": {
        "name": "Scala",
        "ext": ".scala",
        "intro": "Scala combines FP and OOP on the JVM. These solutions leverage high-order functions and recursion.",
        "problems": [
            {"title": "Swap Variables", "code": "var (a, b) = (5, 10)\nval (b2, a2) = (a, b)", "exp": "Tuple-based destructuring swap.", "time": "O(1)", "space": "O(1)"},
            {"title": "Factorial (recursive)", "code": "def fact(n: Int): Int = if (n <= 1) 1 else n * fact(n-1)", "exp": "Recursive factorial definition.", "time": "O(n)", "space": "O(n)"},
            {"title": "Fibonacci", "code": "def fib(n: Int): Int = if (n<2) n else fib(n-1) + fib(n-2)", "exp": "Standard recursion.", "time": "O(2^n)", "space": "O(n)"},
            {"title": "Prime Check", "code": "def isPrime(n: Int) = n > 1 && !(2 to math.sqrt(n).toInt).exists(n % _ == 0)", "exp": "FP style prime check using exists.", "time": "O(sqrt(n))", "space": "O(log n)"},
            {"title": "Reverse Array/List", "code": "List(1, 2, 3).reverse", "exp": "Immutable list reversal.", "time": "O(n)", "space": "O(n)"},
            {"title": "Binary Search", "code": "// Recursive or while loop implementation", "exp": "Standard binary split logic.", "time": "O(log n)", "space": "O(1)"},
            {"title": "GCD", "code": "def gcd(a: Int, b: Int): Int = if (b==0) a else gcd(b, a%b)", "exp": "Euclidean algorithm.", "time": "O(log n)", "space": "O(log n)"},
            {"title": "Power Function", "code": "math.pow(2, 10)", "exp": "Math utility call.", "time": "O(1)", "space": "O(1)"},
            {"title": "Sum of Array/List", "code": "List(1, 2, 3).sum", "exp": "Built-in sum aggregation.", "time": "O(n)", "space": "O(1)"},
            {"title": "Max Element", "code": "List(10, 5, 20).max", "exp": "Collection max finder.", "time": "O(n)", "space": "O(1)"},
            {"title": "Sort", "code": "List(5, 2, 9).sorted", "exp": "Stable sort returning new list.", "time": "O(n log n)", "space": "O(n)"},
            {"title": "Remove Duplicates", "code": "List(1, 2, 2, 3).distinct", "exp": "Built-in distinct utility.", "time": "O(n)", "space": "O(n)"},
            {"title": "Factorial (iterative)", "code": "(1 to 5).product", "exp": "Range product calculation.", "time": "O(n)", "space": "O(1)"},
            {"title": "Armstrong Number", "code": "// Digit extraction with map and sum", "exp": "Functional digit analysis.", "time": "O(d)", "space": "O(d)"},
            {"title": "Palindrome", "code": "s == s.reverse", "exp": "Implicit string reversal check.", "time": "O(n)", "space": "O(n)"},
            {"title": "Largest of 3 numbers", "code": "List(a, b, c).max", "exp": "Max finding via collection.", "time": "O(1)", "space": "O(1)"},
            {"title": "Even/Odd Count", "code": "arr.count(_ % 2 == 0)", "exp": "Condition-based counting.", "time": "O(n)", "space": "O(1)"}
        ]
    },
    "sql": {
        "name": "SQL",
        "ext": ".sql",
        "intro": "SQL is for data. These problems translate algorithmic logic into declarative queries.",
        "problems": [
            {"title": "Swap Variables", "code": "UPDATE table SET a = b, b = a;", "exp": "Cross-assignment in modern DB engines.", "time": "O(1)", "space": "O(1)"},
            {"title": "Factorial (recursive)", "code": "WITH RECURSIVE fact(n, v) AS (\n  SELECT 1, 1 UNION ALL\n  SELECT n + 1, (n + 1) * v FROM fact WHERE n < 5\n) SELECT v FROM fact WHERE n = 5;", "exp": "CTE recursive factorial generation.", "time": "O(n)", "space": "O(n)"},
            {"title": "Fibonacci", "code": "WITH RECURSIVE fib(n, a, b) AS (\n  SELECT 1, 0, 1 UNION ALL\n  SELECT n + 1, b, a + b FROM fib WHERE n < 10\n) SELECT a FROM fib;", "exp": "Recursive sequence generation.", "time": "O(n)", "space": "O(n)"},
            {"title": "Prime Check", "code": "SELECT 1 WHERE NOT EXISTS (SELECT 1 FROM numbers WHERE num BETWEEN 2 AND SQRT(17) AND 17 % num = 0);", "exp": "Primality via non-existence of divisors.", "time": "O(sqrt(n))", "space": "O(1)"},
            {"title": "Reverse Array/List", "code": "SELECT val FROM data ORDER BY id DESC;", "exp": "Order-based reversal.", "time": "O(n log n)", "space": "O(log n)"},
            {"title": "Binary Search", "code": "SELECT * FROM data WHERE val = 4; -- Indexes handle the work", "exp": "Implicitly handled by B-Tree indexing.", "time": "O(log n)", "space": "O(log n)"},
            {"title": "GCD", "code": "Manual implementation not standard; usually via functions.", "exp": "Logic involves repeated modulo math.", "time": "O(log n)", "space": "O(1)"},
            {"title": "Power Function", "code": "SELECT POWER(2, 10);", "exp": "Standard mathematical function.", "time": "O(1)", "space": "O(1)"},
            {"title": "Sum of Array/List", "code": "SELECT SUM(col) FROM table;", "exp": "Aggregate SUM function.", "time": "O(n)", "space": "O(1)"},
            {"title": "Max Element", "code": "SELECT MAX(col) FROM table;", "exp": "Aggregate MAX function.", "time": "O(n)", "space": "O(1)"},
            {"title": "Sort", "code": "SELECT * FROM table ORDER BY col ASC;", "exp": "Standard sorting clause.", "time": "O(n log n)", "space": "O(n)"},
            {"title": "Remove Duplicates", "code": "SELECT DISTINCT col FROM table;", "exp": "DISTINCT keyword.", "time": "O(n log n)", "space": "O(n)"},
            {"title": "Factorial (iterative)", "code": "Handled via recursive CTE or loops.", "exp": "Aggregated value generation.", "time": "O(n)", "space": "O(n)"},
            {"title": "Armstrong Number", "code": "// Multi-step digit isolation and math SELECT", "exp": "Calculation through string/math conversion.", "time": "O(d)", "space": "O(1)"},
            {"title": "Palindrome", "code": "SELECT val = REVERSE(val);", "exp": "Built-in reverse comparison.", "time": "O(n)", "space": "O(n)"},
            {"title": "Largest of 3 numbers", "code": "SELECT GREATEST(a, b, c);", "exp": "Multi-value maximum finder.", "time": "O(1)", "space": "O(1)"},
            {"title": "Even/Odd Count", "code": "SELECT SUM(CASE WHEN val % 2 = 0 THEN 1 ELSE 0 END) as even FROM data;", "exp": "Conditional aggregation.", "time": "O(n)", "space": "O(1)"}
        ]
    },
    "r": {
        "name": "R",
        "ext": ".r",
        "intro": "R is for statistical computing. These problems show R's vectorization and data-centric approach.",
        "problems": [
            {"title": "Swap Variables", "code": "a <- 5; b <- 10\nt <- a; a <- b; b <- t", "exp": "Temporary variable swap.", "time": "O(1)", "space": "O(1)"},
            {"title": "Factorial (recursive)", "code": "fact <- function(n) if(n <= 1) 1 else n * fact(n-1)", "exp": "Recursive function definition.", "time": "O(n)", "space": "O(n)"},
            {"title": "Fibonacci", "code": "fib <- function(n) if(n < 2) n else fib(n-1) + fib(n-2)", "exp": "Recursive Fibonacci implementation.", "time": "O(2^n)", "space": "O(n)"},
            {"title": "Prime Check", "code": "is_prime <- function(n) n > 1 && all(n %% 2:sqrt(n) != 0)", "exp": "Vectorized prime check.", "time": "O(sqrt(n))", "space": "O(sqrt(n))"},
            {"title": "Reverse Array/List", "code": "rev(c(1, 2, 3))", "exp": "Internal vector reversal utility.", "time": "O(n)", "space": "O(n)"},
            {"title": "Binary Search", "code": "// Manual implementation in R", "exp": "Index manipulation search.", "time": "O(log n)", "space": "O(1)"},
            {"title": "GCD", "code": "gcd <- function(a, b) if(b == 0) a else gcd(b, a %% b)", "exp": "Recursive Euclidean logic.", "time": "O(log n)", "space": "O(log n)"},
            {"title": "Power Function", "code": "2 ^ 10", "exp": "Exponentiation operator.", "time": "O(1)", "space": "O(1)"},
            {"title": "Sum of Array/List", "code": "sum(c(1, 2, 3))", "exp": "Vectorized sum function.", "time": "O(n)", "space": "O(1)"},
            {"title": "Max Element", "code": "max(c(10, 5, 20))", "exp": "Vector maximum finding.", "time": "O(n)", "space": "O(1)"},
            {"title": "Sort", "code": "sort(c(5, 2, 9))", "exp": "Optimized shell or quick sort.", "time": "O(n log n)", "space": "O(n)"},
            {"title": "Remove Duplicates", "code": "unique(c(1, 2, 2, 3))", "exp": "Vectorized uniqueness utility.", "time": "O(n)", "space": "O(n)"},
            {"title": "Factorial (iterative)", "code": "factorial(5)", "exp": "Built-in gamma-based factorial.", "time": "O(1)", "space": "O(1)"},
            {"title": "Armstrong Number", "code": "// Vectorized digit split and sum", "exp": "Calculation through digit analysis.", "time": "O(d)", "space": "O(d)"},
            {"title": "Palindrome", "code": "s == paste(rev(strsplit(s, '')[[1]]), collapse='')", "exp": "String split and reversal check.", "time": "O(n)", "space": "O(n)"},
            {"title": "Largest of 3 numbers", "code": "max(a, b, c)", "exp": "Variadic max function.", "time": "O(1)", "space": "O(1)"},
            {"title": "Even/Odd Count", "code": "sum(arr %% 2 == 0)", "exp": "Vectorized logical count.", "time": "O(n)", "space": "O(1)"}
        ]
    }
}




# The template for the article
TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>17 Essential {name} Coding Problems (With Solutions) | CodeRunner Pro</title>
    <meta name="description" content="Master {name} with these 17 essential coding problems. Includes full working solutions, detailed explanations, and time/space complexity analysis. Perfect for interview prep.">
    
    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
    <link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png">
    <link rel="icon" type="image/png" sizes="192x192" href="/favicon-192x192.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/favicon-192x192.png">
    <link rel="stylesheet" href="styles.css?v=1.4">
    <script defer src="/_vercel/insights/script.js"></script>
    <style>
        .article-container {{ max-width: 900px; margin: 0 auto; padding: 40px 20px; }}
        .intro-section {{ margin-bottom: 40px; border-bottom: 1px solid var(--border-color); padding-bottom: 20px; }}
        .problem-section {{ margin-bottom: 60px; scroll-margin-top: 100px; }}
        .problem-title {{ color: var(--accent-color); font-size: 1.8rem; margin-bottom: 15px; display: flex; align-items: center; gap: 10px; }}
        .problem-statement {{ font-style: italic; color: var(--text-secondary); margin-bottom: 20px; font-size: 1.1rem; }}
        .code-container {{ background: #0d1117; border-radius: 8px; padding: 20px; margin-bottom: 15px; position: relative; }}
        .code-container pre {{ margin: 0; overflow-x: auto; }}
        .btn-run-live {{ display: inline-flex; align-items: center; gap: 8px; margin-bottom: 15px; text-decoration: none; padding: 8px 16px; border-radius: 6px; font-weight: 600; font-size: 0.9rem; transition: all 0.2s; }}
        .complexity-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; background: rgba(255,255,255,0.05); padding: 15px; border-radius: 8px; margin-top: 20px; }}
        .complexity-item h4 {{ color: var(--text-secondary); margin-bottom: 5px; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; }}
        .complexity-item p {{ font-family: 'JetBrains Mono', monospace; color: var(--accent-color); }}
        .explanation {{ line-height: 1.6; margin: 15px 0; }}
        .sidebar {{ position: sticky; top: 100px; height: fit-content; }}
        .toc-list {{ list-style: none; padding: 0; border-left: 2px solid var(--border-color); padding-left: 15px; }}
        .toc-list li {{ margin-bottom: 10px; }}
        .toc-list a {{ color: var(--text-secondary); text-decoration: none; font-size: 0.9rem; transition: color 0.2s; }}
        .toc-list a:hover {{ color: var(--accent-color); }}
        @media (max-width: 1100px) {{ .toc-container {{ display: none; }} }}
        .main-layout {{ display: grid; grid-template-columns: 1fr 250px; gap: 40px; }}
        @media (max-width: 1100px) {{ .main-layout {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body class="compiler-page">
    <div class="app-container">
        <header class="header">
            <div class="logo">
                <a href="index.html" class="logo-link">
                    <img src="logo.png" alt="CodeRunner Pro" style="width:32px;height:32px;border-radius:6px;">
                </a>
                <a href="index.html" style="text-decoration: none; color: inherit;">
                    <span class="logo-text">CodeRunner<span class="pro">Pro</span></span>
                </a>
            </div>
            <nav class="nav-actions">
                <div class="nav-links">
                    <a href="index.html" class="nav-link">Home</a>
                    <a href="tutorials.html" class="nav-link">Important Functions</a>
                    <a href="examples.html" class="nav-link">Examples</a>
                    <a href="articles.html" class="nav-link">Articles</a>
                    <a href="guides.html" class="nav-link">Guide Book</a>
                    <a href="editor.html" class="nav-link">Editor</a>
                </div>
            </nav>
        </header>

        <div class="article-container">
            <div class="intro-section">
                <h1>17 Essential {name} Coding Problems</h1>
                <p class="tagline">Boost your logic and interview skills with these foundational {name} challenges.</p>
                <div class="explanation">
                    <p>{intro}</p>
                    <p>Whether you're preparing for a technical interview or just starting your journey in {name}, mastering these 17 problems will give you a solid foundation in algorithm design and problem-solving. Each solution includes an interactive "Run Live" button so you can experiment with the code yourself!</p>
                </div>
            </div>

            <div class="main-layout">
                <div class="content">
                    {problems_html}
                </div>
                <div class="toc-container">
                    <div class="sidebar">
                        <h3>In this article</h3>
                        <ul class="toc-list">
                            {toc_html}
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <footer class="footer">
            <div class="footer-grid">
                <div class="footer-column">
                    <h3>Compilers</h3>
                    <ul>
                        <li><a href="python-online-compiler.html">Python Compiler</a></li>
                        <li><a href="javascript-online-compiler.html">JavaScript Compiler</a></li>
                        <li><a href="java-online-compiler.html">Java Compiler</a></li>
                        <li><a href="cpp-online-compiler.html">C++ Compiler</a></li>
                        <li><a href="c-online-compiler.html">C Compiler</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h3>Resources</h3>
                    <ul>
                        <li><a href="editor.html">Online Editor</a></li>
                        <li><a href="guides.html">Programming Guides</a></li>
                        <li><a href="examples.html">Code Examples</a></li>
                        <li><a href="tutorials.html">Important Functions</a></li>
                        <li><a href="articles.html">Problem Solving</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h3>Legal</h3>
                    <ul>
                        <li><a href="privacy.html">Privacy Policy</a></li>
                        <li><a href="terms.html">Terms of Service</a></li>
                        <li><a href="https://www.effectivegatecpm.com/z2g7jdtk?key=412ba1f8e27fcea0bff7d1ea1b59a2bc" target="_blank" style="color: #ffd700; font-weight: bold;">Featured Tools ✨</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024-2025 CodeRunner Pro. All rights reserved.</p>
            </div>
        </footer>
    </div>
</body>
</html>"""

def generate_articles():
    for slug, data in LANG_DATA.items():
        problems_html = ""
        toc_html = ""
        for i, p in enumerate(data["problems"], 1):
            id_str = p['title'].lower().replace(" ", "-").replace("(", "").replace(")", "")
            encoded_code = urllib.parse.quote(p['code'])
            
            toc_html += f'<li><a href="#{id_str}">{i}. {p["title"]}</a></li>'
            
            problems_html += f'''
            <section id="{id_str}" class="problem-section">
                <h2 class="problem-title">
                    <span class="number">{i}.</span> {p["title"]}
                </h2>
                <p class="problem-statement">Problem: Implementation of {p["title"]} algorithm in {data["name"]}.</p>
                
                <a href="editor.html?lang={slug}&code={encoded_code}" class="btn btn-primary btn-run-live">
                    <svg style="width:18px;height:18px" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <polygon points="5 3 19 12 5 21 5 3"></polygon>
                    </svg>
                    Run Live
                </a>

                <div class="code-container">
                    <pre><code class="language-{slug}">{p["code"]}</code></pre>
                </div>

                <div class="explanation">
                    <p>{p["exp"]}</p>
                </div>

                <div class="complexity-grid">
                    <div class="complexity-item">
                        <h4>Time Complexity</h4>
                        <p>{p["time"]}</p>
                    </div>
                    <div class="complexity-item">
                        <h4>Space Complexity</h4>
                        <p>{p["space"]}</p>
                    </div>
                </div>
            </section>
            '''

        filename = f"17-essential-{slug}-coding-problems.html"
        content = TEMPLATE.format(
            name=data["name"],
            intro=data["intro"],
            problems_html=problems_html,
            toc_html=toc_html
        )

        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {filename}")

if __name__ == "__main__":
    generate_articles()
