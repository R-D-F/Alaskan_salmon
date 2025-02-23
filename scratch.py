import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Sample data
categories = ["A", "B", "C", "D", "E"]
num_categories = len(categories)

# Initialize figure and axis
fig, ax = plt.subplots()
bars = ax.bar(categories, np.zeros(num_categories))  # Start with empty bars
ax.set_ylim(0, 100)  # Set y-axis limits


# Update function for animation
def update(frame):
    new_values = np.random.randint(10, 100, num_categories)
    print(new_values)  # Generate random data
    for bar, new_val in zip(bars, new_values):
        bar.set_height(new_val)  # Update bar height
    return bars


# Create animation
ani = animation.FuncAnimation(fig, update, frames=50, interval=500, blit=False)


# x = np.linspace(0, 2 * np.pi, 400)
# y = np.sin(x**2)

# f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
# ax1.plot(x, y)
# ax1.set_title("Sharing Y axis")
# ax2.scatter(x, y)
plt.show()
