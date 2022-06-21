from point_rect import Rectangle, Point


rect = Rectangle()

rect.point1 = Point(4,3)
rect.point2 = Point(10,7)

center_point = rect.center()

center_point.show_values()
