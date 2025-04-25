# This Space Pass Wordlist

This wordlist was created to generate passphrases for the crackmywallet.org Bitcoin wallet challenge.

## What We Did

We created a script that generates passphrases with the following constraints:
- First word is always "this"
- Last word is always one of: "pass", "password", or "passphrase"
- Words are separated by spaces
- No occurrence of "this" or password-related words in middle positions
- Generates combinations of 2 to 6 words in length

## Why We Did This

Based on hints from crackmywallet.org, the password is likely a mutation of phrases like "this is a bad password" or similar self-degrading statements. This wordlist explores combinations that follow this pattern with spaces between words.

## Wordlist Details

- **File Name**: `this_space_pass.txt`
- **Total Permutations**: 662,640
- **File Size**: 21.17 MB
- **Words in Refined Wordlist**: 39 (excluding "this", "pass", "password", "passphrase")

### Combinations by Length
- 2 words: 3 combinations
- 3 words: 117 combinations
- 4 words: 4,563 combinations
- 5 words: 177,957 combinations
- 6 words: 480,000 combinations

### Sample Passphrases
```
this pass
this a pass
this a an pass
this a an and pass
this a an and bad pass
```

## Files Included

1. `this_space_pass.txt` - The generated wordlist
2. `generate_this_space_pass.py` - The Python script used to generate the wordlist
3. `README.md` - This documentation file

## Usage

To regenerate the wordlist, run:
```bash
python3 generate_this_space_pass.py
```

The script will analyze the combinations and prompt you to generate the file if the estimated size is under 1GB.
