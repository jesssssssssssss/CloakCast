import tkinter as tk
def create_rounded_rect(canvas, x1, y1, x2, y2, radius, **kwargs):
    """Create a rounded rectangle on the canvas."""
    points = [
        x1 + radius, y1, #Top-left arc
        x2 - radius, y1, #Top-right arc
        x2, y1 + radius, #top-right arc
        x2, y2 - radius, #Bottom-right arc
        x2 - radius, y2, #Bottom-left arc
        x1 + radius, y2, #Bottom-left arc
        x1, y2 - radius, #Bottom-left arc
        x1, y1 + radius, #Top-left arc
    ]
    return canvas.create_polygon(points, **kwargs, smooth=True)

#create window
window = tk.Tk()
window.title('Embed')
window.geometry('800x800') #Size of the window

#Create a canvas
canvas = tk.Canvas(window, width=200, height=100)
canvas.pack(pady=20)

#Drawing rounded rectangle
rounded_rect = create_rounded_rect(canvas, 10, 10, 190, 90,
                                   radius=15, fill='white',
                                   outline='black', width=8)

#Add text over the rounded rectangle with text
canvas.create_text(100, 50, text='Upload Audio', font = 'Calibri 15', fill='red')

#run
window.mainloop()