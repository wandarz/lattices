"""
Buffon's Needle Experiment - Web Simulation
Simulates throwing needles on a grid of vertical lines.
"""

import random
import math
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def throw_needles(l: float, d: float, n: int, canvas_width: float, canvas_height: float) -> dict:
    """
    Simulate throwing n needles on a grid of vertical lines.
    
    Args:
        l: Spacing between vertical lines
        d: Needle length
        n: Number of needles to throw
        canvas_width: Width of the canvas
        canvas_height: Height of the canvas
    
    Returns:
        Dict with needles (list of {x, y, angle, crosses}) and crossing_count
    """
    needles = []
    crossing_count = 0
    
    for _ in range(n):
        # Random position: center of needle
        x = random.uniform(0, canvas_width)
        y = random.uniform(0, canvas_height)
        
        # Random angle in [0, 2π)
        angle = random.uniform(0, 2 * math.pi)
        
        # Check if needle crosses any vertical line
        # Lines are at x = 0, l, 2l, 3l, ...
        # Needle's horizontal extent: from x - (d/2)*|cos(θ)| to x + (d/2)*|cos(θ)|
        # Crosses line at k*l if |x - k*l| <= (d/2) * |cos(θ)|
        half_horizontal_span = (d / 2) * abs(math.cos(angle))
        
        crosses = False
        if half_horizontal_span > 0 and l > 0:
            # Check all lines the needle could cross (infinite lattice)
            k_min = int(math.floor((x - half_horizontal_span) / l))
            k_max = int(math.ceil((x + half_horizontal_span) / l))
            for k in range(k_min, k_max + 1):
                line_x = k * l
                if abs(x - line_x) <= half_horizontal_span:
                    crosses = True
                    break
        
        if crosses:
            crossing_count += 1
        
        needles.append({
            "x": x,
            "y": y,
            "angle": angle,
            "crosses": crosses
        })
    
    return {
        "needles": needles,
        "crossing_count": crossing_count,
        "total_count": n
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/throw", methods=["POST"])
def throw():
    data = request.get_json()
    l = float(data.get("l", 50))
    d = float(data.get("d", 30))
    n = int(data.get("n", 100))
    canvas_width = float(data.get("canvas_width", 800))
    canvas_height = float(data.get("canvas_height", 600))
    
    if n <= 0 or n > 1000000:
        return jsonify({"error": "N must be between 1 and 1000000"}), 400
    
    if l <= 0 or d <= 0:
        return jsonify({"error": "l and d must be positive"}), 400
    
    result = throw_needles(l, d, n, canvas_width, canvas_height)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
