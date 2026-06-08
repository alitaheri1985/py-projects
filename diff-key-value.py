import sys

def read_env(f):
    try:
        return {l.split('=', 1)[0].strip(): l.split('=', 1)[1].strip() for l in open(f) if '=' in l and not l.startswith('#')}
    except FileNotFoundError:
        print(f'Error: File "{f}" not found.')
        sys.exit(1)

# Get inputs from the user interactively
example_file = input('Enter the name of your template file (e.g., env.example): ').strip()
prod_file = input('Enter the name of your production file (e.g., env-prod): ').strip()
output_file = input('Enter the desired output report filename (e.g., report.txt): ').strip()

ex = read_env(example_file)
prod = read_env(prod_file)

missing_in_prod = 0
missing_in_ex = 0
mismatches = 0

# Open the file specified by the user to write outputs
with open(output_file, 'w') as f:
    # Temporarily redirect standard print to the file
    sys.stdout = f

    print('=== MISSING IN PROD (Value in Template) ===')
    for k in ex:
        if k not in prod: 
            print(f'  {k} = {ex[k]}')
            missing_in_prod += 1

    print('\n=== MISSING IN EXAMPLE (Value in Prod) ===')
    for k in prod:
        if k not in ex: 
            print(f'  {k} = {prod[k]}')
            missing_in_ex += 1

    print('\n=== VALUE MISMATCHES ===')
    for k in ex:
        if k in prod and ex[k] != prod[k]:
            print(f'  {k}:\n    Template: {ex[k]}\n    Prod:     {prod[k]}')
            mismatches += 1

    print('\n========================================')
    print('=== SUMMARY METRICS ===')
    print(f'Total Missing in Prod:    {missing_in_prod}')
    print(f'Total Missing in Example: {missing_in_ex}')
    print(f'Total Value Mismatches:   {mismatches}')
    print(f'Total Differences Found:  {missing_in_prod + missing_in_ex + mismatches}')

# Restore print back to terminal screen to show success message
sys.stdout = sys.__stdout__
print(f'\n[Success] Analysis complete. Results saved to: {output_file}')