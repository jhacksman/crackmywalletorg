# This Space Number Pass Wordlist

This wordlist generator was created for the crackmywallet.org Bitcoin wallet challenge to produce passphrases with numbers appended.

## What We're Doing

We're creating a script that generates passphrases with the following constraints:
- First word is always "this"
- Last word is always one of: "pass", "password", or "passphrase"
- Words are separated by spaces or periods (two separate wordlists)
- Common numbers are appended to the end of the passphrase
- Numbers are appended both with and without a separator after the last word
- Generates combinations of 2 to 6 words in length

## Why We're Doing This

Based on hints from crackmywallet.org, the password might include common numbers appended at the end. This wordlist explores combinations that follow this pattern with both spaces and periods between words, and with numbers appended in different ways.

## Common Numbers Used

The following common numbers are appended to the passphrases:
- 1
- 12
- 123
- 1234
- 69
- 403
- 404
- 420

## Wordlist Details

The script generates two separate wordlist files:

### Space-Separated Variant
- **File Name**: `this_space_number_pass.txt`
- **Total Permutations**: 1,325,280
- **Estimated File Size**: 42.34 MB

### Period-Separated Variant
- **File Name**: `this_period_number_pass.txt`
- **Total Permutations**: 1,325,280
- **Estimated File Size**: 42.34 MB

### Combined Statistics
- **Total Permutations (both variants)**: 2,650,560
- **Total Estimated File Size**: 84.68 MB
- **Words in Refined Wordlist**: 39 (excluding "this", "pass", "password", "passphrase")
- **Number of Common Numbers**: 8

### Combinations by Length (per variant)
- 2 words with numbers: 48 combinations
- 3 words with numbers: 1,872 combinations
- 4 words with numbers: 73,008 combinations
- 5 words with numbers: 240,000 combinations
- 6 words with numbers: 1,010,352 combinations

### Sample Passphrases (Space-Separated)
```
this pass1
this pass 1
this a pass404
this a pass 404
this a an pass69
this a an and pass 123
```

### Sample Passphrases (Period-Separated)
```
this.pass1
this.pass.1
this.a.pass404
this.a.an.pass69
this.a.an.and.pass.123
```

## Files Included

1. `generate_this_space_number_pass.py` - The Python script used to generate both wordlists
2. `README.md` - This documentation file

## Usage

To generate the wordlists, run:
```bash
python3 generate_this_space_number_pass.py
```

The script will analyze the combinations and prompt you to generate the files if the estimated size is under 1GB.
