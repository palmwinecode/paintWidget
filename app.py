from random import random
# Kivy 2.3.0
from kivy.app import App # type: ignore
from kivy.uix.widget import Widget # type: ignore
from kivy.uix.button import Button # type: ignore
from kivy.graphics import Color, Ellipse, Line # type: ignore

class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        # Create random color tuple
        color = (random(), 1., 1,)

        # Use widget's canvas object to represent data visually
        with self.canvas:
            # Set color with hsv color space
            Color(*color, mode="hsv")

            # Diamter variable
            d = 30.

            # Draw Ellipse at touch coordinates
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))

            # Store touch coordinates in ud dictionary
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_up(self, touch):
        # Create random color tuple
        color = (random(), 1., 1,)

        # Use widget's canvas object to represent data visually
        with self.canvas:
            # Set color with hsv color space
            Color(*color, mode="hsv")

            # Diamter variable
            d = 30.

            # Draw Ellipse at touch point
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            # touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        # Add new touch coordinates as touch moves
        touch.ud["line"].points += [touch.x, touch.y]

# Base class
class MyPaintApp(App):

    def build(self):
        # Create a parent for widget and clear button
        parent = Widget()

        # Create an object of the widget
        self.painter = MyPaintWidget()

        # Create clear button
        clearbtn = Button(text="Clear")
        clearbtn.bind(on_release=self.clear_canvas)

        # Add widget and clear button to parent
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
               
        return parent
    
    # Function to clear canvas
    def clear_canvas(self, obj):
        self.painter.canvas.clear()

# Run App
if __name__ == "__main__":
    MyPaintApp().run()