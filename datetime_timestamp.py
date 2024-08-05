from datetime import datetime

# Create a timestamped backup filename
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
backup_filename = f"backup_{timestamp}.tar.gz" # f-strings: Introduced in Python 3.6, f-strings provide a way to embed expressions inside string literals, using curly braces {}.

print(backup_filename)