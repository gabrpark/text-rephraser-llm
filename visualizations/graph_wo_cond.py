import matplotlib.pyplot as plt

# Data from the runs
runs = range(1, 8)
similarity_original_current = [
    0.9999999946937794, 0.9181446317078543, 0.8974146660923511, 0.9188836373514236,
    0.903130025111666, 0.8810246086808899, 0.9048709387637109
]
similarity_current_rephrased = [
    0.9181446317078543, 0.9919157769946687, 0.9939578916359822, 0.9962308416643132,
    0.9935413514632677, 0.9915032780724284, 0.9951718240546022
]

# Creating the plot
plt.figure(figsize=(10, 6))
plt.plot(runs, similarity_original_current, marker='o',
         linestyle='-', color='r', label='Original to Current')
plt.plot(runs, similarity_current_rephrased, marker='o',
         linestyle='-', color='b', label='Current to Rephrased')

# Adding titles and labels
plt.title('Similarity Across Text Adaptation Runs')
plt.xlabel('Run Number')
plt.ylabel('Similarity Score')
plt.xticks(runs)  # Set x-ticks to be explicit about the run numbers
plt.ylim(0.75, 1)  # Set the limits for the y-axis
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
