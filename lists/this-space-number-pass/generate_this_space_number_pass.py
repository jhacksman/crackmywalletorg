
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
common_numbers = ["1", "12", "123", "1234", "69", "403", "404", "420"]

def generate_space_number_passphrases(output_file="this_space_number_pass.txt"):
    """
    Generates passphrases with spaces between words and numbers appended at the end.
    The numbers are appended both with and without a space after the last word.
    """
    with open(output_file, "w") as f:
        for suffix in suffixes:
            for num in common_numbers:
                f.write(f"{prefix} {suffix}{num}\n")
                f.write(f"{prefix} {suffix} {num}\n")
        
        for middle in refined_wordlist:
            for suffix in suffixes:
                for num in common_numbers:
                    f.write(f"{prefix} {middle} {suffix}{num}\n")
                    f.write(f"{prefix} {middle} {suffix} {num}\n")
        
        for middle1 in refined_wordlist:
            for middle2 in refined_wordlist:
                for suffix in suffixes:
                    for num in common_numbers:
                        f.write(f"{prefix} {middle1} {middle2} {suffix}{num}\n")
                        f.write(f"{prefix} {middle1} {middle2} {suffix} {num}\n")
        
        subset_size_5 = 10  # Use a smaller subset to reduce combinations
        for middle1 in refined_wordlist[:subset_size_5]:
            for middle2 in refined_wordlist[:subset_size_5]:
                for middle3 in refined_wordlist[:subset_size_5]:
                    for suffix in suffixes:
                        for num in common_numbers:
                            f.write(f"{prefix} {middle1} {middle2} {middle3} {suffix}{num}\n")
                            f.write(f"{prefix} {middle1} {middle2} {middle3} {suffix} {num}\n")
        
        subset_size_6 = 5  # Use an even smaller subset for 6-word combinations
        for middle1 in refined_wordlist[:subset_size_6]:
            for middle2 in refined_wordlist[:subset_size_6]:
                for middle3 in refined_wordlist[:subset_size_6]:
                    for middle4 in refined_wordlist[:subset_size_6]:
                        for suffix in suffixes:
                            for num in common_numbers:
                                f.write(f"{prefix} {middle1} {middle2} {middle3} {middle4} {suffix}{num}\n")
                                f.write(f"{prefix} {middle1} {middle2} {middle3} {middle4} {suffix} {num}\n")

def generate_period_number_passphrases(output_file="this_period_number_pass.txt"):
    """
    Generates passphrases with periods between words and numbers appended at the end.
    The numbers are appended both with and without a period after the last word.
    """
    with open(output_file, "w") as f:
        for suffix in suffixes:
            for num in common_numbers:
                f.write(f"{prefix}.{suffix}{num}\n")
                f.write(f"{prefix}.{suffix}.{num}\n")
        
        for middle in refined_wordlist:
            for suffix in suffixes:
                for num in common_numbers:
                    f.write(f"{prefix}.{middle}.{suffix}{num}\n")
                    f.write(f"{prefix}.{middle}.{suffix}.{num}\n")
        
        for middle1 in refined_wordlist:
            for middle2 in refined_wordlist:
                for suffix in suffixes:
                    for num in common_numbers:
                        f.write(f"{prefix}.{middle1}.{middle2}.{suffix}{num}\n")
                        f.write(f"{prefix}.{middle1}.{middle2}.{suffix}.{num}\n")
        
        subset_size_5 = 10  # Use a smaller subset to reduce combinations
        for middle1 in refined_wordlist[:subset_size_5]:
            for middle2 in refined_wordlist[:subset_size_5]:
                for middle3 in refined_wordlist[:subset_size_5]:
                    for suffix in suffixes:
                        for num in common_numbers:
                            f.write(f"{prefix}.{middle1}.{middle2}.{middle3}.{suffix}{num}\n")
                            f.write(f"{prefix}.{middle1}.{middle2}.{middle3}.{suffix}.{num}\n")
        
        subset_size_6 = 5  # Use an even smaller subset for 6-word combinations
        for middle1 in refined_wordlist[:subset_size_6]:
            for middle2 in refined_wordlist[:subset_size_6]:
                for middle3 in refined_wordlist[:subset_size_6]:
                    for middle4 in refined_wordlist[:subset_size_6]:
                        for suffix in suffixes:
                            for num in common_numbers:
                                f.write(f"{prefix}.{middle1}.{middle2}.{middle3}.{middle4}.{suffix}{num}\n")
                                f.write(f"{prefix}.{middle1}.{middle2}.{middle3}.{middle4}.{suffix}.{num}\n")

def analyze_combinations():
    """
    Analyzes the number of combinations and estimated file size for both variants.
    """
    two_word_combinations = len(suffixes) * len(common_numbers) * 2  # With and without separator
    three_word_combinations = len(refined_wordlist) * len(suffixes) * len(common_numbers) * 2
    four_word_combinations = len(refined_wordlist) * len(refined_wordlist) * len(suffixes) * len(common_numbers) * 2
    
    subset_size_5 = 10
    five_word_combinations = (subset_size_5 * subset_size_5 * subset_size_5 * 
                             len(suffixes) * len(common_numbers) * 2)
    
    subset_size_6 = 5
    six_word_combinations = (subset_size_6 * subset_size_6 * subset_size_6 * subset_size_6 * 
                            len(suffixes) * len(common_numbers) * 2)
    
    total_combinations = (two_word_combinations + three_word_combinations + 
                         four_word_combinations + five_word_combinations + 
                         six_word_combinations)
    
    avg_word_length = sum(len(word) for word in refined_wordlist) / len(refined_wordlist)
    avg_subset5_word_length = sum(len(word) for word in refined_wordlist[:subset_size_5]) / subset_size_5
    avg_subset6_word_length = sum(len(word) for word in refined_wordlist[:subset_size_6]) / subset_size_6
    avg_suffix_length = sum(len(suffix) for suffix in suffixes) / len(suffixes)
    avg_number_length = sum(len(num) for num in common_numbers) / len(common_numbers)
    
    avg_two_word_length = len(prefix) + 1 + avg_suffix_length + avg_number_length + 1  # +1 for newline
    avg_three_word_length = len(prefix) + 1 + avg_word_length + 1 + avg_suffix_length + avg_number_length + 1
    avg_four_word_length = len(prefix) + 1 + avg_word_length + 1 + avg_word_length + 1 + avg_suffix_length + avg_number_length + 1
    avg_five_word_length = len(prefix) + 1 + avg_subset5_word_length + 1 + avg_subset5_word_length + 1 + avg_subset5_word_length + 1 + avg_suffix_length + avg_number_length + 1
    avg_six_word_length = len(prefix) + 1 + avg_subset6_word_length + 1 + avg_subset6_word_length + 1 + avg_subset6_word_length + 1 + avg_subset6_word_length + 1 + avg_suffix_length + avg_number_length + 1
    
    avg_bytes_per_line = ((avg_two_word_length * two_word_combinations) +
                         (avg_three_word_length * three_word_combinations) +
                         (avg_four_word_length * four_word_combinations) +
                         (avg_five_word_length * five_word_combinations) +
                         (avg_six_word_length * six_word_combinations)) / total_combinations
    
    space_file_size = total_combinations * avg_bytes_per_line
    period_file_size = space_file_size  # Roughly the same size, just with periods instead of spaces
    
    def format_size(size_bytes):
        if size_bytes < 1024:
            return f"{size_bytes:.2f} bytes"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.2f} KB"
        elif size_bytes < 1024 * 1024 * 1024:
            return f"{size_bytes / (1024 * 1024):.2f} MB"
        else:
            return f"{size_bytes / (1024 * 1024 * 1024):.2f} GB"
    
    space_size_str = format_size(space_file_size)
    period_size_str = format_size(period_file_size)
    
    print(f"Number of words in refined wordlist: {len(refined_wordlist)}")
    print(f"Number of common numbers to append: {len(common_numbers)}")
    
    print(f"\nCombinations by length (for each variant - space and period):")
    print(f"2 words with numbers: {two_word_combinations:,}")
    print(f"3 words with numbers: {three_word_combinations:,}")
    print(f"4 words with numbers: {four_word_combinations:,}")
    print(f"5 words with numbers: {five_word_combinations:,}")
    print(f"6 words with numbers: {six_word_combinations:,}")
    print(f"Total combinations per variant: {total_combinations:,}")
    print(f"Total combinations (both variants): {total_combinations * 2:,}")
    
    print(f"\nEstimated file sizes:")
    print(f"Space-separated variant: {space_size_str}")
    print(f"Period-separated variant: {period_size_str}")
    print(f"Total size (both files): {format_size(space_file_size + period_file_size)}")
    
    print("\nSample passphrases (space-separated):")
    print(f"{prefix} {suffixes[0]}{common_numbers[0]}")  # Without space
    print(f"{prefix} {suffixes[0]} {common_numbers[0]}")  # With space
    print(f"{prefix} {refined_wordlist[0]} {suffixes[0]}{common_numbers[0]}")
    print(f"{prefix} {refined_wordlist[0]} {refined_wordlist[1]} {suffixes[0]}{common_numbers[0]}")
    
    print("\nSample passphrases (period-separated):")
    print(f"{prefix}.{suffixes[0]}{common_numbers[0]}")  # Without period
    print(f"{prefix}.{suffixes[0]}.{common_numbers[0]}")  # With period
    print(f"{prefix}.{refined_wordlist[0]}.{suffixes[0]}{common_numbers[0]}")
    print(f"{prefix}.{refined_wordlist[0]}.{refined_wordlist[1]}.{suffixes[0]}{common_numbers[0]}")
    
    return {
        "total_combinations_per_variant": total_combinations,
        "total_combinations": total_combinations * 2,
        "space_file_size": space_file_size,
        "period_file_size": period_file_size,
        "space_size_str": space_size_str,
        "period_size_str": period_size_str,
        "total_size_str": format_size(space_file_size + period_file_size),
        "combinations": {
            "two_word": two_word_combinations,
            "three_word": three_word_combinations,
            "four_word": four_word_combinations,
            "five_word": five_word_combinations,
            "six_word": six_word_combinations
        }
    }

if __name__ == "__main__":
    print("Analyzing combinations for number-appended passphrases...")
    stats = analyze_combinations()
    
    print("\nThis script can generate two wordlist files:")
    print("1. this_space_number_pass.txt - Space-separated words with numbers appended")
    print("2. this_period_number_pass.txt - Period-separated words with numbers appended")
    
    if stats["space_file_size"] + stats["period_file_size"] < 1024 * 1024 * 1024:  # Less than 1GB total
        choice = input("Do you want to generate these files? (y/n): ")
        
        if choice.lower() == 'y':
            print("Generating space-separated passphrases with numbers...")
            generate_space_number_passphrases()
            print("File 'this_space_number_pass.txt' has been generated successfully!")
            
            print("Generating period-separated passphrases with numbers...")
            generate_period_number_passphrases()
            print("File 'this_period_number_pass.txt' has been generated successfully!")
        else:
            print("File generation cancelled.")
    else:
        print("\nWARNING: The estimated total file size exceeds 1GB.")
        print("Please modify the script to reduce the number of combinations.")
