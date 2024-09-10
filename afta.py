import requests
import zipfile
import os

headers = {
    "Referer": "https://afta.gov.ir/fa-IR/Portal/4934/news/view/14615/2163/Staging/%D9%81%D8%A7%DB%8C%D9%84%E2%80%8C%D9%87%D8%A7%DB%8C-%D8%AD%D8%A7%D9%88%DB%8C-IP%D9%87%D8%A7%D8%8C-%D8%AF%D8%A7%D9%85%D9%86%D9%87%E2%80%8C%D9%87%D8%A7-%D9%88-URL%D9%87%D8%A7%DB%8C-%D8%A2%D9%84%D9%88%D8%AF%D9%87",
    "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Opera\";v=\"112\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "Windows",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0"
}

url = "https://afta.gov.ir:443/_portal/documents/ip/afta-threat-intel.zip"
file_name = url.split("/")[-1]

download_directory = "/opt/Threatintel"
extract_directory = "/opt/Threatintel"

# Create the directories if they don't exist
os.makedirs(download_directory, exist_ok=True)
download_path = os.path.join(download_directory, file_name)

print("[+] Downloading file ...")
response = requests.get(url, headers=headers, verify=False)

file_format = response.headers["Content-Type"]

if "zip" in file_format:
    print(f"[+] Saving file as {download_path}")
    with open(download_path, "wb") as f:
        f.write(response.content)
    print("[+] File Downloaded Successfully!")

    os.makedirs(extract_directory, exist_ok=True)
    
    # Extract the zip file
    with zipfile.ZipFile(download_path, 'r') as zip_ref:
        zip_ref.extractall(extract_directory)
    print(f"[+] File extracted to {extract_directory} successfully!")

    # Remove the zip file after extraction
    os.remove(download_path)
    print(f"[+] Zip file {download_path} deleted after extraction.")

else:
    print("[-] Error: Not a valid zip file.")
