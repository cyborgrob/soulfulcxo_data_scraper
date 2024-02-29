import json

# Extract podcast audio transcript from AWS Transcribe JSON file
with open(r"C:\Users\rwynn\Desktop\asrOutput.json", "r") as json_file:
    data = json.load(json_file)
    transcript = data['results']['transcripts'][0]['transcript']
    print(transcript)
