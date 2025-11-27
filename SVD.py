# Import necessary libraries
from surprise import SVD, Dataset
from surprise.model_selection import train_test_split
from surprise import accuracy
import matplotlib.pyplot as plt

# Load the MovieLens 100k dataset
data = Dataset.load_builtin('ml-100k')

# Split the data into training and testing sets
trainset, testset = train_test_split(data, test_size=0.2, random_state=42)

# Initialize and train the SVD algorithm
svd = SVD()
svd.fit(trainset)

# Predict on the test set
predictions = svd.test(testset)

# Evaluate performance
rmse = accuracy.rmse(predictions)
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")

# ---------------- Visualization ----------------

# Extract actual and predicted ratings
y_true = [pred.r_ui for pred in predictions]     # actual ratings
y_pred = [pred.est for pred in predictions]      # predicted ratings

# Create scatter plot: Actual vs Predicted ratings
plt.figure(figsize=(8,6))
plt.scatter(y_true, y_pred, alpha=0.5, color='blue')
plt.plot([0, 5], [0, 5], '--r')  # ideal prediction line
plt.title("Actual vs Predicted Ratings (SVD on MovieLens 100k)")
plt.xlabel("Actual Rating")
plt.ylabel("Predicted Rating")
plt.grid(True)
plt.show()

# Plot prediction error distribution
errors = [true - pred for true, pred in zip(y_true, y_pred)]
plt.figure(figsize=(8,5))
plt.hist(errors, bins=30, color='purple', edgecolor='black')
plt.title("Distribution of Prediction Errors")
plt.xlabel("Prediction Error (Actual - Predicted)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
