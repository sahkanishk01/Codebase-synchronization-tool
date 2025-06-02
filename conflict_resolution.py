def resolve_conflict(original_code, new_code, translated_code):
    print("Conflict detected!")
    print("Original Code:\n", original_code)
    print("New Code:\n", new_code)
    print("Translated Code:\n", translated_code)

    
    choice = input("Choose which code to keep (o: original, n: new, t: translated): ")
    if choice == 'o':
        return original_code
    
    elif choice == 'n':
        return new_code
    
    elif choice == 't':
        return translated_code
    
    else:
        print("Invalid choice. Keeping original code.")
        return original_code
