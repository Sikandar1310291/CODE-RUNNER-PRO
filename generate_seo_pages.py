import os

LANGUAGES_DATA = {
    "python": {
        "name": "Python",
        "slug": "python",
        "version": "3.12",
        "target": "Students/Data Scientists",
        "tagline": "Run Python 3.12 + NumPy/Pandas instantly",
        "benefit": "Fast, versatile, and beginner-friendly for everything from web scrapers to data science.",
        "examples": [
            {"title": "Hello World", "code": 'print("Hello, World!")'},
            {"title": "Fibonacci Sequence", "code": 'def fib(n):\n    a, b = 0, 1\n    for _ in range(n):\n        yield a\n        a, b = b, a + b\n\nprint(list(fib(10)))'},
            {"title": "Pandas DataFrame", "code": 'import pandas as pd\ndata = {"Name": ["Alice", "Bob"], "Age": [25, 30]}\ndf = pd.DataFrame(data)\nprint(df)'},
            {"title": "Matplotlib Plot (Prep)", "code": 'import matplotlib.pyplot as plt\nx = [1, 2, 3]\ny = [4, 5, 6]\nplt.plot(x, y)\nprint("Plot logic defined.")'},
            {"title": "Simple Web Scraper", "code": 'import requests\nfrom bs4 import BeautifulSoup\n# Logic template\nprint("Scraper template ready.")'}
        ],
        "useCases": ["DataCamp homework", "LeetCode practice", "Quick data analysis"],
        "faqs": [
            {"q": "Does it support NumPy/Pandas?", "a": "Yes! Our environment includes major data science libraries like NumPy and Pandas."},
            {"q": "Can I read/write files?", "a": "File I/O is restricted to the current working directory for security reasons."},
            {"q": "What are the timeout limits?", "a": "Scripts are limited to 30 seconds of execution time to ensure fair resource usage."},
            {"q": "Is it free?", "a": "Yes, our Python compiler is 100% free with no sign-up required."}
        ]
    },
    "javascript": {
        "name": "JavaScript",
        "slug": "javascript",
        "version": "Node 20",
        "target": "Frontend Devs",
        "tagline": "Test Node.js + Browser JS instantly",
        "benefit": "Modern Node.js runtime for lightning-fast testing and prototyping.",
        "examples": [
            {"title": "Async/Await", "code": 'async function fetchMsg() {\n    return "Hello from Async!";\n}\nfetchMsg().then(console.log);'},
            {"title": "Express API Skeleton", "code": 'console.log("Setting up Express style routes...");'},
            {"title": "DOM Manipulation", "code": 'console.log("Testing frontend logic in Node console...");'},
            {"title": "Fetch API", "code": 'fetch("https://jsonplaceholder.typicode.com/todos/1")\n  .then(res => res.json())\n  .then(console.log);'},
            {"title": "Canvas Logic", "code": 'console.log("Testing Canvas API logic patterns...");'}
        ],
        "useCases": ["React prototyping", "Node.js API testing", "Frontend interviews"],
        "faqs": [
            {"q": "Can I use npm packages?", "a": "Standard Node.js built-in modules are supported by default."},
            {"q": "Browser vs Node environment?", "a": "This compiler runs in a Node.js 20 environment."},
            {"q": "Is ES6+ supported?", "a": "Yes, full ES2023 support is included for modern syntax."},
            {"q": "Is it secure?", "a": "Yes, code runs in an isolated Docker container for your safety."}
        ]
    },
    "java": {
        "name": "Java",
        "slug": "java",
        "version": "21",
        "target": "Android/Enterprise Devs",
        "tagline": "Full JDK 21 - No Eclipse needed",
        "benefit": "Powerful JDK 21 runtime for enterprise-grade coding and Android prototyping.",
        "examples": [
            {"title": "OOP Class", "code": 'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Java OOP works!");\n    }\n}'},
            {"title": "Java Streams", "code": 'import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        List<String> list = Arrays.asList("a", "b", "c");\n        list.stream().map(String::toUpperCase).forEach(System.out::println);\n    }\n}'},
            {"title": "Multithreading", "code": 'public class Main {\n    public static void main(String[] args) {\n        new Thread(() -> System.out.println("Thread running")).start();\n    }\n}'},
            {"title": "REST API logic", "code": 'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Endpoint logic validated.");\n    }\n}'},
            {"title": "LeetCode Example", "code": 'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Solving Two Sum...");\n    }\n}'}
        ],
        "useCases": ["Android Studio prototyping", "Java Certifications", "LeetCode challenges"],
        "faqs": [
            {"q": "Maven/Gradle support?", "a": "Current support is for single-file standard Java libraries."},
            {"q": "Java 8 vs 21?", "a": "We use JDK 21 for modern features like switch patterns and virtual threads."},
            {"q": "Memory limits?", "a": "Default JVM heap is limited to 512MB for stability."},
            {"q": "Can I run GUI apps?", "a": "Headless execution only; GUI (Swing/AWT) is not supported in the cloud."}
        ]
    },
    "c": {
        "name": "C",
        "slug": "c",
        "version": "GCC 13",
        "target": "Systems Programmers",
        "tagline": "Compile C code with full stdlib instantly",
        "benefit": "Low-level power with modern GCC 13 safety and performance optimizations.",
        "examples": [
            {"title": "Pointers", "code": '#include <stdio.h>\nint main() {\n    int x = 10; int *p = &x;\n    printf("Val: %d, Addr: %p\\n", *p, (void*)p);\n    return 0;\n}'},
            {"title": "Dynamic Memory", "code": '#include <stdlib.h>\nint main() {\n    int *arr = malloc(5 * sizeof(int));\n    if(arr) free(arr);\n    return 0;\n}'},
            {"title": "File I/O", "code": '#include <stdio.h>\nint main() {\n    printf("File streaming logic...");\n    return 0;\n}'},
            {"title": "Linked List", "code": '#include <stdio.h>\nstruct Node { int val; struct Node* next; };\nint main() { printf("Linked list ready"); return 0; }'},
            {"title": "QuickSort", "code": 'void quickSort(int arr[], int low, int high) { /* Algo logic */ }'}
        ],
        "useCases": ["Embedded systems study", "OS courses", "Hardware interviews"],
        "faqs": [
            {"q": "Fast I/O support?", "a": "Standard printf/scanf are supported; use fast-io tricks for CP if needed."},
            {"q": "GDB debugging?", "a": "Currently provides standard output/error; full GDB coming soon."},
            {"q": "Compiler flags?", "a": "We use -O2 -Wall by default for performance and safety."},
            {"q": "Standard headers?", "a": "All standard C library headers (stdio, stdlib, math, etc.) are available."}
        ]
    },
    "cpp": {
        "name": "C++",
        "slug": "cpp",
        "version": "C++20",
        "target": "Competitive Programmers",
        "tagline": "C++20 + STL for Codeforces/AtCoder",
        "benefit": "Blazing fast execution with full C++20 and STL support.",
        "examples": [
            {"title": "Binary Search", "code": '#include <iostream>\n#include <algorithm>\n#include <vector>\nusing namespace std;\nint main() { vector<int> v={1,2,3}; cout << binary_search(v.begin(), v.end(), 2); return 0; }'},
            {"title": "Dijkstra Algorithm", "code": '#include <queue>\n#include <vector>\n// Dijkstra logic...'},
            {"title": "Fast I/O Template", "code": '#include <iostream>\nusing namespace std;\nint main() { ios_base::sync_with_stdio(false); cin.tie(NULL); return 0; }'},
            {"title": "STL Vectors", "code": '#include <vector>\n#include <iostream>\nint main() { std::vector<int> v; v.push_back(1); return 0; }'},
            {"title": "Segment Tree", "code": 'void build(int node, int start, int end) { /* Segment Tree Logic */ }'}
        ],
        "useCases": ["CP contests (Codeforces)", "Google Kickstart", "University assignments"],
        "faqs": [
            {"q": "Fast I/O?", "a": "Yes, use sync_with_stdio(false) for competitive programming contests."},
            {"q": "C++17 vs 20?", "a": "We provide C++20 so you can use modern concepts and ranges."},
            {"q": "-O2 optimization?", "a": "Yes, all code is compiled with -O2 for maximum production speed."},
            {"q": "Time limit?", "a": "Execution is capped at 5 seconds for C++ programs."}
        ]
    },
    "csharp": {
        "name": "C#",
        "slug": "csharp",
        "version": ".NET 8",
        "target": "Unity/.NET Devs",
        "tagline": "Run C# .NET 8 for Unity prototyping",
        "benefit": "Latest .NET 8 features for C# development, right in your browser.",
        "examples": [
            {"title": "LINQ", "code": 'using System;\nusing System.Linq;\nvar nums = new[] {1,2,3}; var even = nums.Where(n => n%2==0);\nforeach(var n in even) Console.WriteLine(n);'},
            {"title": "ASP.NET Endpoint", "code": 'using System;\nConsole.WriteLine("Mapping API endpoint routes...");'},
            {"title": "Async Tasks", "code": 'using System;\nusing System.Threading.Tasks;\nawait Task.Delay(100);\nConsole.WriteLine("Done");'},
            {"title": "Unity Script Patterns", "code": 'using System;\n// Prototyping MonoBehaviour logic\nConsole.WriteLine("Unity logic start");'},
            {"title": "Modern Classes", "code": 'using System;\npublic record Person(string Name, int Age);\nvar p = new Person("Coder", 25);'}
        ],
        "useCases": ["Unity game prototyping", ".NET API testing", "Interview preparation"],
        "faqs": [
            {"q": "NuGet packages?", "a": "Standard .NET 8 libraries are included; NuGet integration is coming soon."},
            {"q": ".NET Framework support?", "a": "We focus on the modern cross-platform .NET 8 runtime."},
            {"q": "Unity support?", "a": "Perfect for testing Unity C# scripts and specific logic snippets."},
            {"q": "Async/Await?", "a": "Full support for modern asynchronous programming in C#."}
        ]
    },
    "typescript": {
        "name": "TypeScript",
        "slug": "typescript",
        "version": "5.4",
        "target": "Frontend Devs",
        "tagline": "TypeScript compiler + Node.js runtime",
        "benefit": "Type-safe development for enterprise-scale web applications.",
        "examples": [
            {"title": "Interfaces", "code": 'interface User { id: number; name: string; }\nconst u: User = { id: 1, name: "TS" };'},
            {"title": "Generics", "code": 'function wrap<T>(item: T): T { return item; }\nconsole.log(wrap<string>("Generics!"));'},
            {"title": "React Component logic", "code": 'type Props = { title: string };\nconst render = (p: Props) => p.title;'},
            {"title": "Express TS API", "code": '// Using TS types for web server logic\nconsole.log("TS server logic ready");'},
            {"title": "Decorators", "code": 'function log(target: any) { console.log("Decorating..."); }'}
        ],
        "useCases": ["Angular/React logic", "Node.js TS APIs", "Type safety testing"],
        "faqs": [
            {"q": "tsconfig.json?", "a": "Pre-configured for strict mode and modern ES targets by default."},
            {"q": "JS interop?", "a": "Fully compatible with all standard JavaScript global objects."},
            {"q": "Source maps?", "a": "TS is compiled to JS and run via Node.js runtime instantly."},
            {"q": "TypeScript version?", "a": "Currently running the latest stable TypeScript 5.4."}
        ]
    },
    "go": {
        "name": "Go",
        "slug": "go",
        "version": "1.22",
        "target": "Backend Devs",
        "tagline": "Golang playground with goroutines",
        "benefit": "Simplicity and speed for modern cloud and backend services.",
        "examples": [
            {"title": "HTTP Server", "code": 'package main\nimport "fmt"\nfunc main() { fmt.Println("Go Server snippet") }'},
            {"title": "Goroutines", "code": 'package main\nimport "fmt"\nfunc main() { go func(){ fmt.Println("Async") }(); }'},
            {"title": "Gin Framework logic", "code": 'package main\nfunc main() { /* Gin routes logic */ }'},
            {"title": "Database Connection", "code": 'package main\nimport "database/sql"\nfunc main() { /* db connection */ }'},
            {"title": "Structs", "code": 'package main\ntype User struct { Name string }'}
        ],
        "useCases": ["Microservices", "Docker logic", "Cloud functions"],
        "faqs": [
            {"q": "go.mod support?", "a": "Single-file execution with full standard library support."},
            {"q": "Cgo support?", "a": "Cgo is disabled for security and cloud performance."},
            {"q": "Build flags?", "a": "Compiled with standard Go optimization flags for speed."},
            {"q": "Goroutines?", "a": "Full concurrent execution support included."}
        ]
    },
    "rust": {
        "name": "Rust",
        "slug": "rust",
        "version": "1.80",
        "target": "Systems Programmers",
        "tagline": "Safe Rust compilation in browser",
        "benefit": "Safety, speed, and concurrency without the garbage collector.",
        "examples": [
            {"title": "Ownership", "code": 'fn main() { let s = String::from("Rust"); println!("{}", s); }'},
            {"title": "Async Rust", "code": 'async fn test() { println!("Async Rust"); }'},
            {"title": "CLI Tool", "code": 'use std::env;\nfn main() { println!("CLI logic"); }'},
            {"title": "Web Server logic", "code": '// Using Axum/Actix style logic\nfn main() { println!("Server ready"); }'},
            {"title": "Vectors", "code": 'fn main() { let v = vec![1, 2, 3]; println!("{:?}", v); }'}
        ],
        "useCases": ["WebAssembly", "Systems programming", "Memory safety study"],
        "faqs": [
            {"q": "Cargo support?", "a": "Single-file rustc execution for instant browser testing."},
            {"q": "Nightly features?", "a": "We use the Stable 1.80 channel for maximum reliability."},
            {"q": "WASM support?", "a": "Native execution; WASM compilation is a separate toolchain."},
            {"q": "Error messages?", "a": "Full rustc colorized and detailed error reports provided."}
        ]
    },
    "ruby": {
        "name": "Ruby",
        "slug": "ruby",
        "version": "3.3",
        "target": "Web Devs",
        "tagline": "Rails/Ruby testing environment",
        "benefit": "A focus on simplicity and productivity for elegant coding.",
        "examples": [
            {"title": "Sinatra App logic", "code": 'puts "Sinatra route ready"'},
            {"title": "Gems usage", "code": 'require "json"\nputs JSON.generate({status: "ok"})'},
            {"title": "ActiveRecord pattern", "code": 'class User; end\nputs "Model defined"'},
            {"title": "Blocks/Procs", "code": '[1,2,3].each { |n| puts n * 2 }'},
            {"title": "String interpolation", "code": 'name = "Ruby"; puts "Hello #{name}"'}
        ],
        "useCases": ["Ruby on Rails logic", "Scripting", "Automation tools"],
        "faqs": [
            {"q": "Bundler support?", "a": "Core gems and standard library are fully included."},
            {"q": "Rails console?", "a": "Full Rails environment is not included, only pure Ruby 3.3 core."},
            {"q": "JRuby?", "a": "No, we use standard MRI Ruby 3.3 (CRuby)."},
            {"q": "Performance?", "a": "Ruby 3.3 YJIT is enabled for boosted execution speed."}
        ]
    },
    "php": {
        "name": "PHP",
        "slug": "php",
        "version": "8.3",
        "target": "Web Developers",
        "tagline": "PHP 8.3 for Laravel/WordPress",
        "benefit": "Modern PHP 8.3 features for backend and web development.",
        "examples": [
            {"title": "Laravel Route logic", "code": 'echo "Route::get(\'/\', fn() => \'PHP 8\');";'},
            {"title": "Composer Package logic", "code": 'echo "Using Guzzle style logic...";'},
            {"title": "PDO Database", "code": 'echo "PDO logic ready";'},
            {"title": "Attributes", "code": '#[MyAttr] class User {}\necho "Attributes tested";'},
            {"title": "Match expression", "code": '$v = 1; echo match($v) { 1 => "one", default => "other" };'}
        ],
        "useCases": ["WordPress plugins", "Laravel APIs", "Full-stack development"],
        "faqs": [
            {"q": "Composer support?", "a": "Standard PHP 8.3 extensions and core library are included."},
            {"q": "PHP 7 vs 8?", "a": "We use PHP 8.3 for the latest JIT and syntax features."},
            {"q": "Extensions?", "a": "Includes PDO, OpenSSL, cURL, GD, and Mbstring by default."},
            {"q": "Input support?", "a": "Full support for stdin and CLI arguments in PHP scripts."}
        ]
    },
    "swift": {
        "name": "Swift",
        "slug": "swift",
        "version": "5.10",
        "target": "iOS Devs",
        "tagline": "Swift compiler for iOS prototyping",
        "benefit": "The official language for Apple platforms, running in your browser.",
        "examples": [
            {"title": "Optionals", "code": 'let name: String? = "Swift"\nprint(name ?? "Unknown")'},
            {"title": "Closures", "code": 'let greet = { print("Hi Swift!") }\ngreet()'},
            {"title": "Codable JSON", "code": 'struct User: Codable { let id: Int }\nprint("Codable ready")'},
            {"title": "Async/Await", "code": 'import Foundation\nprint("Async logic ready")'},
            {"title": "Control Flow", "code": 'for i in 1...5 { print(i) }'}
        ],
        "useCases": ["iOS app logic", "SwiftUI prototyping", "Server-side Swift"],
        "faqs": [
            {"q": "Xcode required?", "a": "No, this is a web-based Swift compiler running on Linux backend."},
            {"q": "Swift Package Manager?", "a": "Core Swift libraries are provided for instant browser testing."},
            {"q": "Playgrounds?", "a": "Similar functionality to Swift Playgrounds but fully cross-platform."},
            {"q": "UIKit support?", "a": "No GUI; console logic and Foundation library are fully supported."}
        ]
    },
    "dart": {
        "name": "Dart",
        "slug": "dart",
        "version": "3.2",
        "target": "Flutter Devs",
        "tagline": "Flutter/Dart online compiler",
        "benefit": "Modern Dart 3.2 with strict null-safety for high-performance apps.",
        "examples": [
            {"title": "Futures", "code": 'void main() async { print("Dart 3 logic"); }'},
            {"title": "Streams", "code": 'Stream<int> count() async* { yield 1; }'},
            {"title": "Flutter Widget logic", "code": 'class MainApp extends StatelessWidget {}'},
            {"title": "HTTP Client", "code": 'void fetch() { /* http logic */ }'},
            {"title": "Records (Dart 3)", "code": 'void main() { var (a, b) = (1, 2); print(a); }'}
        ],
        "useCases": ["Flutter mobile apps", "Web apps", "Async programming study"],
        "faqs": [
            {"q": "Flutter SDK?", "a": "Full Dart 3.2 core SDK with Flutter logic support provided."},
            {"q": "Dart 2 vs 3?", "a": "We run Dart 3.2 with strict sound null safety enabled."},
            {"q": "Packages?", "a": "Standard dart:core, dart:async, dart:math and more are included."},
            {"q": "Hot reload?", "a": "Code is re-compiled and run instantly on every click."}
        ]
    },
    "scala": {
        "name": "Scala",
        "slug": "scala",
        "version": "3.5",
        "target": "Data Engineers",
        "tagline": "Scala 3 + Spark support",
        "benefit": "Functional programming meets object-oriented design for data processing.",
        "examples": [
            {"title": "Case Classes", "code": 'case class User(name: String)\nval u = User("Scala")'},
            {"title": "Pattern Matching", "code": 'val x = 1\nx match { case 1 => println("One") }'},
            {"title": "Futures", "code": 'import scala.concurrent.Future\nprintln("Future ready")'},
            {"title": "Spark DataFrame logic", "code": 'println("Spark type logic validated")'},
            {"title": "Givens/Using", "code": 'given String = "context"\nprintln("Scala 3 context active")'}
        ],
        "useCases": ["Apache Spark logic", "Akka actors", "Functional programming research"],
        "faqs": [
            {"q": "SBT support?", "a": "Single-file Scala 3.5 execution for fast browser-based testing."},
            {"q": "Scala 2 vs 3?", "a": "We use the latest Scala 3 (Dotty) for modern features."},
            {"q": "Java interop?", "a": "Full access to the standard Java library is available."},
            {"q": "Implicit support?", "a": "Yes, full support for Scala 3 givens, using, and implicits."}
        ]
    },
    "sql": {
        "name": "SQL",
        "slug": "sql",
        "version": "SQLite 3",
        "target": "Data Analysts",
        "tagline": "Run SQL queries on sample databases",
        "benefit": "Professional-grade SQL testing environment for complex query design.",
        "examples": [
            {"title": "JOINs", "code": 'SELECT * FROM users JOIN orders ON users.id = orders.uid;'},
            {"title": "Window Functions", "code": 'SELECT rank() OVER (ORDER BY salary DESC) FROM employees;'},
            {"title": "Subqueries", "code": 'SELECT name FROM users WHERE id IN (SELECT uid FROM logs);'},
            {"title": "CTEs", "code": 'WITH sales AS (SELECT 100 as total) SELECT * FROM sales;'},
            {"title": "GROUP BY", "code": 'SELECT category, COUNT(*) FROM products GROUP BY category;'}
        ],
        "useCases": ["Data analysis tasks", "SQL interview preparation", "Database logic testing"],
        "faqs": [
            {"q": "MySQL vs PostgreSQL?", "a": "We use SQLite 3 internally for instant, portable SQL testing."},
            {"q": "Sample data?", "a": "You can easily create and seed data into in-memory tables."},
            {"q": "BigQuery?", "a": "Standard ANSI SQL syntax is used, compatible with most platforms."},
            {"q": "Persistent tables?", "a": "In-memory database; it will reset when you refresh the page."}
        ]
    },
    "r": {
        "name": "R",
        "slug": "r",
        "version": "4.4",
        "target": "Statisticians",
        "tagline": "R + ggplot2/data analysis",
        "benefit": "Comprehensive statistical computing and high-quality graphics in the cloud.",
        "examples": [
            {"title": "ggplot2 Plot", "code": 'library(ggplot2)\nprint("ggplot2 ready for plotting")'},
            {"title": "dplyr Pipeline", "code": 'library(dplyr)\nprint("dplyr pipeline logic is active")'},
            {"title": "Linear Regression", "code": 'model <- lm(mpg ~ wt, data = mtcars)\nprint(summary(model))'},
            {"title": "Shiny App logic", "code": 'print("Shiny reactive logic tested")'},
            {"title": "Tidyverse", "code": 'library(tidyverse)\nprint("Tidyverse loaded")'}
        ],
        "useCases": ["Data science projects", "Academic stats homework", "Kaggle data research"],
        "faqs": [
            {"q": "CRAN packages?", "a": "Includes primary tidyverse, ggplot2, and base R packages by default."},
            {"q": "RStudio?", "a": "This is a lightweight browser alternative to RStudio for quick scripts."},
            {"q": "Shiny support?", "a": "Core Shiny logic is supported for testing, but not web hosting."},
            {"q": "Matrix math?", "a": "Full native support for R matrices and statistical operations."}
        ]
    },
    "html": {
        "name": "HTML/CSS",
        "slug": "html",
        "version": "HTML5/CSS3",
        "target": "Frontend Beginners",
        "tagline": "Live HTML/CSS preview + editor",
        "benefit": "Visual-first web design with instant feedback on every line of code.",
        "examples": [
            {"title": "Responsive Navbar", "code": '<nav style="background: #333; color: white; padding: 1rem;">Logo</nav>'},
            {"title": "CSS Grid", "code": '<div style="display: grid; grid-template-columns: 1fr 1fr;"><div>Left</div><div>Right</div></div>'},
            {"title": "Flexbox", "code": '<div style="display: flex; justify-content: space-between;"><span>A</span><span>B</span></div>'},
            {"title": "Animations", "code": '<div style="animation: spin 2s infinite linear;">Hello</div>'},
            {"title": "Modern Forms", "code": '<form><input type="text" placeholder="Your Name" style="padding: 10px;"></form>'}
        ],
        "useCases": ["Web design practice", "Frontend learning", "Rapid UI prototyping"],
        "faqs": [
            {"q": "JavaScript too?", "a": "Yes, our previewer supports integrated HTML, CSS, and JS code."},
            {"q": "Tailwind support?", "a": "Simply include CDN links in the head to use Tailwind or Bootstrap."},
            {"q": "External Assets?", "a": "You can use any external image or font URL in your code."},
            {"q": "Mobile testing?", "a": "The preview window is fully responsive to different screen sizes."}
        ]
    }
}

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <script src="https://encyclopediaskilled.com/c4/2e/5e/c42e5e96b7bd7419526c97c8e2bdd5fa.js"></script>
    <script src="https://pl28374060.effectivegatecpm.com/c4/2e/5e/c42e5e96b7bd7419526c97c8e2bdd5fa.js"></script>
    
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} Online Compiler - Run {version} Code Instantly | Code Runner Pro</title>
    <meta name="description" content="Free {name} online compiler with VS Code editor. Run {version} code instantly - no installation needed. Perfect for {use_cases_str}. {benefit}">
    <meta name="keywords" content="{name} online compiler, free {name} compiler, run {name} code online, {name} playground">
    
    <meta property="og:title" content="{name} Online Compiler - Code Runner Pro">
    <meta property="og:description" content="Test your {name} code in the cloud with our free compiler.">
    <meta property="og:type" content="website">
    
    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
    <link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png">
    <link rel="icon" type="image/png" sizes="192x192" href="/favicon-192x192.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/favicon-192x192.png">
    <link rel="stylesheet" href="styles.css?v=1.4">
    <script defer src="/_vercel/insights/script.js"></script>
</head>
<body class="compiler-page">
    <div class="app-container">
        <header class="header">
            <div class="logo">
                <a href="index.html" class="logo-link">
                    <div class="logo-icon">
                        <img src="logo.png" alt="CodeRunner Pro" style="width:32px;height:32px;border-radius:6px;">
                    </div>
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

        <main class="page-content">
            <div class="header-content">
                <h1>{name} Online Compiler</h1>
                <p class="tagline">{tagline}. No setup required.</p>
            </div>

            <div class="compiler-container">
                <iframe src="editor.html?lang={slug}&embed=true" title="{name} Editor" width="100%" height="100%" frameborder="0"></iframe>
            </div>

            <div class="ad-container">
                <script type="text/javascript">
                    atOptions = {{ 'key' : '09658977ae434a0281263553b0a86199', 'format' : 'iframe', 'height' : 90, 'width' : 728, 'params' : {{}} }};
                </script>
                <script type="text/javascript" src="https://www.highperformanceformat.com/09658977ae434a0281263553b0a86199/invoke.js"></script>
            </div>

            <article class="seo-section">
                <h2>{name} Online Compiler – Power and Performance in Your Browser</h2>
                <p>Welcome to the most advanced <strong>{name} online compiler</strong> on the web. Whether you are a {target} or a professional programmer, CodeRunner Pro provides a seamless environment to write, debug, and execute your code instantly. No more wasting time on complex installations or environment path errors—just pure coding from any device, anywhere in the world.</p>
                <p>Our cloud-based architecture uses the latest {version} engine to ensure your programs run exactly as they would on a local machine, but with the added benefits of instant accessibility and secure sandboxing. {benefit}</p>
            </article>

            <section class="seo-section features">
                <h2>Professional Features for {name}</h2>
                <div class="feature-grid">
                    <div class="feature-item">
                        <h3>Latest {version} Runtime</h3>
                        <p>We keep our compilers updated with the latest stable releases, including {version}, so you can use modern syntax and libraries.</p>
                    </div>
                    <div class="feature-item">
                        <h3>VS Code Experience</h3>
                        <p>Our editor is built on Monaco, the same engine behind VS Code, giving you shortcuts, syntax highlighting, and themes you love.</p>
                    </div>
                    <div class="feature-item">
                        <h3>Docker-Powered Safety</h3>
                        <p>Your code runs in a isolated, secure Docker container. Experiment freely knowing your session is private and protected.</p>
                    </div>
                    <div class="feature-item">
                        <h3>Lightning Fast</h3>
                        <p>Optimized compiled execution means your {name} code is processed in milliseconds, giving you instant feedback and faster iteration.</p>
                    </div>
                </div>
            </section>

            <section class="seo-section examples">
                <h2>Ready-to-Use {name} Examples</h2>
                <p>Get started quickly with these common patterns and algorithms. Just click "Run Now" to load them directly into the editor.</p>
                {examples_html}
            </section>

            <section class="seo-section use-cases">
                <h2>Is this {name} Compiler right for you?</h2>
                <p>CodeRunner Pro is designed for a diverse range of users, specifically helping {target} solve real-world problems:</p>
                <ul>
                    {use_cases_html}
                </ul>
                <p style="margin-top:20px;">From competitive programming on Codeforces to rapid API prototyping, our {name} playground has everything you need to succeed.</p>
            </section>

            {logic_link_html}

            <section class="seo-section faq">
                <h2>Frequently Asked Questions</h2>
                <div class="faq-list">
                    {faqs_html}
                </div>
            </section>
        </main>

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

    <!-- Schema Markup -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "{name} Online Compiler",
      "operatingSystem": "All",
      "applicationCategory": "DeveloperApplication",
      "description": "Free online {name} compiler and IDE. Run {version} code instantly in your browser with VS Code editor features.",
      "offers": {{
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }},
      "featureList": "Syntax highlighting, Cloud execution, Docker sandboxing, Latest {version} support",
      "url": "https://coderunnerpro.site/{slug}-online-compiler.html"
    }}
    </script>
</body>
</html>"""

import urllib.parse

def generate_pages():
    for key, data in LANGUAGES_DATA.items():
        examples_html = ""
        for ex in data["examples"]:
            # URL encode the code for the Run Now button
            encoded_code = urllib.parse.quote(ex['code'])
            examples_html += f"""
            <div class="example-item">
                <h3>{ex['title']}</h3>
                <a href="editor.html?lang={data['slug']}&code={encoded_code}" class="btn btn-primary btn-run-now">Run Now</a>
                <pre><code>{ex['code']}</code></pre>
            </div>"""
        
        use_cases_html = "".join([f"<li><strong>{uc}</strong></li>" for uc in data["useCases"]])
        faqs_html = ""
        for faq in data["faqs"]:
            faqs_html += f"""
            <div class="faq-item">
                <div class="faq-q">{faq['q']}</div>
                <div class="faq-a">{faq['a']}</div>
            </div>"""
            
        logic_link_html = ""
        if data["slug"] != "html":
            logic_link_html = f'''
            <section class="seo-section logic-mastery" style="background: rgba(var(--accent-rgb), 0.1); border: 1px solid var(--accent-color); border-radius: 12px; padding: 30px; margin-top: 40px; text-align: center;">
                <h2 style="color: var(--accent-color); margin-bottom: 15px;">Master {data["name"]} Problem Solving</h2>
                <p style="font-size: 1.1rem; margin-bottom: 25px;">Ready to level up? We've compiled 17 essential {data["name"]} coding problems with full solutions, explanations, and complexity analysis.</p>
                <a href="17-essential-{data["slug"]}-coding-problems.html" class="btn btn-primary" style="padding: 12px 24px; font-size: 1rem;">View {data["name"]} Interview Questions</a>
            </section>
            '''
            
        use_cases_str = ", ".join(data["useCases"])
        
        filename = f"{data['slug']}-online-compiler.html"
        content = TEMPLATE.format(
            name=data["name"],
            version=data["version"],
            slug=data["slug"],
            target=data["target"],
            tagline=data["tagline"],
            benefit=data["benefit"],
            use_cases_str=use_cases_str,
            examples_html=examples_html,
            use_cases_html=use_cases_html,
            faqs_html=faqs_html,
            logic_link_html=logic_link_html
        )
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {filename}")

if __name__ == "__main__":
    generate_pages()
