from subprocess import Popen, PIPE
from os import remove
from matrix import *
from prop import *

def is_number(s):
    try:
        float(s)
        return True
    except:
        return False
    
def approx(v):
##    for i in range(len(v)):
##        v[i] = round(v[i],5)
    return v

class PPMGrid(object):

    #constants
    XRES = 500
    YRES = 500
    MAX_COLOR = 255
    RED = 0
    GREEN = 1
    BLUE = 2

    DEFAULT_COLOR = [0, 0, 0]

    def __init__( self, width = XRES, height = YRES ):
        self.screen = []
        self.z_buffer = []
        self.width = width
        self.height = height
        for y in range( height ):
            self.screen.append( [] )
            self.z_buffer.append( [] )
            for x in range( width ):
                self.screen[y].append( PPMGrid.DEFAULT_COLOR[:] )
                self.z_buffer[y].append( float("-inf") )

    def __getitem__(self, i):
        return self.screen[i]

    def __setitem__(self, i, val):
        self.screen[i] = val
        return self.screen[i]

    def __len__(self):
        return len(self.screen)

    def __str__(self):
        ppm = 'P3\n' + str(len(self[0])) +' '+ str(len(self)) +' '+ str(PPMGrid.MAX_COLOR) +'\n'
        for y in range( len(self) ):
            row = ''
            for x in range( len(self[y]) ):
                pixel = self[y][x]
                row+= str( pixel[ PPMGrid.RED ] ) + ' '
                row+= str( pixel[ PPMGrid.GREEN ] ) + ' '
                row+= str( pixel[ PPMGrid.BLUE ] ) + ' '
            ppm+= row + '\n'
        return ppm

    def plot( self, color, x, y, z ):
        (x,y) = (int(x),int(y))
        newy = PPMGrid.YRES - 1 - y
        z = round(z,5)
##        z = int(z*1000000/1000000)
        if ( x >= 0 and x < PPMGrid.XRES and newy >= 0 and newy < PPMGrid.YRES
             and z >= self.z_buffer[newy][x] ):
            self[newy][x] = color[:]
            self.z_buffer[newy][x] = z

    def clear( self ):
        for y in range( len(self) ):
            for x in range( len(self[y]) ):
                self[y][x] = PPMGrid.DEFAULT_COLOR[:]
                self.z_buffer[y][x] = float("-inf")

    def save_ppm( self, fname ):
        f = open( fname, 'w' )
        f.write( str(self) )
        f.close()

    def save_extension( self, fname ):
        ppm_name = fname[:fname.find('.')] + '.ppm'
        self.save_ppm( ppm_name )
        p = Popen( ['convert', ppm_name, fname ], stdin=PIPE, stdout = PIPE )
        p.communicate()
        remove(ppm_name)

    def display( self ):
        ppm_name = 'pic.ppm'
        self.save_ppm( ppm_name )
        p = Popen( ['display', ppm_name], stdin=PIPE, stdout = PIPE )
        p.communicate()
        remove(ppm_name)

    def draw_line( self, x0, y0, z0, x1, y1, z1, color ):
        if ( x1 < x0 ):
            (x0, x1) = (x1, x0)
            (y0, y1) = (y1, y0)
            (z0, z1) = (z1, z0)
        a = y1 - y0
        b = x0 - x1
        (x,y,z) = (x0,y0,z0)
        if ( 0 <= a <= -b ): # oct 1
            d = 2*a + b
            dz = (z1 - z0) / (x1 - x0) if x1 != x0 else 0
            while ( x <= x1 ):
                self.plot( color, x, y, z )
                if ( d > 0 ):
                    y += 1
                    d += 2*b
                    
                x += 1
                d += 2*a
                z += dz
            return
        if ( -b <= a ): # oct 2
            d = a + 2*b
            dz = (z1 - z0) / abs(y1 - y0) if y1 != y0 else 0
            while ( y <= y1 ):
                self.plot( color, x, y, z )
                if ( d < 0 ):
                    x += 1
                    d += 2*a
                y += 1
                d += 2*b
                z += dz
            return
        if ( b <= a <= 0 ): # oct 8
            d = 2*a - b
            dz = (z1 - z0) / (x1 - x0) if x1 != x0 else 0
            while ( x <= x1 ):
                self.plot( color, x, y, z )
                if ( d < 0 ):
                    y -= 1
                    d -= 2*b
                x += 1
                d += 2*a
                z += dz
            return
        if ( a <= b ): # oct 7
            d = a - 2*b
            dz = (z1 - z0) / abs(y1 - y0) if y1 != y0 else 0
            while ( y >= y1 ):
                self.plot( color, x, y, z )
                if ( d > 0 ):
                    x += 1
                    d += 2*a
                y -= 1
                d -= 2*b
                z += dz
            return
        
    def draw_lines( self, matrix, color ):
        for c in range(matrix.cols//2):
            self.draw_line( *matrix[c*2][:3], *matrix[c*2+1][:3], color )

    def draw_polygons( self, prop, view, ambient_light, light_sources, mode="gouraud" ):
        matrix = prop.polygons
        neighbors = {}
        for i in range(prop.polygons.cols):
            neighbors[tuple(approx(matrix[i]))] = []
        for c in range(prop.polygons.cols//3):
            if not mode == "flat":
                neighbors[tuple(approx(matrix[c*3]))].append(c*3+1)
                neighbors[tuple(approx(matrix[c*3]))].append(c*3+2)
                neighbors[tuple(approx(matrix[c*3+1]))].append(c*3+2)
                neighbors[tuple(approx(matrix[c*3+1]))].append(c*3)
                neighbors[tuple(approx(matrix[c*3+2]))].append(c*3)
                neighbors[tuple(approx(matrix[c*3+2]))].append(c*3+1)
            normal = Vector.normal(*prop.polygons[c*3:c*3+3])
            if ( Vector.dot(normal, view) > 0 ):
                draw_outline = False
                color = [255,0,255]
                if ( draw_outline ):
                    self.draw_line( *matrix[c*3][:3], *matrix[c*3+1][:3], color )
                    self.draw_line( *matrix[c*3+1][:3], *matrix[c*3+2][:3], color )
                    self.draw_line( *matrix[c*3+2][:3], *matrix[c*3][:3], color )
                self.scanline_convert( prop, c, neighbors, view, ambient_light, light_sources, mode )

    def scanline_convert( self, prop, c, neighbors, view, ambient_light, light_sources, mode ):
        polygon = prop.polygons[c*3:c*3+3]
        [p0,p1,p2] = polygon
        if mode == "flat":
            normal = Vector.normal(p0,p1,p2).norm()
            color = prop.get_lighting(normal, view, ambient_light, light_sources)
        else:
            surface_normals = []
            vertex_normals = []
            for i in range(c*3,c*3+3):
##                print(neighbors)
                surface_normals.append([])
                for j in range(len(neighbors[tuple(prop.polygons[i])])//2):
                    surface_normals[-1].append(Vector.normal(prop.polygons[i],
                                                             prop.polygons[neighbors[tuple(approx(prop.polygons[i]))][j*2]],
                                                             prop.polygons[neighbors[tuple(approx(prop.polygons[i]))][j*2+1]]).norm())
##                    print(len(neighbors[i]))
                vertex_normals.append(Vector([0,0,0]))
                for j in range(len(surface_normals[-1])):
##                    print( str(vertex_normals[-1]) + " & & " + str(surface_normals[-1][j]) )
##                    print( str(i) + str(j) + str(surface_normals) )
                    if len(surface_normals[-1][j]) == 3:
                        vertex_normals[-1] += surface_normals[-1][j]
                if len(surface_normals[-1]) != 0:
                    vertex_normals[-1] = vertex_normals[-1].norm()
##                print(surface_normals[-1])
##            print(len(neighbors))
##            print()
            ys = []
            for i in range(len(polygon)):
                ys.append(polygon[i][1])
            vertex_normals = [x for y,x in sorted(zip(ys,vertex_normals), key=lambda pair: pair[0])]
        polygon.sort(key = lambda x: x[1])
        bot,mid,top = polygon[0],polygon[1],polygon[2]
        if mode == "gouraud":
            if c%2==0:
                color_bot = prop.get_lighting(vertex_normals[0], view, ambient_light, light_sources)
                color_mid = prop.get_lighting(vertex_normals[1], view, ambient_light, light_sources)
                color_top = prop.get_lighting(vertex_normals[2], view, ambient_light, light_sources)
            else:
                color_bot = prop.get_lighting(vertex_normals[0], view, ambient_light, light_sources)
                color_mid = prop.get_lighting(vertex_normals[1], view, ambient_light, light_sources)
                color_top = prop.get_lighting(vertex_normals[2], view, ambient_light, light_sources)
##            print([color_bot,color_mid,color_top])
        y = int(bot[1])
        x0,x1 = bot[0],bot[0]
        z0,z1 = bot[2],bot[2]
        if mode == "gouraud":
            r0,r1 = color_bot[0],color_bot[0]
            g0,g1 = color_bot[1],color_bot[1]
            b0,b1 = color_bot[2],color_bot[2]
        elif mode == "phong":
            vx0, vx1 = vertex_normals[0][0],vertex_normals[0][0]
            vy0, vy1 = vertex_normals[0][1],vertex_normals[0][1]
            vz0, vz1 = vertex_normals[0][2],vertex_normals[0][2]
        cy0 = int(top[1]) - y * 1.0
        cy1 = int(mid[1]) - y * 1.0
        dx0 = (top[0] - bot[0])/cy0 if cy0 != 0 else 0
        dx1 = (mid[0] - bot[0])/cy1 if cy1 != 0 else 0
        dz0 = (top[2] - bot[2])/cy0 if cy0 != 0 else 0
        dz1 = (mid[2] - bot[2])/cy1 if cy1 != 0 else 0
        if mode == "gouraud":
            dr0 = (color_top[0] - color_bot[0])/cy0 if cy0 != 0 else 0
            dr1 = (color_mid[0] - color_bot[0])/cy1 if cy1 != 0 else 0
            dg0 = (color_top[1] - color_bot[1])/cy0 if cy0 != 0 else 0
            dg1 = (color_mid[1] - color_bot[1])/cy1 if cy1 != 0 else 0
            db0 = (color_top[2] - color_bot[2])/cy0 if cy0 != 0 else 0
            db1 = (color_mid[2] - color_bot[2])/cy1 if cy1 != 0 else 0
        elif mode == "phong":
            dvx0 = (vertex_normals[2][0] - vertex_normals[0][0])/cy0 if cy0 != 0 else 0
            dvx1 = (vertex_normals[1][0] - vertex_normals[0][0])/cy1 if cy1 != 0 else 0
            dvy0 = (vertex_normals[2][1] - vertex_normals[0][1])/cy0 if cy0 != 0 else 0
            dvy1 = (vertex_normals[1][1] - vertex_normals[0][1])/cy1 if cy1 != 0 else 0
            dvz0 = (vertex_normals[2][2] - vertex_normals[0][2])/cy0 if cy0 != 0 else 0
            dvz1 = (vertex_normals[1][2] - vertex_normals[0][2])/cy1 if cy1 != 0 else 0
        while ( y < int(mid[1]) ):
            if mode == "flat":
                self.draw_line(int(x0),y,z0,int(x1),y,z1,color)
            elif mode == "gouraud":
                dz = (z1 - z0) / (x1 - x0) if x1 != x0 else 0
                dr = (r1 - r0) / (x1 - x0) if x1 != x0 else 0
                dg = (g1 - g0) / (x1 - x0) if x1 != x0 else 0
                db = (b1 - b0) / (x1 - x0) if x1 != x0 else 0
                if ( x1 > x0 ):
                    z,r,g,b = z0,r0,g0,b0
                    for x in range(int(x0), int(x1)+1):
                        self.plot([int(r),int(g),int(b)], x, y, z)
                        z += dz
                        r += dr
                        g += dg
                        b += db
                else:
                    z,r,g,b = z1,r1,g1,b1
                    for x in range(int(x1), int(x0)+1):
                        self.plot([int(r),int(g),int(b)], x, y, z)
                        z += dz
                        r += dr
                        g += dg
                        b += db
            elif mode == "phong":
                dz = (z1 - z0) / (x1 - x0) if x1 != x0 else 0
                dvx = (vx1 - vx0) / (x1 - x0) if x1 != x0 else 0
                dvy = (vy1 - vy0) / (x1 - x0) if x1 != x0 else 0
                dvz = (vz1 - vz0) / (x1 - x0) if x1 != x0 else 0
                if ( x1 > x0 ):
                    z,vx,vy,vz = z0,vx0,vy0,vz0
                    for x in range(int(x0), int(x1)+1):
                        self.plot(prop.get_lighting(Vector([vx,vy,vz]).norm(), view, ambient_light, light_sources),
                            x, y, z)
                        z += dz
                        vx += dvx
                        vy += dvy
                        vz += dvz
                else:
                    z,vx,vy,vz = z1,vx1,vy1,vz1
                    for x in range(int(x1), int(x0)+1):
                        self.plot(prop.get_lighting(Vector([vx,vy,vz]).norm(), view, ambient_light, light_sources),
                            x, y, z)
                        z += dz
                        vx += dvx
                        vy += dvy
                        vz += dvz
##                if r < 0 or g < 0 or b < 0:
##                    print(str([r,g,b]))
##                    [r,g,b] = [255,0,255]
            y += 1
            x0 += dx0
            x1 += dx1
            z0 += dz0
            z1 += dz1
            if mode == "gouraud":
                r0 += dr0
                r1 += dr1
                g0 += dg0
                g1 += dg1
                b0 += db0
                b1 += db1
            elif mode == "phong":
                vx0 += dvx0
                vx1 += dvx1
                vy0 += dvy0
                vy1 += dvy1
                vz0 += dvz0
                vz1 += dvz1
        y = int(mid[1])
        x1 = mid[0]
        z1 = mid[2]
        if mode == "gouraud":
            r1 = color_mid[0]
            g1 = color_mid[1]
            b1 = color_mid[2]
        elif mode == "phong":
            vx1 = vertex_normals[1][0]
            vy1 = vertex_normals[1][1]
            vz1 = vertex_normals[1][2]
        cy1 = int(top[1]) - int(mid[1]) * 1.0
        dx1 = (top[0] - mid[0])/cy1 if cy1 != 0 else 0
        dz1 = (top[2] - mid[2])/cy1 if cy1 != 0 else 0
        if mode == "gouraud":
            dr1 = (color_top[0] - color_mid[0])/cy1 if cy1 != 0 else 0
            dg1 = (color_top[1] - color_mid[1])/cy1 if cy1 != 0 else 0
            db1 = (color_top[2] - color_mid[2])/cy1 if cy1 != 0 else 0
        elif mode == "phong":
            dvx1 = (vertex_normals[2][0] - vertex_normals[1][0])/cy1 if cy1 != 0 else 0
            dvy1 = (vertex_normals[2][1] - vertex_normals[1][1])/cy1 if cy1 != 0 else 0
            dvz1 = (vertex_normals[2][2] - vertex_normals[1][2])/cy1 if cy1 != 0 else 0
        while ( y <= int(top[1]) ):
            if mode == "flat":
                self.draw_line(int(x0),y,z0,int(x1),y,z1,color)
            elif mode == "gouraud":
                dz = (z1 - z0) / (x1 - x0) if x1 != x0 else 0
                dr = (r1 - r0) / (x1 - x0) if x1 != x0 else 0
                dg = (g1 - g0) / (x1 - x0) if x1 != x0 else 0
                db = (b1 - b0) / (x1 - x0) if x1 != x0 else 0
                if ( x1 > x0 ):
                    z,r,g,b = z0,r0,g0,b0
                    for x in range(int(x0), int(x1)+1):
                        self.plot([int(r),int(g),int(b)], x, y, z)
                        z += dz
                        r += dr
                        g += dg
                        b += db
                else:
                    z,r,g,b = z1,r1,g1,b1
                    for x in range(int(x1), int(x0)+1):
                        self.plot([int(r),int(g),int(b)], x, y, z)
                        z += dz
                        r += dr
                        g += dg
                        b += db
            elif mode == "phong":
                dz = (z1 - z0) / (x1 - x0) if x1 != x0 else 0
                dvx = (vx1 - vx0) / (x1 - x0) if x1 != x0 else 0
                dvy = (vy1 - vy0) / (x1 - x0) if x1 != x0 else 0
                dvz = (vz1 - vz0) / (x1 - x0) if x1 != x0 else 0
                if ( x1 > x0 ):
                    z,vx,vy,vz = z0,vx0,vy0,vz0
                    for x in range(int(x0), int(x1)+1):
                        self.plot(prop.get_lighting(Vector([vx,vy,vz]).norm(), view, ambient_light, light_sources),
                            x, y, z)
                        z += dz
                        vx += dvx
                        vy += dvy
                        vz += dvz
                else:
                    z,vx,vy,vz = z1,vx1,vy1,vz1
                    for x in range(int(x1), int(x0)+1):
                        self.plot(prop.get_lighting(Vector([vx,vy,vz]).norm(), view, ambient_light, light_sources),
                            x, y, z)
                        z += dz
                        vx += dvx
                        vy += dvy
                        vz += dvz
##                if r < 0 or g < 0 or b < 0:
##                    print(str([r,g,b]))
##                    [r,g,b] = [255,0,255]
            y += 1
            x0 += dx0
            x1 += dx1
            z0 += dz0
            z1 += dz1
            if mode == "gouraud":
                r0 += dr0
                r1 += dr1
                g0 += dg0
                g1 += dg1
                b0 += db0
                b1 += db1
            elif mode == "phong":
                vx0 += dvx0
                vx1 += dvx1
                vy0 += dvy0
                vy1 += dvy1
                vz0 += dvz0
                vz1 += dvz1

    def parse_file( self, fname, color ):
        fopen = open(fname,'r')
        fread = fopen.read()
        fopen.close()

        t = Matrix.ident()

        coordinate_system = [Matrix.ident()]

        cmd = fread.split('\n')
        for i in range(len(cmd)):
            e = Matrix(0,4)
            p = Matrix(0,4)
            r = [ [1,1,1],
                  [1,1,1],
                  [1,1,1] ]
            view = Vector([0,0,1])
            ambient_light = [100,100,100]
            light_sources = [ Light( Vector([1,1,1]).norm(), [180,20,20] ) ]
            
            if ( i != len(cmd)-1 ):
                args = cmd[i+1].split()
                for j in range(len(args)):
                    if ( is_number(args[j]) ):
                        args[j] = float(args[j])
            
            if ( cmd[i] == "line" ):
                e.add_edge(*args)
                self.draw_lines(coordinate_system[-1]*e, color)
            elif ( cmd[i] == "ident" ):
                t = Matrix.ident()
            elif ( cmd[i] == "scale" ):
##                t *= Matrix.scaler(*args)
                coordinate_system[-1] = coordinate_system[-1] * Matrix.scaler(*args)
            elif ( cmd[i] == "move" ):
##                t *= Matrix.mover(*args)
                coordinate_system[-1] = coordinate_system[-1] * Matrix.mover(*args)
            elif ( cmd[i] == "rotate" ):
                if ( args[0] == 'x' ):
##                    t *= Matrix.rotx(args[1])
                    coordinate_system[-1] = coordinate_system[-1] * Matrix.rotx(args[1])
                elif ( args[0] == 'y' ):
##                    t *= Matrix.roty(args[1])
                    coordinate_system[-1] = coordinate_system[-1] * Matrix.roty(args[1])
                elif ( args[0] == 'z' ):
##                    t *= Matrix.rotz(args[1])
                    coordinate_system[-1] = coordinate_system[-1] * Matrix.roty(args[1])
            elif ( cmd[i] == "apply" ):
                e *= t
                p *= t
            elif ( cmd[i] == "clear" ):
                e = Matrix(0,4)
                p = Matrix(0,4)
                coordinate_system = [Matrix.ident()]
                self.clear()
            elif ( cmd[i] == "display" ):
##                self.clear()
##                self.draw_lines(e, color)
##                self.draw_polygons(p, color)
                self.display()
##                self.clear()
            elif ( cmd[i] == "save" ):
##                self.clear()
##                self.draw_lines(e, color)
##                self.draw_polygons(p, color)
                self.save_extension(args[0])
##                self.clear()
            elif ( cmd[i] == "quit" ):
                return
            elif ( cmd[i] == "circle" ):
                e.add_circle(*args)
                self.draw_lines(coordinate_system[-1]*e, color)
            elif ( cmd[i] == "bezier" or cmd[i] == "hermite" ):
                e.add_curve(*args,0.001,cmd[i])
                self.draw_lines(coordinate_system[-1]*e, color)
            elif ( cmd[i] == "box" ):
                p.add_box(*args)
                p = coordinate_system[-1]*p
                self.draw_polygons(Prop(p,r), view, ambient_light, light_sources)
            elif ( cmd[i] == "sphere" ):
                p.add_sphere(*args)
                p = coordinate_system[-1]*p
                self.draw_polygons(Prop(p,r), view, ambient_light, light_sources)
            elif ( cmd[i] == "torus" ):
                p.add_torus(*args)
                p = coordinate_system[-1]*p
                self.draw_polygons(Prop(p,r), view, ambient_light, light_sources)
            elif ( cmd[i] == "push" ):
                coordinate_system.append(coordinate_system[-1].copy())
            elif ( cmd[i] == "pop" ):
                coordinate_system.pop()
        

