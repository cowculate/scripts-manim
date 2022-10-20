from manim import *

class Integral(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 4],
            y_range=[0, 4],
            x_length=10,
            axis_config={"color": PINK},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()

        graph = axes.plot(lambda x: -(x**2)+4*x, x_range = [0, 4], color=PINK)

        area = axes.get_area(graph, [0, 4], color=LIGHT_PINK, opacity=0.5)

        area_center_coords = area.get_center()
        area_unknown_text = Text("?").move_to(area_center_coords)

        labels = VGroup(axes_labels)
        self.add(axes, labels)

        self.play(Create(graph))
        self.play(Create(area))
        self.play(Write(area_unknown_text))
        self.play(FadeOut(area, area_unknown_text))

        riemann_area = axes.get_riemann_rectangles(graph, x_range=[0, 4], dx=0.5, color=LIGHT_PINK, fill_opacity=0.5)
        self.play(Create(riemann_area))
        self.wait(1)
        self.play(FadeOut(riemann_area))
        self.wait(1)

        riemann_area = axes.get_riemann_rectangles(graph, x_range=[0, 4], dx=0.1, color=LIGHT_PINK, fill_opacity=0.5)
        self.play(Create(riemann_area))
        self.wait(1)        
        self.play(FadeOut(riemann_area))
        self.wait(1)

        riemann_area = axes.get_riemann_rectangles(graph, x_range=[0, 4], dx=0.05, color=LIGHT_PINK, fill_opacity=0.5)
        self.play(Create(riemann_area))
        self.wait(1)    
        self.play(FadeOut(riemann_area))
        self.wait(1)    

        riemann_area = axes.get_riemann_rectangles(graph, x_range=[0, 4], dx=0.01, color=LIGHT_PINK, fill_opacity=0.5)
        self.play(Create(riemann_area))
        self.wait(1)    
        self.play(FadeOut(riemann_area))
        self.wait(1)    
