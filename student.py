import ollama
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv("student_performance_dataset.csv")

# print(df.head())
# print(df.isnull().sum())

x = df[
    [
        "daily_study_hours",
        "attendance_percent",
        "exam_score"
    ]
]

y = df["study_efficiency"]

dt = DecisionTreeRegressor(
    max_depth=5,
    random_state=42
)

dt.fit(x, y)

messages = [
    {
        "role": "system",
        "content": "You are a helpful and friendly AI chatbot and student performance. Explain predictions clearly and simply."
    }
]

while True:

    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break

    if user_input.lower() == "predict":
        daily_study_hours = float(
            input("Study hours: ")
        )

        attendance_percent = float(
            input("Attendance percentage: ")
        )

        exam_score = float(
            input("Exam score: ")
        )

        prediction = dt.predict([
            [
                daily_study_hours,
                attendance_percent,
                exam_score
            ]
        ])[0]

        print(
            "ML Prediction:",
            round(prediction, 2)
        )

        messages.append({
            "role": "user",
            "content": f"""
Student details:

Study hours: {daily_study_hours}
Attendance percentage: {attendance_percent}
Exam score: {exam_score}

Predicted study efficiency: {prediction:.2f}

Explain this prediction to the student clearly and simply.
Mention how the student's study hours, attendance,
and exam score relate to the prediction.
"""
        })

    else:

        messages.append({
            "role": "user",
            "content": user_input
        })

    print("Chatbot: ", end="", flush=True)

    stream = ollama.chat(
        model="llama3.2",
        messages=messages,
        stream=True
    )

    answer = ""
    for chunk in stream:
        text = chunk["message"]["content"]
        print(text, end="", flush=True)
        answer += text

    print()

    messages.append({
        "role": "assistant",
        "content": answer
    })