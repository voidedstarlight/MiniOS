"""
System/rerun.py
Rerun main.py script for imports

"""

def rerun():
	print("Successfully installed required packages.")
	__import__("os").system("python3 System/main.py")
