# Parse and compute values for multiple entries from i4.txt
with open('i4.txt', 'r') as file:
    lines = file.readlines()

# Ensure the number of lines is a multiple of 4
if len(lines) % 4 != 0:
    print("Error: i4.txt does not contain a complete set of data (missing lines).")
else:
    # Process each group of four lines
    results = []
    for i in range(0, len(lines), 4):
        try:
            a = float(lines[i].split('=')[1].strip())
            b = float(lines[i + 1].split('=')[1].strip())
            c = float(lines[i + 2].split('=')[1].strip())
            x = float(lines[i + 3].split('=')[1].strip())

            # Compute y for the current set of values
            y = (a * (x ** 2)) + (b * x) + c
            results.append((a, b, c, x, y))
        except Exception as e:
            print(f"Error processing lines {i}-{i+3}: {lines[i:i+4]} -> {e}")

    # Display results
    print("\nResults from i4.txt:")
    for a, b, c, x, y in results:
        print(f"a={a}, b={b}, c={c}, x={x} -> y={y}")

    # Optionally write results to a file
    with open('output.txt', 'w') as file:
        for a, b, c, x, y in results:
            file.write(f"a={a}, b={b}, c={c}, x={x} -> y={y}\n")
