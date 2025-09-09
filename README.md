# Genesis Project Template

A Cookiecutter-like template generator for creating new projects from customizable templates.

## Overview

Genesis-Templates is a tool that helps you quickly bootstrap new projects using predefined templates. It generates project structures with all necessary files, configurations, and boilerplate code based on your specifications.

## Features

- 🚀 Quick project initialization
- 📁 Customizable template system
- ⚙️ Configurable template settings
- 🐍 Python-based tooling
- 🧪 Tox testing environment

## Prerequisites

- Python 3.8+
- pip
- tox (recommended)

## Installation

### Using tox (Recommended)

```bash
# Clone the repository
git clone https://github.com/infraguys/genesis_templates.git
cd genesis_templates

# Install and activate development environment
tox -e develop
. .tox/develop/bin/activate
```

### Manual Installation

```bash
source <path-to-your-venv>/bin/activate
pip install -e .
```

## Usage

### Basic Usage

After activating the environment (if using tox), you can generate a new project:

```bash
genesis-create-project \
    --template_settings templates/py_element.settings.json \
    --target_directory ../my-new-project
```

### Command Options

- `--template_settings` (required): Path to the template settings JSON file
- `--target_directory` (required): Directory where the new project will be created
- `--help`: Show help message and exit

### Available Templates

Currently available templates:

1. **Python basic web app project** (`templates/py_element.settings.json`)
   - Basic Python package structure
   - DB models and migrations configuration
   - API skeleton
   - Daemon services
   - Testing framework setup

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## Support

If you have any questions or issues:

1. Check the existing issues
2. Create a new issue with detailed description
3. Contact the maintainers
