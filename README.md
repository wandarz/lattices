# Buffon's Needle Experiment

A web-based simulation of the classic Buffon's needle experiment—throwing needles onto a grid of vertical lines.

## Features

- **Needle/line ratio (d/l)**: Set the ratio of needle length to line spacing (default: 0.6)
- **Number of vertical lines**: Set how many vertical lines to display (default: 16)
- **Throw N needles**: Specify how many needles to throw (1–10,000)
- **Visual feedback**: Needles that cross lines are shown in green, others in gray
- **Crossing counter**: Displays how many needles crossed at least one vertical line

## Running the Simulation

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Start the Flask server:
   ```
   python app.py
   ```

3. Open http://127.0.0.1:5000 in your browser.

## Usage

1. Set **ratio (d/l)** – needle length relative to line spacing (default: 0.6)
2. Set **number of vertical lines** – how many lines to show (default: 16)
3. Set **number of needles (N)** – how many to throw (default: 100)
4. Click **Throw needles** to run the simulation
5. View the needles on the canvas and the crossing count below

When d ≤ l, the classical Buffon's needle formula gives the probability of a crossing as 2d/(πl), which can be used to estimate π.
