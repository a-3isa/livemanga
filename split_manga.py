from math import ceil
import my_fn
step = 1
page = 0

def cut_panels(imageColor, polygons):
    imagesOut = []

    if len(polygons) > 0:
       
        for polygon in polygons:
            x0, y0 = polygon[0]
            x1, y1 = polygon[1]
            y2 = polygon[2][1]
            y3 = polygon[3][1]

            yUp = y0 if y0 >= y1 else y1
            yDown = y2 if y2 >= y3 else y3
            box = (x0, yUp, x1, yDown)
            temp = imageColor.crop(box)
            imagesOut.append(temp)

    return imagesOut

def search_left_right_borders(imageGrey, tolerance):
    sizeX, sizeY = imageGrey.size
    x_left = 0
    x_right = sizeX
    stop = 0

    while x_left < (sizeX/2) and stop <= tolerance:
        y = 0
        stop = 0
        while y < sizeY and stop <= tolerance:
            if imageGrey.getpixel((x_left, y)) < 250:
                stop += 1
            y += step
        if stop <= tolerance:
            x_left += 1

    stop = 0
    while x_right - 1 >= (sizeX /4)*2 and stop <= tolerance:
        y = 0
        stop = 0
        while y < sizeY and stop <= tolerance:
            if imageGrey.getpixel((x_right - 1, y)) < 250:
                stop += 1
            y += step
        if stop <= tolerance:
            x_right -= 1
    return x_left, x_right


def search_horizontal(imageGrey, tolerance, y):
    sizeX = imageGrey.size[0]
    x = 0
    stop = 0
    while x < sizeX and stop <= tolerance:
        pix = imageGrey.getpixel((x, y))
        if pix < 250:
            stop += 1
        x += 1
    return (x, stop)

def search_multi_diago(y, yUp, yDown, imageGrey, tolerance):
    sizeX = imageGrey.size[0]
    while yUp < yDown:
        x1, y1 = 0, y
        x2, y2 = sizeX - 1, yUp
        dx = x2 - x1
        dy = y2 - y1

        error = int(dx / 2.0)
        ystep = 1 if y1 < y2 else -1

        stop = 0
        while x1 <= x2 and stop <= tolerance:
            coord = (x1, y1)
            if imageGrey.getpixel(coord) < 250:
                stop += 1

            if stop <= tolerance:
                error -= abs(dy)
                if error < 0:
                    y1 += ystep
                    error += dx
                x1 += 1

        if stop > tolerance: #inutile de continuer la diagonale, on calcule la prochaine hauteur max (dy)
            # dy = (y * dx + int(dx/2)) / x
            yy = y1 - y + 1
            ddy = ceil((dx * abs(yy) - int(dx/2)) / x1)
            yyUp = y - ddy if yy < 0 else y + ddy
            yUp = yyUp if yyUp > yUp else yUp + 1
        else:
            return yUp
    return False

def horizontal_cut(imageGrey, tolerance, diago=True, angle=1):
    sizeX, sizeY = imageGrey.size
    panels = []
    startSquare = False
    lastY = 0

    for y in range(0, sizeY, step):
        if not startSquare: #search for begin of a panel
            lastY = y
            square = [(0, lastY), (sizeX, lastY)]
            startSquare = True

        else: #search for end of a panel
            if y > lastY and search_horizontal(imageGrey, tolerance, y)[0] == sizeX: #find blanck line
                square.append((sizeX, y))
                square.append((0, y))
                panels.append(square)
                startSquare = False
                lastY = y
            elif diago:
                yUp = max(y - angle, lastY)
                yDown = min(y + angle, sizeY - 1)
                yUp = search_multi_diago(y, yUp, yDown, imageGrey, tolerance)
                if yUp:
                    startSquare = False
                    square.append((sizeX, yUp))
                    square.append((0, y))
                    panels.append(square)
                    lastY = yUp
                    
                    

    if startSquare: #fin de page
        square.append((sizeX, sizeY))
        square.append((0, sizeY))
        panels.append(square)


    return panels

def search_split(imageGrey, diago=True, tolerance=20):
    case2split = []
    sizeY = imageGrey.size[1]

    x_left, x_right = search_left_right_borders(imageGrey, tolerance)
 
    print("x_left = {}, x_right = {}".format(x_left, x_right))
    box = (x_left, 0, x_right, sizeY)
    imageGrey = imageGrey.crop(box)
    horiSplit = horizontal_cut(imageGrey, tolerance, diago)

    
    

    if len(horiSplit) == 0:
        case2split.append([(x_left, 0), (x_right, 0), (x_right, sizeY), (x_left, sizeY)])
    else:
        for square in horiSplit:
                y0 = square[0][1]
                y1 = square[1][1]
                y2 = square[2][1]
                y3 = square[3][1]

                more_panels = my_fn.vertical_split(imageGrey, square)
                if len(more_panels) > 0:
                    case2split += more_panels
                case2split.append([(x_left, y0), (x_right, y1), (x_right, y2), (x_left, y3)])

    return case2split

