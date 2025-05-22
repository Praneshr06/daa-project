def find_two_sum_presort(arr, target_sum):
    sorted_arr = sorted(arr)
    left = 0
    right = len(sorted_arr) - 1
    
    while left < right:
        current_sum = sorted_arr[left] + sorted_arr[right]
        
        if current_sum == target_sum:
            return True, (sorted_arr[left], sorted_arr[right])
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1
    return False, None
if __name__ == "__main__":
    try:
        print("Enter the array elements (space-separated numbers):")
        arr_input = input().strip()
        arr = [float(x) for x in arr_input.split()]
        print("Enter the target sum:")
        target_sum = float(input().strip())
        found, pair = find_two_sum_presort(arr, target_sum)
        print("\nResults:")
        print(f"Array: {arr}")
        print(f"Target sum: {target_sum}")
        if found:
            print(f"Found pair: {pair[0]} + {pair[1]} = {target_sum}")
        else:
            print("No pair found that sums to target")
            
    except ValueError:
        print("Error: Please enter valid numbers")
    except Exception as e:
        print(f"An error occurred: {str(e)}") 