import pandas as pd

df = pd.read_csv("student_data.csv")

print(df.head())

x = df[["Study_Hours","Attendance","Previous_Marks"]]
y = df[["Final_Marks"]]

print(x.head())
print(y.head())

from sklearn.model_selection import train_test_split
x_train, x_test , y_train , y_test = train_test_split(
    x,
    y,
    test_size = 0.2,
    random_state=42
)

print("Training rows:", len(x_train))
print("Testing rows:" , len(x_test))

from sklearn.linear_model import LinearRegression
model = LinearRegression()

model.fit(x_train, y_train)

import pandas as pd

new_student = pd.DataFrame({
    "Study_Hours":[8],
    "Attendance" :[90],
    "Previous_Marks" :[80]
})
prediction = model.predict(new_student)
print("predicted marks:" , prediction)

print("Model Trained Succesfully")

from sklearn.metrics import mean_absolute_error
y_pred = model.predict(x_test)
mae = mean_absolute_error(y_test, y_pred)
print("MAE:", mae)

print(type(x))
print(type(y))
print(type(new_student))
print(type(df["Attendance"]))
print(type(df[["Attendance"]]))

from sklearn.metrics import r2_score

y_pred = model.predict(x_test)

r2 = r2_score(y_test, y_pred)

print("R2 Score:", r2)

import matplotlib.pyplot as plt
plt.scatter(y_test,y_pred)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
)

plt.xlabel("Actual marks")
plt.ylabel("Predicted marks")
plt.title("Actual vs predicted marks")
plt.savefig("graph.png")
plt.show()