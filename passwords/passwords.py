import hashlib
import datetime
import time




# # THIS DOES PASSWORDS1 CRACKING
# # Create an empty dictionary to store hash-word pairs

# start = datetime.datetime.now()
# hash_word_dict = {}

# words_file = "./passwords/words.txt"

# # Read the list of words from the 'words.txt' file
# with open(words_file, 'r') as file:
#     words = [line.strip().lower() for line in file]

# # Iterate through the list of words and compute SHA-256 hashes
# for word in words:
#     # Hash the word using SHA-256
#     hashed_word = hashlib.sha256(word.encode()).hexdigest()
    
#     # Store the hash-word pair in the dictionary
#     hash_word_dict[hashed_word] = word


# # Open the 'passwords1.txt' file for reading and 'passwords1cracked.txt' for writing
# with open('./passwords/passwords1.txt', 'r') as passwords_file, open('./passwords/passwords1cracked.txt', 'w') as cracked_file:
#     for line in passwords_file:
#         # Split the line into username and hash (assuming the format is "username:hash")
#         parts = line.strip().split(':')
        
#         username, hash_value = parts[0], parts[1]

#         # Check if the hash is in the dictionary
#         cracked_password = hash_word_dict.get(hash_value, None)

#         if cracked_password is not None:
#             # Write the username and cracked password to the 'passwords1cracked.txt' file
#             cracked_file.write(f'{username}:{cracked_password}\n')

# endtime = datetime.datetime.now()

# elapsetime = endtime - start
# print("Execution time:", elapsetime, "seconds")




# # THIS DOES PASSWORDS2 CRACKING
# # Create an empty dictionary to store hash-username pairs for passwords2.txt
# hash_username_dict = {}

# start = datetime.datetime.now()

# # Open the 'passwords2.txt' file for reading
# with open('./passwords/passwords2.txt', 'r') as passwords_file:
#     print("HERE")
#     for line in passwords_file:
#         # Split the line into username and two-word hash
#         parts = line.strip().split(':')
#         username, hash_value = parts[0], parts[1]
#         print("Username: " + username + " Hash: " + hash_value)
#         # Store the hash-username pair in the dictionary
#         hash_username_dict[hash_value] = username
#     print("HERE")

# with open("./passwords/words.txt", 'r') as file:
#     words = [line.strip().lower() for line in file]

# for key, value in hash_username_dict.items():
#         print(f"Key: {key}, Value: {value}")


# # Now, iterate through all possible two-word combinations and hash them
# # Compare the hash against the hash_username_dict to find the corresponding username
# with open('./passwords/passwords2cracked.txt', 'a') as cracked_file:
#     for word1 in words:
#         for word2 in words:
#             two_word_password = word1 + word2
#             # print(two_word_password)
#             hashed_password = hashlib.sha256(two_word_password.encode()).hexdigest()
#             # print(hashed_password)
#             # Check if the hash exists in the dictionary
#             if hashed_password in hash_username_dict:
#                 username = hash_username_dict[hashed_password]
#                 # Write the username and cracked password to 'passwords2cracked.txt'
#                 cracked_file.write(f'{username}:{two_word_password}\n')
#                 curtime = datetime.datetime.now()
#                 elapsed_time = curtime - start
#                 print("Username: " + username + " || Password: " + two_word_password + " || Elapsed time: " + str(elapsed_time))





# THIS DOES PASSWORD3 CRACKING
# Load words from the words.txt file
with open("./passwords/words.txt", 'r') as file:
    words = [line.strip().lower() for line in file]

start = datetime.datetime.now()

hash_count = 0
# salt = "213ae676"
# password = "marmot"
# combined = salt + password
# hashed_correct = hashlib.sha256(combined.encode()).hexdigest()
# print(hashed_correct)

# Read the list of username-hash combos from passwords3.txt
with open('./passwords/passwords3.txt', 'r') as hash_file:
    with open('./passwords/passwords3cracked.txt', 'w') as cracked_file:
        for line in hash_file:
            # Split the line into parts
            parts = line.split(':')
            
            username = parts[0]
            user_hash = parts[1]
            # Split the user hash to get salt and target hash
            hash_parts = user_hash.split('$')
            salt = hash_parts[2]
            target_hash = hash_parts[-1]


            # print(username + " " + salt + " " + target_hash)
            
            for word in words:
                # Concatenate the salt and word
                candidate_password = salt + word
                # print(candidate_password)
                # Hash the candidate password
                hashed_password = hashlib.sha256(candidate_password.encode()).hexdigest()
                hash_count = hash_count + 1
                if hashed_password == target_hash:
                    print("Username: " + username + " || Password: " + word)
                    cracked_file.write(f"{username}:{word}\n")
                    break


curtime = datetime.datetime.now()
elapsed_time = curtime - start
print("Elapsed time: " + str(elapsed_time) + " || Total number of hashes computed = " + str(hash_count))