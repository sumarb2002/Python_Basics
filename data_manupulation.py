import re

def modify_emails(data_list):
    count_list_data = []
    final_data = {'unique_count':0,'repeated_words':[],'palindromes':[]}
    palindromes = []
    repeated_words = []
    new_list = data_list.split(" ")
    for text in new_list:
        cleaned_text = re.sub(r'[^A-Za-z]', '', text).lower()
        if cleaned_text in count_list_data:
            repeated_words.append(cleaned_text)
        else:
            count_list_data.append(cleaned_text)
            final_data['unique_count'] += 1
            if cleaned_text[::-1] == cleaned_text:
                palindromes.append(cleaned_text)      
    
    final_data['palindromes'] = sorted(palindromes)
    final_data['repeated_words'] = sorted(repeated_words)
    print(final_data)
                
            
            
            
        



# test_data = "Wow! Did Hannah see that Race car? Mom was there too. Hannah did see it!"
test_data = input("Enter a String ")
modify_emails(test_data)