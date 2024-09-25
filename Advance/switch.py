def switch_case(option):
    match option:
        case 1:
            return "Case 1"
        case 2:
            return "Case 2"
        case 3:
            return "Case 3"
        case _:
            return "Default case"

# Example usage
result = switch_case(2)
print(result)  # Output: Case 2
