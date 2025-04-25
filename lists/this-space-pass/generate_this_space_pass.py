
refined_wordlist = [
    "a", "an", "and", "bad", "derpy", "dumb", "dumbest", "extremely",
    "herp", "idiot", "idiotic", "is", "just", "lol", "lulz", "my",
    "noob", "poop", "poopy", "poopiest", "potato", "pretty", "pwned", 
    "quite", "really", "retard", "retarded", "rofl", "shit", "shitty", 
    "shittiest", "simple", "so", "stupid", "stupidest", "super", "the", 
    "very", "weak"
]

prefix = "this"
suffixes = ["pass", "password", "passphrase"]

def generate_passphrases(output_file="this_space_pass.txt"):
    with open(output_file, "w") as f:
        for suffix in suffixes:
            f.write(f"{prefix} {suffix}\n")
        
        for middle in refined_wordlist:
            for suffix in suffixes:
                f.write(f"{prefix} {middle} {suffix}\n")
        
        for middle1 in refined_wordlist:
            for middle2 in refined_wordlist:
                for suffix in suffixes:
                    f.write(f"{prefix} {middle1} {middle2} {suffix}\n")
        
        for middle1 in refined_wordlist:
            for middle2 in refined_wordlist:
                for middle3 in refined_wordlist:
                    for suffix in suffixes:
                        f.write(f"{prefix} {middle1} {middle2} {middle3} {suffix}\n")
        
        subset_size = 20  # Use only the first 20 words to reduce combinations
        for middle1 in refined_wordlist[:subset_size]:
            for middle2 in refined_wordlist[:subset_size]:
                for middle3 in refined_wordlist[:subset_size]:
                    for middle4 in refined_wordlist[:subset_size]:
                        for suffix in suffixes:
                            f.write(f"{prefix} {middle1} {middle2} {middle3} {middle4} {suffix}\n")

def analyze_combinations():
    print(f"Number of words in refined wordlist: {len(refined_wordlist)}")
    
    two_word_combinations = len(suffixes)
    three_word_combinations = len(refined_wordlist) * len(suffixes)
    four_word_combinations = len(refined_wordlist) * len(refined_wordlist) * len(suffixes)
    five_word_combinations = len(refined_wordlist) * len(refined_wordlist) * len(refined_wordlist) * len(suffixes)
    
    subset_size = 20  # Use only the first 20 words to reduce combinations
    six_word_combinations = subset_size * subset_size * subset_size * subset_size * len(suffixes)
    
    total_combinations = (two_word_combinations + three_word_combinations + 
                         four_word_combinations + five_word_combinations + 
                         six_word_combinations)
    
    avg_word_length = sum(len(word) for word in refined_wordlist) / len(refined_wordlist)
    avg_subset_word_length = sum(len(word) for word in refined_wordlist[:subset_size]) / subset_size
    avg_suffix_length = sum(len(suffix) for suffix in suffixes) / len(suffixes)
    
    avg_two_word_length = len(prefix) + 1 + avg_suffix_length + 1
    avg_three_word_length = len(prefix) + 1 + avg_word_length + 1 + avg_suffix_length + 1
    avg_four_word_length = len(prefix) + 1 + avg_word_length + 1 + avg_word_length + 1 + avg_suffix_length + 1
    avg_five_word_length = len(prefix) + 1 + avg_word_length + 1 + avg_word_length + 1 + avg_word_length + 1 + avg_suffix_length + 1
    avg_six_word_length = len(prefix) + 1 + avg_subset_word_length + 1 + avg_subset_word_length + 1 + avg_subset_word_length + 1 + avg_subset_word_length + 1 + avg_suffix_length + 1
    
    estimated_two_word_size = two_word_combinations * avg_two_word_length
    estimated_three_word_size = three_word_combinations * avg_three_word_length
    estimated_four_word_size = four_word_combinations * avg_four_word_length
    estimated_five_word_size = five_word_combinations * avg_five_word_length
    estimated_six_word_size = six_word_combinations * avg_six_word_length
    
    total_file_size = (estimated_two_word_size + estimated_three_word_size + 
                      estimated_four_word_size + estimated_five_word_size + 
                      estimated_six_word_size)
    
    if total_file_size < 1024:
        size_str = f"{total_file_size:.2f} bytes"
    elif total_file_size < 1024 * 1024:
        size_str = f"{total_file_size / 1024:.2f} KB"
    elif total_file_size < 1024 * 1024 * 1024:
        size_str = f"{total_file_size / (1024 * 1024):.2f} MB"
    else:
        size_str = f"{total_file_size / (1024 * 1024 * 1024):.2f} GB"
    
    print(f"\nCombinations by length:")
    print(f"2 words: {two_word_combinations:,}")
    print(f"3 words: {three_word_combinations:,}")
    print(f"4 words: {four_word_combinations:,}")
    print(f"5 words: {five_word_combinations:,}")
    print(f"6 words: {six_word_combinations:,}")
    print(f"Total combinations: {total_combinations:,}")
    print(f"Estimated file size: {size_str}")
    
    print("\nSample passphrases:")
    print(f"{prefix} {suffixes[0]}")  # 2 words
    print(f"{prefix} {refined_wordlist[0]} {suffixes[0]}")  # 3 words
    print(f"{prefix} {refined_wordlist[0]} {refined_wordlist[1]} {suffixes[0]}")  # 4 words
    print(f"{prefix} {refined_wordlist[0]} {refined_wordlist[1]} {refined_wordlist[2]} {suffixes[0]}")  # 5 words
    print(f"{prefix} {refined_wordlist[0]} {refined_wordlist[1]} {refined_wordlist[2]} {refined_wordlist[3]} {suffixes[0]}")  # 6 words
    
    return total_combinations, total_file_size

if __name__ == "__main__":
    print("Analyzing combinations with spaces between words...")
    total_combinations, total_file_size = analyze_combinations()
    
    if total_file_size < 1024 * 1024 * 1024:  # Less than 1GB
        print("\nThis script will generate a file with all combinations starting with 'this' and ending with 'pass', 'password', or 'passphrase'")
        print("with spaces between words.")
        choice = input("Do you want to generate the file? (y/n): ")
        
        if choice.lower() == 'y':
            print("Generating passphrases...")
            generate_passphrases()
            print("File 'this_space_pass.txt' has been generated successfully!")
        else:
            print("File generation cancelled.")
    else:
        print("\nWARNING: The estimated file size exceeds 1GB.")
        print("Please modify the script to reduce the number of combinations.")
