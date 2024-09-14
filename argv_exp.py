import sys
  # Set default values if no alpha is provided
alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5

# Set default values if no l1_ratio is provided
l1_ratio = float(sys.argv[2]) if len(sys.argv) > 1 else 0.5

print(alpha, l1_ratio)
