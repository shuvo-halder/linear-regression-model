import pandas as pd
import numpy as np

data = {
    'Student_ID': np.arange(1, 6),
    'Name': ['John', 'Emily', 'Michael', 'Sophia', 'William'],
    'Age': [20, 21, 19, 22, 20],
    'Grade': [3.8, 3.9, 3.5, 4.0, 3.7],
    'Major': ['Computer Science', 'Biology', 'Mathematics', 'Engineering', 'Psychology']
}

student_df = pd.DataFrame(data)

summery_state = student_df.describe()
print(summery_state)