## Soulful CXO Podcast Recommendation Engine
These are a collection of scripts to collect data from the Soulful CXO podcast library (https://soulful-cxo.simplecast.com/episodes), load that data into an SQLite database, provide transcriptions for the podcasts that didn't have any (using OpenAI's Whisper model), and use machine learning to compare transcripts and provide recommendations for similar podcast episodes to the one selected.

Currently the app can be launched using a Gradio interface. The user selects a particular podcast from a dropdown menu and the output will be three episodes that the model predicts are the most similar to the one selected.
