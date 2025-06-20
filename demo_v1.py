import google.generativeai as genai
import pandas as pd
# Initialize Gemini model
genai.configure(api_key="yourkey")
model = genai.GenerativeModel("gemini-2.0-flash")

# Define Agent class
class Agent:
    def __init__(self, name, role, private_info, personality):
        self.name = name
        self.role = role
        self.private_info = private_info
        self.personality = personality
        self.memory = []

    def generate_prompt(self, public_info, conversation_history):
        prompt = f"""You are {self.name}, your role is {self.role}.
Your personality is {self.personality}.
Known public information: {public_info}
Your private information: {self.private_info}

Here is the current conversation record:
{conversation_history}

Please continue your speech as this character in the next round:"""
        return prompt

    def speak(self, model, public_info, conversation_history):
        prompt = self.generate_prompt(public_info, conversation_history)
        response = model.generate_content(prompt)
        return response.text.strip()

# Set up agent list
agents = [
    Agent("Michael", "SVP of Human Resources", "You are especially concerned that the new CFO can help the company heal its internal tensions and avoid worsening existing conflicts on the management team. You have gathered the following confidential insights about each candidate: Suzanne T. Valdez is often late to meetings but has strong attention to detail. She once won a local photography contest and enjoys playing chess. Kristin B. Koljord is an excellent public speaker, though some staff describe her as interpersonally overbearing. She is detail-oriented, led a United Way charity campaign, and worked in London for two years in the finance division of Technology Solutions’ European operation. Nancy F. Larson is also detail-oriented but tends to overlook others’ contributions once projects are complete. She completed the company's internal leadership training and is described by subordinates as demanding but fair.", "Empathetic"),
    Agent("Olivia", "SVP of Marketing", "You are especially concerned that the new CFO has a total organizational perspective. If the candidate cannot help unify company strategy, it will be difficult to run a coherent marketing campaign. You have gathered the following confidential insights about each candidate: Suzanne T. Valdez is described by staff as cold and aloof, though she has good attention to detail. She completed the company’s managerial leadership program and enjoys playing chess. Kristin B. Koljord is an excellent public speaker, but some staff also view her as cold and aloof. She is detail-oriented, played a key role in a stock issue for Technology Solutions two years ago, and worked in London in the finance division of their European operations. Nancy F. Larson tends not to recognize others’ contributions once projects are finished. She completed the company’s leadership course, organized the farewell tribute for the retiring CFO, and has extensive international experience in travel and business consulting.", "Persuasive"),
    Agent("Sophia", "SVP of Operations", "You are especially concerned that the new CFO must be able to make the tough financial decisions needed to keep operations financially sound. PB Technologies is planning significant investments in technology, and you want to ensure the company has the financial leadership to support them. You have gathered the following confidential insights about the candidates: Suzanne T. Valdez is not an inspiring speaker but is known for her attention to detail. She received strong reviews as chair of the company’s dispute resolution committee and enjoys playing chess. Kristin B. Koljord is an excellent public speaker and is skilled at using organizational politics to her advantage. She is detail-oriented, served as volunteer CFO of a homeless shelter for two years, and worked in London in Technology Solutions’ European finance division. Nancy F. Larson tends to overlook others’ contributions once projects end but is insightful about internal organizational politics. She completed the company’s leadership training and published a guide on improving internal audit practices.", "Pragmatic")
]

# Public information
public_info = """
You are an interviewer tasked with selecting one of the candidates for the position of CFO of PB technology company. 
First, review your private information and state your initial preference in the first round. 
Then, begin the discussion with the other interviewers. 
The discussion will last for 5 rounds, and a final decision must be made by the end of round 5.

Each interviewer must keep their response under 50 words per round. In Round 1, simply state your initial preference without explanation.

Three candidates are being considered:

1. Suzanne T. Valdez  
- Current Position: Vice President of Finance, PB Technologies  
- Past Positions: Analyst at Price Waterhouse; 18 years in various finance roles at PB Technologies  
- Education: Executive MBA, 5 years ago  

2. Kristin B. Koljord  
- Current Position: Vice President of Finance, Technology Solutions, Inc. (PB Technologies’ main competitor)  
- Past Positions: Sales at IBM (2 years); Managerial roles at Technology Solutions, Inc.  
- Education: MBA in Finance, 15 years ago  

3. Nancy F. Larson  
- Current Position: Vice President of Accounting and Controller, PB Technologies  
- Past Positions: SEC Analyst; Accounting roles at PB Technologies  
- Education: MBA (15 years ago); CPA certification (19 years ago)
"""
conversation = ""
conversation_records = []

# Simulate rounds of conversation and collect history
history_by_round = []

for round_num in range(10):
    print(f"\n🔁 Round {round_num+1} Discussion")
    current_round = [f"🔁 Round {round_num+1} Discussion"]
    for agent in agents:
        response = agent.speak(model, public_info, conversation)

        # Avoid duplicate role name prefix
        if response.startswith(f"{agent.name}：") or response.startswith(f"{agent.name}:"):
            line = response
        else:
            line = f"{agent.name}：{response}"
        print(line)

        conversation_records.append({
            "Round": round_num + 1,
            "Speaker": agent.name,
            "Content": response
        })

        conversation += f"\n{line}"
        current_round.append(line)
    history_by_round.append("\n".join(current_round))

import os

def get_next_filename(prefix, suffix):
    i = 1
    while os.path.exists(f"{prefix}{i}{suffix}"):
        i += 1
    return f"{prefix}{i}{suffix}"

csv_filename = get_next_filename("test", ".csv")

df = pd.DataFrame(conversation_records)
df.to_csv(csv_filename, index=False, encoding="utf-8-sig")
print(f"📝 Conversation log saved as '{csv_filename}'")


