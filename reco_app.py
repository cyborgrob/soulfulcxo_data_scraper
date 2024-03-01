import gradio as gr
from clean_text import top_three_podcasts

choices = ["Ep. 1 - Understanding ‘Privacy by Design’ Principles - Dr. Ann Cavoukian", "Ep. 2 - How to Build Trust and Set Boundaries - Theresa 'Terry' Grafenstine", "Ep. 3 - Achieving and Maintaining Cyber Resilience - Jim Routh", "Ep. 4 - Finding Your Calling and Your Passion - Theresa Payton", "Ep. 5 - Getting Through the Daily Noise - Ryan Kalember", "Ep. 6 - Identifying a 'World-Class CISO' with One Question - Dr. Eric Cole", "Ep. 7 - Critical Leadership Principles - Rick Howard", "Ep. 8 - Open Source Intelligence (OSINT) the Risks - Michele Stuart", "Ep. 9 - Setting the Scope of the Conversation - Ryan Fay", "Ep. 10 - Moving Away from the Comfortable - Todd Fitzgerald", "Ep. 11 - Practical Wisdom on Developing a Leadership Presence that Works - Debra Benton", "Ep. 12 - Career Progression and Holistic Hiring - Gary Hayslip", "Ep. 13 - Shift Your Mindset and Find a Job That Makes You Happy - Lisa Rangel", "Ep. 14 - Women Absolutely Belong in Cyber and as Leaders - Diana Kelley", "Ep. 15 - How to Translate Expertise in Technology to the Real World - Kate Fazzini", "Ep. 16 - Secrets to Successful Vendor Partnerships - Dorene Rettas", "Ep. 17 - The New ERA of AI Warfare - Chuck Brooks", "Ep. 18 - Be Deeply Passionate About What You Do - Avani Desai", "Ep. 19 - Finding Ways to Connect to the Culture - Kim Jones", "Ep. 20 - Evaluating Your Culture for Success - Caroline Wong", "Ep. 21 - Thrilling Story of a Secret Woman Spy", "Ep. 22 - Know How Your Company Makes Money - Anne Marie Zettlemoyer", "Ep. 23 - Do You Need a Career Escape - Jennifer Brick", "Ep. 24 - What Do You Stand For - Margaret Molloy", "Ep. 25 - Let's Go Back to Being Human - Chris Roberts", "Ep. 26 - Getting Yourself to a Better Place - Joey Johnson", "Ep. 27 - Create a Safe Environment to Fail - Sue Bergamo", "Ep. 28 - Success is Based Upon Your Habits - Jason Elrod", "Ep. 29 - Be Bold and Rebellious in Your Career - Nadja El Fertasi", "Ep. 30 - Getting to a Better Cyber Future - Ryan Kalember", "Ep. 31 - Better Yourself to Better Your Team - Bryan Kissinger", "Ep. 32 - Stand Firm in Your Ethics - Matthew Rosenquist", "Ep. 33 - The 5 Step Process Framework for Success - Theresa Payton", "Ep. 34 - How to Claim a Better Life - Tara LaFon Gooch", "Ep. 35 - What Do You Bring to the Table - Bob Turner", "Ep. 36 - Take Control of Your Destiny - Drew Simonis", "Ep. 37 - Achieve Success by Playing to Your Strengths - Jane Frankland", "Ep. 38 - True Personal Cost of a Cyber Attack - Gary Berman", "Ep. 39 - How to Accelerate Your Career Growth - Meredith Harper", "Ep. 40 - Set Yourself Up to Win - Mike Wilkes", "Ep. 41 - The Secret to Business Strategy Success - Jeroen Kraaijenbrink", "Ep. 42 - Top 3 Cyber Roadmaps for 2024-2034 - Dr. Georgianna 'George' Shea", "Ep. 43 - Be Your Own Best Advocate - Arti Raman", "Ep. 44 - You Must Be Ready for Change - Randi Levin", "Ep. 45 - To Be Successful Find Your Why - Masha Sedova", "Ep. 46 - Find Your Perfect Harmony and Life Meaning - Teresa Devine", "Ep. 47 - What Really Motivates Your Team - Chris Caruso", "Ep. 48 - Embrace Your Own Unique Voice - Marco Ciappelli", "Ep. 49 - Letting Go and Trusting Your Team - Tonia Dudley", "Ep. 50 - Proactive Privacy in the Age of AI - Dr. Ann Cavoukian", "Ep. 51 - CISO Master Class: Unveiling the Unexpected Game-Changer - Bob Chaput"]

# Function to recommend similar podcasts
def recommend_similar_podcasts(podcast_id):
    # Use reco model to get the top similar podcasts for the given ID
    similar_podcasts = []
    # get top 3 similar in int form
    top3 = top_three_podcasts(choices.index(podcast_id))
    # convert int form to name form
    for n in top3:
        name_form = choices[n]
        similar_podcasts.append(name_form)
    return similar_podcasts

# Interface setup
podcast_dropdown = gr.components.Dropdown(choices=choices, label="Select Podcast:")
output_text = gr.components.Textbox(label="Recommended podcasts:")

# Create gradio interface
interface = gr.Interface(fn=recommend_similar_podcasts, inputs=podcast_dropdown, outputs=output_text)
interface.launch()

