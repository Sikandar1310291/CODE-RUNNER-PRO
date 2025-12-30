/**
 * CodeRunner Pro - Configuration
 * Server and language configuration
 */

module.exports = {
    // Server port
    port: process.env.PORT || 3001,

    // Piston API URL (public or self-hosted)
    pistonUrl: process.env.PISTON_URL || 'https://emkc.org/api/v2/piston',

    // CORS allowed origins
    corsOrigins: [
        'http://localhost:3000',
        'http://localhost:5500',
        'http://127.0.0.1:3000',
        'http://127.0.0.1:5500',
        'http://localhost:8080',
        '*' // Allow all for development
    ],

    // Rate limiting
    rateLimit: {
        maxRequests: 30 // per minute
    },

    // Execution limits
    limits: {
        maxCodeLength: 65536, // 64KB max code
        compileTimeout: 10000, // 10 seconds
        runTimeout: 5000, // 5 seconds
        memoryLimit: 134217728, // 128MB
        requestTimeout: 30000 // 30 seconds total request timeout
    },

    // Supported languages mapping
    languages: {
        python: {
            name: 'Python',
            piston: 'python',
            version: '3.10'
        },
        r: {
            name: 'R',
            piston: 'rlang',
            version: '4.1.1'
        },
        sql: {
            name: 'SQL',
            piston: 'sqlite3',
            version: '3.36.0'
        },
        java: {
            name: 'Java',
            piston: 'java',
            version: '15.0.2'
        },
        c: {
            name: 'C',
            piston: 'c',
            version: '10.2.0'
        },
        'c++': {
            name: 'C++',
            piston: 'c++',
            version: '10.2.0'
        },
        csharp: {
            name: 'C#',
            piston: 'csharp.net',
            version: '5.0'
        },
        javascript: {
            name: 'JavaScript',
            piston: 'javascript',
            version: '18.15.0'
        },
        typescript: {
            name: 'TypeScript',
            piston: 'typescript',
            version: '5.0.3'
        },
        go: {
            name: 'Go',
            piston: 'go',
            version: '1.16.2'
        },
        rust: {
            name: 'Rust',
            piston: 'rust',
            version: '1.68.2'
        },
        scala: {
            name: 'Scala',
            piston: 'scala',
            version: '3.2.2'
        },
        dart: {
            name: 'Dart',
            piston: 'dart',
            version: '2.19.6'
        },
        ruby: {
            name: 'Ruby',
            piston: 'ruby',
            version: '3.0.1'
        },
        php: {
            name: 'PHP',
            piston: 'php',
            version: '8.2.3'
        },
        swift: {
            name: 'Swift',
            piston: 'swift',
            version: '5.3.3'
        }
    }
};
