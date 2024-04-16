import re, requests



response = requests.request("GET", "https://mullvad.net/en/servers")

      
# Find all matches
matches = re.findall(r'socks_name:\".*?\"', response.text)

extracted_texts_with_port = [text.split('"')[1] + ':1080' for text in matches]

print(extracted_texts_with_port)



with open('mullvad-socks5.txt', 'w') as file:
    for item in extracted_texts_with_port:
        file.write(f"{item}\n")
