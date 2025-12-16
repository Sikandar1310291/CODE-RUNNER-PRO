# CodeRunner Pro - Online Compiler

A professional, production-ready online compiler supporting **17 programming languages**. Built with open-source technologies and completely free to operate.

![Languages](https://img.shields.io/badge/Languages-17-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)

## ✨ Features

- 🎨 **Modern UI** - Dark theme with glassmorphism design
- 📝 **Monaco Editor** - VS Code-quality code editing
- 🚀 **17 Languages** - Python, Java, C/C++, JavaScript, Go, Rust, and more
- 🔒 **Secure** - Sandboxed execution with resource limits
- ⚡ **Fast** - Real-time code execution and output
- 📱 **Responsive** - Works on desktop and mobile

## 🛠️ Supported Languages

| Language | Compiler/Runtime | Language | Compiler/Runtime |
|----------|-----------------|----------|-----------------|
| Python | Python 3.10 | Ruby | Ruby 3.0 |
| Java | OpenJDK 15 | PHP | PHP 8.2 |
| C | GCC 10.2 | Swift | Swift 5.3 |
| C++ | G++ 10.2 | Scala | Scala 3.2 |
| C# | .NET 5.0 | Dart | Dart 2.19 |
| JavaScript | Node.js 18 | R | R 4.1.1 |
| TypeScript | TypeScript 5.0 | SQL | SQLite 3.36 |
| Go | Go 1.16 | HTML/CSS | Live Preview |
| Rust | Rust 1.68 | | |

## 🚀 Quick Start

### Option 1: Direct Open (Uses Public API)

Simply open `index.html` in your browser. The frontend will use the public Piston API.

```bash
# Using Python
python -m http.server 3000

# Using Node.js 
npx serve -p 3000

# Using VS Code Live Server extension
# Just right-click index.html → "Open with Live Server"
```

### Option 2: Full Stack with Docker (Recommended)

```bash
# Start all services
docker-compose up -d

# Access the app
open http://localhost:3000
```

### Option 3: Manual Setup

**Step 1: Start the backend**
```bash
cd server
npm install
npm start
```

**Step 2: Serve the frontend**
```bash
# In project root
npx serve -p 3000
```

## 📁 Project Structure

```
online-compiler-website/
├── index.html          # Main HTML file
├── styles.css          # CSS styles
├── app.js              # Frontend JavaScript
├── docker-compose.yml  # Docker configuration
├── server/
│   ├── index.js        # Express server
│   ├── config.js       # Configuration
│   ├── package.json    # Dependencies
│   └── Dockerfile      # Container config
└── README.md           # Documentation
```

## 🔧 Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | 3001 | Backend server port |
| `PISTON_URL` | `https://emkc.org/api/v2/piston` | Piston API URL |

### Execution Limits

| Limit | Value | Purpose |
|-------|-------|---------|
| Compile Timeout | 10s | Maximum compilation time |
| Run Timeout | 5s | Maximum execution time |
| Memory | 128MB | Maximum memory per execution |
| Code Size | 64KB | Maximum code length |
| Rate Limit | 30/min | Requests per minute per IP |

## 🔒 Security Features

- **Sandboxed Execution** - All code runs in isolated Docker containers
- **Resource Limits** - CPU, memory, and time constraints
- **Rate Limiting** - Prevents abuse
- **Input Validation** - Strict validation of all inputs
- **No Network Access** - Containers have no internet access
- **Security Headers** - Helmet.js protection

## 🌐 Deployment

### Cloud Hosting (Free Options)

| Provider | Free Tier | Best For |
|----------|-----------|----------|
| Oracle Cloud | 4 ARM CPUs, 24GB RAM | ✅ Production |
| Railway | 500 hours/month | Small scale |
| Render | Static sites | Frontend only |

### Production Checklist

- [ ] Set up SSL/TLS certificate
- [ ] Configure firewall rules
- [ ] Set up monitoring and logging
- [ ] Configure backup strategy
- [ ] Set proper CORS origins
- [ ] Enable rate limiting

## 📝 API Reference

### POST `/api/execute`

Execute code in the specified language.

**Request:**
```json
{
  "language": "python",
  "code": "print('Hello, World!')",
  "stdin": ""
}
```

**Response:**
```json
{
  "success": true,
  "output": "Hello, World!\n",
  "error": "",
  "executionTime": 45
}
```

### GET `/api/languages`

Get list of supported languages.

### GET `/api/health`

Health check endpoint.

## 🤝 Contributing

Contributions are welcome! Please open an issue for bugs or feature requests.

## 📄 License

MIT License - feel free to use for personal or commercial projects.

---

Built with ❤️ using Monaco Editor, Express.js, and Piston Execution Engine.
