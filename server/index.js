/**
 * CodeRunner Pro - Backend Server
 * Express.js server with Piston code execution integration
 */

const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const axios = require('axios');
const config = require('./config');

const app = express();

// ===== Security Middleware =====
app.use(helmet({
    contentSecurityPolicy: false, // Allow inline scripts for dev
    crossOriginEmbedderPolicy: false
}));

// CORS configuration
app.use(cors({
    origin: config.corsOrigins,
    methods: ['GET', 'POST'],
    allowedHeaders: ['Content-Type']
}));

// Body parser
app.use(express.json({ limit: '1mb' }));

// Rate limiting
const limiter = rateLimit({
    windowMs: 60 * 1000, // 1 minute
    max: config.rateLimit.maxRequests,
    message: {
        success: false,
        error: 'Too many requests. Please wait a minute before trying again.'
    },
    standardHeaders: true,
    legacyHeaders: false
});
app.use('/api/', limiter);

// ===== Health Check =====
app.get('/api/health', (req, res) => {
    res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// ===== Get Supported Languages =====
app.get('/api/languages', (req, res) => {
    res.json({
        success: true,
        languages: Object.entries(config.languages).map(([id, lang]) => ({
            id,
            name: lang.name,
            version: lang.version
        }))
    });
});

// ===== Execute Code =====
app.post('/api/execute', async (req, res) => {
    try {
        const { language, code, stdin = '' } = req.body;

        // Validate request
        if (!language || !code) {
            return res.status(400).json({
                success: false,
                error: 'Missing required fields: language and code'
            });
        }

        // Check if language is supported
        const langConfig = config.languages[language];
        if (!langConfig) {
            return res.status(400).json({
                success: false,
                error: `Unsupported language: ${language}`
            });
        }

        // Validate code length
        if (code.length > config.limits.maxCodeLength) {
            return res.status(400).json({
                success: false,
                error: `Code exceeds maximum length of ${config.limits.maxCodeLength} characters`
            });
        }

        // Execute via Piston API
        const startTime = Date.now();
        const result = await executePiston(language, langConfig, code, stdin);
        const executionTime = Date.now() - startTime;

        res.json({
            success: true,
            output: result.output,
            error: result.error,
            executionTime
        });

    } catch (error) {
        console.error('Execution error:', error.message);
        res.status(500).json({
            success: false,
            error: error.message || 'Code execution failed'
        });
    }
});

// ===== Piston Execution =====
async function executePiston(language, langConfig, code, stdin) {
    try {
        const response = await axios.post(
            `${config.pistonUrl}/execute`,
            {
                language: langConfig.piston,
                version: '*', // Use latest available version
                files: [{ content: code }],
                stdin: stdin,
                compile_timeout: config.limits.compileTimeout,
                run_timeout: config.limits.runTimeout,
                compile_memory_limit: config.limits.memoryLimit,
                run_memory_limit: config.limits.memoryLimit
            },
            {
                timeout: config.limits.requestTimeout,
                headers: { 'Content-Type': 'application/json' }
            }
        );

        const data = response.data;

        // Handle compilation errors
        if (data.compile && data.compile.stderr) {
            return {
                output: data.compile.stdout || '',
                error: data.compile.stderr
            };
        }

        // Handle runtime output
        return {
            output: data.run?.stdout || '',
            error: data.run?.stderr || ''
        };

    } catch (error) {
        if (error.code === 'ECONNABORTED') {
            throw new Error('Execution timed out');
        }
        if (error.response?.data?.message) {
            throw new Error(error.response.data.message);
        }
        throw new Error('Failed to execute code');
    }
}

// ===== Error Handler =====
app.use((err, req, res, next) => {
    console.error('Server error:', err);
    res.status(500).json({
        success: false,
        error: 'Internal server error'
    });
});

// ===== 404 Handler =====
app.use((req, res) => {
    res.status(404).json({
        success: false,
        error: 'Endpoint not found'
    });
});

// ===== Start Server =====
const PORT = config.port;
app.listen(PORT, () => {
    console.log(`
╔═══════════════════════════════════════════════╗
║       CodeRunner Pro - Backend Server         ║
╠═══════════════════════════════════════════════╣
║  🚀 Server running on http://localhost:${PORT}   ║
║  📡 Piston API: ${config.pistonUrl.substring(0, 30)}...  ║
║  🔒 Rate limit: ${config.rateLimit.maxRequests} requests/minute       ║
╚═══════════════════════════════════════════════╝
    `);
});

module.exports = app;
