#!/bin/bash
# Setup script for Google Tasks CSV Exporter

echo "🚀 Setting up Google Tasks CSV Exporter..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

echo "✅ Python 3 found"

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Check if credentials template exists
if [ ! -f "credentials.json" ]; then
    if [ -f "credentials.json.template" ]; then
        echo "📋 Credentials template found. You need to:"
        echo "   1. Copy credentials.json.template to credentials.json"
        echo "   2. Fill in your Google API credentials"
        echo ""
        echo "   cp credentials.json.template credentials.json"
        echo "   # Then edit credentials.json with your actual credentials"
    else
        echo "⚠️  No credentials template found"
    fi
else
    echo "✅ Credentials file found"
fi

# Run tests
echo "🧪 Running tests..."
python3 test.py

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Setup completed successfully!"
    echo ""
    echo "Next steps:"
    echo "1. Set up your Google API credentials in credentials.json"
    echo "2. Run: python3 main.py --help"
    echo "3. Export your tasks: python3 main.py"
else
    echo "⚠️  Tests failed, but setup may still work"
fi