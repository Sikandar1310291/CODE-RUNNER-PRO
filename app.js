// ===== Language Configuration with Icons =====
const LANGUAGES = {
    python: {
        id: 'python',
        name: 'Python',
        icon: '🐍',
        monaco: 'python',
        piston: 'python',
        version: '3.10',
        extension: '.py',
        template: `# Python 3 - Welcome to CodeRunner Pro!
print("Hello, World!")

# Example with input
name = "Developer"
print(f"Welcome, {name}!")

# Quick math
numbers = [1, 2, 3, 4, 5]
print(f"Sum: {sum(numbers)}")
`
    },
    r: {
        id: 'r',
        name: 'R',
        icon: '📊',
        monaco: 'r',
        piston: 'r',
        version: '4.1.1',
        extension: '.r',
        template: `# R Programming
print("Hello, World!")

# Vector operations
numbers <- c(1, 2, 3, 4, 5)
print(paste("Mean:", mean(numbers)))
print(paste("Sum:", sum(numbers)))
`
    },
    sql: {
        id: 'sql',
        name: 'SQL',
        icon: '🗃️',
        monaco: 'sql',
        piston: 'sqlite3',
        version: '3.36.0',
        extension: '.sql',
        template: `-- SQL Example (SQLite)
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);

INSERT INTO users (name, email) VALUES 
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com');

SELECT * FROM users;
`
    },
    java: {
        id: 'java',
        name: 'Java',
        icon: '☕',
        monaco: 'java',
        piston: 'java',
        version: '15.0.2',
        extension: '.java',
        template: `public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        
        // Variables and loops
        String name = "Java Developer";
        System.out.println("Welcome, " + name + "!");
        
        for (int i = 1; i <= 5; i++) {
            System.out.println("Count: " + i);
        }
    }
}
`
    },
    c: {
        id: 'c',
        name: 'C',
        icon: '⚙️',
        monaco: 'c',
        piston: 'c',
        version: '10.2.0',
        extension: '.c',
        template: `#include <stdio.h>

int main() {
    printf("Hello, World!\\n");
    
    // Variables and loops
    int sum = 0;
    for (int i = 1; i <= 5; i++) {
        sum += i;
        printf("Sum so far: %d\\n", sum);
    }
    
    return 0;
}
`
    },
    cpp: {
        id: 'cpp',
        name: 'C++',
        icon: '⚡',
        monaco: 'cpp',
        piston: 'c++',
        version: '10.2.0',
        extension: '.cpp',
        template: `#include <iostream>
#include <vector>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    
    // Modern C++ features
    vector<int> numbers = {1, 2, 3, 4, 5};
    
    cout << "Numbers: ";
    for (const auto& num : numbers) {
        cout << num << " ";
    }
    cout << endl;
    
    return 0;
}
`
    },
    csharp: {
        id: 'csharp',
        name: 'C#',
        icon: '💜',
        monaco: 'csharp',
        piston: 'csharp',
        version: '6.12.0',
        extension: '.cs',
        template: `using System;
using System.Linq;

class Program {
    static void Main() {
        Console.WriteLine("Hello, World!");
        
        // LINQ example
        int[] numbers = {1, 2, 3, 4, 5};
        var doubled = numbers.Select(n => n * 2);
        
        Console.WriteLine("Doubled: " + string.Join(", ", doubled));
    }
}
`
    },
    javascript: {
        id: 'javascript',
        name: 'JavaScript',
        icon: '🟨',
        monaco: 'javascript',
        piston: 'javascript',
        version: '18.15.0',
        extension: '.js',
        template: `// JavaScript (Node.js)
console.log("Hello, World!");

// Modern JS features
const greet = (name) => \`Welcome, \${name}!\`;
console.log(greet("Developer"));

// Array methods
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(n => n * 2);
console.log("Doubled:", doubled);

// Async example
const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));
console.log("JavaScript is awesome! 🚀");
`
    },
    typescript: {
        id: 'typescript',
        name: 'TypeScript',
        icon: '🔷',
        monaco: 'typescript',
        piston: 'typescript',
        version: '5.0.3',
        extension: '.ts',
        template: `// TypeScript
interface User {
    name: string;
    age: number;
    role: "admin" | "user";
}

const user: User = {
    name: "Alice",
    age: 30,
    role: "admin"
};

console.log("Hello, World!");
console.log(\`User: \${user.name}, Age: \${user.age}, Role: \${user.role}\`);

// Generic function
function identity<T>(arg: T): T {
    return arg;
}

console.log(identity<string>("TypeScript rocks! 💪"));
`
    },
    go: {
        id: 'go',
        name: 'Go',
        icon: '🐹',
        monaco: 'go',
        piston: 'go',
        version: '1.16.2',
        extension: '.go',
        template: `package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
    
    // Slices and loops
    numbers := []int{1, 2, 3, 4, 5}
    
    sum := 0
    for _, num := range numbers {
        sum += num
    }
    
    fmt.Printf("Sum of %v = %d\\n", numbers, sum)
}
`
    },
    rust: {
        id: 'rust',
        name: 'Rust',
        icon: '🦀',
        monaco: 'rust',
        piston: 'rust',
        version: '1.68.2',
        extension: '.rs',
        template: `fn main() {
    println!("Hello, World!");
    
    // Variables and ownership
    let name = String::from("Rustacean");
    println!("Welcome, {}!", name);
    
    // Vectors and iterators
    let numbers = vec![1, 2, 3, 4, 5];
    let sum: i32 = numbers.iter().sum();
    println!("Sum: {}", sum);
}
`
    },
    scala: {
        id: 'scala',
        name: 'Scala',
        icon: '🔴',
        monaco: 'scala',
        piston: 'scala',
        version: '3.2.2',
        extension: '.scala',
        template: `object Main extends App {
    println("Hello, World!")
    
    // Functional programming
    val numbers = List(1, 2, 3, 4, 5)
    val doubled = numbers.map(_ * 2)
    
    println(s"Original: $numbers")
    println(s"Doubled: $doubled")
}
`
    },
    dart: {
        id: 'dart',
        name: 'Dart',
        icon: '🎯',
        monaco: 'dart',
        piston: 'dart',
        version: '2.19.6',
        extension: '.dart',
        template: `void main() {
  print('Hello, World!');
  
  // Variables and null safety
  String name = 'Dart Developer';
  print('Welcome, $name!');
  
  // Collections
  var numbers = [1, 2, 3, 4, 5];
  var sum = numbers.reduce((a, b) => a + b);
  print('Sum: $sum');
}
`
    },
    ruby: {
        id: 'ruby',
        name: 'Ruby',
        icon: '💎',
        monaco: 'ruby',
        piston: 'ruby',
        version: '3.0.1',
        extension: '.rb',
        template: `# Ruby
puts "Hello, World!"

# Variables and string interpolation
name = "Rubyist"
puts "Welcome, #{name}!"

# Array operations
numbers = [1, 2, 3, 4, 5]
puts "Sum: #{numbers.sum}"
puts "Doubled: #{numbers.map { |n| n * 2 }}"
`
    },
    php: {
        id: 'php',
        name: 'PHP',
        icon: '🐘',
        monaco: 'php',
        piston: 'php',
        version: '8.2.3',
        extension: '.php',
        template: `<?php
echo "Hello, World!\\n";

// Variables and functions
$name = "PHP Developer";
echo "Welcome, $name!\\n";

// Arrays
$numbers = [1, 2, 3, 4, 5];
$sum = array_sum($numbers);
echo "Sum: $sum\\n";

// Mapping
$doubled = array_map(fn($n) => $n * 2, $numbers);
echo "Doubled: " . implode(", ", $doubled) . "\\n";
?>
`
    },
    swift: {
        id: 'swift',
        name: 'Swift',
        icon: '🦅',
        monaco: 'swift',
        piston: 'swift',
        version: '5.3.3',
        extension: '.swift',
        template: `import Foundation

print("Hello, World!")

// Variables and string interpolation
let name = "Swift Developer"
print("Welcome, \\(name)!")

// Arrays and higher-order functions
let numbers = [1, 2, 3, 4, 5]
let sum = numbers.reduce(0, +)
print("Sum: \\(sum)")

let doubled = numbers.map { $0 * 2 }
print("Doubled: \\(doubled)")
`
    },
    html: {
        id: 'html',
        name: 'HTML/CSS',
        icon: '🌐',
        monaco: 'html',
        piston: null, // HTML runs in preview mode
        version: 'Live Preview',
        extension: '.html',
        template: `<!DOCTYPE html>
<html>
<head>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: 'Segoe UI', sans-serif;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        .card {
            background: rgba(255,255,255,0.95);
            padding: 3rem;
            border-radius: 20px;
            box-shadow: 0 25px 50px rgba(0,0,0,0.25);
            text-align: center;
            max-width: 400px;
            animation: slideUp 0.6s ease-out;
        }
        
        @keyframes slideUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        h1 {
            font-size: 2rem;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
        }
        
        p { color: #666; line-height: 1.6; }
        
        .btn {
            display: inline-block;
            margin-top: 1.5rem;
            padding: 12px 32px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 30px;
            font-size: 1rem;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        
        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(102,126,234,0.4);
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Hello, World! 👋</h1>
        <p>Edit the HTML/CSS above to see live changes. 
           Create beautiful web pages right here!</p>
        <button class="btn">Get Started</button>
    </div>
</body>
</html>
`
    }
};

// ===== API Configuration =====
const API_BASE_URL = 'http://localhost:3001/api';
const PISTON_PUBLIC_API = 'https://emkc.org/api/v2/piston';

// ===== Global Variables =====
let editor = null;
let currentLanguage = 'python';
let isResizing = false;

// ===== Initialize Application =====
document.addEventListener('DOMContentLoaded', () => {
    initParticles();
    initTheme();

    // Conditional initialization based on page content
    if (document.getElementById('languageGrid')) {
        initLanguageGrid();
    }

    initEventListeners();

    if (document.getElementById('editor')) {
        initEditor();
        initResizer();
    }
});

// ===== Initialize Monaco Editor =====
function initEditor() {
    require.config({ paths: { vs: 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.45.0/min/vs' } });

    require(['vs/editor/editor.main'], function () {
        // Define custom dark theme
        monaco.editor.defineTheme('code-dark', {
            base: 'vs-dark',
            inherit: true,
            rules: [
                { token: 'comment', foreground: '6A9955', fontStyle: 'italic' },
                { token: 'keyword', foreground: 'C586C0' },
                { token: 'string', foreground: 'CE9178' },
                { token: 'number', foreground: 'B5CEA8' },
                { token: 'type', foreground: '4EC9B0' },
            ],
            colors: {
                'editor.background': '#0a0a10',
                'editor.foreground': '#D4D4D4',
                'editor.lineHighlightBackground': '#111118',
                'editorCursor.foreground': '#6366f1',
                'editor.selectionBackground': '#6366f140',
                'editorLineNumber.foreground': '#4b5563',
                'editorLineNumber.activeForeground': '#9ca3af',
            }
        });

        // Create editor
        const editorElement = document.getElementById('editor');
        if (editorElement) {
            editor = monaco.editor.create(editorElement, {
                value: LANGUAGES[currentLanguage].template,
                language: LANGUAGES[currentLanguage].monaco,
                theme: localStorage.getItem('theme') === 'light' ? 'vs' : 'code-dark',
                automaticLayout: true,
                fontSize: 14,
                fontFamily: "'JetBrains Mono', 'Fira Code', monospace",
                fontLigatures: true,
                minimap: { enabled: true, scale: 0.75 },
                scrollBeyondLastLine: false,
                wordWrap: 'on',
                padding: { top: 16, bottom: 16 },
                renderLineHighlight: 'all',
                cursorBlinking: 'smooth',
                cursorSmoothCaretAnimation: 'on',
                smoothScrolling: true,
                bracketPairColorization: { enabled: true },
            });

            // Keyboard shortcut: Ctrl+Enter to run
            editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter, runCode);
        }
    });
}

// ===== Particles Animation =====
function initParticles() {
    const container = document.getElementById('particles');
    if (!container) return;

    const count = 30;

    for (let i = 0; i < count; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.top = Math.random() * 100 + '%';
        particle.style.animationDelay = Math.random() * 4 + 's';
        particle.style.animationDuration = 3 + Math.random() * 3 + 's';
        container.appendChild(particle);
    }
}

// ===== Initialize Language Grid =====
function initLanguageGrid() {
    const grid = document.getElementById('languageGrid');
    if (!grid) return;

    Object.values(LANGUAGES).forEach(lang => {
        const card = document.createElement('div');
        card.className = 'language-card';
        card.dataset.langId = lang.id;

        if (lang.id === currentLanguage) {
            card.classList.add('selected');
        }

        card.innerHTML = `
            <div class="lang-icon">${lang.icon}</div>
            <span class="lang-name">${lang.name}</span>
            <span class="lang-version">v${lang.version}</span>
        `;

        card.addEventListener('click', () => {
            if (document.getElementById('editor')) {
                // We're on editor page
                selectLanguage(lang.id);
                closeLanguageModal();
            } else {
                // We're on home page - navigate to editor
                // In a real app we might pass the selected language via URL param
                // For now just go to editor
                window.location.href = 'editor.html';
            }
        });

        grid.appendChild(card);
    });
}

// ===== Event Listeners =====
function initEventListeners() {
    // Hero buttons
    document.getElementById('viewLanguages')?.addEventListener('click', openLanguageModal);

    // Language picker
    document.getElementById('languagePicker')?.addEventListener('click', openLanguageModal);

    // Modal
    document.getElementById('modalClose')?.addEventListener('click', closeLanguageModal);
    document.getElementById('modalOverlay')?.addEventListener('click', closeLanguageModal);

    // Language search
    document.getElementById('languageSearch')?.addEventListener('input', filterLanguages);

    // Run button
    document.getElementById('runBtn')?.addEventListener('click', runCode);

    // Clear button
    document.getElementById('clearBtn')?.addEventListener('click', clearEditor);

    // Copy output
    document.getElementById('copyOutput')?.addEventListener('click', copyOutput);

    // Input toggle
    document.getElementById('inputToggle')?.addEventListener('click', toggleInput);

    // Keyboard shortcut for modal
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeLanguageModal();
        }
    });

    // Theme toggle
    document.getElementById('themeToggle')?.addEventListener('click', toggleTheme);
}

// ===== Theme Management =====
function initTheme() {
    const savedTheme = localStorage.getItem('theme') || 'dark';
    setTheme(savedTheme);
}

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    setTheme(newTheme);
}

function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);

    // Update Icon
    const btn = document.getElementById('themeToggle');
    if (btn) {
        // Animation
        const iconInfo = theme === 'dark'
            // Sun icon (to switch to light)
            ? '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"></path></svg>'
            // Moon icon (to switch to dark)
            : '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>';

        btn.innerHTML = iconInfo;
        btn.title = theme === 'dark' ? "Switch to Light Mode" : "Switch to Dark Mode";

        // Rotate animation
        const icon = btn.querySelector('svg');
        if (icon) {
            icon.style.transform = 'rotate(0deg)'; // Reset
            setTimeout(() => {
                icon.style.transition = 'transform 0.5s ease';
                icon.style.transform = 'rotate(360deg)';
            }, 10);
        }
    }

    // Update Monaco Editor Theme
    if (editor) {
        monaco.editor.setTheme(theme === 'dark' ? 'code-dark' : 'vs');
    }
}


// ===== Language Selection =====
function selectLanguage(langId) {
    currentLanguage = langId;
    const lang = LANGUAGES[langId];

    // If editor exists, update it
    if (editor) {
        monaco.editor.setModelLanguage(editor.getModel(), lang.monaco);
        editor.setValue(lang.template);

        // Update picker UI
        const iconEl = document.getElementById('currentLangIcon');
        const nameEl = document.getElementById('currentLangName');
        const verEl = document.getElementById('currentLangVersion');
        const fileEl = document.getElementById('fileName');

        if (iconEl) iconEl.innerHTML = `<span>${lang.icon}</span>`;
        if (nameEl) nameEl.textContent = lang.name;
        if (verEl) verEl.textContent = `v${lang.version}`;
        if (fileEl) fileEl.textContent = `main${lang.extension}`;
    }

    // Update grid selection
    document.querySelectorAll('.language-card').forEach(card => {
        card.classList.toggle('selected', card.dataset.langId === langId);
    });

    if (document.getElementById('editor')) {
        clearOutput();
    }
}

function filterLanguages(e) {
    const query = e.target.value.toLowerCase();

    document.querySelectorAll('.language-card').forEach(card => {
        const name = card.querySelector('.lang-name').textContent.toLowerCase();
        card.style.display = name.includes(query) ? 'flex' : 'none';
    });
}

// ===== Modal Controls =====
function openLanguageModal() {
    const modal = document.getElementById('languageModal');
    if (modal) {
        modal.classList.add('active');
        document.getElementById('languageSearch')?.focus();
    }
}

function closeLanguageModal() {
    const modal = document.getElementById('languageModal');
    if (modal) {
        modal.classList.remove('active');
        const search = document.getElementById('languageSearch');
        if (search) {
            search.value = '';
            filterLanguages({ target: { value: '' } });
        }
    }
}

// ===== Run Code =====
async function runCode() {
    if (!editor) return;

    const code = editor.getValue();
    const stdinEl = document.getElementById('stdinInput');
    const stdin = stdinEl ? stdinEl.value : '';
    const lang = LANGUAGES[currentLanguage];

    // Handle HTML/CSS live preview
    if (currentLanguage === 'html') {
        renderHTMLPreview(code);
        return;
    }

    showLoading(true);
    const startTime = performance.now();

    try {
        let result;
        try {
            result = await executeViaLocalAPI(code, lang, stdin);
        } catch (localError) {
            console.log('Local API unavailable, using public Piston API...');
            result = await executeViaPistonPublic(code, lang, stdin);
        }

        const executionTime = Math.round(performance.now() - startTime);
        displayOutput(result, executionTime);
    } catch (error) {
        displayError(error.message);
    } finally {
        showLoading(false);
    }
}

// ===== Execute via Local Backend =====
async function executeViaLocalAPI(code, lang, stdin) {
    const response = await fetch(`${API_BASE_URL}/execute`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            language: lang.piston,
            version: lang.version,
            code: code,
            stdin: stdin
        })
    });

    if (!response.ok) {
        const error = await response.json();
        throw new Error(error.error || 'Execution failed');
    }

    return response.json();
}

// ===== Execute via Public Piston API =====
async function executeViaPistonPublic(code, lang, stdin) {
    const response = await fetch(`${PISTON_PUBLIC_API}/execute`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            language: lang.piston,
            version: '*',
            files: [{ content: code }],
            stdin: stdin
        })
    });

    if (!response.ok) {
        throw new Error('Execution failed');
    }

    const data = await response.json();

    return {
        success: !data.run?.stderr,
        output: data.run?.stdout || '',
        error: data.run?.stderr || data.compile?.stderr || '',
        executionTime: 0
    };
}

// ===== Render HTML Preview =====
function renderHTMLPreview(htmlCode) {
    const output = document.getElementById('output');
    if (!output) return;

    output.innerHTML = '';

    const iframe = document.createElement('iframe');
    iframe.style.width = '100%';
    iframe.style.height = '300px';
    iframe.style.border = 'none';
    iframe.style.borderRadius = '8px';
    iframe.style.background = 'white';

    output.appendChild(iframe);

    const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
    iframeDoc.open();
    iframeDoc.write(htmlCode);
    iframeDoc.close();

    const timeEl = document.getElementById('executionTime');
    if (timeEl) timeEl.textContent = 'Live Preview';
}

// ===== Display Output =====
function displayOutput(result, executionTime) {
    const output = document.getElementById('output');
    if (!output) return;

    if (result.error && result.error.trim()) {
        output.innerHTML = `<span class="output-error">${escapeHtml(result.error)}</span>`;
        if (result.output && result.output.trim()) {
            output.innerHTML += `\n${escapeHtml(result.output)}`;
        }
    } else if (result.output && result.output.trim()) {
        output.innerHTML = `<span class="output-success">${escapeHtml(result.output)}</span>`;
    } else {
        output.innerHTML = '<span class="output-success">[Program executed successfully with no output]</span>';
    }

    const timeEl = document.getElementById('executionTime');
    if (timeEl) timeEl.textContent = `${executionTime}ms`;
}

// ===== Display Error =====
function displayError(message) {
    const output = document.getElementById('output');
    if (output) {
        output.innerHTML = `<span class="output-error">Error: ${escapeHtml(message)}</span>`;
    }

    const timeEl = document.getElementById('executionTime');
    if (timeEl) timeEl.textContent = '';
}

// ===== Clear Functions =====
function clearEditor() {
    if (editor) {
        editor.setValue(LANGUAGES[currentLanguage].template);
    }
    clearOutput();
}

function clearOutput() {
    const output = document.getElementById('output');
    if (!output) return;

    output.innerHTML = `
        <div class="output-placeholder">
            <div class="placeholder-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polygon points="5 3 19 12 5 21 5 3"></polygon>
                </svg>
            </div>
            <p>Click <strong>Run Code</strong> to see output</p>
            <span class="shortcut-hint">or press Ctrl+Enter</span>
        </div>
    `;

    const timeEl = document.getElementById('executionTime');
    if (timeEl) timeEl.textContent = '';
}

// ===== Toggle Input Section =====
function toggleInput() {
    const section = document.getElementById('inputSection');
    if (section) {
        section.classList.toggle('collapsed');
    }
}

// ===== Copy Output =====
function copyOutput() {
    const output = document.getElementById('output');
    if (!output) return;

    navigator.clipboard.writeText(output.textContent).then(() => {
        const btn = document.getElementById('copyOutput');
        if (btn) {
            btn.style.color = 'var(--success)';
            setTimeout(() => {
                btn.style.color = '';
            }, 1000);
        }
    });
}

// ===== Loading State =====
function showLoading(show) {
    const overlay = document.getElementById('loadingOverlay');
    const runBtn = document.getElementById('runBtn');

    if (overlay) {
        if (show) {
            overlay.classList.remove('hidden');
        } else {
            overlay.classList.add('hidden');
        }
    }

    if (runBtn) {
        runBtn.disabled = show;
    }
}

// ===== Resizer =====
function initResizer() {
    const resizer = document.getElementById('resizer');
    const editorPanel = document.querySelector('.editor-panel');
    const outputPanel = document.querySelector('.output-panel');

    if (!resizer || !editorPanel || !outputPanel) return;

    resizer.addEventListener('mousedown', (e) => {
        isResizing = true;
        document.body.style.cursor = 'col-resize';
        document.body.style.userSelect = 'none';

        // Prevent default to avoid text selection issues
        e.preventDefault();
    });

    document.addEventListener('mousemove', (e) => {
        if (!isResizing) return;

        const container = document.querySelector('.editor-container');
        if (!container) return;

        const containerRect = container.getBoundingClientRect();
        const percentage = ((e.clientX - containerRect.left) / containerRect.width) * 100;

        if (percentage > 20 && percentage < 80) {
            editorPanel.style.flex = `0 0 ${percentage}%`;
            outputPanel.style.flex = `0 0 ${100 - percentage - 1}%`;
        }
    });

    document.addEventListener('mouseup', () => {
        isResizing = false;
        document.body.style.cursor = '';
        document.body.style.userSelect = '';
    });
}

// ===== Utility Functions =====
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
