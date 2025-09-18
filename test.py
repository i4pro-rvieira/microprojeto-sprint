#!/usr/bin/env python3
"""
Simple test script to verify the implementation
"""
import sys
import os

def test_imports():
    """Test that all modules can be imported"""
    try:
        import google_tasks
        import csv_exporter
        import config
        print("✅ All modules imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_config():
    """Test configuration module"""
    try:
        from config import config
        print(f"✅ Config loaded - Credentials file: {config.get_credentials_path()}")
        print(f"✅ Config loaded - Token file: {config.get_token_path()}")
        print(f"✅ Config loaded - Scopes: {config.get_scopes()}")
        return True
    except Exception as e:
        print(f"❌ Config test failed: {e}")
        return False

def test_csv_exporter():
    """Test CSV exporter with sample data"""
    try:
        from csv_exporter import CSVExporter
        
        # Sample task data
        sample_tasks = [
            {
                'id': 'test-1',
                'title': 'Test Task 1',
                'notes': 'This is a test task',
                'status': 'needsAction',
                'due': '2023-12-31T23:59:59.000Z',
                'taskListTitle': 'Test List'
            },
            {
                'id': 'test-2', 
                'title': 'Test Task 2',
                'status': 'completed',
                'completed': '2023-12-15T10:00:00.000Z',
                'taskListTitle': 'Test List'
            }
        ]
        
        exporter = CSVExporter()
        
        # Test summary printing
        print("\n--- Testing CSV Exporter Summary ---")
        exporter.print_tasks_summary(sample_tasks)
        
        # Test CSV export
        filename = '/tmp/test_export.csv'
        result_file = exporter.export_tasks(sample_tasks, filename)
        
        if os.path.exists(result_file):
            print(f"✅ CSV export test successful: {result_file}")
            # Read and display the CSV content
            with open(result_file, 'r', encoding='utf-8') as f:
                content = f.read()
                print("CSV Content:")
                print(content)
            os.remove(result_file)  # Clean up
            return True
        else:
            print("❌ CSV file was not created")
            return False
            
    except Exception as e:
        print(f"❌ CSV exporter test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Running Tests for Google Tasks CSV Exporter")
    print("=" * 50)
    
    tests = [
        ("Module Imports", test_imports),
        ("Configuration", test_config), 
        ("CSV Exporter", test_csv_exporter)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Testing {test_name}...")
        if test_func():
            passed += 1
        
    print(f"\n{'='*50}")
    print(f"Tests Results: {passed}/{total} passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("⚠️  Some tests failed")
        return 1

if __name__ == '__main__':
    sys.exit(main())