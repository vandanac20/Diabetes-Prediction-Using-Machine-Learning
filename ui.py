import tkinter as tk
from tkinter import ttk, messagebox

def make_prediction():
    try:
        pregnancies = float(entries[0].get())
        plasma_glucose = float(entries[1].get())
        diastolic_blood_pressure = float(entries[2].get())
        bmi = float(entries[3].get())
        diabetes_pedigree = float(entries[4].get())
        age = float(entries[5].get())

        is_diabetic = (
            plasma_glucose > 125 or
            diastolic_blood_pressure >= 85 or bmi >= 30 or
            diabetes_pedigree > 0.5 
        )

        is_likely = (
            not is_diabetic and (
               101 <= plasma_glucose <= 125 or
                81 <= diastolic_blood_pressure <= 89 or
                25 <= bmi <= 29 or
                0.4 <= diabetes_pedigree <= 0.5 
            )
        )

        if is_diabetic:
            result_label.config(text="🔴 Diabetic", foreground="#e63946")
            probability_label.config(text="Confidence: 100%", foreground="#e63946")
            precautions_text = (
                "📝 Precautions:\n\n"
                "🚶‍♂ Stay active daily\n"
                "🧘 Practice yoga & reduce stress\n"
                "🩺 Monitor blood sugar regularly\n"
                "🚫 Avoid sugary foods and drinks\n"
                "🥗 Eat balanced meals"
            )
            food_text = (
                "🍽 Food to Eat:\n\n"
                "🥦 Broccoli, Kale, Spinach\n"
                "🍚 Brown rice, Quinoa\n"
                "🐟 Grilled Fish, 🐔 Chicken\n"
                "🥑 Avocados, 🥜 Nuts\n"
                "🍎 Apples, 🍓 Berries"
            )
        elif is_likely:
            result_label.config(text="🟠 Likely Diabetic", foreground="#ff9900")
            probability_label.config(text="Confidence: 70%", foreground="#ff9900")
            precautions_text = (
                "📝 Precautions:\n\n"
                "🚶 Walk at least 30 mins/day\n"
                "🧂 Control salt & sugar intake\n"
                "📉 Keep BMI in healthy range\n"
                "🥤 Avoid soda and fried foods"
            )
            food_text = (
                "🍽 Food to Eat:\n\n"
                "🥒 Zucchini, Cabbage\n"
                "🍗 Tofu, Chicken\n"
                "🥣 Oats, Multigrain roti\n"
                "🍇 Berries, 🍓 Strawberries"
            )
        else:
            result_label.config(text="🟢 Not Diabetic", foreground="#2a9d8f")
            probability_label.config(text="Confidence: 30%", foreground="#2a9d8f")
            precautions_text = (
                "📝 Precautions:\n\n"
                "🏃‍♀ Stay physically active\n"
                "🍎 Eat a balanced diet\n"
                "😴 Get enough sleep\n"
                "🧘‍♀ Manage stress levels"
            )
            food_text = (
                "🍽 Food to Eat:\n\n"
                "🥗 Leafy greens, Vegetables\n"
                "🍞 Whole grains\n"
                "🍉 Fruits in moderation\n"
                "🥜 Olive oil, Nuts"
            )

        result_card.pack(pady=10)
        precautions_note.pack(pady=15)
        food_note.pack(pady=15)
        precautions_label.config(text=precautions_text)
        food_label.config(text=food_text)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers in all fields.")

# Setup
root = tk.Tk()
root.title("🌈 Diabetes Risk Predictor")
root.geometry("950x850")
root.configure(bg="#f0f2f5")

style = ttk.Style()
style.configure("TEntry", padding=10, font=("Segoe UI", 14))
style.configure("TButton", font=("Segoe UI", 14, "bold"), padding=12)

# Header
header = tk.Frame(root, bg="#6a0572", height=80)
header.pack(fill="x")
tk.Label(header, text="🌟 Diabetes Risk Predictor", font=("Helvetica", 28, "bold"),
         bg="#6a0572", fg="white").pack(pady=20)

# Layout
main_container = tk.Frame(root, bg="#f0f2f5")
main_container.pack(pady=20, padx=20, fill="both", expand=True)

# Left: Inputs + Button
input_frame = tk.Frame(main_container, bg="white", bd=2, relief="solid", padx=20, pady=20)
input_frame.pack(side="left", fill="y", expand=True, padx=10)

labels_text = [
    "Pregnancies", "Plasma Glucose", "Diastolic Blood Pressure",
    "BMI", "Diabetes Pedigree", "Age"
]
entries = []
for i, label_text in enumerate(labels_text):
    tk.Label(input_frame, text=f"{label_text}:", font=("Segoe UI", 14, "bold"),
             bg="white", anchor="w", fg="#6a0572").grid(row=i, column=0, sticky="w", padx=10, pady=10)
    entry = ttk.Entry(input_frame, width=25)
    entry.grid(row=i, column=1, padx=10, pady=10)
    entries.append(entry)

# Predict Button under inputs
predict_btn = tk.Button(input_frame, text="🔍 Predict", command=make_prediction,
                        font=("Segoe UI", 16, "bold"), bg="#6a0572", fg="white",
                        activebackground="#4a148c", bd=0, padx=20, pady=12, cursor="hand2")
predict_btn.grid(row=len(labels_text), column=0, columnspan=2, pady=30)

# Right: Results & Notes
right_frame = tk.Frame(main_container, bg="white", bd=2, relief="solid", padx=20, pady=20)
right_frame.pack(side="left", fill="y", expand=True, padx=10)

# Hidden sections until prediction
result_card = tk.Frame(right_frame, bg="white", bd=2, relief="groove", padx=10, pady=10)
result_label = tk.Label(result_card, text="", font=("Segoe UI", 22, "bold"), bg="white")
result_label.pack(pady=5)
probability_label = tk.Label(result_card, text="", font=("Segoe UI", 14), bg="white")
probability_label.pack()
result_card.pack_forget()

# Precautions
precautions_note = tk.LabelFrame(right_frame, text="📋 Precautions Note", font=("Segoe UI", 16, "bold"),
                                fg="#d00000", bg="#fff0f0", padx=10, pady=10, bd=2, relief="ridge")
precautions_label = tk.Label(precautions_note, text="", font=("Segoe UI", 13), bg="#fff0f0",
                             anchor="w", justify="left", wraplength=350)
precautions_label.pack()
precautions_note.pack_forget()

# Food
food_note = tk.LabelFrame(right_frame, text="🍉 Food Recommendations", font=("Segoe UI", 16, "bold"),
                          fg="#007f5f", bg="#f0fff0", padx=10, pady=10, bd=2, relief="ridge")
food_label = tk.Label(food_note, text="", font=("Segoe UI", 13), bg="#f0fff0",
                      anchor="w", justify="left", wraplength=350)
food_label.pack()
food_note.pack_forget()

# Footer
tk.Label(root, text="Made with ❤ using Tkinter", bg="#f0f2f5", fg="#6a0572",
         font=("Segoe UI", 12)).pack(side="bottom", pady=15)

root.mainloop()