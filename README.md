# GitBranchTest - Refactored Architecture

## Overview — edited by arunsam091heu

This project demonstrates a major refactoring with improved code organization, better separation of concerns, and comprehensive error handling.

## Architecture

### Module Structure

- **main.py**: Core application entry point with Application class
- **config.py**: Centralized configuration management (ConfigManager)
- **utils.py**: Utility modules for logging and error handling
- **test_main.py**: Comprehensive unit test suite

### Key Improvements

#### 1. Configuration Management
- Centralized ConfigManager class
- Support for config files and environment variables
- Type hints for better IDE support

#### 2. Error Handling
- Custom ErrorHandler class with context-aware logging
- Consistent error reporting across modules
- Graceful failure modes

#### 3. Logging Infrastructure
- Custom Logger wrapper for consistent formatting
- Singleton logger instances
- Configurable log levels

#### 4. Testing
- Unit test suite for all modules
- Mock-based testing for dependencies
- Test coverage for critical paths

## Usage

```python
from main import Application

# Initialize and run application
app = Application(config_file='config.json')
app.run()
```

## Configuration

Set environment variables with `APP_` prefix:

```bash
export APP_DEBUG=True
export APP_LOG_LEVEL=DEBUG
python main.py
```

## Running Tests

```bash
python -m pytest test_main.py -v
```

## Future Enhancements

- Database integration layer
- API endpoint framework
- Advanced caching mechanisms
- Performance monitoring
