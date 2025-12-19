// Examples Data - 85 examples (5 per language x 17 languages)
const EXAMPLE_LANGUAGES = [
    { id: 'python', name: 'Python', icon: '🐍' },
    { id: 'javascript', name: 'JavaScript', icon: '🟨' },
    { id: 'java', name: 'Java', icon: '☕' },
    { id: 'cpp', name: 'C++', icon: '⚡' },
    { id: 'c', name: 'C', icon: '⚙️' },
    { id: 'csharp', name: 'C#', icon: '💜' },
    { id: 'typescript', name: 'TypeScript', icon: '🔷' },
    { id: 'go', name: 'Go', icon: '🐹' },
    { id: 'rust', name: 'Rust', icon: '🦀' },
    { id: 'ruby', name: 'Ruby', icon: '💎' },
    { id: 'php', name: 'PHP', icon: '🐘' },
    { id: 'swift', name: 'Swift', icon: '🦅' },
    { id: 'dart', name: 'Dart', icon: '🎯' },
    { id: 'scala', name: 'Scala', icon: '🔴' },
    { id: 'r', name: 'R', icon: '📊' },
    { id: 'sql', name: 'SQL', icon: '🗃️' },
    { id: 'html', name: 'HTML/CSS', icon: '🌐' }
];

const EXAMPLES = {
    python: [
        {
            title: 'Hello World', level: 'beginner', desc: 'Print Hello World', code: `# Python Hello World
print("Hello, World!")
print("Welcome to Python!")`},
        {
            title: 'Add Two Numbers', level: 'beginner', desc: 'Add two numbers', code: `# Add Two Numbers
a, b = 10, 20
print(f"Sum: {a + b}")`},
        {
            title: 'Prime Number', level: 'intermediate', desc: 'Check if prime', code: `# Check Prime Number
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
print(is_prime(17))`},
        {
            title: 'Factorial', level: 'intermediate', desc: 'Calculate factorial', code: `# Factorial
def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)
print(factorial(5))`},
        {
            title: 'Fibonacci', level: 'advanced', desc: 'Fibonacci sequence', code: `# Fibonacci Sequence
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
fib(10)`}
    ],
    javascript: [
        {
            title: 'Hello World', level: 'beginner', desc: 'Console log message', code: `// JavaScript Hello World
console.log("Hello, World!");
console.log("Welcome to JavaScript!");`},
        {
            title: 'Add Two Numbers', level: 'beginner', desc: 'Add two numbers', code: `// Add Two Numbers
const a = 10, b = 20;
console.log(\`Sum: \${a + b}\`);`},
        {
            title: 'Prime Number', level: 'intermediate', desc: 'Check if prime', code: `// Check Prime Number
function isPrime(n) {
    if (n < 2) return false;
    for (let i = 2; i <= Math.sqrt(n); i++)
        if (n % i === 0) return false;
    return true;
}
console.log(isPrime(17));`},
        {
            title: 'Factorial', level: 'intermediate', desc: 'Calculate factorial', code: `// Factorial
const factorial = n => n <= 1 ? 1 : n * factorial(n-1);
console.log(factorial(5));`},
        {
            title: 'Array Sort', level: 'advanced', desc: 'Sort array', code: `// Array Sorting
const arr = [64, 34, 25, 12, 22];
arr.sort((a, b) => a - b);
console.log(arr);`}
    ],
    java: [
        {
            title: 'Hello World', level: 'beginner', desc: 'Print Hello World', code: `public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}`},
        {
            title: 'Add Two Numbers', level: 'beginner', desc: 'Add two numbers', code: `public class Main {
    public static void main(String[] args) {
        int a = 10, b = 20;
        System.out.println("Sum: " + (a + b));
    }
}`},
        {
            title: 'Prime Number', level: 'intermediate', desc: 'Check if prime', code: `public class Main {
    static boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i <= Math.sqrt(n); i++)
            if (n % i == 0) return false;
        return true;
    }
    public static void main(String[] args) {
        System.out.println(isPrime(17));
    }
}`},
        {
            title: 'Factorial', level: 'intermediate', desc: 'Calculate factorial', code: `public class Main {
    static int factorial(int n) {
        return n <= 1 ? 1 : n * factorial(n-1);
    }
    public static void main(String[] args) {
        System.out.println(factorial(5));
    }
}`},
        {
            title: 'Fibonacci', level: 'advanced', desc: 'Fibonacci sequence', code: `public class Main {
    public static void main(String[] args) {
        int a = 0, b = 1;
        for (int i = 0; i < 10; i++) {
            System.out.print(a + " ");
            int t = a + b; a = b; b = t;
        }
    }
}`}
    ],
    cpp: [
        {
            title: 'Hello World', level: 'beginner', desc: 'Print Hello World', code: `#include <iostream>
using namespace std;
int main() {
    cout << "Hello, World!" << endl;
    return 0;
}`},
        {
            title: 'Add Two Numbers', level: 'beginner', desc: 'Add two numbers', code: `#include <iostream>
using namespace std;
int main() {
    int a = 10, b = 20;
    cout << "Sum: " << a + b << endl;
    return 0;
}`},
        {
            title: 'Prime Number', level: 'intermediate', desc: 'Check if prime', code: `#include <iostream>
#include <cmath>
using namespace std;
bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i <= sqrt(n); i++)
        if (n % i == 0) return false;
    return true;
}
int main() {
    cout << isPrime(17) << endl;
    return 0;
}`},
        {
            title: 'Factorial', level: 'intermediate', desc: 'Calculate factorial', code: `#include <iostream>
using namespace std;
int factorial(int n) {
    return n <= 1 ? 1 : n * factorial(n-1);
}
int main() {
    cout << factorial(5) << endl;
    return 0;
}`},
        {
            title: 'Vector Sort', level: 'advanced', desc: 'Sort vector', code: `#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    vector<int> v = {64, 34, 25, 12};
    sort(v.begin(), v.end());
    for (int x : v) cout << x << " ";
    return 0;
}`}
    ],
    c: [
        {
            title: 'Hello World', level: 'beginner', desc: 'Print Hello World', code: `#include <stdio.h>
int main() {
    printf("Hello, World!\\n");
    return 0;
}`},
        {
            title: 'Add Two Numbers', level: 'beginner', desc: 'Add two numbers', code: `#include <stdio.h>
int main() {
    int a = 10, b = 20;
    printf("Sum: %d\\n", a + b);
    return 0;
}`},
        {
            title: 'Prime Number', level: 'intermediate', desc: 'Check if prime', code: `#include <stdio.h>
int isPrime(int n) {
    if (n < 2) return 0;
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0) return 0;
    return 1;
}
int main() {
    printf("%d\\n", isPrime(17));
    return 0;
}`},
        {
            title: 'Factorial', level: 'intermediate', desc: 'Calculate factorial', code: `#include <stdio.h>
int factorial(int n) {
    return n <= 1 ? 1 : n * factorial(n-1);
}
int main() {
    printf("%d\\n", factorial(5));
    return 0;
}`},
        {
            title: 'Array Sort', level: 'advanced', desc: 'Bubble sort', code: `#include <stdio.h>
int main() {
    int arr[] = {64, 34, 25, 12};
    int n = 4;
    for (int i = 0; i < n-1; i++)
        for (int j = 0; j < n-i-1; j++)
            if (arr[j] > arr[j+1]) {
                int t = arr[j]; arr[j] = arr[j+1]; arr[j+1] = t;
            }
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    return 0;
}`}
    ],
    csharp: [
        {
            title: 'Hello World', level: 'beginner', desc: 'Print Hello World', code: `using System;
class Program {
    static void Main() {
        Console.WriteLine("Hello, World!");
    }
}`},
        {
            title: 'Add Two Numbers', level: 'beginner', desc: 'Add two numbers', code: `using System;
class Program {
    static void Main() {
        int a = 10, b = 20;
        Console.WriteLine($"Sum: {a + b}");
    }
}`},
        {
            title: 'Prime Number', level: 'intermediate', desc: 'Check if prime', code: `using System;
class Program {
    static bool IsPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i * i <= n; i++)
            if (n % i == 0) return false;
        return true;
    }
    static void Main() {
        Console.WriteLine(IsPrime(17));
    }
}`},
        {
            title: 'Factorial', level: 'intermediate', desc: 'Calculate factorial', code: `using System;
class Program {
    static int Factorial(int n) => n <= 1 ? 1 : n * Factorial(n-1);
    static void Main() {
        Console.WriteLine(Factorial(5));
    }
}`},
        {
            title: 'LINQ Query', level: 'advanced', desc: 'Filter with LINQ', code: `using System;
using System.Linq;
class Program {
    static void Main() {
        int[] nums = {1, 2, 3, 4, 5, 6};
        var evens = nums.Where(n => n % 2 == 0);
        Console.WriteLine(string.Join(", ", evens));
    }
}`}
    ],
    typescript: [
        {
            title: 'Hello World', level: 'beginner', desc: 'Console log message', code: `// TypeScript Hello World
const message: string = "Hello, World!";
console.log(message);`},
        {
            title: 'Add Two Numbers', level: 'beginner', desc: 'Add two numbers', code: `// Add Two Numbers
function add(a: number, b: number): number {
    return a + b;
}
console.log(add(10, 20));`},
        {
            title: 'Interface Example', level: 'intermediate', desc: 'Using interfaces', code: `// Interface Example
interface Person {
    name: string;
    age: number;
}
const user: Person = { name: "John", age: 30 };
console.log(user);`},
        {
            title: 'Generic Function', level: 'intermediate', desc: 'Generic types', code: `// Generic Function
function identity<T>(arg: T): T {
    return arg;
}
console.log(identity<string>("Hello"));
console.log(identity<number>(42));`},
        {
            title: 'Async/Await', level: 'advanced', desc: 'Async function', code: `// Async/Await Example
async function fetchData(): Promise<string> {
    return new Promise(resolve => {
        setTimeout(() => resolve("Data loaded!"), 100);
    });
}
fetchData().then(console.log);`}
    ],
    go: [
        {
            title: 'Hello World', level: 'beginner', desc: 'Print Hello World', code: `package main
import "fmt"
func main() {
    fmt.Println("Hello, World!")
}`},
        {
            title: 'Add Two Numbers', level: 'beginner', desc: 'Add two numbers', code: `package main
import "fmt"
func main() {
    a, b := 10, 20
    fmt.Printf("Sum: %d\\n", a+b)
}`},
        {
            title: 'Prime Number', level: 'intermediate', desc: 'Check if prime', code: `package main
import "fmt"
func isPrime(n int) bool {
    if n < 2 { return false }
    for i := 2; i*i <= n; i++ {
        if n%i == 0 { return false }
    }
    return true
}
func main() {
    fmt.Println(isPrime(17))
}`},
        {
            title: 'Factorial', level: 'intermediate', desc: 'Calculate factorial', code: `package main
import "fmt"
func factorial(n int) int {
    if n <= 1 { return 1 }
    return n * factorial(n-1)
}
func main() {
    fmt.Println(factorial(5))
}`},
        {
            title: 'Goroutine', level: 'advanced', desc: 'Concurrent execution', code: `package main
import ("fmt"; "time")
func say(s string) {
    for i := 0; i < 3; i++ {
        time.Sleep(100 * time.Millisecond)
        fmt.Println(s)
    }
}
func main() {
    go say("world")
    say("hello")
}`}
    ],
    rust: [
        {
            title: 'Hello World', level: 'beginner', desc: 'Print Hello World', code: `fn main() {
    println!("Hello, World!");
}`},
        {
            title: 'Add Two Numbers', level: 'beginner', desc: 'Add two numbers', code: `fn main() {
    let a = 10;
    let b = 20;
    println!("Sum: {}", a + b);
}`},
        {
            title: 'Prime Number', level: 'intermediate', desc: 'Check if prime', code: `fn is_prime(n: u32) -> bool {
    if n < 2 { return false; }
    for i in 2..=((n as f64).sqrt() as u32) {
        if n % i == 0 { return false; }
    }
    true
}
fn main() {
    println!("{}", is_prime(17));
}`},
        {
            title: 'Factorial', level: 'intermediate', desc: 'Calculate factorial', code: `fn factorial(n: u64) -> u64 {
    if n <= 1 { 1 } else { n * factorial(n - 1) }
}
fn main() {
    println!("{}", factorial(5));
}`},
        {
            title: 'Vector Operations', level: 'advanced', desc: 'Vector manipulation', code: `fn main() {
    let mut v = vec![64, 34, 25, 12];
    v.sort();
    println!("{:?}", v);
}`}
    ],
    ruby: [
        {
            title: 'Hello World', level: 'beginner', desc: 'Print Hello World', code: `# Ruby Hello World
puts "Hello, World!"
puts "Welcome to Ruby!"`},
        {
            title: 'Add Two Numbers', level: 'beginner', desc: 'Add two numbers', code: `# Add Two Numbers
a, b = 10, 20
puts "Sum: #{a + b}"`},
        {
            title: 'Prime Number', level: 'intermediate', desc: 'Check if prime', code: `# Check Prime Number
def prime?(n)
  return false if n < 2
  (2..Math.sqrt(n)).none? { |i| n % i == 0 }
end
puts prime?(17)`},
        {
            title: 'Factorial', level: 'intermediate', desc: 'Calculate factorial', code: `# Factorial
def factorial(n)
  n <= 1 ? 1 : n * factorial(n - 1)
end
puts factorial(5)`},
        {
            title: 'Array Methods', level: 'advanced', desc: 'Ruby array methods', code: `# Array Methods
arr = [3, 1, 4, 1, 5, 9]
puts arr.sort.inspect
puts arr.map { |x| x * 2 }.inspect`}
    ],
    php: [
        {
            title: 'Hello World', level: 'beginner', desc: 'Print Hello World', code: `<?php
echo "Hello, World!\\n";
echo "Welcome to PHP!\\n";
?>`},
        {
            title: 'Add Two Numbers', level: 'beginner', desc: 'Add two numbers', code: `<?php
$a = 10;
$b = 20;
echo "Sum: " . ($a + $b) . "\\n";
?>`},
        {
            title: 'Prime Number', level: 'intermediate', desc: 'Check if prime', code: `<?php
function isPrime($n) {
    if ($n < 2) return false;
    for ($i = 2; $i * $i <= $n; $i++)
        if ($n % $i == 0) return false;
    return true;
}
echo isPrime(17) ? "true" : "false";
?>`},
        {
            title: 'Factorial', level: 'intermediate', desc: 'Calculate factorial', code: `<?php
function factorial($n) {
    return $n <= 1 ? 1 : $n * factorial($n - 1);
}
echo factorial(5);
?>`},
        {
            title: 'Array Functions', level: 'advanced', desc: 'PHP array functions', code: `<?php
$arr = [64, 34, 25, 12];
sort($arr);
print_r($arr);
$filtered = array_filter($arr, fn($x) => $x > 20);
print_r($filtered);
?>`}
    ],
    swift: [
        {
            title: 'Hello World', level: 'beginner', desc: 'Print Hello World', code: `// Swift Hello World
print("Hello, World!")
print("Welcome to Swift!")`},
        {
            title: 'Add Two Numbers', level: 'beginner', desc: 'Add two numbers', code: `// Add Two Numbers
let a = 10
let b = 20
print("Sum: \\(a + b)")`},
        {
            title: 'Prime Number', level: 'intermediate', desc: 'Check if prime', code: `// Check Prime Number
func isPrime(_ n: Int) -> Bool {
    if n < 2 { return false }
    for i in 2...Int(Double(n).squareRoot()) {
        if n % i == 0 { return false }
    }
    return true
}
print(isPrime(17))`},
        {
            title: 'Factorial', level: 'intermediate', desc: 'Calculate factorial', code: `// Factorial
func factorial(_ n: Int) -> Int {
    n <= 1 ? 1 : n * factorial(n - 1)
}
print(factorial(5))`},
        {
            title: 'Array Operations', level: 'advanced', desc: 'Swift array methods', code: `// Swift Array Operations
var arr = [64, 34, 25, 12]
arr.sort()
print(arr)
let evens = arr.filter { $0 % 2 == 0 }
print(evens)`}
    ],
    dart: [
        {
            title: 'Hello World', level: 'beginner', desc: 'Print Hello World', code: `// Dart Hello World
void main() {
  print('Hello, World!');
  print('Welcome to Dart!');
}`},
        {
            title: 'Add Two Numbers', level: 'beginner', desc: 'Add two numbers', code: `// Add Two Numbers
void main() {
  int a = 10, b = 20;
  print('Sum: \${a + b}');
}`},
        {
            title: 'Prime Number', level: 'intermediate', desc: 'Check if prime', code: `// Check Prime Number
bool isPrime(int n) {
  if (n < 2) return false;
  for (int i = 2; i * i <= n; i++)
    if (n % i == 0) return false;
  return true;
}
void main() {
  print(isPrime(17));
}`},
        {
            title: 'Factorial', level: 'intermediate', desc: 'Calculate factorial', code: `// Factorial
int factorial(int n) => n <= 1 ? 1 : n * factorial(n - 1);
void main() {
  print(factorial(5));
}`},
        {
            title: 'List Operations', level: 'advanced', desc: 'Dart list methods', code: `// Dart List Operations
void main() {
  var list = [64, 34, 25, 12];
  list.sort();
  print(list);
  var evens = list.where((x) => x % 2 == 0).toList();
  print(evens);
}`}
    ],
    scala: [
        {
            title: 'Hello World', level: 'beginner', desc: 'Print Hello World', code: `// Scala Hello World
object Main extends App {
  println("Hello, World!")
}`},
        {
            title: 'Add Two Numbers', level: 'beginner', desc: 'Add two numbers', code: `// Add Two Numbers
object Main extends App {
  val a = 10
  val b = 20
  println(s"Sum: ${"$"}{a + b}")
}`},
        {
            title: 'Prime Number', level: 'intermediate', desc: 'Check if prime', code: `// Check Prime Number
object Main extends App {
  def isPrime(n: Int): Boolean =
    n >= 2 && !(2 to math.sqrt(n).toInt).exists(n % _ == 0)
  println(isPrime(17))
}`},
        {
            title: 'Factorial', level: 'intermediate', desc: 'Calculate factorial', code: `// Factorial
object Main extends App {
  def factorial(n: Int): Int = if (n <= 1) 1 else n * factorial(n - 1)
  println(factorial(5))
}`},
        {
            title: 'List Operations', level: 'advanced', desc: 'Scala collections', code: `// Scala List Operations
object Main extends App {
  val list = List(64, 34, 25, 12)
  println(list.sorted)
  println(list.filter(_ % 2 == 0))
}`}
    ],
    r: [
        {
            title: 'Hello World', level: 'beginner', desc: 'Print Hello World', code: `# R Hello World
print("Hello, World!")
cat("Welcome to R!\\n")`},
        {
            title: 'Add Two Numbers', level: 'beginner', desc: 'Add two numbers', code: `# Add Two Numbers
a <- 10
b <- 20
cat("Sum:", a + b, "\\n")`},
        {
            title: 'Statistics', level: 'intermediate', desc: 'Basic statistics', code: `# Basic Statistics
data <- c(10, 20, 30, 40, 50)
cat("Mean:", mean(data), "\\n")
cat("SD:", sd(data), "\\n")`},
        {
            title: 'Vector Operations', level: 'intermediate', desc: 'R vector ops', code: `# Vector Operations
v <- c(64, 34, 25, 12)
print(sort(v))
print(v[v > 20])`},
        {
            title: 'Data Frame', level: 'advanced', desc: 'Working with data frames', code: `# Data Frame
df <- data.frame(
  name = c("Alice", "Bob", "Carol"),
  age = c(25, 30, 35)
)
print(df)
print(df[df$age > 25, ])`}
    ],
    sql: [
        {
            title: 'Select All', level: 'beginner', desc: 'Select all rows', code: `-- Select All Rows
SELECT * FROM users;`},
        {
            title: 'Where Clause', level: 'beginner', desc: 'Filter with WHERE', code: `-- Filter with WHERE
SELECT * FROM users
WHERE age > 18;`},
        {
            title: 'Join Tables', level: 'intermediate', desc: 'Inner join', code: `-- Inner Join
SELECT u.name, o.total
FROM users u
INNER JOIN orders o ON u.id = o.user_id;`},
        {
            title: 'Aggregation', level: 'intermediate', desc: 'Group and count', code: `-- Aggregation
SELECT category, COUNT(*) as count, AVG(price) as avg_price
FROM products
GROUP BY category
HAVING COUNT(*) > 5;`},
        {
            title: 'Subquery', level: 'advanced', desc: 'Nested query', code: `-- Subquery Example
SELECT * FROM users
WHERE id IN (
    SELECT user_id FROM orders
    WHERE total > 1000
);`}
    ],
    html: [
        {
            title: 'Basic Page', level: 'beginner', desc: 'HTML structure', code: `<!DOCTYPE html>
<html>
<head>
    <title>Hello</title>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>`},
        {
            title: 'Styled Page', level: 'beginner', desc: 'With CSS', code: `<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial; background: #f0f0f0; }
        h1 { color: #333; text-align: center; }
    </style>
</head>
<body>
    <h1>Styled Page</h1>
</body>
</html>`},
        {
            title: 'Flexbox Layout', level: 'intermediate', desc: 'CSS Flexbox', code: `<style>
.container {
    display: flex;
    justify-content: space-between;
    gap: 20px;
}
.box { padding: 20px; background: #6366f1; color: white; }
</style>
<div class="container">
    <div class="box">Box 1</div>
    <div class="box">Box 2</div>
</div>`},
        {
            title: 'Grid Layout', level: 'intermediate', desc: 'CSS Grid', code: `<style>
.grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
}
.item { padding: 20px; background: #8b5cf6; color: white; }
</style>
<div class="grid">
    <div class="item">1</div>
    <div class="item">2</div>
    <div class="item">3</div>
</div>`},
        {
            title: 'Animation', level: 'advanced', desc: 'CSS Animation', code: `<style>
@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.1); }
}
.animated {
    width: 100px; height: 100px;
    background: linear-gradient(135deg, #6366f1, #a855f7);
    border-radius: 50%;
    animation: pulse 2s infinite;
}
</style>
<div class="animated"></div>`}
    ]
};

// Render functions
function renderExamples() {
    const container = document.getElementById('examplesContainer');
    const langFilters = document.getElementById('langFilters');
    if (!container || !langFilters) return;

    // Render language filters
    langFilters.innerHTML = `<button class="filter-btn active" data-lang="all">All Examples</button>` +
        EXAMPLE_LANGUAGES.map(l => `<button class="filter-btn" data-lang="${l.id}">${l.icon} ${l.name}</button>`).join('');

    // Render examples by language
    let html = '';
    EXAMPLE_LANGUAGES.forEach(lang => {
        const examples = EXAMPLES[lang.id] || [];
        if (examples.length === 0) return;

        html += `<section class="examples-section lang-examples" data-lang="${lang.id}">
            <h2 class="section-heading">${lang.icon} ${lang.name} Examples</h2>
            <div class="examples-grid-cards">`;

        examples.forEach(ex => {
            html += `
                <div class="example-card-full" data-lang="${lang.id}" data-level="${ex.level}">
                    <div class="example-header-full">
                        <div class="example-meta">
                            <span class="example-lang-badge">${lang.icon} ${lang.name}</span>
                            <span class="example-level-badge ${ex.level}">${ex.level.charAt(0).toUpperCase() + ex.level.slice(1)}</span>
                        </div>
                        <h3>${ex.title}</h3>
                        <p>${ex.desc}</p>
                    </div>
                    <pre class="example-code"><code>${escapeHtml(ex.code)}</code></pre>
                    <div class="example-actions">
                        <a href="editor.html?lang=${lang.id}" class="btn btn-primary">Try in Editor</a>
                    </div>
                </div>`;
        });

        html += `</div></section>`;
    });

    container.innerHTML = html;
    initFilters();
}

function escapeHtml(text) {
    return text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function initFilters() {
    const langBtns = document.querySelectorAll('.filter-btn');
    const levelBtns = document.querySelectorAll('.level-btn');
    let currentLang = 'all', currentLevel = 'all';

    function filter() {
        document.querySelectorAll('.lang-examples').forEach(section => {
            const sectionLang = section.dataset.lang;
            section.style.display = (currentLang === 'all' || currentLang === sectionLang) ? 'block' : 'none';
        });
        document.querySelectorAll('.example-card-full').forEach(card => {
            const cardLang = card.dataset.lang;
            const cardLevel = card.dataset.level;
            const matchLang = currentLang === 'all' || cardLang === currentLang;
            const matchLevel = currentLevel === 'all' || cardLevel === currentLevel;
            card.style.display = (matchLang && matchLevel) ? 'flex' : 'none';
        });
    }

    langBtns.forEach(btn => btn.addEventListener('click', () => {
        langBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentLang = btn.dataset.lang;
        filter();
    }));

    levelBtns.forEach(btn => btn.addEventListener('click', () => {
        levelBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentLevel = btn.dataset.level;
        filter();
    }));
}

document.addEventListener('DOMContentLoaded', renderExamples);
