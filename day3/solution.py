import re
import os
def compute_mul(text):
    #Use regex to find all the mul(x,y) in the text
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, text)
    return sum(int(x) * int(y) for x, y in matches)

def compute_mul2(text):
    # Find do() and don't() instructions first
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    # Get all positions of do/don't instructions
    do_positions = [(m.start(), True) for m in re.finditer(do_pattern, text)]
    dont_positions = [(m.start(), False) for m in re.finditer(dont_pattern, text)]
    
    # Combine and sort by position
    enable_positions = sorted(do_positions + dont_positions)
    
    # Find all mul instructions with their positions
    mul_pattern = r"mul\((\d+),(\d+)\)"
    mul_matches = [(m.start(), int(m.group(1)), int(m.group(2))) for m in re.finditer(mul_pattern, text)]
    
    total = 0
    enabled = True  # Initially enabled
    
    for mul_pos, x, y in mul_matches:
        # Update enabled status based on any do/don't before this mul
        for pos, status in enable_positions:
            if pos < mul_pos:
                enabled = status
            else:
                break
                
        if enabled:
            total += x * y
            
    return total

def text2string(text):
    with open(text, 'r') as file:
        return file.read()

if __name__ == "__main__":

    test="xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    assert compute_mul(test) == 161

    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, "input.txt")
    text = text2string(input_file)

    print(f"Part 1: {compute_mul(text)}")
    print(f"Part 2: {compute_mul2(text)}")
