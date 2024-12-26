import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Student_ID': np.arange(1, 6),
    'Name': ['John', 'Emily', 'Michael', 'Sophia', 'William'],
    'Age': [20, 21, 19, 22, 20],
    'Grade': [3.8, 3.9, 3.5, 4.0, 3.7],
    'Major': ['Computer Science', 'Biology', 'Mathematics', 'Engineering', 'Psychology']
}

student_df = pd.DataFrame(data)

# detect outlayer using z-score with NumPy

z_score = (student_df['Grade'] - np.mean(student_df['Grade'])) / np.std(student_df['Grade'])

outliers = student_df[z_score > 3] | (z_score <- 3)

print(outliers)