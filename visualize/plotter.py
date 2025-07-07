import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import os

# A list to store all chart data in memory
chart_data = []  # Each element = (pair_name, equity_series, zscore_series)

def add_chart_data(pair_name, equity_series, z_series):
    chart_data.append((pair_name, equity_series, z_series))

def show_chart_viewer():
    if not chart_data:
        print("No chart data to display.")
        return

    # Create main window
    root = tk.Tk()
    root.title("Pairs Trading Visualizer")

    root.bind('<Right>', lambda event: next_chart())
    root.bind('<Left>', lambda event: prev_chart())

    current_index = [0]  # Use mutable type to allow modification in inner scope

    # Create figure and subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    def draw_chart(index):
        pair, equity, z = chart_data[index]
        ax1.clear()
        ax2.clear()

        # Equity Curve
        ax1.plot(equity)
        ax1.set_title(f"Equity Curve - {pair}")
        ax1.set_ylabel("Portfolio Value ($)")
        ax1.grid(True)

        # Z-Score
        ax2.plot(z, label="Z-Score")
        ax2.axhline(2, color='red', linestyle='--')
        ax2.axhline(-2, color='green', linestyle='--')
        ax2.axhline(0, color='black', linestyle='-')
        ax2.set_title(f"Z-Score of Spread - {pair}")
        ax2.legend()
        ax2.grid(True)

        fig.tight_layout()
        canvas.draw()

    def next_chart():
        current_index[0] = (current_index[0] + 1) % len(chart_data)
        draw_chart(current_index[0])

    def prev_chart():
        current_index[0] = (current_index[0] - 1) % len(chart_data)
        draw_chart(current_index[0])

    def on_close():
        plt.close('all')
        root.destroy()

    # Buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    prev_button = tk.Button(button_frame, text="⟵ Previous", command=prev_chart)
    prev_button.pack(side=tk.LEFT, padx=10)

    next_button = tk.Button(button_frame, text="Next ⟶", command=next_chart)
    next_button.pack(side=tk.LEFT, padx=10)

    quit_button = tk.Button(button_frame, text="Exit", command=on_close)
    quit_button.pack(side=tk.LEFT, padx=10)

    # Draw the first chart and start GUI loop
    draw_chart(current_index[0])
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()
