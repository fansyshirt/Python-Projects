def count_elements(text):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
    

def calculate_entropy(text):
    """Calculate the entropy of a given text."""
    # Remove non-printable characters and empty string cases
    text = ''.join(filter(str.isprintable, text)).strip()
    if not text:
        return 0
    
    # Calculate frequency of each character
    frequency = count_elements(text)
    length = len(text)
    
    # Calculate entropy
    entropy = 0
    for count in frequency.values():
        probability = count / length
        entropy -= probability
    
    return entropy

def analyze_text(text):
    """Analyze the text and classify it based on entropy."""
    entropy = calculate_entropy(text)
    
    # Define thresholds (these values can be adjusted based on empirical data)
    RANDOM_THRESHOLD = 4.5
    HUMAN_READABLE_THRESHOLD = 1.5
    
    if entropy > RANDOM_THRESHOLD:
        classification = "Random"
    elif entropy < HUMAN_READABLE_THRESHOLD:
        classification = "Human-readable"
    else:
        classification = "Mixed"
    
    return entropy, classification

def main():
    # Example texts
    random_text = "fghjklqwertyuiopasdfgh"
    human_readable_text = "This is a sample text."

    # Analyze texts
    random_entropy, random_classification = analyze_text(random_text)
    readable_entropy, readable_classification = analyze_text(human_readable_text)
    
    # Print results
    print(f"Random Text Entropy: {random_entropy:.2f}, Classification: {random_classification}")
    print(f"Human-readable Text Entropy: {readable_entropy:.2f}, Classification: {readable_classification}")

if __name__ == "__main__":
    main()
