import mdl
from display import *
from matrix import *

def run(filename):
    """
    This function runs an mdl script
    """
    view = Vector([0,0,1])
    ambient_light = [100,100,100]
    light_sources = [ Light( Vector([1,1,1]).norm(), [180,20,20] ) ]
    r = [ [1,1,1],
          [1,1,1],
          [1,1,1] ]
    color = [0, 0, 0]
    coordinate_system = [Matrix.ident()]
    screen = PPMGrid()

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
        for cmd in commands:
            e = Matrix(0,4)
            p = Matrix(0,4)

            if ( len(cmd) > 1 ):
                args = list(cmd[1:])
                i = 0
                while i < len(args):
                    if ( is_number(args[i]) ):
                        args[i] = float(args[i])
                    if ( args[i] == None ):
                        args.pop(i)
                    else:
                        i += 1
                        
            
            if ( cmd[0] == "line" ):
                e.add_edge(*args)
                screen.draw_lines(coordinate_system[-1]*e, color)
            elif ( cmd[0] == "ident" ):
                t = Matrix.ident()
            elif ( cmd[0] == "scale" ):
                coordinate_system[-1] = coordinate_system[-1] * Matrix.scaler(*args)
            elif ( cmd[0] == "move" ):
                coordinate_system[-1] = coordinate_system[-1] * Matrix.mover(*args)
            elif ( cmd[0] == "rotate" ):
                if ( args[0] == 'x' ):
                    coordinate_system[-1] = coordinate_system[-1] * Matrix.rotx(args[1])
                elif ( args[0] == 'y' ):
                    coordinate_system[-1] = coordinate_system[-1] * Matrix.roty(args[1])
                elif ( args[0] == 'z' ):
                    coordinate_system[-1] = coordinate_system[-1] * Matrix.roty(args[1])
            elif ( cmd[0] == "apply" ):
                e *= t
                p *= t
            elif ( cmd[0] == "clear" ):
                e = Matrix(0,4)
                p = Matrix(0,4)
                coordinate_system = [Matrix.ident()]
                screen.clear()
            elif ( cmd[0] == "display" ):
                screen.display()
            elif ( cmd[0] == "save" ):
                screen.save_extension(args[0])
            elif ( cmd[0] == "quit" ):
                return
            elif ( cmd[0] == "circle" ):
                e.add_circle(*args)
                screen.draw_lines(coordinate_system[-1]*e, color)
            elif ( cmd[0] == "bezier" or cmd[0] == "hermite" ):
                e.add_curve(args[0],args[1],args[2],args[3],args[4],args[5],0.001,cmd[0])
                screen.draw_lines(coordinate_system[-1]*e, color)
            elif ( cmd[0] == "box" ):
                p.add_box(*args)
                p = coordinate_system[-1]*p
                screen.draw_polygons(Prop(p,r), view, ambient_light, light_sources)
            elif ( cmd[0] == "sphere" ):
                p.add_sphere(*args)
                p = coordinate_system[-1]*p
                screen.draw_polygons(Prop(p,r), view, ambient_light, light_sources)
            elif ( cmd[0] == "torus" ):
                p.add_torus(*args)
                p = coordinate_system[-1]*p
                screen.draw_polygons(Prop(p,r), view, ambient_light, light_sources)
            elif ( cmd[0] == "push" ):
                coordinate_system.append(coordinate_system[-1].copy())
            elif ( cmd[0] == "pop" ):
                coordinate_system.pop()
        


    else:
        print("Parsing failed.")
        return
