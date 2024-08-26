import matplotlib.pyplot as plt

# Data from the runs
runs = range(1, 8)
similarity_original_current = [
    0.9999999946937794, 0.977447589046914, 0.9678367714140134, 0.9590747346876928,
    0.9590747346876928, 0.8444628468177453, 0.8219572238309572
]
similarity_current_rephrased = [
    0.977447589046914, 0.969503316388233, 0.9754293543306672, 0.9999999956691429,
    0.9309912596481553, 0.9879115467792287, 0.9829721585835615
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
