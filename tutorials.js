// Tutorials Page JavaScript
// Additional language tutorial content and interactivity

const TUTORIAL_DATA = {
    javascript: {
        icon: '🟨',
        name: 'JavaScript',
        desc: 'Complete JavaScript reference with array, string, object methods and DOM API.',
        categories: [
            {
                title: 'JavaScript Array Methods',
                methods: [
                    { name: 'concat()', desc: 'Joins arrays', code: '[1,2].concat([3,4])' },
                    { name: 'every()', desc: 'Tests all elements', code: 'arr.every(x => x > 0)' },
                    { name: 'filter()', desc: 'Filters elements', code: 'arr.filter(x => x > 2)' },
                    { name: 'find()', desc: 'Finds first match', code: 'arr.find(x => x > 2)' },
                    { name: 'findIndex()', desc: 'Finds index', code: 'arr.findIndex(x => x > 2)' },
                    { name: 'flat()', desc: 'Flattens array', code: '[[1,2],[3]].flat()' },
                    { name: 'forEach()', desc: 'Iterates elements', code: 'arr.forEach(x => log(x))' },
                    { name: 'includes()', desc: 'Checks inclusion', code: '[1,2,3].includes(2)' },
                    { name: 'indexOf()', desc: 'Finds index', code: 'arr.indexOf(2)' },
                    { name: 'join()', desc: 'Joins to string', code: '[1,2,3].join(",")' },
                    { name: 'map()', desc: 'Transforms elements', code: 'arr.map(x => x * 2)' },
                    { name: 'pop()', desc: 'Removes last', code: 'arr.pop()' },
                    { name: 'push()', desc: 'Adds to end', code: 'arr.push(4)' },
                    { name: 'reduce()', desc: 'Reduces to value', code: 'arr.reduce((a,b) => a+b)' },
                    { name: 'reverse()', desc: 'Reverses array', code: 'arr.reverse()' },
                    { name: 'shift()', desc: 'Removes first', code: 'arr.shift()' },
                    { name: 'slice()', desc: 'Extracts portion', code: 'arr.slice(1, 3)' },
                    { name: 'some()', desc: 'Tests some elements', code: 'arr.some(x => x > 5)' },
                    { name: 'sort()', desc: 'Sorts array', code: 'arr.sort((a,b) => a-b)' },
                    { name: 'splice()', desc: 'Changes contents', code: 'arr.splice(1, 2)' },
                    { name: 'unshift()', desc: 'Adds to start', code: 'arr.unshift(0)' }
                ]
            },
            {
                title: 'JavaScript String Methods',
                methods: [
                    { name: 'charAt()', desc: 'Gets character', code: '"hello".charAt(0)' },
                    { name: 'charCodeAt()', desc: 'Gets char code', code: '"A".charCodeAt(0)' },
                    { name: 'concat()', desc: 'Joins strings', code: '"hi".concat(" there")' },
                    { name: 'endsWith()', desc: 'Checks ending', code: '"file.js".endsWith(".js")' },
                    { name: 'includes()', desc: 'Checks substring', code: '"hello".includes("ell")' },
                    { name: 'indexOf()', desc: 'Finds index', code: '"hello".indexOf("l")' },
                    { name: 'lastIndexOf()', desc: 'Finds last index', code: '"hello".lastIndexOf("l")' },
                    { name: 'match()', desc: 'Matches regex', code: '"test".match(/e/)' },
                    { name: 'padEnd()', desc: 'Pads end', code: '"5".padEnd(3, "0")' },
                    { name: 'padStart()', desc: 'Pads start', code: '"5".padStart(3, "0")' },
                    { name: 'repeat()', desc: 'Repeats string', code: '"ab".repeat(3)' },
                    { name: 'replace()', desc: 'Replaces substring', code: '"hi".replace("i", "o")' },
                    { name: 'slice()', desc: 'Extracts portion', code: '"hello".slice(1, 4)' },
                    { name: 'split()', desc: 'Splits string', code: '"a,b,c".split(",")' },
                    { name: 'startsWith()', desc: 'Checks start', code: '"hello".startsWith("he")' },
                    { name: 'substring()', desc: 'Gets substring', code: '"hello".substring(1,4)' },
                    { name: 'toLowerCase()', desc: 'To lowercase', code: '"HELLO".toLowerCase()' },
                    { name: 'toUpperCase()', desc: 'To uppercase', code: '"hello".toUpperCase()' },
                    { name: 'trim()', desc: 'Trims whitespace', code: '" hi ".trim()' },
                    { name: 'trimEnd()', desc: 'Trims end', code: '"hi  ".trimEnd()' },
                    { name: 'trimStart()', desc: 'Trims start', code: '"  hi".trimStart()' }
                ]
            },
            {
                title: 'JavaScript Object Methods',
                methods: [
                    { name: 'Object.assign()', desc: 'Copies properties', code: 'Object.assign({}, obj)' },
                    { name: 'Object.entries()', desc: 'Gets entries', code: 'Object.entries(obj)' },
                    { name: 'Object.freeze()', desc: 'Freezes object', code: 'Object.freeze(obj)' },
                    { name: 'Object.keys()', desc: 'Gets keys', code: 'Object.keys(obj)' },
                    { name: 'Object.values()', desc: 'Gets values', code: 'Object.values(obj)' },
                    { name: 'hasOwnProperty()', desc: 'Checks property', code: 'obj.hasOwnProperty("x")' }
                ]
            }
        ]
    },
    java: {
        icon: '☕',
        name: 'Java',
        desc: 'Complete Java reference with String, Array, Collection, and utility methods.',
        categories: [
            {
                title: 'Java String Methods',
                methods: [
                    { name: 'charAt()', desc: 'Gets character at index', code: 'str.charAt(0)' },
                    { name: 'compareTo()', desc: 'Compares strings', code: 'str.compareTo("other")' },
                    { name: 'concat()', desc: 'Concatenates strings', code: 'str.concat(" world")' },
                    { name: 'contains()', desc: 'Checks substring', code: 'str.contains("sub")' },
                    { name: 'endsWith()', desc: 'Checks ending', code: 'str.endsWith(".txt")' },
                    { name: 'equals()', desc: 'Checks equality', code: 'str.equals("test")' },
                    { name: 'indexOf()', desc: 'Finds index', code: 'str.indexOf("o")' },
                    { name: 'isEmpty()', desc: 'Checks if empty', code: 'str.isEmpty()' },
                    { name: 'length()', desc: 'Gets length', code: 'str.length()' },
                    { name: 'replace()', desc: 'Replaces chars', code: 'str.replace("a", "b")' },
                    { name: 'split()', desc: 'Splits string', code: 'str.split(",")' },
                    { name: 'startsWith()', desc: 'Checks start', code: 'str.startsWith("Hi")' },
                    { name: 'substring()', desc: 'Gets substring', code: 'str.substring(0, 5)' },
                    { name: 'toLowerCase()', desc: 'To lowercase', code: 'str.toLowerCase()' },
                    { name: 'toUpperCase()', desc: 'To uppercase', code: 'str.toUpperCase()' },
                    { name: 'trim()', desc: 'Trims whitespace', code: 'str.trim()' }
                ]
            },
            {
                title: 'Java ArrayList Methods',
                methods: [
                    { name: 'add()', desc: 'Adds element', code: 'list.add("item")' },
                    { name: 'clear()', desc: 'Removes all', code: 'list.clear()' },
                    { name: 'contains()', desc: 'Checks element', code: 'list.contains("x")' },
                    { name: 'get()', desc: 'Gets element', code: 'list.get(0)' },
                    { name: 'indexOf()', desc: 'Finds index', code: 'list.indexOf("x")' },
                    { name: 'isEmpty()', desc: 'Checks empty', code: 'list.isEmpty()' },
                    { name: 'remove()', desc: 'Removes element', code: 'list.remove(0)' },
                    { name: 'set()', desc: 'Sets element', code: 'list.set(0, "new")' },
                    { name: 'size()', desc: 'Gets size', code: 'list.size()' },
                    { name: 'sort()', desc: 'Sorts list', code: 'Collections.sort(list)' },
                    { name: 'toArray()', desc: 'To array', code: 'list.toArray()' }
                ]
            },
            {
                title: 'Java Math Methods',
                methods: [
                    { name: 'Math.abs()', desc: 'Absolute value', code: 'Math.abs(-5)' },
                    { name: 'Math.ceil()', desc: 'Rounds up', code: 'Math.ceil(4.2)' },
                    { name: 'Math.floor()', desc: 'Rounds down', code: 'Math.floor(4.9)' },
                    { name: 'Math.max()', desc: 'Maximum value', code: 'Math.max(5, 10)' },
                    { name: 'Math.min()', desc: 'Minimum value', code: 'Math.min(5, 10)' },
                    { name: 'Math.pow()', desc: 'Power', code: 'Math.pow(2, 3)' },
                    { name: 'Math.random()', desc: 'Random number', code: 'Math.random()' },
                    { name: 'Math.round()', desc: 'Rounds', code: 'Math.round(4.5)' },
                    { name: 'Math.sqrt()', desc: 'Square root', code: 'Math.sqrt(16)' }
                ]
            }
        ]
    },
    cpp: {
        icon: '⚡',
        name: 'C++',
        desc: 'Complete C++ STL reference with vector, string, algorithm functions.',
        categories: [
            {
                title: 'C++ Vector Methods',
                methods: [
                    { name: 'push_back()', desc: 'Adds to end', code: 'vec.push_back(5)' },
                    { name: 'pop_back()', desc: 'Removes last', code: 'vec.pop_back()' },
                    { name: 'size()', desc: 'Gets size', code: 'vec.size()' },
                    { name: 'empty()', desc: 'Checks empty', code: 'vec.empty()' },
                    { name: 'clear()', desc: 'Clears vector', code: 'vec.clear()' },
                    { name: 'front()', desc: 'Gets first', code: 'vec.front()' },
                    { name: 'back()', desc: 'Gets last', code: 'vec.back()' },
                    { name: 'at()', desc: 'Gets at index', code: 'vec.at(0)' },
                    { name: 'insert()', desc: 'Inserts element', code: 'vec.insert(it, val)' },
                    { name: 'erase()', desc: 'Erases element', code: 'vec.erase(it)' },
                    { name: 'begin()', desc: 'Iterator begin', code: 'vec.begin()' },
                    { name: 'end()', desc: 'Iterator end', code: 'vec.end()' }
                ]
            },
            {
                title: 'C++ String Methods',
                methods: [
                    { name: 'length()', desc: 'Gets length', code: 'str.length()' },
                    { name: 'size()', desc: 'Gets size', code: 'str.size()' },
                    { name: 'empty()', desc: 'Checks empty', code: 'str.empty()' },
                    { name: 'append()', desc: 'Appends string', code: 'str.append(" world")' },
                    { name: 'substr()', desc: 'Gets substring', code: 'str.substr(0, 5)' },
                    { name: 'find()', desc: 'Finds substring', code: 'str.find("hello")' },
                    { name: 'replace()', desc: 'Replaces', code: 'str.replace(0, 2, "Hi")' },
                    { name: 'c_str()', desc: 'C-style string', code: 'str.c_str()' },
                    { name: 'compare()', desc: 'Compares strings', code: 'str.compare("other")' }
                ]
            },
            {
                title: 'C++ Algorithm Functions',
                methods: [
                    { name: 'sort()', desc: 'Sorts range', code: 'sort(v.begin(), v.end())' },
                    { name: 'reverse()', desc: 'Reverses range', code: 'reverse(v.begin(), v.end())' },
                    { name: 'find()', desc: 'Finds element', code: 'find(v.begin(), v.end(), x)' },
                    { name: 'count()', desc: 'Counts element', code: 'count(v.begin(), v.end(), x)' },
                    { name: 'max_element()', desc: 'Maximum', code: 'max_element(v.begin(), v.end())' },
                    { name: 'min_element()', desc: 'Minimum', code: 'min_element(v.begin(), v.end())' },
                    { name: 'accumulate()', desc: 'Sum', code: 'accumulate(v.begin(), v.end(), 0)' },
                    { name: 'binary_search()', desc: 'Binary search', code: 'binary_search(v.begin(), v.end(), x)' }
                ]
            }
        ]
    },
    c: {
        icon: '⚙️', name: 'C', desc: 'Complete C tutorial covering fundamentals, pointers, memory management, and file I/O.',
        categories: [
            {
                title: 'C Fundamentals', methods: [
                    { name: 'Variables', desc: 'Storage locations', code: 'int age = 21;' },
                    { name: 'Constants', desc: 'Unchangeable values', code: 'const float PI = 3.14;' },
                    { name: 'Data Types', desc: 'int, float, char, double', code: 'char grade = \'A\';' },
                    { name: 'Input/Output', desc: 'scanf and printf', code: 'scanf("%d", &x);' },
                    { name: 'Operators', desc: 'Arithmetic, Relational', code: 'a + b > c' }
                ]
            },
            {
                title: 'C Flow Control', methods: [
                    { name: 'if...else', desc: 'Conditional logic', code: 'if(x > 0) printf("Pos");' },
                    { name: 'switch', desc: 'Multi-way branch', code: 'switch(x) { case 1: ... }' },
                    { name: 'Loops', desc: 'for, while, do-while', code: 'for(i=0; i<5; i++)' },
                    { name: 'break/continue', desc: 'Loop control', code: 'if(i==3) break;' }
                ]
            },
            {
                title: 'C Functions', methods: [
                    { name: 'Declaration', desc: 'Function prototype', code: 'int add(int a, int b);' },
                    { name: ' Recursion', desc: 'Function calls itself', code: 'return n * fact(n-1);' },
                    { name: 'Scope', desc: 'Local vs Global', code: 'int globalVar = 100;' }
                ]
            },
            {
                title: 'C Arrays & Pointers', methods: [
                    { name: 'Arrays', desc: 'Collection of items', code: 'int arr[5] = {1,2,3,4,5};' },
                    { name: 'Pointers', desc: 'Address variable', code: 'int *ptr = &x;' },
                    { name: 'Pointer Operations', desc: 'Arithmetic, Dereference', code: '*ptr = 10; ptr++;' },
                    { name: 'Dynamic Memory', desc: 'malloc, free', code: 'ptr = (int*)malloc(size);' }
                ]
            },
            {
                title: 'C Strings & Structs', methods: [
                    { name: 'Strings', desc: 'Character arrays', code: 'char str[] = "Hello";' },
                    { name: 'String Functions', desc: 'strlen, strcpy, strcat', code: 'len = strlen(str);' },
                    { name: 'Structure', desc: 'Custom data type', code: 'struct Point { int x, y; };' },
                    { name: 'Union', desc: 'Shared memory', code: 'union Data { int i; float f; };' }
                ]
            },
            {
                title: 'C Files & Extras', methods: [
                    { name: 'File I/O', desc: 'Read/Write files', code: 'fp = fopen("file.txt", "w");' },
                    { name: 'fprintf/fscanf', desc: 'File operations', code: 'fprintf(fp, "%d", x);' },
                    { name: 'Enums', desc: 'Enumerations', code: 'enum Color { RED, GREEN };' },
                    { name: 'Preprocessor', desc: 'Macros, Include', code: '#define MAX 100' }
                ]
            }
        ]
    },
    csharp: {
        icon: '💜', name: 'C#', desc: 'Comprehensive C# guide covering OOP, inheritance, collections, and LINQ.',
        categories: [
            {
                title: 'Introduction & Flow', methods: [
                    { name: 'Variables', desc: 'int, string, bool', code: 'int x = 10;' },
                    { name: 'Conditionals', desc: 'if, switch', code: 'if (x > 5) { ... }' },
                    { name: 'Loops', desc: 'for, foreach, while', code: 'foreach(var x in list)' },
                    { name: 'Arrays', desc: 'Single & Multi-dim', code: 'int[] arr = {1, 2, 3};' }
                ]
            },
            {
                title: 'C# OOP Basics', methods: [
                    { name: 'Classes', desc: 'Blueprint for objects', code: 'class Person { ... }' },
                    { name: 'Objects', desc: 'Instances', code: 'var p = new Person();' },
                    { name: 'Properties', desc: 'Getters/Setters', code: 'public int Age { get; set; }' },
                    { name: 'Methods', desc: 'Functions', code: 'public void SayHi() { ... }' }
                ]
            },
            {
                title: 'C# OOP Advanced', methods: [
                    { name: 'Inheritance', desc: 'Base & Derived', code: 'class Dog : Animal { ... }' },
                    { name: 'Polymorphism', desc: 'Override/Overload', code: 'public override void Run() { ... }' },
                    { name: 'Abstract Class', desc: 'Partial class', code: 'abstract class Shape { ... }' },
                    { name: 'Interface', desc: 'Contract', code: 'interface IMovable { ... }' },
                    { name: 'Sealed Class', desc: 'Prevent inheritance', code: 'sealed class Final { ... }' }
                ]
            },
            {
                title: 'Advanced Topics', methods: [
                    { name: 'Partial Class', desc: 'Split definition', code: 'partial class User { ... }' },
                    { name: 'Exception Handling', desc: 'try-catch-finally', code: 'try { ... } catch (Ex e) { ... }' },
                    { name: 'Collections', desc: 'List, Dictionary', code: 'var list = new List<int>();' },
                    { name: 'LINQ', desc: 'Query syntax', code: 'list.Where(x => x > 5)' }
                ]
            }
        ]
    },
    typescript: {
        icon: '🔷', name: 'TypeScript', desc: 'Complete TypeScript guide including types, interfaces, generics, and modules.',
        categories: [
            {
                title: 'Basic Types', methods: [
                    { name: 'Primitives', desc: 'string, number, boolean', code: 'let age: number = 25;' },
                    { name: 'Arrays', desc: 'Typed arrays', code: 'let list: number[] = [1, 2];' },
                    { name: 'Tuples', desc: 'Fixed types', code: 'let x: [string, number];' },
                    { name: 'Enums', desc: 'Named constants', code: 'enum Color { Red, Green }' },
                    { name: 'Any/Void', desc: 'Dynamic/No return', code: 'let x: any = 4;' }
                ]
            },
            {
                title: 'Interfaces & Classes', methods: [
                    { name: 'Interfaces', desc: 'Structure contract', code: 'interface User { name: string; }' },
                    { name: 'Classes', desc: 'OOP Blueprint', code: 'class Point { x: number; }' },
                    { name: 'Access Modifiers', desc: 'public, private', code: 'private id: number;' },
                    { name: 'Implements', desc: 'Class interface', code: 'class User implements Person' }
                ]
            },
            {
                title: 'Advanced Types', methods: [
                    { name: 'Generics', desc: 'Reusable types', code: 'function identity<T>(arg: T): T' },
                    { name: 'Union Types', desc: 'Multiple types', code: 'let id: string | number;' },
                    { name: 'Type Alias', desc: 'Custom name', code: 'type ID = string | number;' },
                    { name: 'Utility Types', desc: 'Partial, Pick, Omit', code: 'Partial<User>' }
                ]
            },
            {
                title: 'Functions & Modules', methods: [
                    { name: 'Functions', desc: 'Typed arguments', code: 'function add(x: number): number' },
                    { name: 'Optional Params', desc: '?', code: 'function buildName(first: string, last?: string)' },
                    { name: 'Modules', desc: 'Import/Export', code: 'export interface StringValidator...' }
                ]
            }
        ]
    },
    go: {
        icon: '🐹', name: 'Go', desc: 'Complete Go guide covering goroutines, channels, interfaces, and packages.',
        categories: [
            {
                title: 'Go Basics', methods: [
                    { name: 'Variables', desc: 'Short declaration', code: 'x := 10' },
                    { name: 'Constants', desc: 'Immutable values', code: 'const PI = 3.14' },
                    { name: 'For Loop', desc: 'Only loop in Go', code: 'for i := 0; i < 5; i++' },
                    { name: 'If/Else', desc: 'Conditionals', code: 'if x > 0 { ... }' },
                    { name: 'Switch', desc: 'Select case', code: 'switch os { case "mac": ... }' }
                ]
            },
            {
                title: 'Data Structures', methods: [
                    { name: 'Arrays', desc: 'Fixed size', code: 'var a [5]int' },
                    { name: 'Slices', desc: 'Dynamic array', code: 's := []int{1, 2, 3}' },
                    { name: 'Maps', desc: 'Key-value', code: 'm := map[string]int{"a": 1}' },
                    { name: 'Structs', desc: 'Custom types', code: 'type User struct { Name string }' }
                ]
            },
            {
                title: 'Functions & Methods', methods: [
                    { name: 'Functions', desc: 'Multiple returns', code: 'func swap(x, y string) (string, string)' },
                    { name: 'Methods', desc: 'Attached to types', code: 'func (u User) SayHi() { ... }' },
                    { name: 'Interfaces', desc: 'Signatures', code: 'type Shape interface { Area() float64 }' },
                    { name: 'Defer', desc: 'Cleanup', code: 'defer fmt.Println("Done")' }
                ]
            },
            {
                title: 'Concurrency', methods: [
                    { name: 'Goroutines', desc: 'Lightweight threads', code: 'go f(x, y, z)' },
                    { name: 'Channels', desc: 'Communication', code: 'ch <- v    // Send' },
                    { name: 'Select', desc: 'Wait on channels', code: 'select { case msg := <-ch: ... }' },
                    { name: 'WaitGroups', desc: 'Sync', code: 'var wg sync.WaitGroup' }
                ]
            }
        ]
    },
    rust: {
        icon: '🦀', name: 'Rust', desc: 'Comprehensive Rust guide including ownership, borrowing, lifetimes, and traits.',
        categories: [
            {
                title: 'Rust Basics', methods: [
                    { name: 'Variables', desc: 'Immutability by default', code: 'let x = 5; let mut y = 10;' },
                    { name: 'Data Types', desc: 'i32, f64, bool, char', code: 'let x: i32 = 42;' },
                    { name: 'Functions', desc: 'Snake case', code: 'fn main() { ... }' },
                    { name: 'Control Flow', desc: 'if, loop, while, for', code: 'for x in 0..5 { ... }' }
                ]
            },
            {
                title: 'Ownership & Borrowing', methods: [
                    { name: 'Ownership', desc: 'Move semantics', code: 'let s1 = String::from("hi"); let s2 = s1;' },
                    { name: 'Borrowing', desc: 'References &', code: 'fn calc(s: &String) { ... }' },
                    { name: 'Slices', desc: 'View into collection', code: '&s[0..5]' },
                    { name: 'Lifetimes', desc: 'Scope validation', code: 'fn longest<\'a>(x: &\'a str, y: &\'a str)' }
                ]
            },
            {
                title: 'Structs & Enums', methods: [
                    { name: 'Structs', desc: 'Custom data', code: 'struct User { name: String }' },
                    { name: 'Enums', desc: 'Variants', code: 'enum IpAddr { V4, V6 }' },
                    { name: 'Match', desc: 'Pattern matching', code: 'match guess { 1 => println!("One"), ... }' },
                    { name: 'Option', desc: 'Null safety', code: 'Option<T> = Some(T) | None' }
                ]
            },
            {
                title: 'Collections & Error', methods: [
                    { name: 'Vectors', desc: 'Resizable array', code: 'let v: Vec<i32> = Vec::new();' },
                    { name: 'HashMap', desc: 'Key-value', code: 'scores.insert(String::from("Blue"), 10);' },
                    { name: 'Result', desc: 'Error handling', code: 'Result<T, E> = Ok(T) | Err(E)' },
                    { name: 'Panic', desc: 'Unrecoverable', code: 'panic!("crash and burn");' }
                ]
            }
        ]
    },
    ruby: {
        icon: '💎', name: 'Ruby', desc: 'Ruby guide covering OOP, blocks, modules, and metaprogramming.',
        categories: [
            {
                title: 'Ruby Basics', methods: [
                    { name: 'Variables', desc: 'Dynamic typing', code: 'name = "John"' },
                    { name: 'Symbols', desc: 'Immutable strings', code: ':status' },
                    { name: 'Strings', desc: 'Interpolation', code: '"Hello #{name}"' },
                    { name: 'Control', desc: 'If, unless, case', code: 'puts "Hi" if true' }
                ]
            },
            {
                title: 'Collections', methods: [
                    { name: 'Arrays', desc: 'Ordered list', code: 'arr = [1, "two", 3.0]' },
                    { name: 'Hashes', desc: 'Key-value pairs', code: 'options = { font: "Arial", size: 10 }' },
                    { name: 'Ranges', desc: 'Intervals', code: '(1..5).each { |i| puts i }' },
                    { name: 'Enumerables', desc: 'map, select, reject', code: 'arr.map { |x| x * 2 }' }
                ]
            },
            {
                title: 'OOP & Modules', methods: [
                    { name: 'Classes', desc: 'Definition', code: 'class Person; end' },
                    { name: 'Methods', desc: 'Definition', code: 'def speak; puts "Hi"; end' },
                    { name: 'Modules', desc: 'Namespaces/Mixins', code: 'module Greetable; end' },
                    { name: 'Attr Accessor', desc: 'Getters/Setters', code: 'attr_accessor :name' }
                ]
            },
            {
                title: 'Blocks & Procs', methods: [
                    { name: 'Blocks', desc: 'Code chunks', code: '[1,2,3].each { |n| puts n }' },
                    { name: 'Yield', desc: 'Call block', code: 'def wrap; yield; end' },
                    { name: 'Procs/Lambdas', desc: 'Saved blocks', code: 'say = -> { puts "Hi" }' },
                    { name: 'Exceptions', desc: 'Rescue', code: 'begin; 1/0; rescue; puts "Error"; end' }
                ]
            }
        ]
    },
    php: {
        icon: '🐘', name: 'PHP', desc: 'Complete PHP guide for web development, forms, and database interaction.',
        categories: [
            {
                title: 'PHP Basics', methods: [
                    { name: 'Variables', desc: 'Starts with $', code: '$count = 5;' },
                    { name: 'Echo/Print', desc: 'Output', code: 'echo "Hello " . $name;' },
                    { name: 'Data Types', desc: 'String, Integer, Float', code: '$f = 10.5;' },
                    { name: 'Control Flow', desc: 'If, Switch, Loops', code: 'foreach ($arr as $v) { ... }' }
                ]
            },
            {
                title: 'Arrays & Forms', methods: [
                    { name: 'Indexed Arrays', desc: 'Numeric keys', code: '$cars = array("Volvo", "BMW");' },
                    { name: 'Assoc Arrays', desc: 'Named keys', code: '$age = array("Peter"=>"35");' },
                    { name: 'Superglobals', desc: '$_GET, $_POST', code: '$name = $_POST["name"];' },
                    { name: 'Sessions', desc: 'User data', code: '$_SESSION["fav"] = "green";' }
                ]
            },
            {
                title: 'Functions & Strings', methods: [
                    { name: 'Functions', desc: 'Definition', code: 'function add($x, $y) { return $x + $y; }' },
                    { name: 'String Funcs', desc: 'strlen, strpos', code: 'echo strlen("Hello world!");' },
                    { name: 'Date/Time', desc: 'Formatting', code: 'echo date("Y/m/d");' },
                    { name: 'Includes', desc: 'File inclusion', code: 'include "header.php";' }
                ]
            },
            {
                title: 'PHP OOP & MySQL', methods: [
                    { name: 'Classes', desc: 'Blueprint', code: 'class Fruit { public $name; }' },
                    { name: 'Objects', desc: 'Instances', code: '$apple = new Fruit();' },
                    { name: 'Constructor', desc: 'Init', code: 'function __construct($name) { ... }' },
                    { name: 'MySQLi', desc: 'Database conn', code: '$conn = new mysqli($server, $user...);' }
                ]
            }
        ]
    },
    swift: {
        icon: '🦅', name: 'Swift', desc: 'Complete Swift guide covering optionals, closures, structs, and classes.',
        categories: [
            {
                title: 'Swift Basics', methods: [
                    { name: 'Variables', desc: 'var (mutable), let (constant)', code: 'var x = 10; let pi = 3.14' },
                    { name: 'Data Types', desc: 'Int, Double, String, Bool', code: 'var name: String = "Swift"' },
                    { name: 'Control Flow', desc: 'If, Switch, Loops', code: 'for i in 1...5 { ... }' },
                    { name: 'Optionals', desc: 'Handle nulls', code: 'var name: String? = nil' }
                ]
            },
            {
                title: 'Collections', methods: [
                    { name: 'Arrays', desc: 'Ordered list', code: 'var arr = [1, 2, 3]' },
                    { name: 'Sets', desc: 'Unique values', code: 'var set: Set = [1, 2, 3]' },
                    { name: 'Dictionaries', desc: 'Key-value', code: 'var dict = ["a": 1, "b": 2]' },
                    { name: 'Tuples', desc: 'Grouped values', code: 'let http404 = (404, "Error")' }
                ]
            },
            {
                title: 'Functions & Closures', methods: [
                    { name: 'Functions', desc: 'Definition', code: 'fn greet(name: String) -> String' },
                    { name: 'Closures', desc: 'Inline functions', code: '{ (s: String) in return s }' },
                    { name: 'Guard', desc: 'Early exit', code: 'guard let x = y else { return }' },
                    { name: 'Defer', desc: 'Execution order', code: 'defer { cleanUp() }' }
                ]
            },
            {
                title: 'Structures & Classes', methods: [
                    { name: 'Structures', desc: 'Value type', code: 'struct Point { var x = 0.0 }' },
                    { name: 'Classes', desc: 'Reference type', code: 'class Person { var name = "" }' },
                    { name: 'Properties', desc: 'Stored/Computed', code: 'var area: Double { w * h }' },
                    { name: 'Extensions', desc: 'Add functionality', code: 'extension Int { ... }' }
                ]
            }
        ]
    },
    dart: {
        icon: '🎯', name: 'Dart', desc: 'Complete Dart guide for Flutter development, async programming, and OOP.',
        categories: [
            {
                title: 'Dart Basics', methods: [
                    { name: 'Variables', desc: 'Type inference', code: 'var name = "Dart";' },
                    { name: 'Null Safety', desc: 'Avoid null errors', code: 'String? name; // nullable' },
                    { name: 'Control Flow', desc: 'If, switch, loops', code: 'if (year >= 2000) { ... }' },
                    { name: 'Functions', desc: 'Named parameters', code: 'void enable({bool? bold})' }
                ]
            },
            {
                title: 'OOP Features', methods: [
                    { name: 'Classes', desc: 'Blueprint', code: 'class Spacecraft { ... }' },
                    { name: 'Mixins', desc: 'Reuse code', code: 'mixin Piloted { ... }' },
                    { name: 'Interfaces', desc: 'Implicit interfaces', code: 'class Mock implements Point' },
                    { name: 'Constructors', desc: 'Initializers', code: 'Point(this.x, this.y);' }
                ]
            },
            {
                title: 'Async Programming', methods: [
                    { name: 'Futures', desc: 'Async result', code: 'Future<String> fetch() { ... }' },
                    { name: 'Async/Await', desc: 'Clean syntax', code: 'var x = await fetch();' },
                    { name: 'Streams', desc: 'Event sequence', code: 'Stream<int> count() async*' },
                    { name: 'Isolate', desc: 'Concurrency', code: 'Isolate.spawn(entry, msg)' }
                ]
            },
            {
                title: 'Collections', methods: [
                    { name: 'Lists', desc: 'Ordered group', code: 'var list = [1, 2, 3];' },
                    { name: 'Sets', desc: 'Unique items', code: 'var set = {"a", "b"};' },
                    { name: 'Maps', desc: 'Key-value', code: 'var map = {1: "one"};' },
                    { name: 'Spread', desc: 'Insert types', code: 'var list2 = [0, ...list];' }
                ]
            }
        ]
    },
    scala: {
        icon: '🔴', name: 'Scala', desc: 'Complete Scala guide combining OOP and functional programming paradigms.',
        categories: [
            {
                title: 'Scala Basics', methods: [
                    { name: 'Variables', desc: 'val (immutable), var', code: 'val x = 10; var y = 20' },
                    { name: 'Functions', desc: 'Def keyword', code: 'def add(x: Int, y: Int): Int' },
                    { name: 'Control', desc: 'If as expression', code: 'val res = if(x>0) 1 else -1' },
                    { name: 'Classes', desc: 'Primary constructor', code: 'class User(name: String)' }
                ]
            },
            {
                title: 'Functional Features', methods: [
                    { name: 'Higher Order', desc: 'Func as param', code: 'list.map(x => x * 2)' },
                    { name: 'Pattern Matching', desc: 'Switch on steroids', code: 'x match { case 1 => "one" }' },
                    { name: 'Case Classes', desc: 'Immutable data', code: 'case class Point(x: Int)' },
                    { name: 'Traits', desc: 'Interfaces+', code: 'trait Shape { def area(): Int }' }
                ]
            },
            {
                title: 'Collections', methods: [
                    { name: 'List', desc: 'Immutable linked list', code: 'val list = List(1, 2, 3)' },
                    { name: 'Map', desc: 'Key-value pairs', code: 'val map = Map("a" -> 1)' },
                    { name: 'Set', desc: 'Unique elements', code: 'val set = Set(1, 2, 3)' },
                    { name: 'Tuple', desc: 'Grouped types', code: 'val t = (1, "hello", true)' }
                ]
            }
        ]
    },
    r: {
        icon: '📊', name: 'R', desc: 'Complete R guide for statistical computing, data analysis, and plotting.',
        categories: [
            {
                title: 'R Fundamentals', methods: [
                    { name: 'Variables', desc: 'Assignment', code: 'x <- 42' },
                    { name: 'Vectors', desc: 'Basic structure', code: 'v <- c(1, 2, 3, 4)' },
                    { name: 'Matrices', desc: '2D array', code: 'm <- matrix(1:6, nrow=2)' },
                    { name: 'Data Frames', desc: 'Tables', code: 'df <- data.frame(id=1:3, val=c("a","b","c"))' }
                ]
            },
            {
                title: 'Statistics & Math', methods: [
                    { name: 'Summary', desc: 'Stats overview', code: 'summary(df)' },
                    { name: 'Mean/Median', desc: 'Averages', code: 'mean(x); median(x)' },
                    { name: 'Tests', desc: 'Hypothesis testing', code: 't.test(x, y)' },
                    { name: 'Distributions', desc: 'Normal dist', code: 'rnorm(100, mean=0, sd=1)' }
                ]
            },
            {
                title: 'File & Plotting', methods: [
                    { name: 'Read CSV', desc: 'Load data', code: 'data <- read.csv("file.csv")' },
                    { name: 'Plot', desc: 'Basic plot', code: 'plot(x, y)' },
                    { name: 'Hist', desc: 'Histogram', code: 'hist(x)' },
                    { name: 'Packages', desc: 'Install libs', code: 'install.packages("ggplot2")' }
                ]
            },
            {
                title: 'Control Flow', methods: [
                    { name: 'If', desc: 'Condition', code: 'if (x > 0) { ... }' },
                    { name: 'For', desc: 'Loop', code: 'for (i in 1:10) { ... }' },
                    { name: 'Functions', desc: 'Definition', code: 'f <- function(a) { a*a }' },
                    { name: 'Apply', desc: 'Vector operations', code: 'lapply(list, function)' }
                ]
            }
        ]
    },
    sql: {
        icon: '🗃️', name: 'SQL', desc: 'Complete SQL guide including queries, joins, aggregation, and DDL.',
        categories: [
            {
                title: 'Basic Queries', methods: [
                    { name: 'SELECT', desc: 'Retrieve data', code: 'SELECT * FROM users;' },
                    { name: 'WHERE', desc: 'Filter rows', code: 'SELECT * FROM users WHERE age > 18;' },
                    { name: 'ORDER BY', desc: 'Sort results', code: 'ORDER BY name ASC;' },
                    { name: 'LIMIT', desc: 'Restrict count', code: 'LIMIT 10;' },
                    { name: 'DISTINCT', desc: 'Unique values', code: 'SELECT DISTINCT country FROM users;' }
                ]
            },
            {
                title: 'Joins & Unions', methods: [
                    { name: 'INNER JOIN', desc: 'Matching rows', code: 'SELECT * FROM A JOIN B ON A.id = B.id;' },
                    { name: 'LEFT JOIN', desc: 'All from left', code: 'SELECT * FROM A LEFT JOIN B ON ...' },
                    { name: 'FULL JOIN', desc: 'All rows', code: 'SELECT * FROM A FULL JOIN B ...' },
                    { name: 'UNION', desc: 'Combine sets', code: 'SELECT id FROM A UNION SELECT id FROM B;' }
                ]
            },
            {
                title: 'Aggregation', methods: [
                    { name: 'COUNT', desc: 'Count rows', code: 'SELECT COUNT(*) FROM orders;' },
                    { name: 'SUM/AVG', desc: 'Math stats', code: 'SELECT AVG(price) FROM products;' },
                    { name: 'GROUP BY', desc: 'Group result', code: 'GROUP BY category;' },
                    { name: 'HAVING', desc: 'Filter groups', code: 'GROUP BY cat HAVING COUNT > 5;' }
                ]
            },
            {
                title: 'DDL & Modification', methods: [
                    { name: 'INSERT', desc: 'Add row', code: 'INSERT INTO users (name) VALUES ("John");' },
                    { name: 'UPDATE', desc: 'Modify row', code: 'UPDATE users SET age = 21 WHERE id = 1;' },
                    { name: 'DELETE', desc: 'Remove row', code: 'DELETE FROM users WHERE id = 1;' },
                    { name: 'CREATE', desc: 'New table', code: 'CREATE TABLE users (id INT, name TEXT);' }
                ]
            }
        ]
    },
    html: {
        icon: '🌐', name: 'HTML/CSS', desc: 'Comprehensive HTML5 and CSS3 guide for modern web development.',
        categories: [
            {
                title: 'HTML Structure', methods: [
                    { name: 'Document', desc: 'Basic skeleton', code: '<!DOCTYPE html><html>...</html>' },
                    { name: 'Head/Body', desc: 'Metadata/Content', code: '<head>...</head><body>...</body>' },
                    { name: 'Semantics', desc: 'Meaningful tags', code: '<header>, <nav>, <main>, <footer>' },
                    { name: 'Text', desc: 'Headings/Para', code: '<h1>Title</h1><p>Text</p>' }
                ]
            },
            {
                title: 'HTML Forms & Media', methods: [
                    { name: 'Images', desc: 'Display img', code: '<img src="url" alt="desc">' },
                    { name: 'Links', desc: 'Anchor tag', code: '<a href="url">Link</a>' },
                    { name: 'Inputs', desc: 'Data entry', code: '<input type="text" placeholder="..."> ' },
                    { name: 'Buttons', desc: 'Clickable', code: '<button>Click Me</button>' }
                ]
            },
            {
                title: 'CSS Basics', methods: [
                    { name: 'Selectors', desc: 'Targeting', code: '.class, #id, element' },
                    { name: 'Box Model', desc: 'Layout core', code: 'margin: 10px; padding: 20px;' },
                    { name: 'Typography', desc: 'Text styling', code: 'font-size: 16px; color: #333;' },
                    { name: 'Backgrounds', desc: 'Colors/Images', code: 'background: url("bg.jpg");' }
                ]
            },
            {
                title: 'CSS Layout', methods: [
                    { name: 'Flexbox', desc: '1D Layout', code: 'display: flex; justify-content: center;' },
                    { name: 'Grid', desc: '2D Layout', code: 'display: grid; grid-template-columns: 1fr 1fr;' },
                    { name: 'Responsive', desc: 'Media queries', code: '@media (max-width: 768px) { ... }' },
                    { name: 'Position', desc: 'Placement', code: 'position: absolute; top: 0;' }
                ]
            }
        ]
    }
};

// Render additional language sections
function renderLanguageSections() {
    const content = document.querySelector('.tutorials-content');
    if (!content) return;

    Object.entries(TUTORIAL_DATA).forEach(([langId, lang]) => {
        const section = document.createElement('section');
        section.id = langId;
        section.className = 'lang-section';

        let categoriesHTML = '';
        lang.categories.forEach(cat => {
            let methodsHTML = cat.methods.map(m => `
                <div class="method-card">
                    <h4>${m.name}</h4>
                    <p>${m.desc}</p>
                    <code>${m.code}</code>
                </div>
            `).join('');

            categoriesHTML += `
                <div class="tutorial-category">
                    <h3 class="category-title">${cat.title}</h3>
                    <div class="methods-grid">${methodsHTML}</div>
                </div>
            `;
        });

        section.innerHTML = `
            <div class="lang-header">
                <span class="lang-icon-lg">${lang.icon}</span>
                <div>
                    <h2>${lang.name} Tutorial</h2>
                    <p>${lang.desc}</p>
                </div>
                <a href="editor.html?lang=${langId}" class="btn btn-primary">Try ${lang.name}</a>
            </div>
            ${categoriesHTML}
        `;

        content.appendChild(section);
    });
}

// Sidebar navigation
function initSidebarNav() {
    const links = document.querySelectorAll('.sidebar-link');
    const sections = document.querySelectorAll('.lang-section');

    links.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href').substring(1);

            links.forEach(l => l.classList.remove('active'));
            link.classList.add('active');

            sections.forEach(s => s.classList.remove('active'));
            const targetSection = document.getElementById(targetId);
            if (targetSection) {
                targetSection.classList.add('active');
                targetSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });
}

// Search functionality
function initSearch() {
    const searchInput = document.getElementById('tutorialSearch');
    if (!searchInput) return;

    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase();
        const cards = document.querySelectorAll('.method-card');

        cards.forEach(card => {
            const text = card.textContent.toLowerCase();
            card.style.display = text.includes(query) ? 'block' : 'none';
        });
    });
}

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', () => {
    renderLanguageSections();
    initSidebarNav();
    initSearch();
});
