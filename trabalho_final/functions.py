class Box:
    
    def __init__(self):
        box = u'\u2586'
        minibox = u'\u2584'
        heightbox = u'\u25A0'
        bigheight = u'\u2590'
        heightleft = u'\u258C'
        inferior_left = u'\u2599'
        inferior_right = u'\u259F'
        corner1 = u'\u250C'
        corner2 = u'\u2514'
        corner3 = u'\u2510'
        corner4 = u'\u2518'
        self.box = box
        self.minibox = minibox
        self.heightbox = heightbox
        self.bigheight = bigheight
        self.heightleft = heightleft
        self.inferior_left = inferior_left
        self.inferior_right = inferior_right
        self.corner1 = corner1
        self.corner2 = corner2
        self.corner3 = corner3
        self.corner4 = corner4
        
    
   
class Colors:
    def __init__(self):
        white = '\033[99m'
        green = '\033[92m'
        blue = '\033[94m'
        purple = '\033[95m'
        cyan = '\033[96m'
        red = '\033[91m'
        grey = '\033[90m'
        yellow = '\033[93m'
        bold = '\033[1m'
        reset = '\033[0m'
        self.white = white
        self.green = green
        self.blue = blue
        self.purple = purple
        self.cyan = cyan
        self.red = red
        self.grey = grey
        self.yellow = yellow
        self.bold = bold
        self.reset = reset


            