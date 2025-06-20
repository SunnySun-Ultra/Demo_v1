# Demo_v1📝 项目说明

本项目旨在模拟一个由三位公司高管（SVP）组成的多轮角色扮演式讨论场景，围绕三位 CFO 候选人的任命展开。每位角色具备各自的职位、性格特征（Personality）与私人关注点（Private Information）。对话内容由 Google Gemini 模型自动生成，并将全过程结构化保存，便于后续分析与可视化。

⸻

✅ 当前进展
	•	已完成三位角色剧本设定，内容包括姓名、职位、个性特征与私人关注点
	•	编写主脚本 gemini.py，实现以下功能：
	•	支持模拟 10 轮群体讨论过程
	•	每轮调用 Gemini 模型生成每位角色的发言内容
	•	持续维护上下文，确保角色语言逻辑连贯、立场稳定
	•	自动记录发言内容至结构化 CSV 文件，字段为：Round, Speaker, Content
	•	文件命名支持自动编号（如 test1.csv, test2.csv），避免覆盖历史记录

⸻


📌 上次问题：
如何确保在规定轮次内做出最终决策？
项目初始设定中，公共信息明确指出 “共 5 轮讨论，需在第 5 轮作出决定”。但在实际运行中发现：
	•	模型有时无法在第 5 轮前或当轮明确给出决策（例如未明确表态或持续中立）
 
🔧 改进方案：
	•	保持公开信息不变（仍强调第 5 轮为决策点）
	•	将实际模拟轮次扩展为 10 轮，给予模型更充分的时间自然推进对话

✅ 改进效果：
	•	模型能在第 7 轮左右明确形成共识
	•	随后轮次（8~10）进入“重复确认”阶段

🧾 示例：重复确认内容
🔁 Round 8 Discussion
Michael: Okay, everyone. I appreciate the thoughtful discussion and willingness to compromise. Now that we’ve decided on Kristin, let’s focus on ensuring a welcoming and supportive environment for her. I want to personally reach out to both Suzanne and Nancy to acknowledge their contributions and make sure they understand this decision isn’t a reflection of their abilities. We value them both here.

⸻

🔁 Round 9 Discussion
Michael: Okay, everyone. I appreciate the thoughtful discussion and willingness to compromise. Now that we’ve decided on Kristin, let’s focus on ensuring a welcoming and supportive environment for her. I want to personally reach out to both Suzanne and Nancy to acknowledge their contributions and make sure they understand this decision isn’t a reflection of their abilities. We value them both here.

⸻

🔁 Round 10 Discussion
Michael: Okay, everyone. I appreciate the thoughtful discussion and willingness to compromise. Now that we’ve decided on Kristin, let’s focus on ensuring a welcoming and supportive environment for her. I want to personally reach out to both Suzanne and Nancy to acknowledge their contributions and make sure they understand this decision isn’t a reflection of their abilities. We value them both here.
