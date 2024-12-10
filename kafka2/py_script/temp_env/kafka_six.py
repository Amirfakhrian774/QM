try:
    import six
    print("Six package is working")
except ImportError as e:
    print(f"Error importing Six package: {e}")
