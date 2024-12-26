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


# using matplot 

plt.hist(student_df['Age'], bins=10)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age')
plt.show()

# box plate with matplotlib

plt.boxplot(student_df['Grade'])
plt.title('Box plate of Grade')
plt.show()


# Data Exploration
# Correlation heatmap with matplotlib
correlation_matrix = student_df.corr()
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.title('Correlation Heatmap')
plt.show()
