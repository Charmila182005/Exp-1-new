# Experiment 1: Weather Modeling using Quadratic Equation

## Aim
Implement weather modeling using the quadratic solution in stages:
- Hard-coded variables
- Keyboard input
- Read from a file (single and multiple sets)

## Procedure
1. Solve the quadratic equation: ax² + bx + c = 0
2. Compute discriminant: D = b² - 4ac
3. Determine roots:
   - D > 0 → two real roots
   - D = 0 → one real root
   - D < 0 → no real roots
4. Implement in 4 phases:
   - Phase 1: Hardcoded coefficients
   - Phase 2: Keyboard input
   - Phase 3: File input (single set)
   - Phase 4: File input (multiple sets)

## Files
- `weather_model_hardcoded.py` → Hardcoded coefficients
- `weather_model_input.py` → Keyboard input
- `weather_model_file_single.py` → Single set from file
- `weather_model_file_multiple.py` → Multiple sets from file
- `input_single.txt` → Input for single set
- `input_multiple.txt` → Input for multiple sets

## Sample Output
- Phase 1 (hardcoded): Two real roots: 3.0, 2.0
- Phase 2 (keyboard input): Two real roots: 3.0, 2.0
- Phase 3 (file single): Two real roots: 3.0, 2.0
- Phase 4 (file multiple):
  - Set 1: Two real roots: 3.0, 2.0
  - Set 2: One real root: 1.0
  - Set 3: No real roots
